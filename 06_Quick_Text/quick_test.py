"""
quick_test.py

Minimal quick test for the code-availability repository.

This is NOT a reproduction of the manuscript results.
It demonstrates the minimum-spectral-angle decision used by the
Spectral Angle Mapping (SAM) classifier on a tiny synthetic example.

No external Python packages are required.
"""

import math


def spectral_angle(pixel, reference):
    """Return spectral angle in degrees between two equal-length vectors."""
    dot = sum(a * b for a, b in zip(pixel, reference))
    pixel_norm = math.sqrt(sum(a * a for a in pixel))
    ref_norm = math.sqrt(sum(b * b for b in reference))

    if pixel_norm == 0 or ref_norm == 0:
        raise ValueError("Zero-length spectral vector is not valid for SAM.")

    cosine = dot / (pixel_norm * ref_norm)
    cosine = max(-1.0, min(1.0, cosine))
    return math.degrees(math.acos(cosine))


def main():
    # Six-band synthetic example corresponding to Landsat-5 TM
    # B1, B2, B3, B4, B5 and B7.
    pixel = [0.10, 0.12, 0.15, 0.30, 0.22, 0.18]

    references = {
        "Class_A": [0.11, 0.13, 0.16, 0.31, 0.21, 0.17],
        "Class_B": [0.25, 0.22, 0.18, 0.10, 0.08, 0.06],
    }

    angles = {
        class_name: spectral_angle(pixel, spectrum)
        for class_name, spectrum in references.items()
    }

    assigned_class = min(angles, key=angles.get)

    print("Synthetic SAM spectral angles (degrees):")
    for class_name, angle in angles.items():
        print(f"  {class_name}: {angle:.6f}")

    print(f"Assigned class: {assigned_class}")

    if assigned_class != "Class_A":
        raise RuntimeError("QUICK TEST FAILED")

    print("QUICK TEST PASSED")


if __name__ == "__main__":
    main()
