# 5. Architecture (Normative)

This clause defines the architectural requirements for a TimeCard. The architecture is specified in terms of externally observable functions, interfaces, behavior, and documentation. A TimeCard may be implemented as a discrete card, an embedded hardware block, an FPGA or ASIC function, an external module, or another implementation form that satisfies the requirements of this standard.

The architecture separates timing data-plane functions from management and control functions. Timing data-plane functions receive, generate, maintain, timestamp, and provide time, phase, and frequency. Management and control functions configure, monitor, secure, and report the state of those timing functions. Figure 1 shows the principal external relationships.

![TimeCard context within a host system](figures/rendered/architecture-context.pdf)

## 5.1 Architectural Overview

A TimeCard is a timing subsystem that provides time, phase, frequency, or a combination thereof to a host system or downstream system. The host system may be a server, telecommunications platform, industrial controller, scientific instrument, embedded system, or other system that requires a timing service with documented support for system-level traceability analysis.

A conforming TimeCard **shall** include the following externally observable capabilities:

- A local timing function capable of maintaining a unified timescale.
- At least one timing output providing interface.
- At least one control interface.
- Published performance, interface, environmental, and conformance information sufficient for an implementer or operator to evaluate the claimed behavior.

A TimeCard may include one or more timing receive interfaces, one or more time-transfer interfaces, one or more host interface mappings, and one or more reference-selection or ensemble algorithms.

## 5.2 Implementation Boundary

The TimeCard implementation boundary is the set of interfaces through which the TimeCard exchanges timing signals, timestamp values, control information, status, telemetry, firmware, or power with the host system or external equipment.

An implementation **shall** document its implementation boundary. The documentation **shall** identify:

- Host interface mappings.
- Timing receive interfaces, if any.
- Timing providing interfaces.
- Control interfaces.
- Power, thermal, and mechanical dependencies.
- Measurement points used for declared performance values.

Internal partitioning is implementation-specific unless a claimed optional feature or interface mapping makes that partitioning externally observable.

## 5.3 Core Functional Blocks

A TimeCard architecture is described by the following logical blocks. An implementation may combine or subdivide these blocks, provided that the externally observable behavior remains conformant.

### 5.3.1 Local Timing Function

The local timing function maintains the TimeCard's time, phase, and frequency state. It may be based on a quartz oscillator, OCXO, TCXO, CSAC, rubidium oscillator, atomic reference, DDS, host-provided clock, or another timing source.

The implementation **shall** document the oscillator or timing-source class used for each declared performance profile. The implementation **shall** document whether the local timing function is steerable, free-running, disciplined by external references, or operated as a primary reference.

### 5.3.2 Time Generator

The time generator produces the TimeCard's unified timescale. It may include counters, phase accumulators, timestamp interpolation, leap-second or timescale conversion logic, frequency steering, phase steering, or other timing logic.

The time generator **shall** support timestamp representations that permit unambiguous duration computation over the declared operating interval. If an implementation exposes a timescale that is not TAI, UTC, or the IEEE 1588-2019 [4] PTP timescale, the implementation **shall** document the mapping to the declared reference timescale.

The implementation **shall** document the supported timestamp range, epoch, granularity, resolution, and behavior at discontinuities such as leap seconds, leap smearing, holdover entry, reference failover, or manual time steps.

### 5.3.3 Timestamping Facility

If an implementation timestamps events, packets, register accesses, signal edges, or host-bus transactions, the timestamping facility **shall** derive those timestamps from the unified timescale. The implementation **shall** document the timestamping measurement point, timestamp latency or correction model, resolution, granularity, and known fixed offsets.

Hardware timestamping should be used for receive and providing interfaces where the supported protocol or physical interface permits it.

### 5.3.4 Receive Interfaces

Receive interfaces acquire external references that may be used to steer, discipline, initialize, monitor, or validate the unified timescale. Receive interfaces are specified in Clause 7.

