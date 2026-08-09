# 4. Conformance

This clause defines the conditions under which an implementation may claim conformance to IEEE P3335. A conforming implementation **shall** satisfy the mandatory requirements in this clause and the mandatory requirements in Clauses 5 through 9 that apply to the implemented features, interfaces, and operating conditions.

Informative clauses, informative notes, and informative annexes provide explanatory material only. They do not create conformance requirements unless a normative clause explicitly references a requirement stated elsewhere.

## 4.1 Requirement Terms

The following terms are used as defined by IEEE SA rules for standards text:

- **shall** indicates a mandatory requirement.
- **should** indicates a recommended practice among several permissible possibilities.
- **may** indicates a course of action permitted within the limits of this standard.
- **can** indicates capability, possibility, or a statement of fact.

The term **must** is not used as a requirement term in this standard. Where a physical or mathematical inevitability needs to be described, the text should be written as a statement of fact using **is**, **are**, or **can**.

The term **unspecified** is not a requirement term. It identifies a value, behavior, or design choice that P3335 has considered but intentionally does not constrain. The choice is left to the implementation, an applicable profile, or a later specification, subject to any applicable documentation requirements.

## 4.2 Conformance Model

IEEE P3335 uses interspersed requirements with a conformance summary. Mandatory and optional requirements are stated in the technical clauses where the relevant behavior is specified. Clause 4 summarizes how those requirements are applied.

A TimeCard implementation may be realized as a discrete add-in card, an embedded module, an FPGA or ASIC function, a system-on-chip block, or an external timing unit. The form factor does not determine conformance. Conformance is determined by the externally observable interfaces, behavior, documentation, and performance declarations of the implementation.

A claim of conformance **shall** identify at least the following:

- The implementation form factor and host interface mapping.
- The timing receive and providing interfaces implemented.
- The control interfaces implemented.
- The optional feature sets claimed.
- The declared operating environment and environmental limits.
- The performance metrics, measurement points, measurement methods, and limits declared by the supplier.

## 4.3 Base Conformance Requirements

A conforming TimeCard implementation **shall** meet all of the following base requirements:

- The implementation **shall** provide at least one timing output providing interface that distributes time, phase, frequency, or a combination thereof to a host system or downstream system.
- All implemented timing output providing interfaces **shall** derive from the single unified timescale specified in Clause 5.
- The implementation **shall** provide at least one accessible control interface as specified in Clause 8.
- The implementation **shall** document all implemented timing interfaces, control interfaces, physical connectors, protocol mappings, and optional features.
- The implementation **shall** document the performance metrics required by Clause 6 for each applicable measurement point.
- The implementation **shall** document the environmental limits and reliability information required by Clause 9 for the declared deployment environment.
- The implementation **shall** define the conditions under which each declared performance value is valid, including warm-up time, lock time, reference source, temperature range, and measurement bandwidth where applicable.
- The implementation **shall** not claim support for an optional feature unless all mandatory requirements associated with that feature are satisfied.

An implementation may conform to IEEE P3335 without implementing every optional receive interface, providing interface, host interface mapping, management protocol, environmental profile, or security hardening feature described in this standard.

## 4.4 Conformance Profiles

This standard defines the following conformance profiles. An implementation claiming a profile **shall** satisfy the corresponding additional requirements in the following table.

| Profile | Applicability | Additional requirements |
|---------|---------------|-------------------------|
| **Base TimeCard** | All conforming implementations | Satisfy the base requirements in 4.3 and all applicable mandatory requirements in Clauses 5 through 9. |
| **Physical Timing Output** | Implementations with externally accessible physical timing outputs | Provide a 1PPS output that satisfies 7.3.2 and document the alignment of all other physical timing outputs to that 1PPS output. |
| **PCIe Host Mapping** | Implementations claiming PCIe host integration | Satisfy the PCIe host interface profile requirements in 8.9. |
| **Managed TimeCard** | Implementations claiming remote or fleet management | Satisfy the managed security profile in 8.11.2. |
| **Secure Infrastructure TimeCard** | Implementations marketed or designated for secure infrastructure deployments | Satisfy the secure infrastructure profile in 8.11.3. |

