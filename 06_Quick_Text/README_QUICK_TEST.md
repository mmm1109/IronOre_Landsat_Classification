# Quick Test

## Purpose

This folder provides a small example to demonstrate the classification code/algorithm representation supplied with this repository.

The classifications reported in the manuscript were originally performed using ArcMap 10.8.2 and QGIS with the Semi-Automatic Classification Plugin (SCP).

This quick test does not reproduce the complete manuscript classification, maps, confusion matrices, or reported accuracy values. It is included only as a simple demonstration of the Spectral Angle Mapping (SAM) decision principle used in the study.

## Files

This folder contains:

- `README_QUICK_TEST.md` – instructions for the quick test
- `quick_test.py` – small standalone SAM example

## Test description

The example uses one synthetic six-band pixel and two synthetic six-band reference spectra.

The six values represent the same six Landsat-5 TM predictor bands used in the study:

- B1
- B2
- B3
- B4
- B5
- B7

The spectral angle between the test pixel and each reference spectrum is calculated.

The test pixel is assigned to the reference class having the smallest spectral angle.

## Requirements

Python 3.x

No additional Python packages are required.

## How to run

Open a terminal or PowerShell window in this folder and run:

```bash
python quick_test.py