An implementation may operate without a receive interface if it is designed for free-running, primary-reference, laboratory, or isolated holdover operation. If no receive interface is implemented, the conformance statement **shall** state that no external timing reference is supported.

### 5.3.5 Providing Interfaces

Providing interfaces distribute time, phase, frequency, or timestamp information from the TimeCard to a host system or downstream system. Providing interfaces are specified in Clause 7.

At least one providing interface **shall** be implemented. All providing interfaces implemented by a single TimeCard **shall** derive from the same unified timescale.

### 5.3.6 Control Interfaces

Control interfaces provide configuration, monitoring, alarms, telemetry, firmware management, and security operations. Control interfaces are specified in Clause 8.

At least one control interface **shall** be implemented. A control interface may be local, host-integrated, out-of-band, remote, or a combination thereof.

## 5.4 Unified Timescale

A TimeCard **shall** generate one unified timescale for each conforming TimeCard instance. All providing interfaces of that instance **shall** publish, encode, or derive from that unified timescale. Figure 2 illustrates the reference-to-egress flow.

![Unified timescale flow](figures/rendered/unified-timescale-flow.pdf)

The implementation **shall** document:

- The reference timescale used internally or exposed externally.
- The relationship between the unified timescale and UTC, TAI, the IEEE 1588 PTP timescale, or another declared timescale.
- The alignment tolerance among all providing interfaces that claim phase or time alignment.
- The behavior during startup, warm-up, lock acquisition, reference failover, holdover entry, holdover exit, and manual time adjustment.

Analog or periodic providing interfaces that claim continuous phase **shall** not introduce an undocumented phase step during normal locked operation. If a phase step, holdover event, failover transient, or other discontinuity can occur, its detection and reporting mechanism **shall** be documented.

## 5.5 Reference Selection and Ensemble Operation

If more than one receive reference is implemented, the TimeCard **shall** provide a documented reference-selection policy. The policy **shall** identify priority, validity, quality, failure detection, fallback, recovery, and operator override behavior.

If an implementation claims ensemble reference operation, it **shall** document:

- Supported input reference types.
- Weighting, voting, or selection method at a level sufficient for operational evaluation.
- Health and alarm criteria.
- Behavior when one or more ensemble sources degrade or fail.
- Metrics exposed through the control interface.

Ensemble operation **shall** produce one selected or synthesized reference for disciplining the unified timescale. It **shall** not create multiple independent conforming timescales within the same TimeCard instance unless those instances are separately identified and separately documented.

## 5.6 Host and Time-Transfer Interfaces

A host interface mapping defines how a host system discovers, configures, reads, writes, timestamps, or receives time from a TimeCard. PCIe, USB, serial, memory-mapped embedded interfaces, network interfaces, and implementation-specific mappings may be used.

Each host interface mapping **shall** document:

- Physical and logical interface standards used.
- Discovery and enumeration behavior.
- Per-instance selection, instance-identifier derivation, and identifier stability across restart, removal, reinsertion, and host reboot.
- Required driver-visible registers, messages, commands, or API elements.
- Endianness, alignment, units, and timestamp formats.
- Interrupts, polling requirements, and error reporting.
- Concurrency, time-control ownership, and behavior when more than one host client can issue timing-affecting operations.
- Behavior during host low-power states, sleep, hibernation, wake, orderly or surprise removal, hot plug, driver or service restart, and outstanding-operation cancellation.
- Latency, asymmetry, and correction information required for time-transfer evaluation.
- Host-clock identity, epoch, timescale, discontinuity behavior, and freshness information used for host-time correlation.

A host interface mapping that can expose more than one TimeCard **shall** provide unambiguous per-instance selection. An enumeration index **shall** not be the sole persistent selector when a stable supplier-assigned or implementation-derived identity is available.

A mapping that implements host-time correlation **shall** preserve the semantics and validity rules in 8.10.4. A mapping that permits more than one client to set or discipline time **shall** implement the arbitration requirements in 8.5.

