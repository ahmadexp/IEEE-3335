# Annex B: Test Procedures (Informative)

This annex provides example procedures for evaluating TimeCard functions and declared performance. It does not define additional conformance requirements. The applicable normative clause and supplier declaration provide the pass/fail limit.

## B.1 Test record structure

Each test record should identify:

- Test identifier and applicable clause, profile, interface, or optional feature.
- Device under test, hardware revision, firmware or gateware revision, and configuration.
- Entrance conditions, including warm-up, lock state, source, power, and environment.
- Equipment, calibration status, traceability chain, and measurement uncertainty.
- Cabling, termination, corrections, and measurement points.
- Procedure and data-processing method.
- Declared limit, decision rule, and treatment of uncertainty.
- Result, retained evidence, and any deviation from the planned method.

A representative arrangement is shown in Figure 3.

![Representative TimeCard test fixture](figures/rendered/test-fixture.pdf)

## B.2 General measurement conditions

The environment should be controlled and recorded at a level appropriate to the declared limit. The TimeCard should complete the supplier-declared warm-up and stabilization interval before a full-performance measurement begins.

The measurement system should have sufficient bandwidth, noise floor, resolution, stability, and uncertainty to distinguish the declared limit. A fixed instrument-to-device accuracy ratio is not assumed; the test report should justify the selected system and decision rule.

Cable delay, connector adapters, splitters, terminations, and reference-distribution paths should be characterized when their contribution is material. Corrections should be stated with sign convention and uncertainty.

## B.3 Functional verification

### B.3.1 Receive interfaces

| Test | Applicability | Method | Example pass/fail basis |
|------|---------------|--------|-------------------------|
| Discovery and declaration | Each receive interface | Inspect documentation and control capabilities, then compare them with the physical or logical interface. | Type, direction, protocol or signal, limits, measurement point, and source identifier are consistent. |
| Reference qualification and status | Each receive interface | Apply supplier-declared acceptable conditions and selected unacceptable counterexamples, then observe state. | Reported acceptance, rejection, source identity, and alarms agree with the declared qualification rules for the tested conditions. |
| Boundary behavior | Physical receive interfaces | Exercise declared amplitude, frequency, pulse, or protocol acceptance boundaries without exceeding protection limits. | Accepted and rejected conditions agree with the declared thresholds and hysteresis. |
| Loss and reacquisition | Each receive interface used for synchronization | Remove or invalidate the active reference, then restore it. | State, alarms, transition behavior, and reacquisition time agree with the declaration. |
| Source selection | Multiple-reference implementations | Exercise automatic and operator-controlled selection policies. | Active source and selection mode agree with the documented policy. |

P3335 does not prescribe a universal test that proves a reference valid under every possible condition. Reference qualification is evaluated using a finite, declared set of acceptable conditions and counterexamples. The test record should identify that set, the implemented qualification rules, and the limits of the resulting evidence.

### B.3.2 Providing interfaces

| Test | Applicability | Method | Example pass/fail basis |
|------|---------------|--------|-------------------------|
| 1PPS electrical profile | Physical Timing Output profile | Measure low level, high level, on-time edge, pulse width, and rise time into 50 ohms at the declared connector. | Every measured characteristic satisfies 7.3.2 after applying the stated decision rule. |
| 1PPS alignment | Physical Timing Output profile | Compare the 1PPS measurement point with the unified-timescale reference and each interface claiming alignment. | Error remains within the applicable declared and profile limits. |
| Format and epoch | Digital time output | Decode values across startup, normal operation, and a relevant boundary such as second rollover. | Format, epoch, timescale, validity, and rollover agree with the declaration. |
| Discontinuity indication | Interface that can step or become invalid | Cause a declared failover, manual adjustment, reset, or fault. | Output behavior and validity indication agree with 7.3.4 and the supplier declaration. |
| PTM behavior | PCIe Host Mapping profile with PTM | Negotiate PTM and compare its represented measurement point with the unified timescale. | Capability discovery, timestamps, correction model, and uncertainty agree with the declaration. |

### B.3.3 Control interfaces

| Test | Applicability | Method | Example pass/fail basis |
|------|---------------|--------|-------------------------|
| Required objects | All implementations | Read every object in 8.10.2 through the declared baseline control mapping. | Every object is present and does not report unsupported. |
| Atomic time read | All implementations | Repeatedly read `TC_TIME`, emphasizing second rollover and concurrent updates. | No result combines fields from different measurement instants; nanoseconds remain in range. |
| Conditional discovery | Implementations advertising conditional capabilities | Compare `TC_CAPS` with readable objects and exercised operations. | Every advertised object is mapped and unadvertised objects follow the documented unsupported behavior. |
| Invalid and reserved write | Writable mappings | Submit an out-of-range or reserved value in a non-destructive configuration. | The write is rejected and the prior value remains unchanged. |
| Reset and persistence | Reset-capable mappings | Exercise each documented reset type. | Discovery, state, persisted configuration, and time behavior agree with the mapping declaration. |
| Access control | Managed or Secure Infrastructure profile | Exercise monitoring, configuration, update, and security roles with authorized and unauthorized identities. | Each operation is allowed or denied according to the claimed profile and is reported unambiguously. |

## B.4 Performance measurements

### B.4.1 Time accuracy

Compare the declared output or timestamp measurement point with the declared reference timescale. Record enough data to support the stated maximum, percentile, RMS, or confidence result. Include fixed-delay corrections, source-to-reference uncertainty, and measurement-system uncertainty.

### B.4.2 ADEV and TDEV

Acquire a continuous phase or time-error record for a duration sufficient to support the declared averaging intervals. State the sample interval, estimator, overlap, detrending, gap handling, and confidence basis. Compare the resulting curve or points with the bounded declaration.

### B.4.3 MTIE

Acquire the time-error sequence at the declared measurement point and compute MTIE for the stated observation intervals. Record total data length, sample interval, window implementation, missing-data treatment, and preprocessing. Compare each applicable interval with the declared bound.

### B.4.4 Phase noise

Measure the declared carrier with an analyzer configuration whose residual floor is characterized. Record offset range, resolution and measurement bandwidths, cross-correlation settings, averaging, spurs, and instrument floor. Compare the trace with the declared mask or points.

### B.4.5 Pulse timing variation

Capture the declared edge using the stated termination and bandwidth. Use the declared sample population and ideal-event model. Compute the exact RMS, standard-deviation, percentile, peak-to-peak, or bounded statistic stated by the supplier.

### B.4.6 Holdover

Lock the TimeCard for at least the declared preconditioning interval, record initial time and frequency error, remove all applicable references, and observe the declared holdover duration. Record the temperature and power profile. Compare time error or MTIE versus elapsed holdover time with the supplier's bound, then verify reference-restoration behavior.

## B.5 Environmental and transition tests

Environmental tests should follow the supplier-declared profile and the reporting fields in 9.5. Timing measurements should continue during the applied stimulus when the claim concerns operational performance, rather than relying only on a post-test functional check.

Transition testing should cover each state change identified in 6.9. The record should correlate physical outputs, digital timestamps, control state, alarms, and events so that continuity and reporting behavior can be evaluated against the same timeline.

## B.6 Reporting

The final report should include raw or losslessly transformed data, processing software and version, configuration files, plots with units and uncertainty, and a clear mapping from every conclusion to the applicable requirement and declared limit. When data cannot be shared, the report should identify the retained evidence and access authority.
