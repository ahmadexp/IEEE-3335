# Annex B: Test Procedures (Informative)

This annex provides standardized, repeatable engineering test procedures for evaluating the functional and performance characteristics of TimeCard implementations. These procedures are designed to ensure consistency, comparability, and mathematical traceability of measurement results across independent vendors, metrology laboratories, and live deployment environments.

As this annex is explicitly informative, the test methodologies proposed herein serve as best-practice engineering baselines for hardware validation rather than strict normative conformance requirements.

---

## B.1 Overview

Comprehensive validation of a TimeCard architecture encompasses three primary testing domains:
1. **Functional Verification:** Validating logical compliance with the architectural interface, physical connectability, and management plane state-machine behaviors.
2. **Performance Validation:** Empirically measuring TimeCard frequency stability, phase noise, holdover drift, and timestamping jitter against the vendor's declared specifications.
3. **Environmental and Reliability Qualification:** Assessing physical performance consistency and survivability under externally applied, simulated stress conditions (e.g., thermal shock, vibration, or EMI).

To satisfy traceability requirements, it is strongly recommended that all tests be conducted utilizing equipment recently calibrated against recognized national metrology standards.

![Figure B-1 - Representative TimeCard test fixture](figures/rendered/test-fixture.pdf)

---

## B.2 General Test Conditions

### B.2.1 Environmental Setup
- Testing environments are typically maintained under nominal, thermally stable laboratory conditions unless a specific thermal extreme test is actively being executed. Baseline conditions generally sit at $23 \pm 3 ^\circ\text{C}$ with $30\text{--}70\%$ non-condensing relative humidity.
- The Device Under Test (DUT) should be allowed to reach complete thermal equilibrium and internal oscillator operational stability (warm-up) prior to the commencement of any metrology recording.
- Physical cabling (e.g., coaxial cables for 1PPS or 10 MHz) and RF splitters utilized in the test fixture should be phase-matched and carefully impedance-matched (typically $50\,\Omega$) to prevent signal reflections that cause false jitter readings in the instrumentation.

### B.2.2 Power and Initialization
- Evaluators should apply host bus power (e.g., via a PCIe riser) or auxiliary power within the hardware's rated voltage tolerance.
- The initial power-up sequence provides a baseline to map the oscillator's raw warm-up time from cold-start to achieving a steady-state frequency lock.

### B.2.3 Measurement Equipment Calibration Limits
Instrumentation utilized in performance validation should possess a noise floor or error margin substantially lower than the DUT to ensure the DUT is being measured, rather than the noise of the instrumentation itself.
- **Reference Clock:** The primary laboratory reference clock driving the test equipment should possess an Allan Deviation (ADEV) at least one order of magnitude ($10\times$) superior to the target specification of the DUT.
- **Time Interval Counter (TIC):** TICs should possess a native single-shot resolution of $<10\text{ ps}$ for evaluating high-precision OCXOs or GNSS-disciplined TimeCards.
- **Phase Noise Analyzer:** The analyzer's internal local oscillator should possess a phase noise floor at least $10\text{ dB}$, preferably $15\text{ dB}$, lower than the anticipated mask of the DUT across all relevant frequency offsets.

---

## B.3 Functional Verification Tests

Functional tests validate the logical operations and state transitions of the TimeCard without necessarily grading sub-nanosecond physical precision.

Each functional test should document:

- **Applicability:** The conformance profile, optional feature, or interface under test.
- **Entrance criteria:** DUT configuration, firmware revision, reference state, warm-up condition, and test equipment state required before the test begins.
- **Method:** Steps performed by the test operator or automation.
- **Pass/fail basis:** Observable result required to pass the test.
- **Evidence:** Logs, screenshots, instrument captures, register dumps, or other artifacts retained in the test report.

### B.3.1 Receive (Inbound) Interface Tests

| Test | Applicability | Method | Pass/fail basis |
|------|---------------|--------|-----------------|
| Reference detection | Each implemented receive interface | Sequentially apply valid external references (e.g., GNSS antenna input, PTP network feed, external 1PPS) and observe control telemetry. | The DUT reports the physical signal present, identifies the source type, and does not report a false loss-of-signal alarm. |
| Lock acquisition | Each reference source used for locked operation | Apply the reference after warm-up and record transition from free-running or holdover to locked state. | The DUT reaches locked state within the declared acquisition time and reports the active source. |
| Failover response | Implementations with multiple receive references | Disconnect or degrade the active primary reference while a secondary reference is valid. | The DUT enters holdover or switches to the secondary source according to the declared policy and does not reboot or lose control-interface access. |
| Holdover entry | Implementations claiming holdover | Remove all valid external references. | The DUT reports holdover state and exposes elapsed holdover time or equivalent telemetry. |

### B.3.2 Providing (Outbound) Interface Tests

| Test | Applicability | Method | Pass/fail basis |
|------|---------------|--------|-----------------|
| 1PPS amplitude and polarity | Physical Timing Output profile | Capture the 1PPS output edge using an oscilloscope with the declared termination. | On-time edge, pulse width, rise time, and voltage levels match the declaration and 7.3.2. |
| 1PPS alignment | Physical Timing Output profile with multiple providing interfaces | Compare each providing interface to the 1PPS output at the declared measurement points. | Alignment is within the declared bound and within the profile limit when one applies. |
| PCIe PTM validation | PCIe Host Mapping profile with PTM | Execute host-side PTM transactions and correlate returned timestamps against the declared unified-timescale reference. | Returned timestamps use the declared epoch/timescale and remain within declared latency and correction bounds. |
| Time of Day output | ToD output implementations | Decode the ToD stream while comparing against the selected reference source. | ToD values are syntactically valid, monotonically advance according to the declared timescale, and align to the declared output edge or message marker. |

