# FarmewiseAI
Geospatial data analysis using computer vision

Approach:
Data Preparation:

Ensure that your GeoTIFF files (SURINOVA_CBE_DTM.tif, SURINOVA_CBE_DSM.tif, SURINOVA_CBE_ORTHO.tif) are correctly formatted and contain the necessary elevation data.
Verify that the file paths in the code are correct and accessible.
Understanding Thresholds:

Examine the code to understand how the thresholds (approachable_threshold and aoi_threshold) are set. These thresholds determine which areas are considered approachable and part of the area of interest.
Color Mapping:

Understand how the custom colormaps are defined and used in the code. You can experiment with different color combinations by adjusting the colors in the ListedColormap instances.
Run the Code:

Execute the code and observe the generated annotation map and summary table.
Experimentation Results:
Annotation Map:

The annotation map will display different regions with distinct colors:
Area of Interest (Green): Represents regions with elevation differences above the aoi_threshold.
Approachable Area (Blue): Areas where the elevation difference is above the approachable_threshold and within the area of interest.
Unapproachable Area (Red): Areas where the elevation difference is below or equal to the approachable_threshold and within the area of interest.
Summary Table:

The summary table provides quantitative information about the areas:
Area of Interest: Total number of pixels classified as the area of interest.
Approachable Area: Total number of pixels classified as approachable within the area of interest.
Unapproachable Area: Total number of pixels classified as unapproachable within the area of interest.
Total Plant Area: Sum of approachable and unapproachable areas.
Adjusting Thresholds:

Experiment with different values for the approachable_threshold and aoi_threshold to observe how they affect the classification of areas and the resulting annotation map.
Custom Colormaps:

Modify the colors in the custom colormaps (custom_cmap_aoi, custom_cmap_approachable, custom_cmap_unapproachable) to achieve the desired visual representation.
Interpretation:

Interpret the results based on your domain knowledge and the characteristics of the provided datasets. Look for patterns, clusters, or areas of interest based on the elevation differences.
Iterative Experimentation:

Conduct iterative experimentation by adjusting parameters, thresholds, or colormap settings to refine the visualization based on your objectives.
