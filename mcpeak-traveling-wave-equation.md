# McPeak Traveling Wave Equation

**A Magnitude-Based Approach to Finer Phase Measurement Across Wave Types**

- **Creator:** Dearl McPeak
- **Origin:** 2012
- **Field:** Advanced Systems Engineering, Wave Measurement, and Phase Analysis

## 1. Overview

The **McPeak Traveling Wave Equation** was developed by Dearl McPeak to explore a method for achieving finer phase measurements of different types of waves without relying exclusively on time-based measurements.

The concept originated in 2012 while investigating how to measure the phase of a traveling wave at any point in space.

The primary objective is to investigate **whether wave magnitude, measured relative to a reference, can provide a more precise basis for determining phase than measuring extremely small fractions of time.**

This approach is intended to be applicable to multiple types of waves, including electromagnetic, electrical, mechanical, acoustic, optical, and other wave phenomena.

**Core objective:** Explore whether the precision of magnitude measurements can support finer phase resolution than conventional time-slice-based measurements.

## 2. The Challenge of Time-Based Phase Measurement

In conventional wave analysis, phase differences can be determined by measuring the time difference between a signal and a reference.

The relationship between phase and time is:

$$
\Delta\theta = 360^\circ \frac{\Delta t}{T}
$$

**Where**

| **Symbol** | **Description** |
|:---:|---|
| $\Delta\theta$ | Phase difference |
| $\Delta t$ | Measured time difference |
| $T$ | Wave period |


The period of a wave is:

$$
T = \frac{1}{f}
$$

Where $f$ is frequency.

### Why Higher Frequencies Create Measurement Challenges

As frequency increases, the period decreases. Consequently, measuring a small phase difference requires resolving increasingly small time intervals.

For example, one degree of phase corresponds to the following time intervals:

As frequencies increase, the time intervals associated with small phase differences become increasingly difficult to measure accurately.

### The Engineering Objective

The McPeak Traveling Wave Equation was developed to investigate whether phase measurement can be based on measurable wave magnitudes rather than depending exclusively on the ability to resolve increasingly small time intervals.

The objective is to explore a measurement approach in which phase resolution is influenced by the precision of magnitude measurement rather than solely by the precision of time measurement.

## 3. Magnitude as a Basis for Phase Measurement

The McPeak Traveling Wave Equation uses the relationship between wave magnitude and phase as the basis for exploring phase measurement.

A wave's magnitude can be expressed through different physical quantities, depending on the type of wave being measured.

Examples include:

Wave height

Displacement

Amplitude

Voltage

Current

Electrical power

Electromagnetic-field strength

Acoustic pressure

Sound intensity

Mechanical force

Fluid-wave elevation

Optical intensity

Other measurable wave-related quantities

Magnitude and Time

Magnitude is a measurable physical quantity that can be expressed independently of elapsed time.

For example:

The McPeak approach explores whether these measurable quantities can be used with a reference wave and geometric relationships to determine phase with finer resolution.

Important: Although magnitude can be measured as a physical quantity without directly measuring elapsed time, the relationship between magnitude and phase depends on the wave, reference, and measurement conditions.

## 4. The McPeak Triangle Equation

The McPeak Triangle Equation represents the foundational geometric relationship within the McPeak framework.

The equation is:

$$
Δy=±Δθ⋅h⋅cos⁡(θ)
$$

### Where:

The equation is based on the use of a right-triangle relationship to represent the relationship between magnitude and phase.

The McPeak Triangle concept uses a reference position and a measured wave magnitude to establish a geometric relationship.

### Geometric Principle

The McPeak framework associates the adjacent component of the triangle with the y-axis.

The cosine relationship is used to describe the relationship between the phase angle and the measured magnitude.

For additional information, see the documentation on the McPeak Triangle Equation.

## 5. The McPeak Traveling Wave Equation

The McPeak Traveling Wave Equation builds upon the McPeak Triangle Equation by incorporating additional logic for determining phase direction and angular position.

The framework is intended to address the interpretation of phase changes across a complete 360-degree cycle.

Phase-Angle Determination

The phase-angle logic is expressed as:

$$
\theta =
\begin{cases}
360^\circ - \theta', & \text{if sign}(\Delta y) = \text{sign}(\Delta\theta), & \theta',&\text{otherwise}
\end{cases}
$$

### Where:

This logic is intended to determine the appropriate angular interpretation based on the direction of the measured magnitude change and the phase change.

The complete McPeak Traveling Wave framework also considers angular positions beyond 360 degrees.

### Distinction Between the Two Equations

## 6. Types of Waves and Potential Applications

The McPeak Traveling Wave Equation is intended to explore phase measurement across multiple types of waves.

The applicability of the approach depends on whether a measurable magnitude-to-phase relationship can be established for the wave under examination.

### 6.1 Electromagnetic Waves

Examples include:

Radio waves

Microwave signals

Millimeter waves

Terahertz radiation

Infrared radiation

Visible light

Ultraviolet radiation

Potential applications:

Communications

Radar

Electromagnetic sensing

Imaging

Signal synchronization

Electromagnetic system control

### 6.2 Electrical Signals

Examples include:

Alternating-current voltage

Alternating-current

Electrical power waveforms

Transmission-line signals

High-frequency electronic signals

Oscillating electrical fields

Potential applications:

Power-system monitoring

Electrical instrumentation

Signal processing

Electronic synchronization

Power-quality analysis

### 6.3 Mechanical Waves

Examples include:

Mechanical vibrations

Elastic waves

Structural oscillations

Seismic waves

Surface waves

Material stress waves

Potential applications:

Structural health monitoring

Vibration analysis

Mechanical sensing

Material testing

Seismic measurement

### 6.4 Acoustic Waves

Examples include:

Audible sound

Ultrasonic waves

Infrasound

Acoustic pressure waves

Underwater sound waves

Potential applications:

Acoustic sensing

Ultrasonic imaging

Sonar

Structural inspection

Vibration monitoring

### 6.5 Optical Waves

Examples include:

Laser light

Fiber-optic signals

Coherent optical signals

Interferometric light fields

Potential applications:

Optical communications

Interferometry

Precision measurement

Fiber-optic sensing

Laser stabilization

### 6.6 Matter Waves and Quantum Systems

Examples include:

Electron wave phenomena

Matter-wave interference

Atomic wave behavior

Quantum oscillations

Potential applications:

Quantum measurement research

Matter-wave interferometry

Quantum sensing

Note: Applying the McPeak framework to quantum systems would require a formulation consistent with quantum mechanics and experimental validation.

## 7. The Role of Phase in Modern Technology

Phase is already an essential component of many modern technologies.

It is used to measure relationships between signals, determine timing differences, analyze motion, identify position, and coordinate complex systems.

The McPeak Traveling Wave Equation is intended to explore whether finer phase measurements could improve the precision of technologies that already depend on phase information.

### 7.1 Communications

Phase is used in:

Phase-shift keying (PSK)

Quadrature amplitude modulation (QAM)

Coherent optical communications

Carrier synchronization

Phase-locked loops

Software-defined radio

Wireless communication systems

Potential benefit of improved phase measurement:

More precise phase information could support improved synchronization, signal characterization, and analysis of phase-related errors.

### 7.2 Radar and Remote Sensing

Phase is used in:

Radar ranging

Doppler measurements

Synthetic-aperture radar

Interferometric radar

Coherent detection

Motion measurement

Potential benefit of improved phase measurement:

Finer phase measurements could potentially support more precise motion detection, distance measurements, and environmental monitoring.

### 7.3 Navigation and Positioning

Phase is used in:

Carrier-phase GNSS positioning

Radio navigation

Interferometric positioning

Precision timing

Phase-based distance measurement

Potential benefit of improved phase measurement:

More precise phase information could contribute to improved positioning and timing when other sources of error are controlled.

### 7.4 Electrical Power Systems

Phase is fundamental to:

AC power transmission

Three-phase power systems

Power-factor measurement

Grid synchronization

Phasor measurement units

Power-quality monitoring

Potential benefit of improved phase measurement:

Improved phase resolution could support more precise monitoring and control of electrical power systems.

