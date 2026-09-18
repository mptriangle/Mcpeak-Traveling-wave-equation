# The McPeak Traveling Wave Equation

## Overview

The **McPeak Traveling Wave Equation** is a proposed geometric, magnitude-based framework for analyzing the angular characteristics of a traveling wave relative to a reference wave.

The fundamental relationship is:

$$
\boxed{\Delta y=\pm\Delta\theta\,h\cos(\theta)}
$$

The McPeak approach connects traveling-wave characteristics to the geometry of a right triangle. Rather than retaining time as an explicit variable in the traveling-wave relationship, the method uses measured **wave magnitudes and their geometric relationships** to determine angular displacement.

The formulation assumes that the traveling wave and reference wave have the same frequency and period. Under this condition, time is not required as an explicit variable in the geometric relationship.

> **Important:** This document describes the proposed McPeak formulation. Its accuracy, general applicability, and performance should be evaluated through independent mathematical analysis, simulation, and experimental validation.

---

## 1. Geometric Foundation

The McPeak Triangle Equation represents wave magnitudes through a geometric relationship involving a right triangle.

The formulation identifies the following quantities:

- **Traveling-wave magnitude:** represented by the hypotenuse
- **Resultant-wave magnitude:** represented through the adjacent geometric relationship
- **Reference-wave magnitude:** used as the relative starting point for measurement

The reference-wave magnitude is specified to be equal to or greater than the traveling-wave magnitude.

The coordinate system is oriented so that the adjacent component lies along the **y-axis**. This orientation produces the cosine relationship used in the equation.

The geometric arrangement establishes a relationship between measurable wave magnitudes and angular displacement.

---

## 2. Calculation Process

### Step 1 — Measure the Wave Magnitudes

The calculation begins with measurements of three quantities:

1. Traveling-wave magnitude
2. Resultant-wave magnitude
3. Reference-wave magnitude

These measurements establish the geometric relationship used by the McPeak formulation.

### Step 2 — Calculate the Initial Angle

The initial angular measurement is calculated from the magnitude relationship:

$$
\boxed{\theta'=\arccos\left(\frac{\text{adjacent}}{\text{hypotenuse}}\right)}
$$

The inverse-cosine operation produces an angle within the range:

$$
0^\circ\leq\theta'\leq180^\circ
$$

### Step 3 — Determine the True Angle From 0° to 360°

The initial inverse-cosine calculation does not, by itself, distinguish between all possible angular positions around a full circle.

The McPeak formulation uses the sign relationship between $\Delta y$ and $\Delta\theta$ to select the corresponding angular position relative to the reference.

The stated condition is:

```math
\theta =
\begin{cases}
360^\circ-\theta',
& \mathrm{if}\ \mathrm{sign}(\Delta y)=\mathrm{sign}(\Delta\theta)\\
\theta',
& \mathrm{otherwise}
\end{cases}
```

This condition extends the initial $0^\circ$–$180^\circ$ result to an angular position within the range $0^\circ$–$360^\circ$, subject to the sign conventions used by the system.

### Step 4 — Calculate Angular Displacement

The fundamental McPeak relationship is:

$$
\boxed{\Delta y=\pm\Delta\theta\,h\cos(\theta)}
$$

Where:

| Symbol | Meaning |
|---|---|
| $\Delta y$ | Change in the y-direction |
| $\Delta\theta$ | Angular change |
| $h$ | Magnitude of the traveling wave |
| $\theta$ | True angular position |
| $\pm$ | Directional sign relative to the reference |

The units used for $\Delta\theta$ must be defined consistently. If angular displacement is expressed in degrees, the equation must be interpreted according to the formulation's degree-based convention. If standard calculus-based angular units are required, the corresponding unit conversion should be applied.

### Step 5 — Determine Traveling-Wave Direction

Under the stated McPeak sign convention:

$$
+\Delta\theta=\text{forward or unwrapping direction}
$$

The sign of $\Delta\theta$ is used to indicate whether angular displacement occurs in the defined forward/unwrapping direction or in the opposite direction relative to the reference.

The meaning of “forward” and “unwrapping” must be defined by the coordinate system and measurement setup used in a particular implementation.

### Step 6 — Track Angular Displacement Beyond 360°

The McPeak approach permits $\Delta\theta$ to accumulate rather than automatically resetting after one complete revolution.

For example, accumulated angular displacement may be represented as:

$$
360^\circ,\quad720^\circ,\quad1080^\circ,\ldots
$$

This provides a way to represent continuing angular displacement relative to a reference across multiple cycles.

---

## 3. Why Use Magnitude Instead of Time?

Conventional traveling-wave analysis often uses time-domain measurements to determine phase relationships. For a periodic wave, angular displacement can be related to time displacement by:

$$
\Delta t=\frac{\Delta\theta}{360^\circ}T
$$

where:

- $\Delta t$ is the time displacement,
- $\Delta\theta$ is the angular displacement, and
- $T$ is the wave period.

As the desired angular resolution increases, the corresponding time interval becomes smaller. Depending on the frequency and measurement requirements, practical limitations may involve:

- Timing resolution
- Sampling rate
- Clock stability
- Synchronization
- Jitter
- Bandwidth
- Signal-to-noise ratio
- Calibration accuracy

The McPeak formulation approaches the measurement problem differently. Instead of determining angular displacement directly from a very small time interval, it uses the **magnitude relationship among the traveling wave, reference wave, and resultant wave** to establish a geometric angle.

---

## 4. Primary Measurement Concept

The principal distinction of the McPeak approach is that it **shifts the primary measurement challenge from time-domain resolution toward magnitude resolution**.

This is potentially relevant because modern electronic measurement systems can provide high-resolution magnitude measurements using technologies such as:

- High-resolution analog-to-digital converters (ADCs)
- High-resolution digital-to-analog converters (DACs)
- Digital signal processing
- Precision amplitude measurement
- Numerical signal analysis

The approach does not eliminate the need for measurement precision. Instead, it changes the domain in which precision is primarily required.

Potential sources of error remain, including:

- Amplitude noise
- Phase noise
- Nonlinearity
- Quantization
- Calibration errors
- Frequency mismatch
- Reference instability
- Bandwidth limitations
- Geometric-model assumptions

---

## 5. Potential Applications

Because time is not an explicit variable in the stated McPeak traveling-wave relationship, the formulation may be investigated as an alternative approach to wave characterization in systems where high-resolution magnitude measurements are available.

Potential areas for investigation include:

- Angular-offset measurement
- Traveling-wave characterization
- Phase-related measurement systems
- Communications fading analysis
- Signal comparison using a reference wave
- High-resolution measurement and control systems

The practical usefulness of the method depends on the properties of the signals, the measurement architecture, the available resolution, and experimental validation.

---

## 6. What the Formulation Is Intended to Characterize

The stated formulation provides a geometric framework for investigating:

- Angular offset relative to a reference
- Angular position from $0^\circ$ to $360^\circ$
- Direction of angular displacement
- Forward or unwrapping motion relative to a reference
- Accumulated angular displacement beyond $360^\circ$
- Traveling-wave characteristics derived from magnitude relationships

Additional conditions may be required to apply the formulation to specific traveling-wave systems.

---

## 7. Difference From Conventional Time-Based Analysis

The central conceptual distinction can be summarized as follows.

### Conventional time-based approach

$$
\text{Wave characteristic}
\longrightarrow
\text{Time measurement}
\longrightarrow
\text{Phase calculation}
$$

### McPeak magnitude-based approach

$$
\text{Wave magnitudes}
\longrightarrow
\text{Geometric relationship}
\longrightarrow
\text{Angular calculation}
$$

The McPeak formulation treats traveling-wave analysis as a geometric measurement problem. It uses relationships among wave magnitudes to obtain angular information rather than requiring time to remain an explicit variable in the stated traveling-wave equation.

This represents an alternative measurement framework, not necessarily a replacement for conventional time-domain methods.

---

## 8. Limitations and Validation Requirements

Before the formulation can be considered generally applicable, the following issues should be examined:

1. **Dimensional consistency**  
   The units of angular displacement and the scaling of the equation should be explicitly defined.

2. **Angle conventions**  
   The sign conventions and the method used to distinguish angles over a full $360^\circ$ range should be documented.

3. **Signal conditions**  
   The effects of frequency mismatch, amplitude variation, noise, distortion, and reference-wave instability should be evaluated.

4. **Measurement uncertainty**  
   The relationship between magnitude uncertainty and angular uncertainty should be quantified.

5. **Experimental validation**  
   Simulations and controlled experiments should compare the method with established phase-measurement techniques.

6. **Reproducibility**  
   Test data, reference implementations, calibration procedures, and measurement conditions should be documented.

---

## 9. Summary

The **McPeak Traveling Wave Equation** presents a proposed magnitude-based geometric framework for analyzing traveling waves relative to a reference wave.

Its fundamental relationship is:

$$
\boxed{\Delta y=\pm\Delta\theta\,h\cos(\theta)}
$$

The process begins by measuring the magnitudes of the traveling wave, resultant wave, and reference wave. These measurements are used to establish a geometric relationship from which an initial angle is calculated. A sign-based condition is then used to identify the corresponding angular position within a full $360^\circ$ range.

The sign of $\Delta\theta$ is used to represent the defined direction of angular displacement, and accumulated angular displacement may continue beyond $360^\circ$ to represent multiple cycles.

The principal conceptual distinction is a change in measurement domain: **time is removed as an explicit variable from the stated geometric relationship, and the primary precision requirement is shifted toward magnitude measurement**.

In summary:

> **The McPeak Traveling Wave Equation proposes a way to analyze traveling-wave angular relationships as a magnitude-based geometric measurement problem rather than as a primarily time-based measurement problem.**

---

## 10. Suggested Repository Structure

A GitHub repository documenting the formulation could use the following structure:

```text
mcpeak-traveling-wave-equation/
├── README.md
├── LICENSE
├── docs/
│   ├── geometric-foundation.md
│   ├── calculation-process.md
│   └── validation-methodology.md
├── figures/
│   ├── mcpeak-triangle.png
│   └── angle-conventions.png
├── examples/
│   ├── example-calculation.md
│   └── example-data.csv
└── simulations/
    └── README.md
```

## License

Add a license file to the repository that reflects how you want others to use, modify, and redistribute the material.