If PCIe PTM is implemented, the implementation **shall** document the PTM capability defined by the PCI Express Base Specification, Revision 5.0, Version 1.0 [13], the measurement point represented by PTM timestamps, and any correction terms needed to relate PTM time to other providing interfaces.

Annex E provides informative examples of applying these requirements to Windows, macOS, and Linux host software.

## 5.7 Performance and Measurement Architecture

Performance requirements in this standard are expressed as reporting and measurement requirements unless a technical clause explicitly states a numeric limit. This allows TimeCards to serve different use cases while making supplier claims comparable.

An implementation **shall** identify the measurement point for each declared metric. Metrics **shall** be reported with enough context to reproduce or evaluate the claim, including reference source, measurement bandwidth, observation interval, environmental conditions, warm-up conditions, and lock state.

The following performance categories **shall** be addressed when applicable to the implemented interfaces:

- Time accuracy relative to a declared reference.
- Time stability, including MTIE and TDEV where applicable.
- Frequency stability, including ADEV where applicable.
- Phase noise for periodic frequency outputs where applicable.
- Time jitter for pulse outputs where applicable.
- Holdover error versus elapsed time.
- Lock acquisition, recovery, and failover behavior.
- Environmental sensitivity relevant to the declared operating profile.

Clause 6 defines the required reporting details for these categories. Annex A provides informative metric background.

## 5.8 Power, Mechanical, and Environmental Architecture

Physical TimeCard implementations **shall** document the power, mechanical, thermal, connector, and environmental assumptions needed for safe operation and declared timing performance.

Embedded or virtualized TimeCard implementations **shall** document the host resources, clock dependencies, thermal assumptions, and integration constraints that affect declared timing performance.

Detailed environmental requirements are specified in Clause 9.

## 5.9 Optional Features and Extensions

An implementation may include optional features or vendor-specific extensions. An extension **shall** use the documented extension mechanism for the applicable interface and **shall** not change the syntax, semantics, required state transitions, or error behavior of a standardized interface or profile claimed by the implementation.

Vendor-specific extensions **shall** be identified by a documented namespace, identifier range, capability, or version that distinguishes standardized P3335 behavior from implementation-specific behavior. Reserved values, register fields, message types, and identifiers **shall** not be assigned to extension behavior.

## 5.10 Documentation Requirements

Manufacturers **shall** provide documentation sufficient to evaluate and integrate a conforming TimeCard. The documentation **shall** include:

- Conformance statement required by Clause 4.
- Interface descriptions for all receive, providing, host, and control interfaces.
- Register maps, information models, schemas, command descriptions, or API descriptions needed to use the implemented control interfaces.
- PLL or disciplining-loop type and bandwidth, or a statement that the implementation does not use such a loop.
- Warm-up time to first usable output and warm-up time to declared full performance.
- Lock acquisition time, failover behavior, holdover entry and exit behavior, and recovery behavior.
- Declared performance metrics and measurement points required by Clause 6.
- Environmental and reliability information required by Clause 9.
- Reference-chain, calibration, measurement-point, and uncertainty information sufficient to support system-level traceability analysis, or an explicit statement identifying which information is unavailable.
- All optional features claimed and all conditional requirements exercised by those claims.

Documentation should be publicly available for commercial products and available to integrators for non-commercial, embedded, or custom implementations.

## 5.11 Informative Time-Flow Narrative

In a typical TimeCard, one or more receive interfaces acquire external timing references such as GNSS, PTP, PPS, frequency references, or other sources. Reference-selection logic evaluates those inputs and selects or synthesizes a reference. A disciplining function steers the local timing function. The time generator maintains the unified timescale. Providing interfaces distribute that unified timescale as PPS, frequency, Time of Day, packet timestamps, host-bus time, or other representations. Control interfaces report status, telemetry, alarms, and configuration state.

When all usable external references are lost, the TimeCard normally enters holdover or free-running operation. During holdover, the unified timescale continues according to the local timing function and any holdover model implemented by the TimeCard. The TimeCard reports the state transition and exposes the information needed to evaluate the declared holdover behavior.
