# 6. Performance Specifications (Normative)

This clause defines the performance reporting and characterization requirements for TimeCard implementations. Base conformance does not define a single universal numeric performance class for all use cases. Instead, it requires performance claims to be stated using common metrics, defined measurement points, traceable methods, and declared operating conditions.

## 6.1 Performance Declaration Model

Suppliers **shall** publish performance declarations for each conforming TimeCard implementation. Each declared value **shall** identify:

- The metric being reported.
- The measurement point.
- The operating mode, such as locked, holdover, free-running, warm-up, failover, or recovery.
- The TimeCard synchronization source and reference timescale.
- The applicable temperature range, voltage range, airflow or cooling condition, and other environmental conditions.
- The minimum warm-up time and lock time required before the declaration applies.
- The observation interval, averaging time, bandwidth, sample count, or statistical confidence basis used.
- The measurement equipment class and traceability path.

Each required performance declaration **shall** include at least one bounded value or limit. Typical values may be provided in addition to, but not instead of, the bounded value.

A declaration using a performance class or mask **shall** identify the governing document and edition, applicable clause, class or mask identifier, parameter set, observation or averaging intervals, filtering, and acceptance rule. Incorporation by reference is permitted as specified in 4.6; it does not remove the need to identify implementation-specific conditions. Access to underlying test records is governed by 4.7 and 4.8 and is distinct from publication of the performance declaration.

## 6.2 Performance Classes

This standard uses a reporting-only base performance model. A TimeCard conforms to the base performance requirements when it reports the applicable metrics in this clause using the declared measurement methods and operating conditions.

Named numeric performance classes are not defined by this standard. A supplier, procurement profile, application profile, or external standard may define additional numeric classes. If an implementation claims such a class, the class **shall** identify all applicable metric limits, measurement points, operating states, and environmental conditions, with the reference details required by 4.6 and 6.1.

## 6.3 General Measurement Requirements

Measurement results used to support conformance claims **shall** be metrologically traceable to a recognized national metrology institute or another declared reference through a documented calibration chain. Measurement methods **shall** conform to the applicable definitions in IEEE Std 1139-2022 [2], IEEE Std 1193-2022 [3], ITU-T Recommendation G.810 (08/1996) [10], or ITU-T Recommendation G.8260 (11/2022) [11] when those metrics are used.

The reference arrangement **shall** be suitable for the measurand, declared limit, and uncertainty of the reported result. Suitable arrangements may include calibrated laboratory references, characterized GNSS references, or characterized GNSS simulators. A direct UTC(k) connection or measurement at a national metrology institute is not required. The report **shall** identify the reference timescale or frequency, calibration and reference relationships, and relevant uncertainty contributions. Use of GNSS or a simulator does not itself establish traceability or an absolute UTC reference.

A measurement relative to an applied input reference **shall** be distinguished from an absolute time-accuracy claim relative to UTC or another external timescale. The report **shall** identify shared reference paths and account for correlated errors that can cancel in an input-to-output comparison. Evidence of relative transfer performance **shall** not be presented as evidence of absolute time accuracy without the additional reference relationship and uncertainty needed for that claim.

The measurement uncertainty, instrument noise floor, measurement bandwidth, averaging configuration, sample count, data treatment, and environmental conditions **shall** be documented with the reported result. The measurement point **shall** be identified in enough detail that another laboratory can reproduce the setup.

When a measured result is compared with a declared limit, the test report **shall** state the decision rule and treatment of measurement uncertainty. A pass/fail conclusion **shall** not silently treat an uncertainty interval that crosses the limit as an unqualified pass.

If the term **jitter** is used, the implementation documentation **shall** define the exact jitter metric, measurement bandwidth, sample population, and statistical calculation. Constant time error, dynamic time error, phase noise, MTIE, TDEV, ADEV, noise transfer, and noise tolerance **shall** not be used interchangeably.

