# IEEE P3335 PAR Scope and Purpose Trace

This file records the public PAR scope and purpose text used to align Clause 1 of the working draft.

## Sources

- IEEE SA project page: <https://standards.ieee.org/ieee/3335/11127/>
- IEEE IMS standards activities page: <https://ieee-ims.org/activities/about-technical-standards-activities/standards-activities>
- IEEE SA NesCom 2022-12-02 recommendation PDF: <https://standards.ieee.org/wp-content/uploads/2022/12/nescom-12022022rec.pdf>

## Approval Trace

The IEEE SA NesCom recommendation document for 2022-12-02 lists P3335, "Standard for Architecture and Interfaces for Time Card," with the recommendation to approve the new PAR until December 2026.

## Public Scope Text

This standard defines the generic architecture and interfaces of a time card system, which constitutes a traceable source of time-of-day to heterogeneous systems that distribute and/or use that time. Additionally, this standard defines figures of merit that univocally characterize the relevant performance of the Time Card.

The Time Card provides a traceable time-of-day for systems directly attached to it, as well as networked distributed systems. Such systems include, but are not limited to, servers hosting the Time Card, and servers synchronized with the Time Card using such protocols as Precision Time Protocol (PTP) or Network Time Protocol (NTP).

This standard also defines the basic building blocks of the Time Card and their interfaces in order to allow modularization. The main building blocks include time source, local oscillator, and time processor.

Additionally, this standard defines interfaces between the Time Card and other systems. This includes physical interfaces that allow input and output of time-related signals. This also includes logical interfaces that are compatible with Portable Operating System Interface for UNIX (POSIX) and include, for example, an interface to share a Physical Hardware Clock (PHC). This allows sharing the time of day with other systems, as well as providing means for diagnostic and configuration.

The definition of logical interfaces allows for a variety of Time Card form factors, such as Peripheral Component Interconnect Express (PCIe), while ensuring uniform support from the operating system. Any device that complies with this standard provides performance figures that are obtained following the specifications of this standard. As such, different implementations of the Time Card can be easily compared in terms of performance.

## Public Purpose Text

This standard provides:

- Interoperability of different implementations of the Time Card with the systems, and their operating systems, that use it as the source of time-of-day, to support a plug-and-play solution.
- Modular implementation of the Time Card to allow better customization to industry needs.
- Univocal comparison of different implementations of the Time Card in terms of the relevant performance metrics.
