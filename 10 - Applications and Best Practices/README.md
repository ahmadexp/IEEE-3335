# 10. Applications and Best Practices (Informative)

This clause provides deployment considerations for TimeCard systems. It does not add or alter conformance requirements. Application-specific accuracy, availability, security, safety, and regulatory limits remain the responsibility of the system designer and operator.

## 10.1 Selecting a TimeCard

A useful selection process begins with the system timing requirement and works back to the TimeCard measurement point. The evaluation should consider:

- Required timescale and traceability path.
- Maximum permitted time error, frequency offset, or phase error at the consuming application.
- Network, host-bus, software, cable, and interface error between the TimeCard measurement point and that application.
- Required availability and maximum duration of reference loss.
- Environmental and host-integration conditions.
- Monitoring, update, access-control, and recovery needs.

Timestamp granularity or oscillator type alone does not establish end-to-end accuracy. The complete error and uncertainty path and budget should be evaluated.

## 10.2 Application considerations

### 10.2.1 Data centers and distributed computing

TimeCards can serve as PTP grandmasters, host timing sources, or monitored references. Deployments commonly consider redundant references, independent failure domains, hardware timestamping, host PHC integration, monitoring at scale, and the effect of network asymmetry. The relevant accuracy target should be set by the application rather than inferred from the interface technology.

### 10.2.2 Telecommunications

Telecommunications deployments can require specific PTP or frequency-synchronization profiles and bounded holdover during reference failure. Source traceability, packet-network support, asymmetry, environmental qualification, and profile-specific limits should be evaluated together.

### 10.2.3 Regulated event timestamping

Financial, industrial, and other regulated systems can require demonstrable traceability, bounded divergence from UTC, retained evidence, and controlled configuration. Operators should map the applicable rule to the actual event-timestamp measurement point and include all distribution and capture delays in the uncertainty analysis.

### 10.2.4 Power and industrial systems

Industrial and power-system deployments can combine precise timing requirements with extended environmental, EMC, safety, and availability constraints. Applicable industry profiles, qualification standards, isolation, grounding, and fail-safe behavior should be identified by the system specification.

### 10.2.5 Scientific and metrology systems

Scientific applications can prioritize phase coherence, low phase noise, long observation intervals, or calibration access. The selected metrics and test setup should match the experiment's sensitivity and should preserve raw observations needed for later analysis.

## 10.3 Installation

### 10.3.1 Thermal and mechanical integration

The host should provide the airflow, inlet temperature, orientation, and mounting conditions used by the supplier's full-performance declaration. Large local heat sources and changing fan policies can introduce thermal gradients and timing effects that vary independently of ambient temperature.

### 10.3.2 Cabling and delay

Cable type, length, temperature coefficient, connector condition, termination, and adapter delay can materially affect a physical timing measurement point. Fixed corrections should use a consistent sign convention and should be recorded with uncertainty. Installation changes, including connector replacement, cable rerouting, adapter changes, or altered strain relief, should trigger review or recalibration.

### 10.3.3 Antenna and RF paths

GNSS antenna placement should provide the required sky view and should account for cable loss, antenna power, lightning protection, RF interference, jamming, spoofing, and correlated-failure risks. Antenna delay and receiver configuration should be included in the declared reference path.

### 10.3.4 Host software and driver integration

Host software should begin with the declared mapping and capability information, validate every resource range, and keep optional resources inaccessible until the active implementation or image establishes their semantics. Successful reads from guessed MMIO locations, PCI identifiers, or core-version values alone are not reliable evidence that an optional feature is implemented.

Multi-card software should select a card using `TC_INSTANCE_ID` or `TC_SERIAL` when available. An enumeration index or operating-system device number can change after removal, reinsertion, firmware update, or inventory changes and should not be used as the persistent key for configuration or calibration data.

Software correlating TimeCard time with a host clock should preserve both host bounds, the correlation window, capture and discontinuity sequences, card state, source validity, sample age, and the card and host timescales. A raw hardware counter should not be labeled UTC, or used to discipline a host clock, until the timescale relationship and applicable leap information are valid.

Only one authorized component should control time setting or discipline at a time. Monitoring applications, command-line tools, background discipline services, and host time providers should share the ownership and authorization mechanism defined by the mapping rather than applying independent steering actions.

Sleep, wake, hibernation, driver restart, orderly removal, surprise removal, and tunneled-PCIe disconnection should be treated as normal lifecycle cases. Software should cancel bounded operations, stop hardware access when resources disappear, revalidate discovery after recovery, and reject samples captured before an intervening host-clock discontinuity.

Annex E gives platform-specific examples for Windows, macOS, and Linux.

## 10.4 Operation and maintenance

### 10.4.1 Reference policy

Reference priorities and qualification thresholds should reflect independence, accuracy, stability, and failure behavior. A secondary source that shares an antenna, power supply, network path, or upstream clock with the primary source might not provide meaningful redundancy.

### 10.4.2 Monitoring and alarms

Operators should monitor at least source availability, active source, lock state, holdover elapsed time, phase error, frequency offset, environmental conditions, alarms, and software revisions. Alert thresholds should be tied to the time remaining before an application limit might be exceeded, not only to device state names.

### 10.4.3 Updates and configuration

Configuration and update changes should be staged, authorized, recorded, and evaluated for their effect on time continuity. A rollback plan should account for configuration compatibility, security policy, calibration data, and the possibility that timing service is interrupted during recovery.

### 10.4.4 Calibration and evidence retention

Calibration and verification intervals should be based on the declared performance, observed aging, environmental exposure, and application risk. Records should preserve the device identity, configuration, reference chain, uncertainty, result, and processing method.

## 10.5 Common failure syndromes

| Symptom | Possible cause | Investigation |
|---------|----------------|---------------|
| Constant offset | Cable or antenna delay, wrong edge, epoch mismatch, or unapplied correction | Trace the measurement point, correction sign, and correction value through the complete timing path. |
| Intermittent source loss | Marginal signal level, RF interference, packet loss, threshold hysteresis, loose or poorly retained connectors, broken or intermittent cabling, or lack of needed redundancy | Inspect and mechanically verify connectors and cabling, then correlate source health, raw signal indicators, network data, and event logs. |
| Excessive holdover error | Initial frequency offset, temperature change, aging, insufficient preconditioning, or model error | Compare the holdover test conditions with the supplier declaration and recorded environment. |
| Host timestamp disagreement | Different epochs or timescales, non-atomic reads, host-bus delay, or conversion error | Validate the timestamp mapping, rollover behavior, atomicity, and correction model. |
| Unexpected phase step | Reference switch, manual adjustment, restart, or invalid continuity assumption | Correlate physical outputs with control state and transition events. |
| Management loss during host fault | Control path shares host power, software, or network dependencies | Review the intended out-of-band boundary and correlated-failure assumptions. |
