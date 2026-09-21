"""
04_SVM_SCP.py

Support Vector Machine (SVM) used in the study.

ORIGINAL SOFTWARE USED
----------------------
QGIS -> Semi-Automatic Classification Plugin (SCP)
-> Support Vector Machine.

SCP exposes SVM through the open-source Remotior Sensus classification
backend, which uses scikit-learn functionality.

WHAT THIS FILE IS
-----------------
A transparent representation of the SCP/Remotior Sensus SVM tool call
and the settings documented for this study.

Study settings documented in the manuscript:
    Kernel                   = radial basis function (RBF)
    Predictors               = Landsat-5 TM B1, B2, B3, B4, B5, B7
    Classes                  = NEIOZ, EIOZ, BL, VEG, WB
    Multiclass strategy      = one-versus-one interpretation

The manuscript does not record numerical C or gamma values.
The SCP/Remotior Sensus documented defaults are:
    C     = 1
    gamma = "scale"

Those defaults are therefore shown explicitly below and identified as
software defaults rather than newly reconstructed experimental values.
"""

import remotior_sensus


def scp_svm(input_bands, spectral_signatures, output_path):
    """
    Representation of the QGIS SCP Support Vector Machine tool call.
    """

    rs = remotior_sensus.Session()

    result = rs.band_classification(
        input_bands=input_bands,
        output_path=output_path,
        spectral_signatures=spectral_signatures,
        algorithm_name="svm",
        macroclass=False,

        # Study parameter
        svm_kernel="rbf",

        # Documented SCP/Remotior Sensus defaults
        svm_c=1.0,
        svm_gamma="scale",

        # No claim is made that optional tuning switches were enabled
        class_weight=None,
        find_best_estimator=False,

        overwrite=True
    )

    return result


"""
ALGORITHM USED BY SVM
---------------------
For non-linear separation, the classifier uses an RBF kernel:

    K(x, x_i) = exp(-gamma * ||x - x_i||^2)

The SVM seeks a maximum-margin decision boundary while penalising
misclassification through parameter C.

For five classes, the multiclass problem is handled through pairwise
binary class separation in the underlying SVM implementation.
"""