### 7.5 Instrumentation and Signal Processing

Phase measurements are used in:

Network analyzers

Lock-in amplifiers

Frequency-response analyzers

Digital signal processing

Impedance measurement

Scientific instrumentation

Potential benefit of improved phase measurement:

More precise phase measurements could improve the characterization of electronic components, systems, and signal behavior.

### 7.6 Optical and Photonic Technologies

Phase is important in:

Optical interferometry

Fiber-optic communications

Coherent optical detection

Laser stabilization

Optical sensing

Holography

Potential benefit of improved phase measurement:

Finer phase measurements could support precision optical sensing and measurement applications, depending on the measurement method and system limitations.

## 8. Why Magnitude-Based Phase Measurement Matters

The McPeak Traveling Wave Equation is intended to explore whether phase resolution can be improved by using precise magnitude measurements instead of relying exclusively on extremely small time intervals.

The central concept is:

A wave's phase can be determined from its relationship to a reference. If that relationship can be measured through magnitude with sufficient precision, phase resolution may not be limited exclusively by the smallest time interval an instrument can resolve.

This concept is intended to apply to a broad range of wave types and measurement systems.

### Potential Advantages Under Investigation

Reduced dependence on extremely fine time measurements.

Exploration of finer phase resolution.

Application to different physical wave quantities.

Potential improvements in phase-sensitive instrumentation.

New approaches to wave measurement and analysis.

Potential applications in high-frequency systems.

Investigation of phase relationships in distributed systems.

These are potential advantages under investigation, not established performance results.

## 9. Measurement Considerations and Limitations

The McPeak Traveling Wave Equation is a mathematical framework for exploring phase measurement.

Practical phase-measurement accuracy depends on more than the equation itself.

Important factors include:

Measurement noise

Sensor accuracy

Analog-to-digital converter resolution

Reference-wave stability

Calibration

Signal distortion

Environmental conditions

Measurement bandwidth

Waveform characteristics

Magnitude-to-phase relationships

### Important Technical Distinction

Magnitude does not universally provide a unique phase measurement.

For example, a sinusoidal signal can have the same magnitude at multiple phase positions within a cycle.

Therefore, a magnitude-based phase-measurement method requires additional information, such as:

A known reference.

Directional information.

A defined measurement geometry.

A known waveform.

Appropriate sign information.

Additional measurements when necessary.

The McPeak Traveling Wave Equation incorporates directional logic intended to address phase-angle interpretation.

The effectiveness of this approach must be established through mathematical analysis and experimental testing.

## 10. Research and Development Objectives

The continuing objectives of the McPeak Traveling Wave Equation project include:

Documenting the mathematical foundation of the McPeak Triangle Equation.

Defining the complete McPeak Traveling Wave Equation.

Explaining the geometric relationships used in phase measurement.

Investigating magnitude-based phase-resolution techniques.

Exploring applicability across different types of waves.

Examining potential applications in modern technologies.

Developing educational diagrams and calculation examples.

Identifying measurement limitations.

Encouraging technical review and independent validation.

## 11. Conclusion

The McPeak Traveling Wave Equation was developed to explore a different approach to measuring the phase of traveling waves.

Its central objective is to investigate whether precise measurements of wave magnitude can support finer phase resolution than methods that rely exclusively on measuring increasingly small fractions of time.

The concept is intended to be applicable to multiple wave types, including electromagnetic, electrical, mechanical, acoustic, optical, and other wave phenomena.

Because phase is already fundamental to communications, radar, navigation, electrical power systems, instrumentation, and optical technologies, improved phase measurement could potentially contribute to advances in existing technologies.

The McPeak Traveling Wave Equation provides a framework for investigating these possibilities.

Further mathematical development, experimental testing, and comparison with established measurement methods are necessary to determine its practical advantages and limitations.

## 12. Author and Project Information

Creator: Dearl McPeak
Project: McPeak Traveling Wave Equation
Original Development: 2012
Primary Focus: Magnitude-based phase measurement
Areas of Interest: Wave measurement, electromagnetic systems, signal analysis, and advanced engineering

