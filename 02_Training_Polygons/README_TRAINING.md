# Training Polygons

This folder contains the original training polygons used for the five thematic classes in the study.

The same training polygons were used for all four classification methods:

- Maximum Likelihood Classification (MLC)
- Spectral Angle Mapping (SAM)
- Random Forest (RF)
- Support Vector Machine (SVM)

## Training classes

- `NEIOZ` – Non-exposed iron-ore zone
- `EIOZ` – Exposed iron-ore zone / opencast mine
- `Bare_Land` – Bare land
- `Vegetation` – Vegetation
- `Water` – Water body

The polygons were originally prepared in ArcMap and subsequently exported as individual shapefiles for use in the QGIS Semi-Automatic Classification Plugin (SCP).

Each shapefile consists of several associated files, including `.shp`, `.dbf`, `.shx`, `.prj`, `.cpg`, and, where available, `.sbn` and `.sbx`.

These training polygons were used with the Landsat-5 TM bands B1, B2, B3, B4, B5, and B7 for classifier development and evaluation.
