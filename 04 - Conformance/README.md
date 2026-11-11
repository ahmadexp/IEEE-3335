# 4. Conformance

This clause identifies the subject of a conformance claim and the evidence used to evaluate it. Informative material does not add conformance requirements.

## 4.1 Interpreting requirements

Word usage is specified in 1.4. The term *unspecified* is not a requirement term; its meaning as a behavior or object-field status is defined in 3.1.

## 4.2 Conformance Model

IEEE P3335 uses interspersed requirements with a conformance summary. Mandatory and optional requirements are stated in the technical clauses where the relevant behavior is specified. Clause 4 summarizes how those requirements are applied.

A TimeCard implementation may be realized as a discrete add-in card, an embedded module, an FPGA or ASIC function, a system-on-chip block, or an external timing unit. The form factor does not determine conformance. Conformance is determined by the externally observable interfaces, behavior, documentation, and performance declarations of the implementation.

The scope, interfaces, profiles, operating limits, and supporting evidence for a claim are identified in the conformance statement specified in 4.7.

## 4.3 Base Conformance Requirements

A conforming TimeCard **shall** satisfy the applicable requirements in Clauses 4 through 9. The following list locates the controlling provisions; it does not impose a second set of requirements:

- Implementation boundary and local timing function: 5.2 and 5.3.1.
- At least one providing interface and one unified timescale per instance: 5.3.5 and 5.4.
- Performance declarations and conditions of validity: Clause 6.
- Implemented timing receive and providing interfaces, including connector and protocol declarations: Clause 7.
- At least one accessible control interface and its mapping: 8.2 and 8.10.2.
- Environmental and reliability declarations: Clause 9.
- Optional claims, conformance statement, test evidence, and integration documentation: 4.5, 4.7, 4.8, and 5.10.

An implementation may conform to IEEE P3335 without implementing every optional receive interface, providing interface, host interface mapping, management protocol, or security hardening feature described in this standard. Environmental declarations remain mandatory as specified in Clause 9; this standard does not define named numeric environmental classes for particular markets.

## 4.4 Conformance Profiles

The implementation **shall** apply each profile whose applicability condition it meets. The table identifies the controlling provisions for each profile.

| Profile | Applicability | Additional requirements |
|---------|---------------|-------------------------|
| **Base TimeCard** | All conforming implementations | See 4.3. |
| **Physical Timing Output** | Implementations with externally accessible physical timing outputs | See 7.3.2. The supplier **shall** document the alignment of every other physical timing output to that 1PPS output. |
| **PCIe Host Mapping** | Implementations claiming PCIe host integration | Satisfy the PCIe host interface profile requirements in 8.9. |
| **Managed TimeCard** | Implementations claiming remote or fleet management | Satisfy the managed security profile in 8.11.2. |
| **Secure Infrastructure TimeCard** | Implementations marketed or designated for secure infrastructure deployments | Satisfy the secure infrastructure profile in 8.11.3. |

An embedded or logical-only TimeCard implementation may claim Base TimeCard conformance without a physical 1PPS connector if it does not expose externally accessible physical timing outputs. For such an implementation, the supplier **shall** document the equivalent measurement point for timing-performance declarations.

## 4.5 Optional Feature Claims

Optional features are conditional. If an implementation claims support for an optional feature, the implementation **shall** satisfy the mandatory requirements that apply to that feature.

Optional feature claims include, but are not limited to:

- Receive interfaces such as GNSS, PTP, NTP, White Rabbit, WWVB, IRIG, PPS, wireless time transfer, or frequency-reference inputs.
- Providing interfaces such as PPS, frequency outputs, Time of Day outputs, PTP, PCIe PTM, or other host-bus time-transfer mechanisms.
- Host interface mappings such as PCIe, USB, serial, embedded memory-mapped interfaces, or implementation-specific mappings.
- Control protocols such as SMBus, I2C, I3C, IPMI, NC-SI, REST, gRPC, SNMP, Redfish, serial, or USB.
- Security functions such as authenticated management, signed firmware update, secure boot, encrypted telemetry, key storage, sanitization, or tamper response.
- Ensemble reference processing, holdover classes, or other enhanced timing functions.

Each optional feature claim **shall** identify the clause or subclause that defines the claimed behavior and **shall** identify any deviations or implementation-specific limits allowed by that clause.

A reference derived from UTC(k) may be conveyed by a declared pulse, frequency, Time of Day, or packet interface. The reference origin and timescale are distinct from that interface's signal or protocol specification.

## 4.6 Performance Conformance Strategy

Base conformance to this standard requires the bounded and reproducible performance reporting specified in Clause 6. It does not require a universal numeric minimum time-accuracy, frequency-stability, phase-noise, jitter, or holdover class.

An industry or procurement profile can set the limits for its application. A supplier reports what the identified product supports; it need not design a class or set targets for an industry. If a supplier uses its own class designation, the conformance statement **shall** distinguish it from an externally specified class. The identifying details for a class or mask claim are specified in 6.1.

Performance declarations may incorporate a referenced specification instead of reproducing its provisions when the exact applicable requirements and implementation conditions are identified. The supplier **shall** separately document any applicable P3335 declaration not covered by that specification. An informative reference or a document under development does not, by itself, establish a normative P3335 requirement or an approved external performance class.

## 4.7 Conformance Statement

The supplier of a conforming implementation **shall** provide a conformance statement. The conformance statement **shall** be both publicly available and supplied with the product documentation and **shall** include, at a minimum:

