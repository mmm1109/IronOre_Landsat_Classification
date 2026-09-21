# Study Area Boundary (AOI)

This folder contains the Area of Interest (AOI) boundary used for the Landsat-5 TM classification study.

The AOI represents the study region covering the main iron-ore belt across parts of Keonjhar district, Odisha, and Singhbhum district, Jharkhand, eastern India.

## Spatial reference

The analysis was carried out on a common projected raster grid using:

- Coordinate Reference System: WGS 84 / UTM Zone 45N
- EPSG code: 32645
- Spatial resolution: 30 m

## Purpose of the AOI

The AOI boundary was used to:

- define the common study extent;
- clip the Landsat-5 TM surface-reflectance bands;
- maintain a consistent spatial extent for the classification inputs;
- support spatial comparison among the SAM, MLC, RF, and SVM classification outputs.

## Files

The AOI is provided as an ESRI shapefile with its associated component files, including:

- `.shp`
- `.dbf`
- `.shx`
- `.prj`
- `.cpg`

Additional shapefile index files may also be present where available.

The AOI supplied here is the boundary used for the analyses reported in the manuscript.
