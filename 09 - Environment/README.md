# 9. Environmental Specifications (Normative)

This clause specifies environmental, mechanical, electrical, qualification, and lifecycle information needed to evaluate a TimeCard and its declared timing performance. It uses a declaration model because the applicable limits depend on implementation form and deployment environment.

## 9.1 Applicability

A conforming implementation **shall** identify its intended deployment environment and implementation form. Physical TimeCards **shall** provide the declarations applicable to their enclosure, board, connectors, power, cooling, and service conditions. Embedded or virtualized implementations **shall** identify the host-provided environmental and resource conditions on which their declared performance depends.

An environmental declaration **shall** distinguish:

- **Operating limits**, within which the implementation is functional.
- **Full-performance limits**, within which the Clause 6 performance declarations apply.
- **Storage and transport limits**, within which the unpowered implementation is not permanently damaged or degraded.
- **Survival limits**, if claimed, after which operation can require inspection, recalibration, or repair.

## 9.2 Operating and storage conditions

The supplier **shall** declare the conditions and elapsed interval after startup at which normal operation begins, even when full-performance limits do not yet apply. The declaration **shall** distinguish first usable output, normal operation, locked operation, and full-performance operation when those milestones differ.

### 9.2.1 Temperature

The supplier **shall** declare the operating, full-performance, and storage temperature ranges that apply at identified measurement locations. The declaration **shall** state whether the temperature is ambient, inlet-air, component, case, junction, or another defined quantity.

The supplier **shall** declare warm-up conditions and any thermal stabilization interval needed before full-performance limits apply. Temperature coefficients or bounded timing deviations **shall** be reported as required by 6.10 and 9.5.

### 9.2.2 Humidity and condensation

For a physical implementation, the supplier **shall** declare the operating and storage relative-humidity ranges and whether the limits are non-condensing. If condensation, conformal coating, sealing, or corrosion protection affects use or recovery, the relevant condition and procedure **shall** be documented.

### 9.2.3 Altitude, pressure, and cooling

If altitude or ambient pressure affects cooling, electrical spacing, oscillator behavior, or declared performance, the supplier **shall** declare the applicable altitude or pressure range and any derating.

The supplier **shall** document cooling assumptions needed for safe operation and full performance, including airflow direction and minimum airflow, heat-sink or cold-plate requirements, allowable inlet temperature, or host thermal design requirements, as applicable.

Where forced air, liquid, or another coolant is required, the supplier **shall** document the coolant type, cleanliness or contamination limits, filtration requirements, inspection or maintenance interval, and any derating or protective response required when a filter, heat sink, cold plate, or other heat-transfer surface becomes obstructed or fouled.

## 9.3 Mechanical conditions

### 9.3.1 Form factor and installation

A physical implementation **shall** document dimensions, mass, mounting points, connector locations, installation orientation, keep-out areas, insertion or extraction constraints, and retention requirements. If a standardized form factor is claimed, the conformance statement **shall** identify the governing specification and revision.

### 9.3.2 Shock and vibration

If operation, survival, or performance under shock or vibration is claimed, the supplier **shall** declare the test profile, axes, mounting fixture, operating state, sample quantity, acceptance criteria, test method, and governing standard and edition, if any. Frequency sensitivity to vibration **shall** be characterized using IEEE Std 1193-2022 [3] or another method identified in the conformance statement.

### 9.3.3 Connectors and cabling

The supplier **shall** document mating connectors, retention or torque requirements, the expected number of mating cycles where relevant, cable strain-relief assumptions, and environmental limitations for externally accessible timing and RF connectors.

## 9.4 Electrical and electromagnetic conditions

### 9.4.1 Power

For each power source, the supplier **shall** document nominal voltage, operating tolerance, maximum steady-state power, startup or inrush behavior, sequencing, auxiliary or standby power, and behavior outside the operating range.

An implementation powered through a standardized host interface **shall** conform to the power, sequencing, reset, and current limits of the identified host-interface specification. The supplier **shall** document which state, configuration, time, and calibration information persists through each power interruption or reset condition.

