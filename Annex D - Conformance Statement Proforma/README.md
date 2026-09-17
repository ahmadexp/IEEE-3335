# Annex D: Conformance Statement Proforma (Informative)

## D.1 Purpose

This annex provides a common structure for the supplier conformance statement required by 4.7. It is a reporting aid and does not add, remove, or modify any conformance requirement.

The completed proforma should identify each claimed profile and optional feature, the implementation revision evaluated, and the evidence supporting each claim. A supplier may extend the tables when additional interfaces or application-defined profiles are declared.

While this document remains an unapproved draft, this proforma is available for review and trial evaluation only, subject to the front-matter draft-status notice.

## D.2 Implementation identification

| Field | Supplier response |
|-------|-------------------|
| Product or implementation name | To be completed |
| Supplier | To be completed |
| Hardware or implementation revision | To be completed |
| Firmware, gateware, and software revisions | To be completed |
| Host operating systems and versions | To be completed / not applicable |
| Driver, service, and time-provider revisions | To be completed / not applicable |
| Host API or ABI name and revision | To be completed / not applicable |
| Configuration identifier | To be completed |
| Form factor | To be completed |
| Published edition of this standard claimed | To be completed; no conformance claim against an unapproved draft |
| Date of statement | To be completed |
| Statement revision | To be completed |
| Supporting documentation | To be completed |

## D.3 Conformance profile claims

| Profile and clause | Supplier claim and evidence |
|--------------------|-----------------------------|
| Base TimeCard (4.3) | Claimed: \_\_\_\_\_\_\_; evidence or limitation: \_\_\_\_\_\_\_ |
| Physical Timing Output (4.4, 7.3.2, and 7.3.4) | Claimed: \_\_\_\_\_\_\_; evidence or limitation: \_\_\_\_\_\_\_ |
| PCIe Host Mapping (8.9) | Claimed: \_\_\_\_\_\_\_; evidence or limitation: \_\_\_\_\_\_\_ |
| Managed TimeCard (8.11.2) | Claimed: \_\_\_\_\_\_\_; evidence or limitation: \_\_\_\_\_\_\_ |
| Secure Infrastructure TimeCard (8.11.3) | Claimed: \_\_\_\_\_\_\_; evidence or limitation: \_\_\_\_\_\_\_ |

## D.4 Interface and optional-feature claims

Complete one record for each claimed interface or optional feature:

| Field | Supplier response |
|-------|-------------------|
| Interface or feature | To be completed |
| Direction | Receive / providing / control / host |
| Standard, profile, or mapping revision | To be completed |
| Connector or logical endpoint | To be completed |
| Measurement point | To be completed |
| Instance identifier and stability scope | To be completed / not applicable |
| Discovery descriptor or baseline locator | To be completed / not applicable |
| Evidence or limitation | To be completed |

Examples include GNSS, PTP, NTP, 1PPS, frequency outputs, Time of Day, IRIG, PCIe PTM, host timestamping, reference selection, ensemble processing, firmware update, and sanitization.

## D.5 Host-interface and driver declarations

Complete this section for each claimed host interface mapping:

| Field | Supplier response |
|-------|-------------------|
| Host interface and mapping revision | To be completed |
| Supported operating systems, releases, and architectures | To be completed |
| Driver model, package, and signing or authorization status | To be completed |
| Driver, service, host time-provider, and API or ABI revisions | To be completed |
| P3335 discovery-descriptor locator, revision, and encoding | To be completed |
| Supported PCI or implementation identities and board profiles | To be completed |
| `TC_INSTANCE_ID` derivation and stability scope | To be completed |
| `TC_SERIAL` namespace and availability | To be completed / not implemented |
| Host clock identifier, epoch, timescale, units, and adjustment behavior | To be completed |
| Host-time correlation method, measurement point, and maximum window | To be completed / not implemented |
| Sample-age, uncertainty or dispersion, and discipline-eligibility policy | To be completed / not implemented |
| Time-control ownership, arbitration, timeout, and recovery | To be completed / not implemented |
| Sleep, hibernation, wake, removal, reconnection, reboot, and driver-restart behavior | To be completed |
| Read, time-control, configuration, update, and security privileges | To be completed |
| Physical validation coverage and known limitations | To be completed |

## D.6 Control, status, and security declarations

Complete this section for each baseline control mapping and each claimed management or security profile:

| Field | Supplier response |
|-------|-------------------|
| Baseline control mapping, endpoint, and revision | To be completed |
| Required baseline-object coverage and status encoding | To be completed |
| Conditional capabilities and corresponding object mappings | To be completed |
| Atomicity, timeout, cancellation, retry, and error behavior | To be completed |
| Event and telemetry timestamps, ordering, retention, and dropped-record behavior | To be completed / not implemented |
| Extension namespace, version policy, reserved ranges, and unknown-element handling | To be completed / no extensions |
| Authentication, authorization, encrypted transport, and physical-access assumptions | To be completed / `none` |
| Access roles and privileges, including time-control ownership | To be completed / not implemented |
| Update integrity, signing, trust anchors, rollback protection, and recovery | To be completed / `none` |
| Boot-integrity verification and protected key or credential storage | To be completed / `none` |
| Audit records, tamper response, and replay or message-injection protection | To be completed / `none` |
| Sanitization scope, method, and completion or failure indication | To be completed / `none` |

## D.7 Performance declarations

For each applicable metric, identify the synchronization source, reference timescale, operating state, environmental range, warm-up and lock conditions, observation or averaging intervals, bandwidth, sample count or confidence basis, and measurement method required by Clause 6. Include at least one bounded value, the measurement uncertainty, and the decision rule used to evaluate the bound. Documentation references may supply these details when they identify the exact configuration and result.

| Metric | Declaration record |
|--------|--------------------|
| Time accuracy | State: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; bound: \_\_\_\_\_\_\_; conditions: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| TimeCard timestamp accuracy | Event: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; reference: \_\_\_\_\_\_\_; bounded error: \_\_\_\_\_\_\_; resolution and granularity: \_\_\_\_\_\_\_; corrections and latency: \_\_\_\_\_\_\_; uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| MTIE | State: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; bound: \_\_\_\_\_\_\_; intervals: \_\_\_\_\_\_\_; conditions: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| TDEV | State: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; result or limit: \_\_\_\_\_\_\_; intervals: \_\_\_\_\_\_\_; conditions: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Frequency accuracy | State: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; bound: \_\_\_\_\_\_\_; conditions: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| ADEV | State: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; result or limit: \_\_\_\_\_\_\_; intervals: \_\_\_\_\_\_\_; conditions: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Phase noise | State: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; mask or points: \_\_\_\_\_\_\_; offset range: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Pulse timing variation | State: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; statistic and bound: \_\_\_\_\_\_\_; bandwidth and sample count: \_\_\_\_\_\_\_; uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Noise transfer | Input and output points: \_\_\_\_\_\_\_; stimulus and range: \_\_\_\_\_\_\_; state and configuration: \_\_\_\_\_\_\_; response or mask: \_\_\_\_\_\_\_; uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Noise tolerance | Input point and nominal conditions: \_\_\_\_\_\_\_; stimulus and duration: \_\_\_\_\_\_\_; acceptance criteria: \_\_\_\_\_\_\_; threshold or mask: \_\_\_\_\_\_\_; uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Holdover error | Entry condition: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; bound versus elapsed time: \_\_\_\_\_\_\_; environment: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Transition behavior | Transition: \_\_\_\_\_\_\_; point: \_\_\_\_\_\_\_; phase/frequency bound: \_\_\_\_\_\_\_; conditions: \_\_\_\_\_\_\_; method and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |

## D.8 Environment and lifecycle declarations

| Category | Declaration and evidence |
|----------|--------------------------|
| Operating and full-performance temperature | Range and location: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Storage and survival temperature | Range and condition: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Humidity and condensation | Range and condition: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Altitude or pressure | Range and derating: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Airflow or cooling assumptions | Requirement and condition: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Input power, sequencing, and interruption | Limits and behavior: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Host power-state and disconnect behavior | State retention and transition behavior: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Shock and vibration, if applicable | Profile and limit: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| EMC and ESD conformity claims | Standard, edition, level, and configuration: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Reliability model or field-data basis | Metric and method: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Service-life items | Item, interval, and maintenance action: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |
| Calibration interval or method | Interval, reference, method, and uncertainty: \_\_\_\_\_\_\_; evidence: \_\_\_\_\_\_\_ |

## D.9 Test evidence and deviations

Complete one record for each applicable clause, profile, or declared limit:

| Field | Supplier response |
|-------|-------------------|
| Applicable clause or claim | To be completed |
| Verification method | Test / inspection / analysis / documentation |
| Report identifier | To be completed |
| Result | Pass / fail / not applicable |
| Deviation, waiver, or limitation | To be completed |

Any deviation recorded in this table should distinguish a change to the verification method from failure to satisfy a requirement. A method deviation should identify its rationale and the evidence that still supports the claim. An unmet applicable mandatory requirement is a failure, regardless of a test-method waiver. An optional feature excluded from the conformance scope should be identified explicitly and should not be represented as conforming.
