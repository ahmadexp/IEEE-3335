# Annex A: Metrics (Informative)

This annex provides definitions, measurement methodologies, and interpretation guidelines for key timing and frequency metrics used throughout the TimeCard specification. These metrics enable consistent evaluation of stability, accuracy, and performance across different implementations and test environments.

---

## A.1 Overview

Metrics quantify the performance of TimeCards in terms of **time stability**, **frequency stability**, **phase noise**, and **holdover behavior**.  
They provide a standardized framework for comparing devices and ensuring interoperability across vendors.

All metrics referenced in this annex align with ITU-T Recommendations G.810, G.8260, and IEEE 1139.

---

## A.2 Core Timing Metrics

### A.2.1 Allan Deviation (ADEV)
**Definition:** A statistical measure of fractional frequency stability as a function of averaging time (τ).  
**Formula:**

\[
σ_y(τ) = \sqrt{ \frac{1}{2(N-1)} \sum_{i=1}^{N-1} (\bar{y}_{i+1} - \bar{y}_i)^2 }
\]

where \( \bar{y}_i \) are successive frequency averages over intervals of duration τ.  

**Purpose:** Evaluates oscillator and system frequency stability over time.  
**Reference:** ITU-T G.810 Annex I; IEEE Std 1139.  

**Typical Ranges:**
| Oscillator Type | ADEV (τ = 1 s) |
|------------------|----------------|
| TCXO | 1×10⁻⁹ |
| OCXO | 1×10⁻¹¹ |
| Rubidium | 1×10⁻¹² |
| CSAC | 5×10⁻¹² |

---

### A.2.2 Time Deviation (TDEV)
**Definition:** The time-domain equivalent of ADEV, representing time stability.  
**Formula:**

\[
TDEV(τ) = \frac{τ}{\sqrt{3}} \times ADEV(τ)
\]

**Purpose:** Quantifies the variation in time error over an observation period.  
**Reference:** ITU-T G.810 Annex I.

**Usage:** Ideal for evaluating synchronization precision in packet networks or PTP systems.

---

### A.2.3 Maximum Time Interval Error (MTIE)
**Definition:** The maximum phase or time deviation between any two points in a measurement window of duration τ.  
**Formula:**

\[
MTIE(τ) = \max_{i,j} |x_j - x_i|, \quad (t_j - t_i) ≤ τ
\]

**Purpose:** Measures worst-case time wander or drift.  
**Reference:** ITU-T G.8260 Appendix II.5.  
**Use Case:** Defines holdover performance and clock conformance limits.

---

## A.3 Frequency and Phase Noise Metrics

### A.3.1 Phase Noise (PN)
**Definition:** The spectral density of phase fluctuations of a periodic signal, expressed as **dBc/Hz** at an offset frequency from the carrier.  
**Formula:**

\[
L(f) = 10 \log_{10}\left( \frac{S_φ(f)}{2} \right)
\]

**Purpose:** Evaluates short-term oscillator purity and noise behavior.  
**Measurement Points:** Typically measured at 1 Hz, 10 Hz, 100 Hz, 1 kHz, 10 kHz, and 100 kHz offsets.  
**Reference:** IEEE Std 1139; ITU-T G.810.

---

### A.3.2 Jitter
**Definition:** Short-term deviation of a timing signal from its ideal periodicity.  
**Types:**
- **Peak-to-Peak Jitter:** Maximum instantaneous variation.
- **RMS Jitter:** Root-mean-square average of jitter samples.

**Measurement Units:** Picoseconds (ps) or nanoseconds (ns).  
**Reference:** ITU-T G.8251 and IEEE 802.3.  

**Best Practice:** Measure over 1×10⁶ samples with calibrated time interval counters.

---

## A.4 Accuracy, Precision, and Resolution

| Term | Definition | Typical Range | Reference |
|------|-------------|----------------|------------|
| **Accuracy** | Degree of conformance of measured time to a reference timescale (e.g., UTC). | <100 ns for PTP systems | ITU-T G.8271 |
| **Precision** | Repeatability of measurement under identical conditions. | <10 ns | IEEE 1588 |
| **Resolution** | Smallest distinguishable change in measured time or frequency. | 1 ps – 1 ns | IEEE 1139 |
| **Granularity** | Minimal step in reported timestamps or intervals. | 1 ns typical | PCIe PTM |

---

## A.5 Holdover Metrics

When the external reference is lost, a TimeCard enters **holdover** mode, relying on its internal oscillator to maintain timing.

### A.5.1 Holdover Error
**Definition:** The accumulated deviation of time or frequency from the ideal reference during holdover.  
**Formula:**

\[
Δt(t) = \int_0^t Δf(τ) dτ
\]

**Metric:** Expressed in nanoseconds (ns) or parts per billion (ppb) over time.  
**Test Condition:** Reference assumed perfect before disconnection.  

**Example:**  
If a TimeCard has a frequency offset of 1×10⁻¹¹, it will drift approximately 0.864 μs per day in holdover.

### A.5.2 Warm-Up and Recovery
- **Warm-Up Time:** Duration required for the oscillator to reach thermal equilibrium.  
- **Recovery Time:** Time required to re-lock after reacquiring a reference.  
Both parameters **SHOULD** be reported in vendor datasheets.

---

## A.6 Ensemble and Correlation Metrics

When multiple TimeCards or references are combined (ensemble mode), their collective performance can be expressed through:

| Metric | Description |
|---------|-------------|
| **Ensemble Average Stability** | Improvement in ADEV proportional to √N, where N = number of clocks. |
| **Correlation Coefficient (ρ)** | Quantifies dependency between clocks; ideal ensemble has ρ < 0.2. |
| **Voting/Weighting Function** | Determines contribution of each reference based on performance. |

**Reference:** IEEE 1139; ITU-T G.811 Annex A.

---

## A.7 Environmental Influence Metrics

| Parameter | Metric | Typical Requirement |
|------------|---------|----------------------|
| **Temperature Coefficient** | Frequency change per °C | <1×10⁻¹⁰/°C for OCXO |
| **Vibration Sensitivity** | Frequency change per g | <5×10⁻¹¹/g RMS |
| **Aging Rate** | Long-term drift per day | <1×10⁻¹⁰/day (OCXO), <5×10⁻¹²/day (Rubidium) |

Environmental parameters are critical for determining the **real-world holdover stability** and **phase coherence** of TimeCards.

---

## A.8 Measurement Best Practices

- Use calibrated measurement instruments traceable to national standards (NIST, PTB, NPL).  
- Ensure measurement setup minimizes cable delay asymmetries and thermal variations.  
- Perform tests over multiple averaging intervals (τ = 1 s to 10⁴ s).  
- Record both locked and holdover states.  
- Maintain full metadata: temperature, humidity, equipment serials, and calibration date.  

---

## A.9 Summary

The metrics defined in this annex establish a common vocabulary and methodology for evaluating the temporal performance of TimeCards.  
Adhering to these definitions ensures that all implementations—whether GNSS-disciplined, PTP-based, or ensemble-driven—can be compared, certified, and integrated into synchronized infrastructures with full transparency and repeatability.



