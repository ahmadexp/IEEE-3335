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

Reference Implementation and Interoperability Testbed (Informative)

This section defines a recommended reference laboratory environment for evaluating the functional, timing, and interoperability characteristics of TimeCard devices across multiple vendors and use cases.
The intent is to provide a repeatable, transparent test framework for the Open Compute Project (OCP) Time Appliances Project (TAP) and related community test efforts.

12.1 Objectives

The primary objectives of the interoperability testbed are to:

Validate that TimeCards from different vendors interoperate seamlessly with any compliant host platform.

Characterize and compare timing precision, phase alignment, and stability across diverse hardware implementations.

Verify standardized management interfaces and attribute mappings for monitoring and control.

Provide a traceable performance baseline to inform future revisions of the specification and to support certification programs.

Enable continuous regression testing as firmware and host software evolve.

12.2 Testbed Architecture Overview

A typical interoperability testbed consists of the following components:

Reference Time Sources:

Multi-GNSS disciplined master clock (GPS, Galileo, GLONASS, BeiDou).

High-stability rubidium or cesium frequency standard.

Network time infrastructure supporting PTP, NTP, and WR distribution.

Host System Under Test (HSUT):

Server-class platform with PCIe slots supporting PTM and timestamp capture.

Capability to host multiple TimeCards simultaneously for side-by-side comparison.

Isolated management network and power monitoring.

Measurement and Monitoring Equipment:

Multi-channel time interval counter with <100 ps resolution.

PN analyzer or phase noise measurement system for 10 MHz outputs.

Oscilloscope or TIE (Time Interval Error) analyzer for PPS edge correlation.

Network analyzer for PTP latency/asymmetry characterization.

Power analyzer for load profiling and startup current capture.

Management Controller and Data Aggregator:

Collects telemetry from SMBus/I²C, IPMI, or network interfaces.

Runs conformance scripts via REST/gRPC APIs.

Correlates all measurements to a traceable master clock (e.g., UTC via GNSS or ensemble).

Environmental Chamber (Optional):

Provides controlled temperature sweep from −40 °C to +85 °C for thermal performance evaluation.

12.3 Topology Example
      ┌────────────────────────────┐
      │    GNSS / Rb / Cesium     │
      │   Reference Master Clock  │
      └──────────┬────────────────┘
                 │ PPS / 10 MHz
                 ▼
     ┌────────────────────────────┐
     │   Distribution Amplifier   │
     └──┬───────────┬───────────┬─┘
        │           │           │
        ▼           ▼           ▼
   ┌────────┐  ┌────────┐  ┌────────┐
   │TC #1   │  │TC #2   │  │TC #n   │   ← TimeCards Under Test
   └──┬─────┘  └──┬─────┘  └──┬─────┘
      │            │           │
      ▼            ▼           ▼
   ┌────────────────────────────┐
   │  Host System (PCIe/PTM)    │
   │  Multi-Slot Test Chassis   │
   └──────────┬─────────────────┘
              │
              ▼
     ┌────────────────────────────┐
     │ Time Interval Counter /    │
     │ PN Analyzer / Management   │
     │ Data Collector             │
     └────────────────────────────┘

12.4 Interoperability Scenarios

Multi-Vendor Synchronization Test:

Install TimeCards from two or more vendors in the same host or synchronized hosts.

Apply a common reference input (e.g., GNSS or PTP).

Measure PPS and 10 MHz phase offset among all cards.

Offsets SHOULD remain within 1 ns RMS under stable conditions.

Host-Bus Timing Consistency:

Verify that PCIe/PTM timestamps from different TimeCards yield identical time values when cross-referenced.

Any systematic offset MUST be declared and remain stable (<100 ps drift/hour).

Cross-Management Validation:

Access each TimeCard’s management interface (SMBus, IPMI, REST, etc.) using a unified script or API.

Confirm identical response structure for common attributes (clock state, alarms, firmware version).

Inconsistent or vendor-specific extensions MUST be documented and not break baseline compliance.

Failover & Ensemble Evaluation:

Supply two independent references; induce loss on one.

Validate seamless ensemble weighting or reference switching and consistent time output continuity.

Holdover Correlation:

Disconnect all references and measure divergence among TimeCards during holdover.

Drift rates SHOULD remain within declared MTIE envelopes per § 7.5.

12.5 Data Logging and Analysis

All instruments and hosts SHALL log synchronized UTC timestamps.

Logs SHALL be archived in a machine-readable format (CSV/JSON) with metadata: firmware version, card serial, test conditions, calibration date.

Reference datasets SHOULD be publicly available to the OCP-TAP community for benchmarking and regression tracking.

Derived metrics (ADEV, TDEV, MTIE, PN) SHALL be computed using open, documented algorithms to ensure transparency.

12.6 Reporting and Publication

Each interoperability campaign SHOULD produce a report including:

Test setup diagram and equipment list

Participating vendor and firmware versions

Measured inter-card offsets, jitter, and stability comparisons

Summary tables of conformance results

Observed deviations or feature interoperability issues

Recommendations for future revisions of the specification

All reports SHOULD be archived in the OCP-TAP public repository, with anonymization as needed, to encourage open collaboration and iterative improvement.

12.7 Continuous Integration and Automation

The reference testbed SHOULD be automated to support continuous testing of new firmware, drivers, or specification revisions.
Automated regression testing SHOULD include:

Periodic lock/holdover cycles

Randomized power and temperature variations

Automated management telemetry validation

Comparison of results against historical baselines

Integration with CI/CD frameworks (e.g., Jenkins, GitLab CI, or custom Python/Robot scripts) is recommended to facilitate nightly or weekly validation runs.

12.8 Traceability and Calibration

All reference sources MUST be traceable to a recognized national or international standard (e.g., UTC(NIST)).

Calibration certificates SHALL be renewed per manufacturer recommendations.

Any drift or discrepancy found during calibration MUST be recorded and compensated in subsequent measurements.

12.9 Expansion and Evolution

The testbed design is modular and intended to evolve with new TimeCard technologies, such as:

Higher-bandwidth PCIe (Gen5/Gen6) PTM enhancements

Optical or wireless synchronization paths

Quantum or chip-scale atomic clock (CSAC) integration

AI-based ensemble weighting algorithms

Vendors and community contributors SHOULD document experimental extensions to help shape future revisions of the TimeCard specification.

13. Closing Statement

The Reference Implementation and Interoperability Testbed provides a neutral, transparent, and repeatable environment for evaluating TimeCards under consistent, traceable conditions.
By following this framework, the OCP Time Appliances Project ensures that every implementation—commercial or open-source—can be validated on equal technical footing.
This testbed forms the cornerstone of long-term trust, interoperability, and performance assurance across the global ecosystem of precision timing in data centers, AI clusters, and telecommunication infrastructures.