### B.3.3 Control Interface Tests

| Test | Applicability | Method | Pass/fail basis |
|------|---------------|--------|-----------------|
| Baseline object readout | All conforming implementations | Read the required objects listed in 8.10.2 through at least one control interface. | Each object returns a valid value or a documented unsupported/unavailable value. |
| Reserved value handling | All implementations exposing enumerations or bitmaps | Attempt to write a reserved value to writable fields in a non-destructive test configuration. | The DUT rejects the reserved value or ignores it according to documented behavior; reserved read values are ignored by the client. |
| Event logging | Implementations with event logs | Cause a non-destructive event such as reference loss or lock acquisition. | Event record includes timestamp, severity, and source identifier. |
| Security access control | Managed or Secure Infrastructure profiles | Attempt read-only and configuration operations using credentials with different privilege levels. | Operations are allowed or denied according to the claimed security profile. |

---

## B.4 Performance Validation Tests

Performance tests quantify the TimeCard's physical metrology capabilities.

### B.4.1 Frequency Stability (ADEV/TDEV)
- **Procedure:** Connect the TimeCard’s primary continuous clock output (e.g., 10 MHz) to a Phase Noise Analyzer or high-resolution Frequency Counter. Record continuous phase/frequency samples locked against the laboratory primary reference.
- **Analysis:** Calculate and plot the Allan Deviation ($\sigma_y(\tau)$) and Time Deviation (TDEV) across logarithmic averaging intervals ($\tau = 1\text{ s}, 10\text{ s}, 100\text{ s}, 1,\!000\text{ s}, 10,\!000\text{ s}$).
- **Evaluation:** Compare the resulting stability curves against the manufacturer’s published datasheet limits.

### B.4.2 Short-Term Phase Noise ($\mathcal{L}(f)$)
- **Procedure:** Utilize a cross-correlated Phase Noise Analyzer to plot the Single Sideband (SSB) phase noise of the oscillator.
- **Analysis:** Measure the power spectral density in $\text{dBc/Hz}$ at standard decade offsets extending from $1\text{ Hz}$ to $1\text{ MHz}$ from the primary carrier frequency.
- **Evaluation:** Validate that the plotted noise curve sits below the vendor's declared upper-bound phase noise mask.

### B.4.3 Time Jitter
- **Procedure:** Capture a statistically significant sequence of 1PPS pulses (e.g., minimum $1 \times 10^5$ samples) utilizing a TIC triggered against the pristine laboratory 1PPS reference.
- **Analysis:** Calculate the Root-Mean-Square (RMS) jitter and the absolute peak-to-peak ($J_{pk-pk}$) timing variance of the signal edges.

### B.4.4 Holdover Boundary (MTIE)
- **Procedure:** Allow the DUT to lock to a master reference and achieve thermal and mathematical equilibrium for at least 24 hours. Abruptly sever the reference connection to force the unit into holdover.
- **Analysis:** Continuously record the wandering time error of the TimeCard’s 1PPS output against the laboratory master 1PPS for the specified holdover duration (e.g., 4, 12, or 24 hours).
- **Evaluation:** Compute the Maximum Time Interval Error (MTIE) across the observation window and verify the drift profile remains beneath the target limit (e.g., $1.5\mu\text{s}$/24hr).

---

## B.5 Environmental and Stress Qualification

Environmental tests validate that the TimeCard's hardware design robustly compensates for external physical interference.

| Test Profile | Recommended Methodology | Verification Target |
|------|--------------|---------------|
| **Thermal Cycling** | Place the active, locked DUT inside an environmental chamber. Cycle the ambient temperature across the manufacturer's maximum specified operating range (e.g., $0^\circ\text{C}$ to $55^\circ\text{C}$) using a predefined ramp rate ($^\circ\text{C}$/min). | Assess the maximum frequency excursion during temperature gradients. Verify that the oscillator’s internal temperature compensation mechanism functions correctly. |
| **Power Interruption** | Mechanically or electrically interrupt the host power plane for brief intervals ($1\text{ s}$ to $10\text{ s}$) if the TimeCard relies on localized holdover capacitors or batteries. | Verify that the hardware successfully bridges the interruption and maintains the internal unified timescale without experiencing a phase step or discontinuity upon power restoration. |
| **Vibration / Shock** | Subject the TimeCard to variable-frequency, multi-axis harmonic vibration ($5\text{ Hz}$ to $500\text{ Hz}$) using a specialized shaker table. | Record the immediate degradation in phase noise and frequency stability caused by g-force acceleration ($\Gamma$), verifying that the structural design adequately dampens the oscillator. |

---

## B.6 Reporting and Traceability

To maintain engineering transparency, comprehensive test reports for TimeCard validations should document:
- A detailed block diagram describing the physical test fixture, including cable lengths to account for fixed propagation delays.
- Expiration dates and calibration certificates for all primary laboratory measurement instrumentation used during the test.
- The precise firmware revision, hardware board step, and baseboard management controller (BMC) version installed on the DUT.
- Raw and plotted measurement data for all ADEV, TDEV, Phase Noise, and MTIE evaluations.
- Explicitly stated conditions during holdover tests (e.g., the thermal ramp rate applied to the chassis while the reference was disconnected).

With a consistent, traceable testing approach, integrators can confidently compare TimeCard implementations across different vendor ecosystems and ensure reliable behavior in production.

---

**End of Annex B**
