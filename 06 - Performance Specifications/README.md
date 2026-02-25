# Performance Metrics (Normative)

This clause defines the performance reporting and characterization requirements for TimeCard implementations. The intent is to enable measurable, transparent, and comparable timing behavior across vendors. Performance metrics shall be reported in vendor documentation. 

---

## 6.1 Overview

TimeCard performance must quantify the precision, stability, and accuracy with which the device maintains and delivers time and/or frequency in a context aligned with the performance requirements of the intended application.

Performance metrics for the oscillator(s) utilized within the TimeCard shall be provided. These shall include frequency accuracy and temperature stability.

Performance metrics applicable for the characterization of the operation within the applicable use case should be provided. Those metrics should be characterized under both locked (synchronized/syntonized) and holdover operating conditions.

Manufacturers may report the following metrics:
- Frequency stability (ADEV, TDEV)
- Maximum Time Interval Error (MTIE)
- Phase noise (PN)
- Jitter and alignment (PPS and ToD)
- Accuracy and drift relative to reference
- Holdover behavior
- Environmental sensitivity (to temperature, voltage, vibration)

All measurements shall be made by testing equipment traceable to the relevant standards, such as UTC(NIST), and conform to relevant methodologies e.g. ITU-T G.810/G.8260.

## 6.2 Benchmarking and Testing Oscillators on the TimeCard

To validate the capabilities of the onboard oscillator(s) within the context of the TimeCard system, comprehensive testing procedures shall be conducted. The presence of the TimeCard inside a host system (such as a PCIe slot in a standard server) introduces environmental stressors such as thermal gradients, voltage fluctuations, and vibrations, which must be accounted for during benchmarking.

### 6.2.1 Test Environment and Setup

Benchmarking shall be performed using industry-standard precision measurement equipment to ensure reproducibility and traceability:
- **Reference Sources:** An atomic reference standard (e.g., Cesium or Rubidium clock) or a highly stable GNSS-disciplined oscillator (GNSSDO) tracing back to UTC.
- **Measurement Instruments:** High-resolution Time Interval Counters (TIC), Phase Noise Analyzers, and Oscillators with low intrinsic noise.
- **Environmental Controls:** Thermal chambers and vibration tables for simulating realistic operation conditions.

### 6.2.2 Core Performance Characterization

The following tests are standard for evaluating the intrinsic performance of the oscillator on the TimeCard:

1. **Fractional Frequency Stability (ADEV, TDEV):** 
   - Measured by comparing the TimeCard's oscillator output (e.g., 10 MHz or 1 PPS) against the reference source over various observation intervals ($\tau$). 
   - Allan Deviation (ADEV) and Time Deviation (TDEV) metrics shall be plotted to characterize short-term, medium-term, and long-term instability (white noise, flicker noise, and random walk).

2. **Phase Noise Testing:**
   - Evaluated in the frequency domain using a Phase Noise Analyzer to quantify short-term phase fluctuations.
   - Typically reported at standard offset frequencies (e.g., 1 Hz, 10 Hz, 100 Hz, 1 kHz, 10 kHz, 100 kHz) from the carrier.

3. **Maximum Time Interval Error (MTIE) and Time Variance (TVAR):**
   - Assesses the peak-to-peak variation in time delay of the oscillator's output relative to an ideal reference over a specified observation window.
   - Crucial for determining whether the oscillator's wander meets telecom and networking standards (e.g., ITU-T G.8262).

### 6.2.3 Operational and Holdover Benchmarking

The interaction between the synchronization subsystem and the oscillator must be tested under dynamic conditions.

1. **Lock Acquisition and Tracking:**
   - Measure the time required to achieve syntonization and synchronization from a cold start and a warm start.
   - Characterize phase transients and frequency overshoot during the locking phase.

2. **Holdover Performance:**
   - **Procedure:** Allow the TimeCard to reach a fully stabilized locked state using a GNSS or PTP reference. Disconnect the reference source to force the system into holdover mode.
   - **Measurement:** Record the time drift (phase error) accumulation relative to the reference over specific periods (e.g., 1 hour, 4 hours, 24 hours).
   - The reported holdover class must specify the maximum time error observed over a defined duration and temperature profile.

### 6.2.4 Environmental Stress Testing

Since TimeCards are intended for deployment in standard computing hardware, the oscillators must be benchmarked under simulated data center or edge environments.

1. **Thermal Stability Profile:**
   - Expose the TimeCard to a defined temperature ramp (e.g., -5°C to +55°C depending on chassis requirements).
   - For high-precision applications, determine the dynamic thermal gradient response (e.g., drift resulting from a 1°C/minute change) and steady-state frequency over temperature (Δf/f vs. ΔT).

2. **Power Supply and Voltage Variation:**
   - The PCIe bus provides power, but servers can exhibit significant voltage ripple.
   - Test frequency stability and phase noise under ±5% or ±10% input voltage fluctuations, verifying the effectiveness of onboard Low Dropout Regulators (LDOs) and power-filtering circuitry.

3. **Vibration and Airflow:**
   - Data center chassis fans cause mechanical vibration and rapid, localized temperature shifts due to airflow.
   - Benchmark the oscillator using a shaker table matching typical server rack vibration profiles (e.g., ETSI EN 300 019).
   - Measure vibration-induced phase noise and dynamic frequency shifts.

### 6.2.5 PCIe and System Integration Impact

It is critical to test the oscillator's performance when integrated within a standard PCIe environment, rather than isolated on a test bench:
- Compare baseline (standalone test bench) oscillator performance to performance while executing heavy PCIe data transfers.
- Verify that standard clock domains within the server do not induce crosstalk or correlated jitter on the TimeCard's precision timing signals.
