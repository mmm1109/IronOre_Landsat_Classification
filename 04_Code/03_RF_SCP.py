"""
03_RF_SCP.py

Random Forest (RF) used in the study.

ORIGINAL SOFTWARE USED
----------------------
QGIS -> Semi-Automatic Classification Plugin (SCP) -> Random Forest.

SCP exposes Random Forest through the open-source Remotior Sensus
classification backend, which uses scikit-learn functionality.

WHAT THIS FILE IS
-----------------
A transparent representation of the SCP/Remotior Sensus Random Forest
tool call and the parameters documented for this study.

Study settings documented in the manuscript:
    Number of trees          = 500
    Max features per split   = 2
    Minimum leaf size        = 1
    Classes                  = NEIOZ, EIOZ, BL, VEG, WB
    Predictors               = Landsat-5 TM B1, B2, B3, B4, B5, B7
    Final decision           = majority voting

The SCP field "minimum number to split" was not explicitly recorded in
the manuscript. The Remotior Sensus/scikit-learn documented default is 2,
so that value is shown explicitly below as a software default, not as a
newly claimed experimental setting.
"""

import remotior_sensus


def scp_random_forest(input_bands, spectral_signatures, output_path):
    """
    Representation of the QGIS SCP Random Forest tool call.
    """

    rs = remotior_sensus.Session()

    result = rs.band_classification(
        input_bands=input_bands,
        output_path=output_path,
        spectral_signatures=spectral_signatures,
        algorithm_name="rf",
        macroclass=False,

        # Study parameters
        rf_number_trees=500,
        rf_max_features=2,

        # Software default where the original GUI value was not recorded
        rf_min_samples_split=2,

        # No claim is made that optional tuning switches were enabled
        class_weight=None,
        find_best_estimator=False,

        overwrite=True
    )

    return result


"""
ALGORITHM USED BY RANDOM FOREST
-------------------------------
A forest of B decision trees is trained from the labelled samples.

For a pixel x, each tree h_b(x) predicts one class.
The final class is the class receiving the greatest number of votes:

    y_hat = argmax_k sum_b I(h_b(x) = k)

For this study:
    B = 500 trees
    2 predictor features were considered at each split.
"""
