# Annex A: Metrics (Informative)

This annex provides definitions, mathematical measurement methodologies, and interpretation guidelines for the key timing and frequency metrics utilized throughout the IEEE P3335 TimeCard specification. Because this is an informative annex, the metrics and recommendations presented herein do not constitute strict normative requirements, but rather establish a common engineering vocabulary to facilitate consistent evaluation of stability, accuracy, and performance across different hardware implementations and test environments.

All metrics referenced in this annex heavily align with established industry metrology literature, specifically ITU-T Recommendations G.810 and G.8260, as well as IEEE Std 1139.

---

## A.1 Overview

Metrology metrics quantify the operational performance of TimeCards across four primary domains:
1. **Time Stability:** The long-term coherence of the clock's phase.
2. **Frequency Stability:** The consistency of the clock's oscillator over specified averaging periods.
3. **Phase Noise:** The short-term, frequency-domain spectral purity of the oscillator.
4. **Holdover Behavior:** The predictable degradation of the timescale when external references are lost.

Utilizing a standardized mathematical framework allows operators to confidently compare devices from competing vendors and to validate interoperability across heterogeneous networks.

---

## A.2 Core Timing and Stability Metrics

### A.2.1 Allan Deviation (ADEV)
**Definition:** A statistical measure characterizing the fractional frequency stability of an oscillator or a timing system as a function of the averaging time ($\tau$). Unlike standard variance, ADEV converges for common oscillator noise types (such as flicker frequency noise).  
**Formula:**

$$ \sigma_y(\tau) = \sqrt{ \frac{1}{2(N-1)} \sum_{i=1}^{N-1} (\bar{y}_{i+1} - \bar{y}_i)^2 } $$

where $\bar{y}_i$ represents the continuous, successive fractional frequency averages measured over intervals of duration $\tau$, and $N$ represents the total number of frequency samples.  

**Purpose:** ADEV is the primary metric for evaluating both short-term and long-term oscillator frequency stability.  
**Reference:** ITU-T G.810 Annex I; IEEE Std 1139.  

**Typical Baselines for Reference:**
| Oscillator Technology | Typical ADEV ($\tau = 1$ s) | Typical Application |
|------------------|----------------|----------------|
| TCXO (Temperature-Compensated) | $1 \times 10^{-9}$ | Cost-sensitive edge compute |
| OCXO (Oven-Controlled) | $1 \times 10^{-11}$ | Datacenter / Telecom boundary clocks |
| Rubidium (Atomic) | $1 \times 10^{-12}$ | Primary Reference Clocks (PRC) / Core |
| CSAC (Chip-Scale Atomic) | $5 \times 10^{-12}$ | Portable / SWaP-constrained field units |

### A.2.2 Time Deviation (TDEV)
**Definition:** The time-domain equivalent of ADEV. It represents the measure of temporal stability related to the signal's phase variations.  
**Formula:**

$$ \text{TDEV}(\tau) = \frac{\tau}{\sqrt{3}} \times \text{Modified ADEV}(\tau) $$

**Purpose:** TDEV specifically quantifies the variation in absolute time error over a given observation period.  
**Reference:** ITU-T G.810 Annex I.  
**Usage:** TDEV is highly useful for evaluating the precision of synchronization networks, particularly assessing packet delay variation (PDV) noise in PTP deployments.

### A.2.3 Maximum Time Interval Error (MTIE)
**Definition:** The maximum peak-to-peak phase or time deviation observed between any two measurement points within an observation window of duration $\tau$.  
**Formula:**

$$ \text{MTIE}(\tau) = \max_{i,j} |x_j - x_i|, \quad \text{for all } (t_j - t_i) \le \tau $$

where $x$ is the time error constraint.  

**Purpose:** MTIE acts as a worst-case boundary metric, measuring the absolute maximum wander or drift of the timescale.  
**Reference:** ITU-T G.8260 Appendix II.5.  
**Usage:** MTIE is universally utilized to define strict holdover performance boundaries (e.g., assessing if a clock drifts more than $1.5$ $\mu s$ over a 24-hour holdover period).

---

## A.3 Frequency Domain and Jitter Metrics

### A.3.1 Phase Noise ($\mathcal{L}(f)$)
**Definition:** The power spectral density of phase fluctuations of a continuous periodic signal, traditionally expressed in decibels relative to the carrier per hertz ($\text{dBc/Hz}$) at varying offset frequencies from the main carrier frequency.  
**Formula:**

$$ \mathcal{L}(f) = 10 \log_{10}\left( \frac{S_\phi(f)}{2\text{ rad}^2} \right) $$

where $S_\phi(f)$ is the one-sided spectral density of the phase deviations.  

**Purpose:** Phase noise evaluates the short-term spectral purity of the local oscillator.  
**Reporting Profile:** Manufacturers typically plot phase noise across logarithmic decades: $1\text{ Hz}$, $10\text{ Hz}$, $100\text{ Hz}$, $1\text{ kHz}$, $10\text{ kHz}$, and $100\text{ kHz}$ offsets.  
**Reference:** IEEE Std 1139.

### A.3.2 Time Jitter
**Definition:** The short-term variance or instability of a time-domain signal (such as a 1PPS edge or a 10 MHz square wave) from its ideal, mathematically perfect periodic position.  
**Measurement Types:**
- **Peak-to-Peak Jitter ($J_{pk-pk}$):** The absolute maximum time difference between the earliest and latest occurrence of the signal edge over the sample set.
- **RMS Jitter ($J_{rms}$):** The root-mean-square average of the jitter samples, representing the common standard deviation of the timing error.

