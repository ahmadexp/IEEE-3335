# Performance Specifications (Normative)

This chapter defines the minimum performance reporting and characterization requirements for TimeCard implementations. The intent is to ensure measurable, transparent, and comparable timing behavior across vendors and use cases. Each performance attribute SHALL be verified under standardized test conditions and reported in vendor documentation.

---

## 11.1 Overview

TimeCard performance encompasses the precision, stability, and accuracy with which the device maintains and delivers time and frequency. Performance SHALL be characterized under both **locked** (synchronized) and **holdover** (free-running) conditions.

Manufacturers **SHALL** publish the following metrics:
- Frequency stability (ADEV, TDEV)
- Maximum Time Interval Error (MTIE)
- Phase noise (PN)
- Jitter and alignment (PPS and ToD)
- Accuracy and drift relative to reference
- Holdover behavior
- Environmental sensitivity (temperature, voltage, vibration)

All measurements **MUST** reference traceable standards, such as UTC(NIST), and conform to ITU-T G.810/G.8260 methodologies.

---

## 11.2 Stability Metrics

### 11.2.1 Allan Deviation (ADEV)
ADEV quantifies short-term frequency stability as a function of averaging time (τ).  
Vendors **SHALL** report ADEV curves for τ ranging from 1 s to 10⁴ s under reference-locked and holdover conditions.

Example reference: ITU-T G.810 Annex I.

### 11.2.2 Time Deviation (TDEV)
TDEV measures the time-domain equivalent of ADEV, representing timing stability over various intervals.  
Vendors **SHALL** provide TDEV plots corresponding to reported ADEV data, including environmental test conditions.

### 11.2.3 Maximum Time Interval Error (MTIE)
MTIE represents the maximum observed time deviation between any two points in a given observation window.  
Holdover MTIE **SHALL** conform to the ITU-T G.8260 Appendix II.5 definition. Vendors **SHALL** publish MTIE vs. observation interval plots and specify measurement bandwidth.

---

## 11.3 Phase Noise and Jitter

### 11.3.1 Phase Noise (PN)
Phase Noise describes the short-term frequency and phase fluctuations of a periodic signal, expressed in dBc/Hz versus offset frequency.  
For each sinusoidal output (e.g., 10 MHz, 5 MHz), vendors **SHALL** provide PN data at minimum offset frequencies of 1 Hz, 10 Hz, 100 Hz, 1 kHz, 10 kHz, and 100 kHz.

PN **SHALL** be measured with test equipment traceable to a national metrology institute and calibrated for low-noise operation.

### 11.3.2 Time Jitter
Time Jitter characterizes short-term temporal variations of a pulse or event signal (e.g., PPS).  
Vendors **SHALL** report:
- RMS jitter (ps)
- Peak-to-peak jitter (ps)
- Measurement bandwidth (Hz)

These values **MUST** be derived over ≥10⁶ consecutive pulses under nominal conditions.

---

## 11.4 Accuracy and Drift

Accuracy refers to the degree of conformance to a known time or frequency reference. Drift represents the accumulated deviation over time.  
Vendors **SHALL** report absolute accuracy in:
- Nanoseconds (for PPS and ToD outputs)
- Parts per billion (ppb) for frequency stability

Accuracy **SHOULD** be measured against UTC or equivalent traceable reference. Drift rates **SHALL** be reported for holdover intervals from 1 s to 24 h.

---

## 11.5 Holdover Performance

Holdover defines the TimeCard’s ability to maintain precise time in the absence of a reference signal.  
Manufacturers **SHALL** specify:
- Maximum allowable drift (MTIE) over time
- Warm-up and environmental conditioning requirements
- Recovery time to lock after reference restoration

Holdover performance **MUST** be validated under controlled environmental conditions with all external references disconnected.

---

## 11.6 Ensemble Behavior

For implementations supporting multiple reference inputs, ensemble performance **SHALL** be characterized by:
- Convergence time between references
- Ensemble weighting stability
- Output deviation from the unified timescale under reference offset conditions

Vendors **SHOULD** provide ensemble response plots showing time offset vs. reference skew for deterministic analysis.

---

## 11.7 Environmental Sensitivity

Manufacturers **SHALL** characterize and report performance variations due to environmental factors, including:
- Temperature (°C range, coefficient)
- Supply voltage variations (±5% nominal)
- Mechanical vibration or shock

ADEV and MTIE **SHOULD** be measured at temperature extremes to confirm thermal stability and compensation effectiveness.

---

## 11.8 Reporting Format

Each performance report **SHALL** include:
- Test conditions (temperature, humidity, power)
- Measurement equipment and calibration traceability
- Graphical plots (ADEV, TDEV, MTIE, PN, Jitter)
- Tabulated summary with key specifications
- Uncertainty bounds and statistical confidence

All data **SHOULD** be made available in machine-readable format (e.g., CSV, JSON) for inclusion in OCP-TAP conformance databases.

---

## 11.9 Compliance and Certification

A TimeCard implementation is deemed **compliant** if it:
- Meets or exceeds all mandatory (“SHALL”) performance criteria
- Reports all required metrics with traceable data
- Demonstrates conformance via validated test methods

OCP-TAP certification programs **MAY** reference this chapter as the normative basis for timing performance verification.
