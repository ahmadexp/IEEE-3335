Conformance Test Procedures (Normative)

This section defines the procedures for verifying that a TimeCard implementation conforms to the requirements defined in this specification.
Conformance testing ensures interoperability, performance transparency, and repeatability across vendors and use cases.

10.1 General Test Conditions

Environmental Setup

Tests SHALL be performed within the manufacturer’s rated environmental conditions (temperature, humidity, vibration).

Unless otherwise specified, ambient temperature SHOULD be 23 ± 3 °C.

Tests SHALL note oscillator warm-up time, GNSS visibility, and airflow conditions.

Power and Initialization

Apply host or auxiliary power within specified limits.

Verify correct sequencing and that all outputs stabilize within manufacturer-declared lock time.

Record total power consumption during cold start, warm start, and steady state.

Reference Inputs

All external references (GNSS, PPS, PTP, etc.) SHALL meet nominal levels, impedance, and signal shape per vendor spec.

Where multiple references are tested, the switching and ensemble-selection behavior SHALL be documented.

Measurement Equipment

Test instruments MUST be traceable to national metrology institutes (e.g., NIST, PTB, NPL).

Equipment SHOULD have at least 10× better stability or resolution than the parameter under test.

10.2 Receive Interface Verification

Signal Acceptance and Lock

Apply each supported input (GNSS, PPS, PTP, WR, etc.).

Verify the TimeCard detects and locks to each within the vendor-specified acquisition time.

Record lock indicators, telemetry state, and alarm behavior during lock/unlock transitions.

Input Priority and Failover

Configure multiple references; induce failure or degradation (e.g., GNSS antenna disconnect).

Confirm the TimeCard transitions to the next valid source per policy and maintains output continuity.

Verify the “active source” and “holdover” status via management telemetry.

Reference Sensitivity and Thresholds

Measure minimum input level for lock and maximum tolerable level without overload.

Document hysteresis or debounce behavior in input detection.

10.3 Providing Interface Verification

Output Format and Electrical Compliance

Measure each output’s amplitude, impedance, rise/fall time, polarity, and duty cycle.

Verify conformance to vendor-published limits.

Output Alignment

Measure relative phase between all outputs (PPS, 10 MHz, ToD).

Alignment error MUST NOT exceed vendor-published specification and SHOULD be < 1 ns for high-stability cards.

Confirm that all outputs represent the same unified timescale.

Host-Bus Timestamping Validation (if applicable)

For PCIe/PTM or similar buses, measure timestamp accuracy and asymmetry across transfers.

Compare against host-reported timestamps and expected hardware-path delay budgets.

Output During Reference Loss

Disconnect all references and observe the transition into holdover.

Verify timing continuity, proper status indication, and controlled drift according to § 7.5 holdover specification.

10.4 Management and Control Interface Verification

Register and Attribute Compliance

Query all required standard attributes: synchronization source, oscillator status, phase/frequency offsets, firmware version, and alarms.

Confirm that unsupported or undefined registers return “Not Implemented” or equivalent status.

Telemetry Accuracy

Cross-validate reported frequency/phase offsets and temperature readings with external measurements.

Discrepancy SHALL NOT exceed ±5 % of measured value or vendor-specified tolerance.

Firmware Update and Integrity

Perform firmware update via management interface.

Verify secure update (signature validation, rollback prevention).

Confirm version change and persistent configuration retention.

Security and Authentication

Validate that management access controls (e.g., credential, API token, or signed command) function correctly.

Confirm audit logging or version tracking, if supported.

10.5 Performance Validation

Frequency Stability (ADEV/TDEV)

Measure Allan deviation over τ = 1 s to 10⁴ s (or vendor-stated range).

Conditions: stable environment, reference locked.

Compare to published ADEV/TDEV curves.

Record results for both locked and holdover states.

Phase Noise

For each periodic output (10 MHz, etc.), measure single-sideband PN (dBc/Hz) at 1 Hz, 10 Hz, 100 Hz, 1 kHz, 10 kHz, and 100 kHz offsets.

Compare to vendor PN mask or specification.

PPS Jitter and Alignment

Record PPS over 1 × 10⁶ samples with respect to reference.

Calculate RMS and peak-to-peak jitter; confirm within published limits.

Verify second boundary alignment across all PPS outputs.

Holdover Drift and MTIE

Disconnect reference and measure 1 PPS phase error vs. time for the declared holdover duration.

Compute MTIE per ITU-T G.8260.

Compare against vendor-guaranteed maximum.

Ensemble Behavior

Apply two or more time sources with deliberate offset (e.g., ±100 ns).

Verify ensemble output converges to within expected range and weight selection behaves deterministically.

Induce one source fault and confirm seamless fallback.

10.6 Environmental and Power Validation

Power Cycling and Recovery

Cycle power 10× under nominal and cold conditions.

Verify consistent startup time, oscillator stabilization, and configuration persistence.

Thermal Response

Sweep temperature across operating range; measure frequency drift and holdover stability.

Validate thermal alarms trigger and clear at specified thresholds.

Power Consumption

Measure consumption under cold start, GNSS acquisition, and steady operation.

Compare to declared power budget; deviations > 10 % SHALL be reported.

10.7 Reporting and Certification

Test Report Contents
Each conformance report SHALL include:

Test environment and equipment list

Firmware and hardware versions

Measured parameters with plots and uncertainty bounds

Deviations or non-conformances

Traceability references to national standards

Certification Criteria

A TimeCard SHALL be deemed conformant if all mandatory (“SHALL”) requirements pass and all optional (“SHOULD”) items are either implemented or documented as intentionally omitted.

Conformance certificates SHOULD reference the applicable standard revision and include the complete test data set.

Re-Verification

Re-testing SHOULD occur after major firmware updates or hardware revisions.

Any parameter regression exceeding 10 % from published performance SHALL be disclosed in updated datasheets.

11. Summary

These conformance test procedures ensure that all TimeCards, regardless of vendor or implementation detail, provide measurable, interoperable, and traceable performance across critical dimensions of time, frequency, and stability.
Adherence to these procedures establishes a verifiable foundation for cross-vendor compatibility, host integration reliability, and long-term confidence in timing infrastructures built around the TimeCard standard.
