# 1. Overview

## 1.1 Scope

This standard defines the generic architecture and interfaces of a TimeCard system, which constitutes a traceable source of time-of-day to heterogeneous systems that distribute or use that time. It also defines figures of merit that characterize the relevant performance of a TimeCard.

The core application covered by this standard is a TimeCard that maintains a unified timescale using a local timing function and supplies that timescale to at least one directly attached host or system. The local timing function is commonly coupled directly to a local timing reference, such as a GNSS receiver, a 1PPS source, a frequency reference, or an internal primary reference. Recovery of timing carried through an upstream packet synchronization chain, including PTP, is an optional receive function. Distribution from the directly attached host or TimeCard to downstream networked systems, including through PTP or NTP, is an optional providing function. An implementation that claims either optional function is subject to the applicable requirements of Clauses 4 through 7.

A TimeCard provides time-of-day to directly attached systems and to networked distributed systems. Such systems include a host containing the TimeCard and systems synchronized through protocols such as the Precision Time Protocol (PTP) or Network Time Protocol (NTP). P3335 requires the reference relationships, measurement points, uncertainty information, and supporting evidence needed to evaluate the TimeCard contribution to a system-level traceability analysis. Conformance to P3335 does not, by itself, establish end-to-end traceability for an integrated system.

This standard defines the basic functional building blocks of a TimeCard and the interfaces among those blocks to support modular implementation. The principal functions include a time source, a local timing function, and a time processor.

This standard also defines physical and logical interfaces between a TimeCard and other systems. Physical interfaces convey time-related input and output signals. Logical interfaces support host operating-system integration, including access to a PTP hardware clock (PHC). The logical model accommodates form factors such as Peripheral Component Interconnect Express (PCIe), embedded hardware functions, and external timing units.

Conforming implementations provide performance figures obtained and reported according to this standard so that TimeCard implementations can be evaluated on a common basis.

## 1.2 Purpose

The purpose of this standard is to provide:

- Interoperability between TimeCard implementations and the systems and operating systems that use them as sources of time-of-day.
- Modular implementation of TimeCard functions to support different application needs and implementation technologies.
- Unambiguous comparison of TimeCard implementations using common performance metrics, measurement points, and operating conditions.

## 1.3 Need

Distributed computing, telecommunications, industrial control, finance, and scientific measurement can depend on precise and traceable time. Existing implementations often use product-specific signal definitions, control models, and performance claims. These differences increase integration effort and make independent comparison difficult.

P3335 addresses that need by defining externally observable TimeCard functions, conditional interface profiles, a unified-timescale model, a transport-neutral control information model, and a common performance declaration framework.

## 1.4 Applicability and implementation freedom

This standard applies to a TimeCard realized as a discrete add-in card, embedded hardware or gateware, a system-on-chip function, or an external timing unit. Conformance is based on observable behavior, implemented interfaces, and supplier declarations rather than physical form factor.

This standard does not prescribe an internal oscillator technology, disciplining algorithm, ensemble algorithm, physical partitioning, or product construction unless that choice affects a claimed interface or externally observable behavior. It does not replace product-safety, electromagnetic-compatibility, environmental, spectrum, export, or other regulatory obligations.

## 1.5 Relationship to other standards

P3335 uses established standards where they define a protocol, signal, or metric needed by a claimed TimeCard function. Clause 2 lists the documents that are indispensable to implementing those functions. Annex C lists related documents used for background or deployment guidance.

The principal areas of coordination are:

- IEEE Std 1588-2019 [4] and IEEE Std 802.1AS-2025 [5] for packet-based time synchronization.
- IEEE Std 1139-2022 [2], IEEE Std 1193-2022 [3], ITU-T Recommendation G.810 (08/1996) [10], and ITU-T Recommendation G.8260 (11/2022) [11] for time and frequency metrology.
- The PCI Express Base Specification, Revision 5.0, Version 1.0 [13], for PCIe and Precision Time Measurement behavior.
- IRIG Standard 200-16 [8] for claimed IRIG time-code interfaces.
- Management protocol specifications for control interfaces that claim those protocols.

## 1.6 Document structure

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
