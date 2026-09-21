IronOre_Landsat_Classification
Study title
A Comparative Evaluation of Potential Iron Ore Zone from Satellite Data using Machine Learning and Conventional Approaches
Purpose of this repository
This repository accompanies the manuscript and provides the study input rasters, training polygons, study-area boundary, classifier code/algorithm representations, and original classified outputs.
The classifications reported in the manuscript were performed through:
ArcMap 10.8.2 for Maximum Likelihood Classification (MLC), and
QGIS with the Semi-Automatic Classification Plugin (SCP) for Spectral Angle Mapping (SAM), Random Forest (RF), and Support Vector Machine (SVM).
The authors did not develop new classification algorithms. The Python files in `04_Code/` document the corresponding software tool/API calls and study-specific settings used for each classifier. They are provided for transparency and code availability and should not be interpreted as independently developed classifier source code.
Repository structure
```text
IronOre_Landsat_Classification/
│
├── README.md
├── LICENSE_attribution.txt
│
├── 01_Bands/
│   ├── L5TM_19910320_AOI_SR_B1.tif
│   ├── L5TM_19910320_AOI_SR_B2.tif
│   ├── L5TM_19910320_AOI_SR_B3.tif
│   ├── L5TM_19910320_AOI_SR_B4.tif
│   ├── L5TM_19910320_AOI_SR_B5.tif
│   └── L5TM_19910320_AOI_SR_B7.tif
│
├── 02_Training_Polygons/
│   ├── NEIOZ.*
│   ├── EIOZ.*
│   ├── Bare_Land.*
│   ├── Vegetation.*
│   └── Water.*
│
├── 03_AOI/
│   └── AOI.*
│
├── 04_Code/
│   ├── 01_MLC_ArcGIS.py
│   ├── 02_SAM_SCP.py
│   ├── 03_RF_SCP.py
│   └── 04_SVM_SCP.py
│
└── 05_Original_Outputs/
    ├── SAM_original.tif
    ├── RF_original.tif
    ├── SVM_original.tif
    └── MLC_original.tif
```
Include `MLC_original.tif` only if the genuine original ArcMap output is available.
Satellite data
The study used Landsat-5 TM Collection 2 Level 2 Surface Reflectance imagery:
Scene: `LT05_L2SP_140045_19910320_20200915_02_T1_SR`
Acquisition date: 20 March 1991
Spatial resolution: 30 m
Bands used: B1, B2, B3, B4, B5, B7
Training classes
The same training polygons were used for all four classifiers.
Class	Meaning
NEIOZ	Non-exposed iron-ore zone
EIOZ	Exposed iron-ore zone / opencast mine
BL	Bare land
VEG	Vegetation
WB	Water body
Classifier code / algorithm representation
Maximum Likelihood Classification (MLC)
Original software: ArcMap 10.8.2, Spatial Analyst
File: `04_Code/01_MLC_ArcGIS.py`
Study settings:
equal a-priori class probabilities;
reject fraction = `0.0`;
class statistics supplied through the ArcGIS signature file;
five thematic classes.
Esri's internal MLC implementation is proprietary and is not redistributed here.
Spectral Angle Mapping (SAM)
Original software: QGIS + Semi-Automatic Classification Plugin (SCP)
File: `04_Code/02_SAM_SCP.py`
Study settings:
class reference spectra derived from the training classes;
minimum spectral-angle assignment;
no global rejection threshold;
six Landsat-5 TM bands.
Random Forest (RF)
Original software: QGIS + Semi-Automatic Classification Plugin (SCP)
File: `04_Code/03_RF_SCP.py`
Study settings documented in the manuscript:
500 trees;
2 features considered per split;
minimum leaf size = 1;
five classes;
six Landsat-5 TM predictor bands;
majority-vote class assignment.
Where a GUI parameter was not explicitly recorded in the manuscript, the code file identifies the corresponding documented software default rather than presenting it as a newly recovered experimental value.
Support Vector Machine (SVM)
Original software: QGIS + Semi-Automatic Classification Plugin (SCP)
File: `04_Code/04_SVM_SCP.py`
Study settings documented in the manuscript:
radial basis function (RBF) kernel;
six Landsat-5 TM predictor bands;
five classes;
one-versus-one multiclass interpretation.
The manuscript does not record numerical values for `C` and `gamma`. Where shown in the code file, documented software defaults are explicitly identified as defaults rather than newly recovered experimental settings.
Original classified outputs
`05_Original_Outputs/` contains the original classified rasters produced during the study using ArcMap and QGIS/SCP.
Accuracy assessment
The manuscript reports the confusion matrices and derived accuracy metrics, including overall accuracy, Kappa, precision, recall, and F1-score. Separate accuracy-result files are not included in this repository package.
Software provenance
See `LICENSE_attribution.txt` for third-party software attribution and licensing information.
Code availability statement
The code/algorithm representations and supporting study files are made publicly available in this repository for transparency and reproducibility of the software-based classification workflow described in the manuscript.
