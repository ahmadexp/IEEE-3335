# Annex B: Test Procedures (Informative)

This annex provides standardized test procedures for evaluating the functional and performance characteristics of TimeCard implementations. These procedures are designed to ensure repeatability, comparability, and traceability of measurement results across vendors, laboratories, and deployment environments.

---

## B.1 Overview

Testing of TimeCards encompasses three primary domains:

1. **Functional Verification** — ensuring compliance with interface and control requirements.  
2. **Performance Validation** — verifying timing accuracy, frequency stability, and jitter metrics.  
3. **Environmental and Reliability Qualification** — assessing performance consistency under stress conditions.

All tests should be conducted using calibrated, traceable instruments and documented per the guidelines in this annex.

---

## B.2 General Test Conditions

### B.2.1 Environmental Setup
- Tests **SHALL** be conducted under nominal laboratory conditions unless otherwise stated:  
  - Temperature: 23 ± 3 °C  
  - Humidity: 30–70% non-condensing  
  - Atmospheric pressure: 86–106 kPa
- The device under test (DUT) **SHALL** reach thermal equilibrium prior to measurement.  
- GNSS antennas, PTP connections, or reference signals **MUST** meet vendor specifications for level and impedance.

### B.2.2 Power and Initialization
- Apply host or auxiliary power within the rated voltage tolerance (±5%).  
- Verify startup sequence and measure oscillator warm-up time.  
- Record steady-state power consumption at idle and during synchronization.

### B.2.3 Measurement Equipment
All instruments used in testing **MUST** be traceable to national metrology standards (e.g., NIST, PTB, NPL).  
Recommended accuracy ratios:
- Frequency counter: 10× better than DUT precision.  
- Time interval counter: 10 ps or better resolution.  
- PN analyzer: 10 dB lower noise floor than DUT.

---

## B.3 Functional Tests

### B.3.1 Receive Interface
| Test | Description | Pass Criteria |
|------|--------------|---------------|
| Reference Detection | Apply GNSS/PTP/PPS and verify detection | Detected within vendor acquisition time |
| Lock Indication | Observe management telemetry | Status transitions to "Locked" |
| Failover Response | Disconnect reference input | TimeCard enters Holdover within 1 s |

### B.3.2 Providing Interface
| Test | Description | Pass Criteria |
|------|--------------|---------------|
| PPS Output | Measure amplitude, polarity, and timing | Within vendor spec |
| Frequency Output | Measure 10 MHz amplitude and stability | <±1×10⁻⁹ deviation |
| PTM Timestamp | Compare PCIe timestamps to reference | Within ±100 ps RMS |

### B.3.3 Management and Control Interface
| Test | Description | Pass Criteria |
|------|--------------|---------------|
| Register Read/Write | Access control registers | Expected values read/write OK |
| Telemetry Accuracy | Cross-check frequency offset readings | ±5% of independent measurement |
| Firmware Update | Perform signed update | Version change validated |

---

## B.4 Performance Tests

### B.4.1 Frequency Stability (ADEV/TDEV)
- Record frequency samples over multiple averaging times (τ = 1 s, 10 s, 100 s, 1000 s).  
- Compute Allan deviation (ADEV) and Time deviation (TDEV) using ITU-T G.810 methodology.  
- Verify values against vendor data.

### B.4.2 Phase Noise (PN)
- Measure PN spectrum at offset frequencies: 1 Hz, 10 Hz, 100 Hz, 1 kHz, 10 kHz, and 100 kHz.  
- Compare to vendor PN mask.  
- Phase noise **SHOULD** remain within ±3 dB of specification.

### B.4.3 PPS Jitter
- Capture 1×10⁶ PPS pulses using a calibrated TIC.  
- Compute RMS and peak-to-peak jitter.  
- Verify that RMS jitter ≤ 50 ps (OCXO) or ≤ 1 ns (GNSS-disciplined).

### B.4.4 Holdover and MTIE
- Lock DUT to external reference. Disconnect reference and record time error for declared holdover duration.  
- Compute MTIE per ITU-T G.8260 Appendix II.5.  
- MTIE **MUST** remain within vendor-declared limit.

### B.4.5 Ensemble Synchronization
- Connect multiple TimeCards with two or more reference inputs.  
- Intentionally offset one reference by ±100 ns.  
- Measure ensemble output convergence and verify correct weighting behavior.

---

## B.5 Environmental and Stress Tests

### B.5.1 Thermal Cycling
- Cycle DUT between minimum and maximum operating temperatures (e.g., −40°C to +85°C).  
- Record frequency drift and recovery upon returning to nominal temperature.

### B.5.2 Power Interruption
- Interrupt power for 1 s, 10 s, and 60 s intervals.  
- Verify that holdover continues within specification and recovery occurs without phase discontinuity.

### B.5.3 Vibration and Shock
- Apply mechanical vibration (5–500 Hz, 1 g RMS).  
- Apply shock per IEC 60068-2-27.  
- Observe frequency deviation ≤ ±5×10⁻¹¹ per g RMS.

### B.5.4 ESD and EMC Tests
- Perform ESD testing per IEC 61000-4-2 (contact ±6 kV, air ±8 kV).  
- Conduct EMC emission/immunity tests per EN 55032 / EN 55035.  
- Verify that no functional or timing anomalies occur.

---

## B.6 Reporting

Each conformance test report **SHALL** include:
- Test setup diagram and instrumentation list.  
- Firmware/hardware versions.  
- Environmental conditions and calibration traceability.  
- Measurement plots (ADEV, TDEV, PN, MTIE).  
- Uncertainty analysis and result interpretation.  
- Declaration of pass/fail for each test.

---

## B.7 Automation and Continuous Testing

### B.7.1 Automated Scripts
- Automated scripts **SHOULD** be developed in Python or Robot Framework for repeatable test execution.  
- Data **MUST** be logged in machine-readable formats (CSV, JSON).

### B.7.2 Continuous Integration (CI)
- Integrate TimeCard testing with CI pipelines (e.g., Jenkins, GitLab CI).  
- Perform nightly regression tests for firmware and driver updates.  
- Compare results against historical baselines for deviation detection.

---

## B.8 Summary

These test procedures provide a structured and traceable framework for evaluating TimeCard implementations. By following these methodologies, vendors and operators can validate compliance, benchmark performance, and ensure interoperability across the OCP Time Appliances Project ecosystem.