**Measurement Best Practice:** Jitter characterization is typically performed using calibrated Time Interval Counters (TICs) operating on a statistically significant dataset (e.g., $1 \times 10^6$ samples) with picosecond-level native resolution.

---

## A.4 Accuracy, Precision, and Granularity

To prevent ambiguity in TimeCard documentation, developers are encouraged to consistently separate the definitions of accuracy, precision, and hardware granularity.

| Metric | Contextual Definition | Example Target Profile |
|------|-------------|----------------|
| **Accuracy** | The degree of conformance or offset of the measured time directly to an absolute primary reference scale (e.g., UTC). | $<100\text{ ns}$ deviation from UTC(NIST) target |
| **Precision** | The internal repeatability or statistical variance of a measurement operation under completely identical conditions. | $<5\text{ ns}$ $1\sigma$ variance over $1,\!000$ consecutive PTM transactions |
| **Resolution** | The absolute smallest physically distinguishable change the circuit can detect or measure. | $10\text{ ps}$ inherent TDC (Time-to-Digital Converter) physical resolution |
| **Granularity** | The minimal mathematical discrete step available in the reported digital timestamps. | $1\text{ ns}$ bit-level granularity within an IEEE 1588 packet payload |

---

## A.5 Holdover Metrics

When a TimeCard suffers a total loss of its inbound external reference signals (e.g., GNSS jamming or fiber cut), the active disciplining loop opens, and the unit transitions to **holdover**.

### A.5.1 Holdover Time Error
**Definition:** The continuously accumulating deviation of absolute time driven by the free-running fractional frequency offset of the internal oscillator during holdover.  
**Mathematical Concept:**

$$ \Delta x(t) = x_0 + \int_0^t \Delta y(\tau) d\tau + \frac{1}{2} D t^2 + \epsilon(t) $$

where $x_0$ is initial phase error, $\Delta y$ is the normalized frequency offset, $D$ is the linear frequency aging rate, and $\epsilon(t)$ represents internal random noise.

**Practical Example:** If a TimeCard enters holdover with an uncorrected frequency offset of $1.15 \times 10^{-11}$, the generated 1PPS signal will mechanically drift by approximately $1\mu\text{s}$ per day of holdover ($\approx 86.4\text{ ns}$ per $1 \times 10^{-12}$ offset).

### A.5.2 Warm-Up and Recovery Behavior
- **Warm-Up Time:** The total duration required for an oscillator (specifically heated OCXOs or Rubidium cells) to reach thermal equilibrium and electrical stabilization upon a cold power cycle. 
- **Recovery Time:** The architectural time required for the PLL to re-establish a solid lock and compress phase errors after successfully reacquiring a valid reference.
- **Note:** It is highly recommended that vendors empirically characterize and publish both parameters in standard hardware datasheets.

---

## A.6 Ensemble and Correlation Metrics

In distributed environments, multiple TimeCards or reference inputs may be mathematically combined to form an **Ensemble Clock**.

| Concept | Description |
|---------|-------------|
| **Ensemble Average Stability** | Statistical improvement in composite ADEV proportional to $\sqrt{N}$, where $N$ represents the number of completely independent, uncorrelated clocks operating in the ensemble. |
| **Correlation Coefficient ($\rho$)** | A statistical measurement quantifying the dependency or shared error vectors between clocks. A highly resilient ensemble relies on sources with low correlation ($\rho \approx 0$). |
| **Weighting Function** | The active algorithm determining the proportional contribution of each individual clock/reference step, dynamically shifting based on real-time MTIE performance or variance. |

---

## A.7 Environmental Influence Metrics

Because oscillators physically react to their environment, static laboratory metrics rarely reflect real-world holdover stability unless environmental parameters are factored in.

| Parameter | Metric Definition | Impact |
|------------|---------|----------------------|
| **Temperature Coefficient** | The variance in fractional frequency ($\Delta f/f$) per degree Celsius ($\Delta^\circ\text{C}$). | Directly dictates holdover drift if the chassis undergoes drastic thermal shifts (e.g., an AC failure). |
| **Vibration Sensitivity ($\Gamma$)** | The relative frequency change per $g$ of mechanical acceleration. | Critical factor for systems deployed in heavily vibrating racks or industrial transit enclosures. |
| **Aging Rate** | The constant, predictable, unidirectional long-term frequency drift of the resonator over time (days/years). | Determines how frequently the TimeCard requires absolute external recalibration to prevent systemic clock bias. |

---

## A.8 Evaluating Hardware: Best Practices

When designing lab tests or automated qualification fixtures to evaluate the metrics detailed in this annex, engineers are encouraged to observe the following best practices:
- **Traceability:** Utilize only highly calibrated measurement instruments (e.g., Phase Noise Analyzers, Counters) that possess verifiable traceability to primary national standards (NIST, PTB, NPL).
- **Control Symmetries:** Rigorously design the physical measurement setup to minimize asymmetric cable propagation delays, thermal gradients, and RF impedance mismatches.
- **Broad Spectrums:** Execute stability validation tests across broad averaging intervals ($\tau = 1\text{ s}$ out to $>10^5\text{ s}$) to capture both short-term jitter and diurnal temperature-driven wander.
- **Contextual Logging:** Always log environmental metadata concurrently with performance data (e.g., ambient temperature, relative humidity, chassis airflow, and test equipment calibration schedules).

---

## A.9 Summary

The mathematical metrics outlined in this annex establish a vital, unified vocabulary for characterizing the temporal performance of TimeCard architectures. 

By standardizing exactly how stability, noise, drift, and holdover are mathematically calculated and reported, the IEEE P3335 ecosystem allows operators to rapidly compare discrete hardware configurations, validate regulatory compliance, and confidently integrate mixed-vendor timing infrastructure.

---

**End of Annex A**
