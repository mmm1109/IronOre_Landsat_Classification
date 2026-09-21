# Quick Test

## Purpose

This quick test provides a very small example associated with the classifier code/algorithm representations supplied in this repository.

The manuscript classifications were performed through ArcMap 10.8.2 and QGIS with the Semi-Automatic Classification Plugin (SCP). The quick test does **not** reproduce the full manuscript classification or the reported accuracy values. It is only intended to demonstrate, on a tiny synthetic example, the minimum-spectral-angle decision used by the Spectral Angle Mapping (SAM) classifier documented in `04_Code/02_SAM_SCP.py`.

No study data are modified.

## Files

- `quick_test.py` – small standalone SAM decision example
- `04_Code/02_SAM_SCP.py` – representation of the QGIS SCP SAM tool/API and study settings

## Requirements

Python 3.x only.

No additional Python packages are required.

## How to run

1. Download or clone this repository.
2. Open a terminal or PowerShell window in the repository folder.
3. Run:

```bash
python quick_test.py
```

## Expected result

The script compares one six-band test pixel with two synthetic six-band reference spectra using the standard spectral-angle equation.

A successful run prints:

```text
QUICK TEST PASSED
Assigned class: Class_A
```

The exact spectral-angle values are also printed.

## Important note

This quick test is intentionally small. It does not reproduce the Landsat-5 TM classification maps, confusion matrices, or accuracy values reported in the manuscript. The full study classifications were executed in ArcMap and QGIS/SCP using the study datasets and settings documented in the repository.
