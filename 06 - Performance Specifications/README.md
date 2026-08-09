# 6. Performance Specifications (Normative)

This clause defines the performance reporting and characterization requirements for TimeCard implementations. Base conformance does not define a single universal numeric performance class for all use cases. Instead, it requires performance claims to be stated using common metrics, defined measurement points, traceable methods, and declared operating conditions.

## 6.1 Performance Declaration Model

Suppliers **shall** publish performance declarations for each conforming TimeCard implementation. Each declared value **shall** identify:

- The metric being reported.
- The measurement point.
- The operating mode, such as locked, holdover, free-running, warm-up, failover, or recovery.
- The reference source or reference timescale.
- The applicable temperature range, voltage range, airflow or cooling condition, and other environmental conditions.
- The minimum warm-up time and lock time required before the declaration applies.
- The observation interval, averaging time, bandwidth, sample count, or statistical confidence basis used.
- The measurement equipment class and traceability path.

Each required performance declaration **shall** include at least one bounded value or limit. Typical values may be provided in addition to, but not instead of, the bounded value.

## 6.2 Performance Classes

This standard uses a reporting-only base performance model. A TimeCard conforms to the base performance requirements when it reports the applicable metrics in this clause using the declared measurement methods and operating conditions.

Named numeric performance classes are not defined by this standard. A supplier, procurement profile, or application profile may define additional numeric classes. If an implementation claims such a class, the class **shall** identify all applicable metric limits, measurement points, operating states, and environmental conditions.

## 6.3 General Measurement Requirements

Measurement results used to support conformance claims **shall** be metrologically traceable to a recognized national metrology institute or another declared reference through a documented calibration chain. Measurement methods **shall** conform to the applicable definitions in IEEE Std 1139-2022 [2], IEEE Std 1193-2022 [3], ITU-T Recommendation G.810 (08/1996) [10], or ITU-T Recommendation G.8260 (11/2022) [11] when those metrics are used.

The measurement uncertainty, instrument noise floor, measurement bandwidth, averaging configuration, sample count, data treatment, and environmental conditions **shall** be documented with the reported result. The measurement point **shall** be identified in enough detail that another laboratory can reproduce the setup.

When a measured result is compared with a declared limit, the test report **shall** state the decision rule and treatment of measurement uncertainty. A pass/fail conclusion **shall** not silently treat an uncertainty interval that crosses the limit as an unqualified pass.

If the term **jitter** is used, the implementation documentation **shall** define the exact jitter metric, measurement bandwidth, sample population, and statistical calculation. Time jitter, phase noise, MTIE, TDEV, and ADEV **shall** not be used interchangeably.

## 6.4 Time Accuracy

Time accuracy declarations **shall** state the error of a TimeCard output or timestamp relative to a declared reference timescale or source.

For each time accuracy declaration, the supplier **shall** document:

- Source of standard time, such as GNSS system time, UTC(k), TAI, PTP grandmaster time, or another declared reference.
- Measurement point, such as 1PPS output, Time of Day output, PTP egress timestamp, PTM timestamp, or register-read timestamp.
- Maximum time error or another explicitly defined bounded statistic.
- Statistical basis, such as maximum observed value, percentile, RMS value, or confidence interval.
- Static error and dynamic error components when they are separately known.
- Valid temperature range and environmental profile.
- Minimum lock time before the declaration applies.
- Relationship between the declared source and UTC or TAI, if the declared source is not itself UTC or TAI.

If an implementation reports IEEE 1588-2019 [4] `clockAccuracy` values, the values **shall** correspond to the measured or declared accuracy range for the applicable operating mode.

## 6.5 Time Stability

Time stability declarations **shall** characterize variation of the TimeCard time output or timestamp stream over a defined observation interval.

Suppliers **shall** report MTIE for time outputs or timestamp streams for which bounded time-error behavior is claimed. The MTIE declaration **shall** include observation intervals, measurement point, lock state, environmental conditions, and applicable limit or measured result.

Suppliers should report TDEV for time outputs or timestamp streams where stochastic time deviation is operationally relevant. TDEV declarations **shall** include averaging intervals and the method used to compute the result.

## 6.6 Frequency Stability and Phase Noise

Frequency stability declarations **shall** characterize the frequency output or local timing function over one or more averaging intervals.

