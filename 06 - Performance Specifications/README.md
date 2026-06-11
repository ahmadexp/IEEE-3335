# 6. Performance Specifications (Normative)

This clause defines the performance reporting and characterization requirements for TimeCard implementations. The standard does not define a single universal numeric performance class for all use cases. Instead, it requires performance claims to be stated using common metrics, defined measurement points, traceable methods, and declared operating conditions.

## 6.1 Performance Declaration Model

Manufacturers shall publish performance declarations for each conforming TimeCard implementation. Each declared value shall identify:

- The metric being reported.
- The measurement point.
- The operating mode, such as locked, holdover, free-running, warm-up, failover, or recovery.
- The reference source or reference timescale.
- The applicable temperature range, voltage range, airflow or cooling condition, and other environmental conditions.
- The minimum warm-up time and lock time required before the declaration applies.
- The observation interval, averaging time, bandwidth, sample count, or statistical confidence basis used.
- The measurement equipment class and traceability path.

Performance values should be stated as bounded claims rather than typical-only values. Typical values may be provided in addition to bounded claims.

## 6.2 General Measurement Requirements

All measurements used to support conformance claims shall be made with equipment traceable to a recognized national metrology institute or other declared primary reference. Measurement methods shall conform to the applicable definitions in IEEE Std 1139, IEEE Std 1193, ITU-T G.810, or ITU-T G.8260 when those metrics are used.

The measurement uncertainty, instrument noise floor, measurement bandwidth, averaging configuration, and environmental conditions shall be documented with the reported result. The measurement point shall be identified in enough detail that another laboratory can reproduce the setup.

If the term **jitter** is used, the implementation documentation shall define the exact jitter metric, measurement bandwidth, sample population, and statistical calculation. Time jitter, phase noise, MTIE, TDEV, and ADEV shall not be used interchangeably.

## 6.3 Time Accuracy

Time accuracy declarations shall state the error of a TimeCard output or timestamp relative to a declared reference timescale or source.

For each time accuracy declaration, the manufacturer shall document:

- Source of standard time, such as GNSS system time, UTC(k), TAI, PTP grandmaster time, or another declared reference.
- Measurement point, such as 1PPS output, Time of Day output, PTP egress timestamp, PTM timestamp, or register-read timestamp.
- Maximum time error or another explicitly defined bounded statistic.
- Statistical basis, such as maximum observed value, percentile, RMS value, or confidence interval.
- Static error and dynamic error components when they are separately known.
- Valid temperature range and environmental profile.
- Minimum lock time before the declaration applies.
- Relationship between the declared source and UTC or TAI, if the declared source is not itself UTC or TAI.

If an implementation reports IEEE 1588 clockAccuracy values, the values shall correspond to the measured or declared accuracy range for the applicable operating mode.

## 6.4 Time Stability

Time stability declarations shall characterize variation of the TimeCard time output or timestamp stream over a defined observation interval.

Manufacturers shall report MTIE for time outputs or timestamp streams for which bounded time-error behavior is claimed. The MTIE declaration shall include observation intervals, measurement point, lock state, environmental conditions, and applicable limit or measured result.

Manufacturers should report TDEV for time outputs or timestamp streams where stochastic time deviation is operationally relevant. TDEV declarations shall include averaging intervals and the method used to compute the result.

## 6.5 Frequency Stability and Phase Noise

Frequency stability declarations shall characterize the frequency output or local timing function over one or more averaging intervals.

Manufacturers shall report frequency accuracy and temperature stability for the local timing function or for each frequency output for which a frequency-performance claim is made.

Manufacturers should report ADEV for frequency outputs or oscillator functions where long-term or short-term frequency stability is relevant. ADEV declarations shall include the averaging intervals and measurement point.

For periodic outputs such as 10 MHz, manufacturers should report phase noise as a function of offset frequency. Phase-noise declarations shall identify carrier frequency, offset-frequency range, measurement bandwidth, instrument configuration, and measurement point.

## 6.6 Pulse and Event Timing

For pulse outputs such as 1PPS, manufacturers shall document:

- On-time edge definition.
- Output polarity.
- Pulse width range.
- Rise and fall time measurement method.
- RMS time jitter or another explicitly defined short-term timing variation metric.
- Peak-to-peak or bounded time variation when claimed.
- Alignment to other providing interfaces of the same TimeCard.

For event-capture or timestamping inputs, manufacturers shall document the event measurement point, timestamp resolution, granularity, latency, fixed corrections, and known uncertainty contributors.

## 6.7 Holdover Performance

Holdover declarations shall characterize accumulated time error after loss of all applicable external synchronization references.

For each holdover declaration, the manufacturer shall document:

- Holdover entry condition and triggering event.
- Reference source and lock duration before holdover begins.
- Minimum warm-up and stabilization conditions before holdover begins.
- Measurement point.
- Maximum time error or MTIE versus elapsed holdover time.
- Temperature profile and voltage conditions during holdover.
- Behavior when the reference is restored.

MTIE as defined by ITU-T G.810 or ITU-T G.8260 shall be used when reporting bounded holdover time error. Other holdover indicators, such as aging rate or estimated drift, may be reported in addition to MTIE.

## 6.8 Dynamic Operation

Manufacturers shall characterize timing behavior during operational transitions that can affect output phase, frequency, or timestamp values. The characterization shall include, where applicable:

- Cold-start and warm-start lock acquisition time.
- Transition from locked operation to holdover.
- Transition from holdover to locked operation.
- Reference failover between two valid sources.
- Manual time step or frequency steering command.
- Firmware update or restart behavior if timing service is interrupted or degraded.

For each transition, the manufacturer shall document whether the unified timescale remains continuous, whether an output phase step can occur, and how the condition is reported through the control interface.

## 6.9 Environmental and System-Integration Effects

Performance declarations shall identify the environmental and host-system conditions under which the declared values apply. The following effects shall be characterized when applicable to the declared deployment profile:

- Temperature and thermal-gradient sensitivity.
- Input-voltage variation and supply noise sensitivity.
- Vibration sensitivity.
- Airflow and host thermal loading.
- Host-bus activity, electromagnetic interference, or crosstalk that can affect timing outputs.

If performance is declared only for a subset of the environmental range specified in Clause 9, that subset shall be explicitly stated.

## 6.10 Performance Documentation Checklist

The performance section of a datasheet or conformance statement shall include the following items when applicable:

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
