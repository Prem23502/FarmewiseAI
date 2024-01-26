import rasterio
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import box
from rasterio.enums import Resampling
from matplotlib.colors import LinearSegmentedColormap

def read_geotiff(file_path, target_shape):
    with rasterio.open(file_path) as src:
        data = src.read(1, out_shape=target_shape, resampling=Resampling.bilinear)
        transform = src.transform
    return data, transform

def generate_annotation_map(dtm, dsm, orthomosaic, transform):
    height_difference = dsm - dtm
    approachable_threshold = 5  # Adjust as needed
    approachable_area = np.where(height_difference > approachable_threshold, 1, 0)
    unapproachable_area = np.where(height_difference <= approachable_threshold, 1, 0)

    aoi_threshold = 1
    area_of_interest = np.where(height_difference > aoi_threshold, 1, 0)

    approachable_area_within_aoi = approachable_area * area_of_interest
    unapproachable_area_within_aoi = unapproachable_area * area_of_interest

    total_plant_area = np.sum(approachable_area) + np.sum(unapproachable_area)

    bounding_box = box(*rasterio.transform.array_bounds(height_difference.shape[0], height_difference.shape[1], transform))
    gdf = gpd.GeoDataFrame({'geometry': [bounding_box]})

    fig, (ax_map, ax_table) = plt.subplots(1, 2, figsize=(15, 8))

    # Define colors using LinearSegmentedColormap
    color_aoi = LinearSegmentedColormap.from_list('custom_aoi', ['white', 'black'])
    color_approachable = LinearSegmentedColormap.from_list('custom_approachable', ['black', 'black'])
    color_unapproachable = LinearSegmentedColormap.from_list('custom_unapproachable', ['white', 'red'])

    # Plotting the annotation map on the first axis (ax_map)
    ax_map.imshow(orthomosaic, cmap='gray', extent=gdf.geometry.total_bounds, alpha=1.0)
    ax_map.imshow(area_of_interest, cmap=color_aoi, alpha=1.0, extent=gdf.geometry.total_bounds)
    ax_map.imshow(approachable_area_within_aoi, cmap=color_approachable, alpha=1.0, extent=gdf.geometry.total_bounds)
    ax_map.imshow(unapproachable_area_within_aoi, cmap=color_unapproachable, alpha=1.0, extent=gdf.geometry.total_bounds)

    table_data = [['Area of Interest', np.sum(area_of_interest)],
                  ['Approachable Area', np.sum(approachable_area_within_aoi)],
                  ['Unapproachable Area', np.sum(unapproachable_area_within_aoi)],
                  ['Total Plant Area', total_plant_area]]

    summary_table = ax_table.table(cellText=table_data, loc='center', cellLoc='center', colLabels=['Category', 'Area'])
    summary_table.auto_set_font_size(False)
    summary_table.set_fontsize(8)
    summary_table.scale(1, 1.5)
    ax_table.axis('off')

    ax_map.set_title('Annotation Map')
    ax_table.set_title('Area Summary Table')

    plt.show()

if __name__ == "__main__":
    dtm_path = "D:\\UNIVERSITY\\FarmwiseAI\\SURINOVA_CBE_DTM.tif"
    dsm_path = "D:\\UNIVERSITY\\FarmwiseAI\\SURINOVA_CBE_DSM.tif"
    orthomosaic_path = "D:\\UNIVERSITY\\FarmwiseAI\\SURINOVA_CBE_ORTHO.tif"

    target_shape = (3070, 2419)

    digital_terrain_model, transformation = read_geotiff(dtm_path, target_shape)
    digital_surface_model, _ = read_geotiff(dsm_path, target_shape)
    orthomosaic_image, _ = read_geotiff(orthomosaic_path, target_shape)

    generate_annotation_map(digital_terrain_model, digital_surface_model, orthomosaic_image, transformation)