## 6.4 Time Error and Noise Response

### 6.4.1 Time accuracy and TimeCard timestamp accuracy

Time accuracy declarations **shall** state the error of a TimeCard time or phase output, or indicated time, relative to a declared reference timescale and TimeCard synchronization source.

For each time accuracy declaration, the supplier **shall** document:

- Reference timescale and TimeCard synchronization source, such as GNSS system time and receiver, UTC(k) and laboratory reference, TAI and primary reference, PTP timescale and grandmaster, or another declared combination.
- Measurement point, such as 1PPS output, Time of Day output, or register-read indication of TimeCard time.
- Maximum time error or another explicitly defined bounded statistic.
- Statistical basis, such as maximum observed value, percentile, RMS value, or confidence interval.
- Constant time error and dynamic time error components when they can be separately estimated under the declared method.
- Valid temperature range and environmental profile.
- Minimum lock time before the declaration applies.
- Relationship between the declared reference timescale and UTC or TAI, if the declared timescale is not itself UTC or TAI.

If an implementation reports IEEE 1588-2019 [4] `clockAccuracy` values, the values **shall** correspond to the measured or declared time-accuracy range for the applicable operating mode.

When TimeCard timestamp accuracy is claimed for an event-capture or timestamping function, the supplier **shall** state a bounded error between the assigned timestamp and the declared reference time at the corresponding event instant. The supplier **shall** identify the event marker, timestamping measurement point, reference timescale, TimeCard synchronization source, resolution, granularity, latency, fixed corrections, known asymmetry, uncertainty contributors, and operating conditions. Timestamp resolution or granularity **shall** not be represented as TimeCard timestamp accuracy.

### 6.4.2 Noise transfer

For each receive interface used to discipline the unified timescale, the supplier **shall** characterize noise transfer to each providing interface for which synchronized performance is declared. The characterization **shall** identify:

- Receive and providing measurement points.
- Applied timing-variation type, amplitude, and frequency range or observation intervals.
- Reference-selection state, local timing function configuration, and operating mode.
- Transfer result expressed as a gain and phase response, bandwidth and peaking bounds, an input-to-output mask, or another explicitly defined bounded response.
- Measurement bandwidth, filtering, data treatment, observation duration, and measurement uncertainty.

The applied timing variation may be phase modulation, wander, packet-delay variation, or another disturbance appropriate to the receive interface. The supplier **shall** define the stimulus and calculation method sufficiently for another laboratory to reproduce the result.

### 6.4.3 Noise tolerance

For each receive interface used to discipline the unified timescale, the supplier **shall** characterize noise tolerance. The characterization **shall** identify:

- Receive-interface measurement point, nominal input conditions, and operating mode.
- Applied timing-variation type, amplitude profile, frequency range or observation intervals, and duration.
- Acceptance criteria, including the applicable reference-validity, alarm, reference-switching, lock, holdover, and providing-interface performance outcomes.
- Threshold, mask, or other bounded input condition that satisfies the declared acceptance criteria.
- Hysteresis, dwell time, filtering, data treatment, and measurement uncertainty relevant to the result.

Noise tolerance **shall** be stated separately from electrical noise immunity and from noise transfer. A tolerance declaration **shall** not imply an output-performance bound unless that bound is included in its acceptance criteria.

## 6.5 Time Stability

Time stability declarations **shall** characterize variation of the TimeCard time output or timestamp stream over a defined observation interval.

Suppliers **shall** report MTIE for time outputs or timestamp streams for which bounded time-error variation is claimed, or when required by a claimed performance class. The MTIE declaration **shall** include observation intervals, measurement point, lock state, environmental conditions, and applicable limit or measured result. MTIE **shall** not be represented as an absolute time-error bound; absolute time-error declarations are specified in 6.4.1.

Suppliers should report TDEV for time outputs or timestamp streams where stochastic time deviation is operationally relevant. TDEV declarations **shall** include averaging intervals and the method used to compute the result.

