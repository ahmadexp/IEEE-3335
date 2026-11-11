# IEEE P3335 approved PAR text

Source: [IEEE SA P3335 project](https://standards.ieee.org/ieee/3335/11127/), [approved PAR 10369](https://development.standards.ieee.org/myproject-web/public/view.html#pardetail/10369), [public project record](https://development.standards.ieee.org/myproject-web/rest/api/public/par/10369). PAR approval: 2022-12-03. Compared 2026-11-10. The three fields below preserve the approved words and punctuation; whitespace is normalized. The RFC 5905 parenthesis and the PHC expansion in the Scope are as recorded; use Clauses 2 and 3 for the technical references and terminology. Refer any correction of PAR wording to the project editor.

## Scope

This standard defines the generic architecture and interfaces of a time card system, which constitutes a traceable source of time-of-day to heterogeneous systems that distribute and/or use that time. Additionally, this standard defines figures of merit that univocally characterize the relevant performance of the Time Card.

The Time Card provides a traceable time-of-day for systems directly attached to it, as well as networked distributed systems. Such systems include, but are not limited to, servers hosting the Time Card, and servers synchronized with the Time Card using such protocols as Precision Time Protocol (PTP) or Network Time Protocol (RFC Request for Comments) 5905).

This standard also defines the basic building blocks of the Time Card and their interfaces in order to allow modularization. The main building blocks include time source, local oscillator, and time processor.

Additionally, this standard defines interfaces between the Time Card and other systems. This includes physical interfaces that allow input and output of time-related signals. This also includes logical interfaces that are compatible with Portable Operating System Interface for UNIX (POSIX) and include for example an interface to share a Physical Hardware Clock (PHC). This allows sharing the time of day with other systems, as well as providing means for diagnostic and configuration. The definition of logical interfaces allows for a variety of Time Card’s form factors (e.g. Peripheral Component Interconnect Express (PCIe)) while ensuring uniform support from the operating system.

Any device that complies with this standard provides performance figures that are obtained following the specifications of this standard. As such, different implementations of the Time Card can be easily compared in terms of performance.

## Purpose

This standard provides 1) interoperability of different implementations of the Time Card with the systems, and their operating systems, that use it as the source of time-of-day; as such, to ensure a plug-and-play solution, 2) modular implementation of the Time Card to allow better customization to industry needs, and 3) univocal comparison of different implementations of the Time Card in terms of the relevant performance metrics.

## Need

So far, typically, traceable time-of-day sources constitute a part of systems that use and/or distribute that time, e.g., the Grandmaster Clock in systems based on IEEE 1588-2019. Such an approach limits versatility and slows down the adoption of new end-user and transport technologies, such as high-speed Ethernet.

This project is needed to improve flexibility, agility, and adaptability of systems that need traceable source of time-of-day. Such systems include, for example, data centers. In particular, this project is needed to decouple devices providing traceable source of time-of-day from the time-distribution protocols and their underlying transport technologies. This is needed to allow quick uptake of transport technology advancements in systems that need traceable time-of-day sources.

There is a need of a standardized modular approach in designing traceable time-of-day sources to increase versatility of implementations. And there is a need to improve clarity of performance specifications of different implementations. These will ensure that implementations are better suited to particular needs of end-users, systems, and industries.
