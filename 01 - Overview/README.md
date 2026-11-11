# 1. Overview

## 1.1 Scope

This standard defines the generic architecture and interfaces of a time card system, which constitutes a traceable source of time-of-day to heterogeneous systems that distribute and/or use that time. Additionally, this standard defines figures of merit that univocally characterize the relevant performance of the Time Card.

The Time Card provides a traceable time-of-day for systems directly attached to it, as well as networked distributed systems. Such systems include, but are not limited to, servers hosting the Time Card, and servers synchronized with the Time Card using such protocols as Precision Time Protocol (PTP) or Network Time Protocol (RFC Request for Comments) 5905).

This standard also defines the basic building blocks of the Time Card and their interfaces in order to allow modularization. The main building blocks include time source, local oscillator, and time processor.

Additionally, this standard defines interfaces between the Time Card and other systems. This includes physical interfaces that allow input and output of time-related signals. This also includes logical interfaces that are compatible with Portable Operating System Interface for UNIX (POSIX) and include for example an interface to share a Physical Hardware Clock (PHC). This allows sharing the time of day with other systems, as well as providing means for diagnostic and configuration. The definition of logical interfaces allows for a variety of Time Card’s form factors (e.g. Peripheral Component Interconnect Express (PCIe)) while ensuring uniform support from the operating system.

Any device that complies with this standard provides performance figures that are obtained following the specifications of this standard. As such, different implementations of the Time Card can be easily compared in terms of performance.

## 1.2 Purpose

This standard provides 1) interoperability of different implementations of the Time Card with the systems, and their operating systems, that use it as the source of time-of-day; as such, to ensure a plug-and-play solution, 2) modular implementation of the Time Card to allow better customization to industry needs, and 3) univocal comparison of different implementations of the Time Card in terms of the relevant performance metrics.

## 1.3 Need

So far, typically, traceable time-of-day sources constitute a part of systems that use and/or distribute that time, e.g., the Grandmaster Clock in systems based on IEEE 1588-2019. Such an approach limits versatility and slows down the adoption of new end-user and transport technologies, such as high-speed Ethernet.

This project is needed to improve flexibility, agility, and adaptability of systems that need traceable source of time-of-day. Such systems include, for example, data centers. In particular, this project is needed to decouple devices providing traceable source of time-of-day from the time-distribution protocols and their underlying transport technologies. This is needed to allow quick uptake of transport technology advancements in systems that need traceable time-of-day sources.

There is a need of a standardized modular approach in designing traceable time-of-day sources to increase versatility of implementations. And there is a need to improve clarity of performance specifications of different implementations. These will ensure that implementations are better suited to particular needs of end-users, systems, and industries.

## 1.4 Word usage

The word **shall** indicates mandatory requirements strictly to be followed in order to conform to the standard and from which no deviation is permitted (**shall** equals *is required to*).[^1],[^2]

The word *should* indicates that among several possibilities one is recommended as particularly suitable, without mentioning or excluding others; or that a certain course of action is preferred but not necessarily required (*should* equals *is recommended that*).

The word *may* is used to indicate a course of action permissible within the limits of the standard (*may* equals *is permitted to*).

The word *can* is used for statements of possibility and capability, whether material, physical, or causal (*can* equals *is able to*).

[^1]: The use of the word *must* is deprecated and cannot be used when stating mandatory requirements; *must* is used only to describe unavoidable situations.

[^2]: The use of *will* is deprecated and cannot be used when stating mandatory requirements; *will* is only used in statements of fact.

## 1.5 Applicability and implementation freedom

The core application is a subsystem explicitly designed to provide timing to a directly attached host or system. Its local timing function maintains a unified timescale and can use a directly connected reference, such as a GNSS receiver, a pulse or frequency reference, or an internal primary reference. Upstream packet timing recovery and downstream network distribution are independent optional functions. An isolated implementation need not have an external receive interface (see 5.3.4). A TimeCard supplies evidence for system-level traceability; conformance alone does not establish end-to-end traceability.

This standard applies to a TimeCard realized as a discrete add-in card, embedded hardware or gateware, a system-on-chip function, or an external timing unit. Conformance is based on observable behavior, implemented interfaces, and supplier declarations rather than physical form factor.

This standard does not prescribe an internal oscillator technology, disciplining algorithm, ensemble algorithm, physical partitioning, or product construction unless that choice affects a claimed interface or externally observable behavior. It does not replace product-safety, electromagnetic-compatibility, environmental, spectrum, export, or other regulatory obligations.

## 1.6 Relationship to other standards

P3335 uses established standards where they define a protocol, signal, or metric needed by a claimed TimeCard function. Clause 2 lists the documents that are indispensable to implementing those functions. Annex C lists related documents used for background or deployment guidance.

The principal areas of coordination are:

- IEEE Std 1588-2019 [4] and IEEE Std 802.1AS-2025 [5] for packet-based time synchronization.
- IEEE Std 1139-2022 [2], IEEE Std 1193-2022 [3], ITU-T Recommendation G.810 (08/1996) [10], and ITU-T Recommendation G.8260 (11/2022) [11] for time and frequency metrology.
- The PCI Express Base Specification, Revision 5.0, Version 1.0 [13], for PCIe and Precision Time Measurement behavior.
- IRIG Standard 200-16 [8] for claimed IRIG time-code interfaces.
- Management protocol specifications for control interfaces that claim those protocols.

## 1.7 Document structure

| Clause or annex | Content |
|-----------------|---------|
| Clause 1 | Scope, purpose, need, applicability, and document organization. |
| Clause 2 | Normative references. |
| Clause 3 | Terms, definitions, acronyms, and abbreviations. |
| Clause 4 | Conformance model, profiles, statements, and evidence. |
| Clause 5 | TimeCard architecture and unified-timescale behavior. |
| Clause 6 | Performance declaration and characterization requirements. |
| Clause 7 | Receive and providing timing interfaces. |
| Clause 8 | Control interfaces and the baseline control information model. |
| Clause 9 | Environmental, mechanical, electrical, and lifecycle declarations. |
| Clause 10 | Informative application and deployment guidance. |
| Annex A | Informative metric background. |
| Annex B | Informative example test procedures. |
| Annex C | Bibliography. |
| Annex D | Informative conformance-statement proforma. |
| Annex E | Informative host operating-system integration guidance. |
