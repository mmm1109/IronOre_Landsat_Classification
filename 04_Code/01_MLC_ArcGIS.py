"""
01_MLC_ArcGIS.py

Maximum Likelihood Classification (MLC) used in the study.

ORIGINAL SOFTWARE USED
----------------------
ArcMap 10.8.2 -> Spatial Analyst -> Maximum Likelihood Classification.

WHAT THIS FILE IS
-----------------
A transparent representation of the official ArcPy tool call and the
study-specific settings used in ArcMap.

WHAT THIS FILE IS NOT
---------------------
It is NOT Esri's proprietary internal source code. Esri does not publish the
internal implementation of MLClassify.

Official ArcPy syntax:
    MLClassify(
        in_raster_bands,
        in_signature_file,
        reject_fraction,
        a_priori_probabilities,
        in_a_priori_file,
        out_confidence_raster
    )

Study settings:
    Reject fraction          = 0.0
    A-priori probabilities   = EQUAL
    A-priori probability file= none
    Classes                  = NEIOZ, EIOZ, BL, VEG, WB
    Landsat-5 TM bands       = B1, B2, B3, B4, B5, B7
"""

from arcpy.sa import MLClassify


def arcmap_mlc(
    in_raster_bands,
    signature_file,
    output_classified_raster,
    output_confidence_raster=""
):
    """
    ArcMap 10.8.2 Maximum Likelihood Classification used for this study.

    The signature file (.gsg) contains the class mean vectors and
    covariance matrices derived from the training samples.
    """

    reject_fraction = "0.0"
    a_priori_probabilities = "EQUAL"
    a_priori_file = ""

    classified = MLClassify(
        in_raster_bands,
        signature_file,
        reject_fraction,
        a_priori_probabilities,
        a_priori_file,
        output_confidence_raster
    )

    classified.save(output_classified_raster)
    return classified


"""
ALGORITHM REPRESENTED BY THE ARCGIS TOOL
----------------------------------------
For class i, ArcGIS Maximum Likelihood Classification evaluates a
Gaussian class-discriminant function based on:

    - class mean vector
    - class covariance matrix
    - a-priori probability

The pixel is assigned to the class with the highest likelihood.

For this study:
    P(class_i) is equal for all five classes
    reject fraction = 0.0

Therefore every eligible pixel is assigned to the class with the
highest computed likelihood.
"""
