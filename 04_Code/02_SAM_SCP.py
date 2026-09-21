"""
02_SAM_SCP.py

Spectral Angle Mapping (SAM) used in the study.

ORIGINAL SOFTWARE USED
----------------------
QGIS 3.42.8 -> Semi-Automatic Classification Plugin (SCP)
-> Spectral Angle Mapping.

SCP exposes this classifier through the open-source Remotior Sensus
classification backend.

WHAT THIS FILE IS
-----------------
A transparent representation of the SCP/Remotior Sensus tool call and
the SAM decision rule used in the study.

Study settings:
    Algorithm                = Spectral Angle Mapping
    Training signatures      = mean spectrum of each class
    Global rejection threshold = none
    Classes                  = NEIOZ, EIOZ, BL, VEG, WB
    Landsat-5 TM bands       = B1, B2, B3, B4, B5, B7
"""

import remotior_sensus


def scp_sam(input_bands, spectral_signatures, output_path):
    """
    Representation of the QGIS SCP Spectral Angle Mapping tool call.

    spectral_signatures:
        SCP/Remotior Sensus SpectralSignaturesCatalog containing the
        five class signatures prepared from the original training ROIs.
    """

    rs = remotior_sensus.Session()

    result = rs.band_classification(
        input_bands=input_bands,
        output_path=output_path,
        spectral_signatures=spectral_signatures,
        algorithm_name="sam",
        macroclass=False,
        threshold=False,
        classification_confidence=False,
        signature_raster=False,
        overwrite=True
    )

    return result


"""
ALGORITHM USED BY SAM
---------------------
For an image pixel x and class reference spectrum y:

                    sum(x_i * y_i)
theta = arccos ---------------------------------------
               sqrt(sum(x_i^2)) * sqrt(sum(y_i^2))

where i = 1...6 for Landsat-5 TM bands B1, B2, B3, B4, B5 and B7.

SCP assigns the pixel to the class having the minimum spectral angle.

In this study:
    no global rejection threshold was applied.
"""