## 6.6 Frequency Stability and Phase Noise

Frequency stability declarations **shall** characterize the frequency output or local timing function at a declared measurement point over one or more averaging intervals. Characterization of inaccessible internal components is not required independently of a claim about those components.

Suppliers **shall** report frequency accuracy and temperature stability for the local timing function or for each frequency output for which a frequency-performance claim is made.

Suppliers should report ADEV where fractional-frequency stability at the declared TimeCard measurement point is relevant to the claim. ADEV declarations **shall** include the averaging intervals and measurement point. ADEV, TDEV, and fractional-frequency offset characterize different quantities and are not interchangeable.

For periodic outputs such as 10 MHz, suppliers should report phase noise as a function of offset frequency. Phase-noise declarations **shall** identify carrier frequency, offset-frequency range, measurement bandwidth, instrument configuration, and measurement point.

A claimed application profile may specify time-domain jitter or wander instead of a phase-noise requirement. The supplier **shall** identify the quantity actually evaluated and the applicable method. When a result is converted between time and frequency domains, the conversion **shall** identify its assumptions, weighting or filtering, integration limits, and uncertainty. An integrated time-domain result **shall** not be represented as verification of a spectral mask unless the method establishes compliance with that mask over its specified offset-frequency range.

## 6.7 Pulse and Event Timing

For pulse outputs such as 1PPS, suppliers **shall** document:

- On-time edge definition.
- Output polarity.
- Pulse width range.
- Rise and fall time measurement method.
- Time error relative to the declared reference, including constant and dynamic components where separately estimable, and the stated bound or timing-variation statistic.
- Peak-to-peak or bounded time variation when claimed.
- Alignment to other providing interfaces of the same TimeCard.

Pulse timing declarations **shall** identify sample interval, observation duration, measurement bandwidth, reference model, and treatment of fixed offsets and missing events. Domain-specific jitter or wander results may supplement these declarations when the applicable definition and sampling method support the reported bandwidth.

For event-capture or timestamping inputs, suppliers **shall** document the event measurement point, timestamp resolution, granularity, latency, fixed corrections, and known uncertainty contributors. Any claimed TimeCard timestamp accuracy **shall** also satisfy 6.4.1.

## 6.8 Holdover Performance

Holdover declarations **shall** characterize accumulated time error after loss of all external synchronization references being used.

For each holdover declaration, the supplier **shall** document:

- Holdover entry condition and triggering event.
- TimeCard synchronization source and lock duration before holdover begins.
- Minimum warm-up and stabilization conditions before holdover begins.
- Measurement point.
- Bounded time error versus elapsed holdover time, reference timescale, and whether the bound is absolute or relative to the error at holdover entry.
- Initial time error and uncertainty, or an explicit statement that the initial error is unknown and the result establishes only an initial-offset-relative bound.
- MTIE versus observation interval when bounded time-error variation or a performance class requiring MTIE is claimed.
- Temperature profile, sensor location, rate of change, dwell conditions, and input-voltage conditions during holdover.
- Behavior when the reference is restored, including qualification, reacquisition, phase and frequency transients, continuity, and the condition for returning to the locked state.

MTIE declarations **shall** use the definitions in ITU-T Recommendation G.810 (08/1996) [10] or ITU-T Recommendation G.8260 (11/2022) [11]. MTIE measures variation and does not include a constant initial offset; it **shall** not replace the holdover time-error envelope. An initial-offset-relative result **shall** not be described as an absolute time-error bound. Other holdover indicators, such as aging rate or estimated drift, may be reported in addition to the applicable error and stability declarations.

An applicable holdover specification may supply limits and test conditions by reference under 4.6. The declaration **shall** identify any conditions or reporting fields above that the referenced specification does not cover.

## 6.9 Dynamic Operation