Suppliers **shall** report frequency accuracy and temperature stability for the local timing function or for each frequency output for which a frequency-performance claim is made.

Suppliers should report ADEV for frequency outputs or oscillator functions where long-term or short-term frequency stability is relevant. ADEV declarations **shall** include the averaging intervals and measurement point.

For periodic outputs such as 10 MHz, suppliers should report phase noise as a function of offset frequency. Phase-noise declarations **shall** identify carrier frequency, offset-frequency range, measurement bandwidth, instrument configuration, and measurement point.

## 6.7 Pulse and Event Timing

For pulse outputs such as 1PPS, suppliers **shall** document:

- On-time edge definition.
- Output polarity.
- Pulse width range.
- Rise and fall time measurement method.
- RMS time jitter or another explicitly defined short-term timing variation metric.
- Peak-to-peak or bounded time variation when claimed.
- Alignment to other providing interfaces of the same TimeCard.

For event-capture or timestamping inputs, suppliers **shall** document the event measurement point, timestamp resolution, granularity, latency, fixed corrections, and known uncertainty contributors.

## 6.8 Holdover Performance

Holdover declarations **shall** characterize accumulated time error after loss of all external synchronization references being used.

For each holdover declaration, the supplier **shall** document:

- Holdover entry condition and triggering event.
- Reference source and lock duration before holdover begins.
- Minimum warm-up and stabilization conditions before holdover begins.
- Measurement point.
- Maximum time error or MTIE versus elapsed holdover time.
- Temperature profile, sensor location, rate of change, dwell conditions, and input-voltage conditions during holdover.
- Behavior when the reference is restored, including qualification, reacquisition, phase and frequency transients, continuity, and the condition for returning to the locked state.

MTIE as defined by ITU-T Recommendation G.810 (08/1996) [10] or ITU-T Recommendation G.8260 (11/2022) [11] **shall** be used when reporting bounded holdover time error. Other holdover indicators, such as aging rate or estimated drift, may be reported in addition to MTIE.

## 6.9 Dynamic Operation

Suppliers **shall** characterize timing behavior during operational transitions that can affect output phase, frequency, or timestamp values. The characterization **shall** include, where applicable:

- Cold-start and warm-start lock acquisition time.
- Transition from locked operation to holdover.
- Transition from holdover to locked operation.
- Reference failover between two valid sources.
- Manual time step or frequency steering command.
- Firmware update or restart behavior if timing service is interrupted or degraded.

For each transition, the supplier **shall** document whether the unified timescale remains continuous and whether a discontinuity can occur in phase or in a time derivative of phase. The documentation **shall** bound applicable phase steps, frequency steps, frequency-slope changes, kinks or corners, and recovery transients, and **shall** identify how each condition is reported through the control interface.

## 6.10 Environmental and host-system effects

Performance declarations **shall** identify the environmental and host-system conditions under which the declared values apply. The following effects **shall** be characterized when applicable to the declared deployment profile:

- Temperature and thermal-gradient sensitivity.
- Input-voltage variation and supply noise sensitivity.
- Vibration sensitivity.
- Airflow and host thermal loading.
- Host-bus activity, electromagnetic interference, or crosstalk that can affect timing outputs.

If performance is declared only for a subset of the environmental range specified in Clause 9, that subset **shall** be explicitly stated.

## 6.11 Performance Documentation Checklist

The performance section of a datasheet or conformance statement **shall** include the following items when applicable:

| Category | Required reporting content |
|----------|-----------------------------|
| Time accuracy | Reference source, measurement point, bounded error, statistic, temperature range, lock time |
| Time stability | MTIE and applicable TDEV intervals, measurement point, state, environmental profile |
| Frequency stability | Frequency accuracy, temperature stability, applicable ADEV intervals, measurement point |
| Phase noise | Carrier frequency, offset-frequency range, measurement bandwidth, phase-noise curve or limits |
| Pulse timing | Edge definition, pulse width, rise/fall time, time jitter definition, alignment to unified timescale |
| Holdover | Entry condition, prior lock duration, MTIE/error versus elapsed time, temperature profile |
| Transitions | Lock acquisition, failover, holdover exit, phase steps, reporting mechanism |
| Environment | Temperature, voltage, vibration, airflow, and host-integration assumptions |