An embedded or logical-only TimeCard implementation may claim Base TimeCard conformance without a physical 1PPS connector if it does not expose externally accessible physical timing outputs. Such an implementation **shall** still provide at least one timing output providing interface and **shall** document the equivalent measurement point for timing-performance declarations.

## 4.5 Optional Feature Claims

Optional features are conditional. If an implementation claims support for an optional feature, the implementation **shall** satisfy the mandatory requirements that apply to that feature.

Optional feature claims include, but are not limited to:

- Receive interfaces such as GNSS, PTP, NTP, White Rabbit, WiWi, WWVB, IRIG, PPS, or frequency-reference inputs.
- Providing interfaces such as PPS, frequency outputs, Time of Day outputs, PTP, PCIe PTM, or other host-bus time-transfer mechanisms.
- Host interface mappings such as PCIe, USB, serial, embedded memory-mapped interfaces, or implementation-specific mappings.
- Control protocols such as SMBus, I2C, I3C, IPMI, NC-SI, REST, gRPC, SNMP, Redfish, serial, or USB.
- Security functions such as authenticated management, signed firmware update, secure boot, encrypted telemetry, key storage, sanitization, or tamper response.
- Environmental profiles such as data-center, telecommunications, industrial, laboratory, or field deployment.
- Ensemble reference processing, holdover classes, or other enhanced timing functions.

Each optional feature claim **shall** identify the clause or subclause that defines the claimed behavior and **shall** identify any deviations or implementation-specific limits allowed by that clause.

## 4.6 Performance Conformance Strategy

Base conformance to this standard requires the bounded and reproducible performance reporting specified in Clause 6. It does not require a universal numeric minimum time-accuracy, frequency-stability, phase-noise, jitter, or holdover class.

An implementation may claim a vendor-defined or application-defined performance class. If such a class is claimed, the conformance statement **shall** identify the class, the metric limits, the measurement points, and the conditions under which the class applies.

## 4.7 Conformance Statement

The supplier of a conforming implementation **shall** provide a conformance statement. The conformance statement **shall** be both publicly available and supplied with the product documentation and **shall** include, at a minimum:

- Product name, hardware revision, firmware revision, and relevant configuration profile.
- Claimed IEEE P3335 conformance scope.
- Supported timing receive interfaces and providing interfaces.
- Supported host interface mapping and control interface classes.
- Host driver, service, API, and ABI revisions required for each claimed host mapping.
- Instance-identifier stability, host lifecycle behavior, and host-time correlation capabilities for each claimed host mapping.
- Claimed conformance profiles from 4.4.
- Supported optional feature sets.
- Declared performance metrics and measurement points.
- Declared environmental operating and storage limits.
- References to datasheets, register maps, interface descriptions, calibration information, and test reports needed to evaluate the claim.

The conformance statement should be written so that an independent test laboratory or system integrator can determine which requirements apply without relying on unpublished implementation details.

## 4.8 Test Evidence

Conformance can be evaluated by functional testing, performance testing, documentation review, or a combination thereof.

Functional testing verifies that the implemented interfaces, state transitions, control operations, and fault responses behave as specified. Performance testing verifies that declared timing, frequency, holdover, and environmental metrics meet the supplier's stated limits using the measurement methods declared for the implementation.

When test evidence is used to support a conformance claim, the evidence **shall** identify:

- The device under test and configuration under test.
- The applicable IEEE P3335 clauses and optional feature claims.
- Test equipment, calibration status, and traceability path.
- Test environment, reference source, cabling, and measurement points.
- Pass/fail criteria and measured results.
- Any deviations, waivers, or limitations of the test method.

Annex B provides informative example test procedures that can be used as a starting point for such evidence. Its procedures do not add, change, or replace the normative conformance criteria.

## 4.9 Conformance Statement Proforma

Annex D provides an informative proforma for organizing the conformance statement required by 4.7. Use of the proforma is optional. The requirements in this clause and the applicable technical clauses remain the controlling source for conformance.