For a host-connected implementation, the supplier **shall** document whether the TimeCard remains powered, maintains the unified timescale, or retains time-control ownership while the host enters a low-power, sleep, hibernation, shutdown, or disconnected state. The documentation **shall** identify the timing-service and control-interface behavior during transition and recovery.

### 9.4.2 Supply sensitivity and interruption

The effect of input-voltage variation and supply noise on declared timing performance **shall** be characterized when applicable. If ride-through, backup energy, or uninterrupted holdover is claimed, the supplier **shall** declare the interruption profile, supported duration, load condition, output behavior, and recovery behavior.

### 9.4.3 EMC and ESD

For a physical implementation, the supplier **shall** identify each EMC emission, immunity, and ESD standard for which conformity is claimed, including edition, test level, port classification, configuration, and result. P3335 conformance does not by itself constitute regulatory approval or EMC/ESD certification.

The supplier **shall** document any operating restriction, cable, enclosure, grounding, or shielding condition required for a claimed EMC, ESD, or timing-performance result.

## 9.5 Environmental performance characterization

Environmental measurements supporting a conformance claim **shall** satisfy the measurement requirements in 6.3. For each environmental factor evaluated, the report **shall** identify:

- Applied stimulus, range, rate of change, dwell, and sequence.
- TimeCard operating state, active reference, and configuration.
- Measurement point and monitored timing metric.
- Test equipment, calibration status, and measurement uncertainty.
- Number of specimens and preconditioning.
- Performance limit and pass/fail rule.
- Pre-test, during-test, and post-test results.
- Recovery or recalibration performed after the test.

Within the declared full-performance range, measured performance **shall** remain within the applicable bounded declarations from Clause 6. Within the wider operating range, the implementation **shall** remain functional. When the implementation can detect that the applicable full-performance bounds are not assured, it **shall** expose a dynamic indication through a control object or alarm, and the supplier **shall** document the indication, the affected bounds, and the conditions for setting and clearing it. When the implementation cannot detect that condition, the supplier **shall** document the external monitoring needed to determine whether the bounds apply.

## 9.6 Reliability, service life, and calibration

### 9.6.1 Reliability declarations

If MTBF, failure rate, availability, or another reliability metric is claimed, the supplier **shall** document the metric definition, prediction or field-data method, environment, duty cycle, confidence basis, exclusions, and source data revision. A predicted reliability value **shall** be distinguishable from a field-observed value.

### 9.6.2 Service-life items

The supplier **shall** identify components or stored data with a service-life limitation that can affect timing service, including batteries, fans, nonvolatile-memory endurance, oscillators, and calibration data, as applicable. The documentation **shall** state the rated interval or endurance, replacement or maintenance action, and effect of expiration or failure.

### 9.6.3 Calibration and traceability

If calibration is required to maintain a declared performance bound, the supplier **shall** document the calibration interval or triggering condition, measurement point, reference, procedure, adjustable parameters, and post-calibration verification. Calibration records **shall** identify the implementation revision, date, result, uncertainty, and traceability chain.

## 9.7 Environmental documentation checklist

The conformance statement or referenced product documentation **shall** include, as applicable:

| Category | Required content |
|----------|------------------|
| Deployment | Intended environment and implementation form. |
| Temperature | Operating, full-performance, storage, and survival ranges; measurement location; warm-up. |
| Humidity | Operating and storage ranges; condensation condition. |
| Altitude and cooling | Range, derating, airflow direction and rate, coolant cleanliness, filtration and maintenance assumptions, or other cooling dependency. |
| Mechanical | Form factor, dimensions, mass, mounting, retention, shock, and vibration claims. |
| Power | Rails, tolerances, consumption, inrush, sequencing, reset, persistence, and interruption behavior. |
| EMC and ESD | Claimed standards, editions, levels, configurations, restrictions, and results. |
| Performance | Environmental characterization method, uncertainty, limits, and qualification evidence. |
| Lifecycle | Reliability basis, service-life items, maintenance, and calibration. |

## 9.8 Regulatory note (Informative)

Manufacturers and integrators remain responsible for the safety, electromagnetic, environmental, spectrum, and other legal requirements of the jurisdictions in which a product is produced, installed, or operated. P3335 only defines TimeCard conformance and does not and cannot grant regulatory approval.
