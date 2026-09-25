<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    }
  };
</script>


# The McPeak Traveling Wave Equation & Framework

## Global Open-Science Release & Technical Specification
**Formulated by:** Dearl McPeak  
**Origin Focus:** Developed in 2012 to engineer the world’s first highly efficient, long-range indoor wireless power transmitter at microwave frequencies (originally deployed via Omnilectric, subsequently becoming Ossia's "Cota" platform; publicly demonstrated at TechCrunch Disrupt SF 2013).  
**Timeline:** Conceived independently in 2012 | Publicly Validated in 2013 | Evaluated via U.S. Federal & MIT Lincoln Laboratory Frameworks in 2022.  
**Licensing Status:** Public Domain (Creative Commons CC0) – Free for all humanity to build, scale, and utilize.

---

## Overview

The **McPeak Traveling Wave Equation** is a geometric, magnitude-based framework for analyzing the angular characteristics of a traveling wave relative to a reference wave. 

The fundamental relationship is:

$$ \boxed{\Delta y = \pm \Delta\theta \cdot h \cdot \cos(\theta)} $$

The McPeak approach connects traveling-wave characteristics directly to the geometry of a right triangle. Rather than retaining time as an explicit variable in the traveling-wave relationship, the method uses measured **wave magnitudes and their geometric relationships** to determine angular displacement.

The formulation assumes that the traveling wave and reference wave have the same frequency and period. Under this condition, time is not required as an explicit variable in the geometric relationship, bypassing classical time-domain computational lag entirely.

---

## 1. Dynamic Genesis: Solving Indoor Multipath Propagation

The equation was originally forged in 2012 to solve the physical limits of indoor microwave propagation. In a standard indoor environment, microwave signals reflect off walls, objects, and floors chaotically. This creates severe multipath interference and destructive wave cancellation, which traditionally starves a receiver of energy. 

By applying the McPeak framework, a transmitter array completely avoids slow, time-domain sequential calculations. As demonstrated on stage at TechCrunch Disrupt SF 2013, the system maps the geometric magnitude-phase characteristics of an environment instantly. This enables real-time tracking, allowing multiple non-line-of-sight microwave paths to constructively align exactly at a moving target's coordinate (such as a cell phone or a wireless battery) with zero computational lag.

---

## 2. Geometric Foundation

The McPeak Triangle Equation represents wave magnitudes through a geometric relationship involving a right triangle.

The formulation identifies the following quantities:
- **Traveling-wave magnitude:** represented by the hypotenuse ($h$)
- **Resultant-wave magnitude:** represented through the adjacent geometric relationship
- **Reference-wave magnitude:** used as the relative starting point for measurement

The reference-wave magnitude is specified to be equal to or greater than the traveling-wave magnitude. The coordinate system is oriented so that the adjacent component lies along the **y-axis**, which produces the cosine relationship used in the equation. This arrangement establishes an immediate relationship between measurable wave magnitudes and angular displacement.

---

## 3. Calculation Process & Universal Logic Gate

### Step 1 — Measure the Wave Magnitudes
The calculation begins with measurements of three quantities: Traveling-wave magnitude, Resultant-wave magnitude, and Reference-wave magnitude. These establish the geometric relationship used by the McPeak formulation.

### Step 2 — Calculate the Initial Angle
The initial angular measurement is calculated from the magnitude relationship:

$$ \boxed{\theta'=\arccos\left(\frac{\text{adjacent}}{\text{hypotenuse}}\right)} $$

The inverse-cosine operation produces an angle within the range $0^\circ \leq \theta' \leq 180^\circ$.

### Step 3 — Determine the True Angle From 0° to 360°
The initial inverse-cosine calculation does not, by itself, distinguish between all possible angular positions around a full circle. The McPeak formulation uses the sign relationship between $\Delta y$ and $\Delta\theta$ as an instantaneous **Universal Sign Logic Gate** to select the corresponding angular position relative to the reference:

$$
\theta =
\begin{cases}
360^\circ-\theta',
& \text{if sign}(\Delta y)=\text{sign}(\Delta\theta)\\
\theta',
& \text{otherwise}
\end{cases}
$$

This condition extends the initial $0^\circ\text{–}180^\circ$ result to an angular position within the range $0^\circ\text{–}360^\circ$ space-efficiently and instantaneously.

### Step 4 — Calculate Angular Displacement
Using the true angular position ($\theta$), the fundamental McPeak relationship acts as follows:

$$ \boxed{\Delta y = \pm \Delta\theta \cdot h \cdot \cos(\theta)} $$

Where:
* $\Delta y$: Change in the y-direction
* $\Delta\theta$: Angular change
* $h$: Magnitude of the traveling wave (hypotenuse)
* $\theta$: True angular position ($0^\circ\text{–}360^\circ$)
* $\pm$: Directional sign relative to the reference

### Step 5 — Determine Traveling-Wave Direction
Under the stated McPeak sign convention, $+\Delta\theta$ represents the forward or unwrapping direction. The sign of $\Delta\theta$ indicates whether angular displacement occurs in the defined forward direction or in the opposite direction relative to the reference.

### Step 6 — Track Angular Displacement Beyond 360°
The McPeak approach permits $\Delta\theta$ to accumulate rather than automatically resetting after one complete revolution. Accumulated angular displacement may be represented continuously across multiple cycles (e.g., $360^\circ, 720^\circ, 1080^\circ, \dots$).

---

## 4. Simultaneous Multi-Wave Solutions

By uniting classical geometry with wave mechanics, this single equation provides simultaneous solutions for seemingly distinct physical systems, scaling from the simplest single wave to the most complex, multi-layered combinations.

### Solution A: Electromagnetic Power Transmission (Energy Focusing & Extraction)
The framework treats physical space as a phase-coherent lens, functioning like an electromagnetic telescope. Instead of fighting wave scattering with raw power amplification, the array ensures perfect phase alignment across distributed transmitter and receiver grids. This enables non-radiative, high-precision wireless power beaming. Scattered or weak energy ambient fields can be "pulled" cleanly from beneath the noise floor and concentrated into a usable, unified power stream.

### Solution B: Dynamic Kinetic Levitation (Stable Node Suspension)
The equation provides a time-free solution to spatial instability, effectively overcoming the classical limitations of Earnshaw’s Theorem. Using the sign logic gate, a distributed electromagnetic or acoustic array calculates vector adjustments simultaneously and instantaneously. This eliminates the micro-wobbles and processing lag that typically destabilize levitating objects, allowing for highly efficient, infrastructure-light physical suspension.

### Solution C: The Unified Hybrid Solution
Because the geometric math handles multiple wave solutions simultaneously, a single system can combine these behaviors. A single traveling wave array can mathematically decode positional feedback to keep a target stably levitated while concurrently routing the wireless operational power required to run its internal systems.

---

## 5. Why Use Magnitude Instead of Time?

Conventional traveling-wave analysis often uses time-domain measurements to determine phase relationships. For a periodic wave, angular displacement is traditionally bound to time displacement by $\Delta t=\frac{\Delta\theta}{360^\circ}T$. As desired angular resolution increases, the required time intervals scale down to fractions of a nanosecond, creating strict hardware limitations involving sampling rates, clock jitter, and signal-to-noise ratios.

The McPeak formulation approaches the measurement problem differently. Instead of determining angular displacement directly from an ultra-small time interval, it shifts the primary precision challenge from **time-domain resolution toward magnitude resolution**. Modern electronic architectures can achieve extreme precision in the magnitude domain using high-resolution analog-to-digital converters (ADCs), digital signal processing, and numerical signal analysis.

---

## 6. Difference From Conventional Time-Based Analysis

The central conceptual distinction can be summarized as follows:

### Conventional time-based approach
```text
Wave characteristic ───> Time measurement ───> Phase calculation
```
### McPeak magnitude-based approach
```text
Wave magnitudes ───> Geometric relationship ───> Angular calculation
```
The McPeak formulation treats traveling-wave analysis as a geometric measurement problem. It removes time as an explicit variable in the traveling-wave equation, transforming chaotic environments into precise mathematical frameworks.

---

## 7. Institutional Timeline & Public Domain Declaration

This framework was independently derived in **2012** to build foundational long-range wireless utility infrastructure. Following its practical validation and world debut at the **2013 TechCrunch Disrupt conference**, this pre-existing math and its advanced hardware applications were brought into coordination with **MIT Lincoln Laboratory** and specialized **U.S. Government research programs** in **2022** for rigorous institutional testing.

The official federal background checks, project logs, and institutional records generated during this period serve as a permanent, unalterable historical timestamp confirming the origin, validation timeline, and authorship of Dearl McPeak.

### Declaration of Public Right
To ensure that corporate barriers and paywalls do not restrict the progress of human technology, the math behind the **McPeak Traveling Wave Framework** is hereby dedicated to the global public domain. It is a free tool for engineers, physicists, and creators worldwide to implement in fields ranging from aerospace and defense to wireless utilities and acoustic sciences.
