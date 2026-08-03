# Annex D: Conformance Statement Proforma (Informative)

## D.1 Purpose

This annex provides a common structure for the supplier conformance statement required by 4.7. It is a reporting aid and does not add, remove, or modify any conformance requirement.

The completed proforma should identify each claimed profile and optional feature, the implementation revision evaluated, and the evidence supporting each claim. A supplier may extend the tables when additional interfaces or application-defined profiles are declared.

## D.2 Implementation identification

| Field | Supplier response |
|-------|-------------------|
| Product or implementation name | To be completed |
| Supplier | To be completed |
| Hardware or implementation revision | To be completed |
| Firmware, gateware, and software revisions | To be completed |
| Configuration identifier | To be completed |
| Form factor | To be completed |
| Date of statement | To be completed |
| Statement revision | To be completed |
| Supporting documentation | To be completed |

## D.3 Conformance profile claims

| Profile and clause | Supplier claim and evidence |
|--------------------|-----------------------------|
| Base TimeCard (4.3) | Claimed: ___; evidence or limitation: ___ |
| Physical Timing Output (7.3.2) | Claimed: ___; evidence or limitation: ___ |
| PCIe Host Mapping (8.9) | Claimed: ___; evidence or limitation: ___ |
| Managed TimeCard (8.11.2) | Claimed: ___; evidence or limitation: ___ |
| Secure Infrastructure TimeCard (8.11.3) | Claimed: ___; evidence or limitation: ___ |

## D.4 Interface and optional-feature claims

Complete one record for each claimed interface or optional feature:

| Field | Supplier response |
|-------|-------------------|
| Interface or feature | To be completed |
| Direction | Receive / providing / control / host |
| Standard, profile, or mapping revision | To be completed |
| Connector or logical endpoint | To be completed |
| Measurement point | To be completed |
| Evidence or limitation | To be completed |

Examples include GNSS, PTP, NTP, 1PPS, frequency outputs, Time of Day, IRIG, PCIe PTM, host timestamping, reference selection, ensemble processing, firmware update, and sanitization.

## D.5 Performance declarations

| Metric | Declaration record |
|--------|--------------------|
| Time accuracy | State: ___; point: ___; bound: ___; conditions: ___; method and uncertainty: ___; evidence: ___ |
| MTIE | State: ___; point: ___; bound: ___; intervals: ___; conditions: ___; method and uncertainty: ___; evidence: ___ |
| TDEV | State: ___; point: ___; result or limit: ___; intervals: ___; conditions: ___; method and uncertainty: ___; evidence: ___ |
| Frequency accuracy | State: ___; point: ___; bound: ___; conditions: ___; method and uncertainty: ___; evidence: ___ |
| ADEV | State: ___; point: ___; result or limit: ___; intervals: ___; conditions: ___; method and uncertainty: ___; evidence: ___ |
| Phase noise | State: ___; point: ___; mask or points: ___; offset range: ___; method and uncertainty: ___; evidence: ___ |
| Pulse timing variation | State: ___; point: ___; statistic and bound: ___; bandwidth and sample count: ___; uncertainty: ___; evidence: ___ |
| Holdover error | Entry condition: ___; point: ___; bound versus elapsed time: ___; environment: ___; method and uncertainty: ___; evidence: ___ |
| Transition behavior | Transition: ___; point: ___; phase/frequency bound: ___; conditions: ___; method and uncertainty: ___; evidence: ___ |

## D.6 Environment and lifecycle declarations

| Category | Declaration and evidence |
|----------|--------------------------|
| Operating and full-performance temperature | Range and location: ___; evidence: ___ |
| Storage and survival temperature | Range and condition: ___; evidence: ___ |
| Humidity and condensation | Range and condition: ___; evidence: ___ |
| Altitude or pressure | Range and derating: ___; evidence: ___ |
| Airflow or cooling assumptions | Requirement and condition: ___; evidence: ___ |
| Input power, sequencing, and interruption | Limits and behavior: ___; evidence: ___ |
| Shock and vibration, if applicable | Profile and limit: ___; evidence: ___ |
| EMC and ESD conformity claims | Standard, edition, level, and configuration: ___; evidence: ___ |
| Reliability model or field-data basis | Metric and method: ___; evidence: ___ |
| Service-life items | Item, interval, and maintenance action: ___; evidence: ___ |
| Calibration interval or method | Interval, reference, method, and uncertainty: ___; evidence: ___ |

## D.7 Test evidence and deviations

Complete one record for each applicable clause, profile, or declared limit:

| Field | Supplier response |
|-------|-------------------|
| Applicable clause or claim | To be completed |
| Verification method | Test / inspection / analysis / documentation |
| Report identifier | To be completed |
| Result | Pass / fail / not applicable |
| Deviation, waiver, or limitation | To be completed |

Any deviation recorded in this table should state whether the affected feature remains within the conformance claim and identify the authority or rationale used for that determination.