- Product or implementation name and form factor; hardware or implementation revision; firmware, gateware, and software revisions; and relevant configuration profile.
- The published edition of this standard against which conformance is claimed, together with the conformance-statement date and revision.
- Claimed IEEE P3335 conformance scope.
- Supported timing receive interfaces and providing interfaces.
- Supported host interface mapping and control interface classes.
- Baseline control mapping and revision, required-object coverage, conditional capabilities, status encoding, and extension or compatibility policy.
- Host driver, service, API, and ABI revisions required for each claimed host mapping.
- Instance-identifier stability, host lifecycle behavior, and host-time correlation capabilities for each claimed host mapping.
- Claimed conformance profiles from 4.4.
- Supported optional feature sets.
- Security properties and deployment assumptions required by 8.11.1, including the claimed security profile and supported security functions.
- Declared performance metrics, measurement points, methods, and limits (see Clause 6).
- Declared environmental operating and storage limits.
- References to datasheets, register maps, interface descriptions, calibration information, and test reports needed to evaluate the claim.

A datasheet can serve as the conformance statement. One identified, revision-controlled source can cover several entries; the statement can point to the relevant sections instead of repeating them, subject to the access rules below.

The conformance statement should be written so that an independent test laboratory or system integrator can determine which requirements apply without relying on proprietary internal design details.

The public conformance statement and published performance declarations are distinct from their supporting records. Detailed calibration records, test data, and integration documentation may be supplied through controlled access arrangements that permit evaluation and integration. The supplier **shall** identify the supporting documents, their revisions, and the process for requesting access. Controlled access **shall** not replace the public information required by this clause or the performance declarations required by 6.1, or excuse missing evidence for an applicable requirement. This standard does not require disclosure of proprietary internal designs, source code, or disciplining algorithms.

## 4.8 Test Evidence

Conformance claims **shall** be supported by functional test evidence for applicable functional requirements and performance test evidence for applicable measured-performance requirements. Documentation review verifies documentation and declaration requirements and can evaluate supporting test records; it **shall** not substitute for evidence that the claimed functions and performance have been demonstrated.

The subject of conformance is the TimeCard implementation, not the test equipment. The supplier is responsible for the evidence supporting its claim. The evaluator records how each result was obtained (see 6.3); the evaluator may be the supplier or another party. There is no separate P3335 conformance claim for an instrument or a laboratory.

Functional testing verifies that the implemented interfaces, state transitions, control operations, and fault responses behave as specified. Performance testing verifies that declared timing, frequency, holdover, and environmental metrics meet the supplier's stated limits using the measurement methods declared for the implementation.

Test evidence supporting a conformance claim **shall** identify:

- The device under test and configuration under test.
- The applicable IEEE P3335 clauses and optional feature claims.
- Test equipment, calibration status, and traceability path.
- Test environment, TimeCard synchronization source, cabling, and measurement points.
- Pass/fail criteria and measured results.
- Any deviations, waivers, or limitations of the test method.

The supplier may perform the evaluation unless a claimed profile or an external obligation requires another evaluator. This standard does not require accredited third-party certification or execution of the complete qualification suite on every manufactured unit. When evidence from a representative configuration supports additional implementations or configurations, the supplier **shall** identify the covered population, the basis for applying that evidence, and any additional verification needed.

Annex B provides informative example test procedures that can be used as a starting point for such evidence. Its procedures do not add, change, or replace the normative conformance criteria.

A deviation or waiver of a test method **shall** not waive an applicable mandatory requirement of this standard.

## 4.9 Conformance Statement Proforma

Annex D provides an informative proforma for organizing the conformance statement required by 4.7. Use of the proforma is optional. If Annex D conflicts with Clause 4 or an applicable technical clause, the normative clause controls.

## 4.10 Implementation examples (Informative)

The examples describe timing subsystems designed to provide a timing service. A laptop or switch becoming a PTP grandmaster does not, by that fact alone, constitute a TimeCard. An identifiable timing subsystem within either product can be evaluated at its declared boundary (see 5.2).

The following examples help locate applicable requirements. They are not additional conformance Types or exhaustive configurations. Every example is subject to base conformance, the implemented-feature rules, and the applicable profiles in 4.4; physical form factor alone does not select a performance class.

| Example configuration | Principal interface provisions | Performance and evidence focus |
|-----------------------|--------------------------------|--------------------------------|
| PCIe TimeCard with GNSS reference | GNSS receive declarations in 7.2, implemented outputs in 7.3, PCIe mapping in 8.9 | Reference-to-output error, host correlation when supported, host lifecycle, and optional PTM when implemented |
| External unit with GNSS input and PTP output | GNSS and PTP declarations in 7.2 and 7.3, implemented control mapping in Clause 8 | Receiver and packet timestamping points, reference path, output profile, and declared environmental limits |
| Dedicated timing subsystem with PTP input and output | Receive and providing protocol/profile declarations in 7.2 and 7.3 | Input-to-output transfer, network asymmetry, reference validity, and the distinction between transfer error and absolute time accuracy |
| Embedded timing function with a logical output | Implementation boundary in 5.2, providing-interface declarations in 7.3, implemented control mapping in Clause 8 | Declared logical measurement point, fixture or host-path effects, and equivalent measurement evidence under 4.4 |

Profiles in 4.4 apply according to the implemented features, not the example name. Clauses 6 and 9 apply to each example's declared performance and environment.