Suppliers **shall** characterize timing behavior during operational transitions that can affect output phase, frequency, or timestamp values. The characterization **shall** include, where applicable:

- Cold-start and warm-start lock acquisition time.
- Transition from locked operation to holdover.
- Transition from holdover to locked operation.
- Reference failover between two valid synchronization sources.
- Manual time step or frequency steering command.
- Firmware update or restart behavior if timing service is interrupted or degraded.
- Host entry into and recovery from a low-power, sleep, or hibernation state.
- Orderly removal, surprise removal, hot-plug disconnection, and reinsertion of a host-connected TimeCard.
- Driver, host service, or time-provider unload, reload, failure, and restart.
- A host-clock discontinuity that invalidates a host-time correlation or a sample awaiting delivery.

For each transition, the supplier **shall** document whether the unified timescale remains continuous and whether a discontinuity can occur in phase or in a time derivative of phase. The documentation **shall** bound applicable phase steps, frequency steps, frequency-slope changes, kinks or corners, and recovery transients, and **shall** identify how each condition is reported through the control interface.

An applicable external specification may supply transition requirements by reference under 4.6. The supplier **shall** identify its coverage and separately characterize applicable transitions not covered by it, including host and driver lifecycle transitions.

## 6.10 Environmental and host-system effects

Performance declarations **shall** identify the environmental and host-system conditions under which the declared values apply. The following effects **shall** be characterized when applicable to the declared deployment profile:

- Temperature and thermal-gradient sensitivity.
- Input-voltage variation and supply noise sensitivity.
- Vibration sensitivity.
- Airflow and host thermal loading.
- Host-bus activity, electromagnetic interference, or crosstalk that can affect timing outputs.
- Host scheduling, interrupt or polling latency, driver and service processing, and host power-management policy when performance is declared at a host API or software measurement point.
- Virtualization, I/O translation, or resource sharing when those host mechanisms are present in the declared deployment profile.

If performance is declared only for a subset of the environmental range specified in Clause 9, that subset **shall** be explicitly stated.

When time-transfer performance is declared at a host API or software measurement point, the supplier **shall** characterize the applicable software-path latency, asymmetry, dispersion, sample age, and host-time correlation window. The declaration **shall** identify the host clock, operating-system and driver revisions, power state, load conditions, and measurement method.

## 6.11 Performance Documentation Checklist

The performance section of a datasheet or conformance statement **shall** include the following items when applicable, together with the governing specification, edition, class or mask, configuration, and acceptance rule required by 6.1:

| Category | Required reporting content |
|----------|-----------------------------|
| Time error | TimeCard synchronization source, reference timescale, measurement point, bounded error, constant and dynamic components, statistic, temperature range, lock time |
| TimeCard timestamp accuracy | Event marker and measurement point, reference timescale, synchronization source, bounded timestamp error, resolution, granularity, corrections, latency, uncertainty |
| Time stability | MTIE and applicable TDEV intervals, measurement point, state, environmental profile |
| Frequency stability | Frequency accuracy, temperature stability, applicable ADEV intervals, measurement point |
| Phase noise | Carrier frequency, offset-frequency range, measurement bandwidth, phase-noise curve or limits |
| Pulse timing | Edge definition, pulse width, rise/fall time, time-error bound and timing-variation statistic, sampling and bandwidth, alignment to unified timescale |
| Noise transfer | Input and output measurement points, stimulus, operating state, transfer response or mask, bandwidth, uncertainty |
| Noise tolerance | Input measurement point and nominal conditions, stimulus and duration, acceptance criteria, tolerance mask or threshold, uncertainty |
| Holdover | Entry condition, prior lock duration, initial error and uncertainty, absolute or initial-offset-relative error envelope, applicable MTIE intervals, temperature profile |
| Transitions | Lock acquisition, failover, holdover exit, phase steps, reporting mechanism |
| Environment | Temperature, voltage, vibration, airflow, and host-integration assumptions |
