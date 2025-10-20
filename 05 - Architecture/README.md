## Architecture

A TimeCard is a modular subsystem designed to interface with a host system through a standardized hardware and software interface. Its primary function is to deliver a stable, accurate, and reliable source of time, whether in the form of phase, frequency, or both, to the host platform.

The establishment of a standard architecture for TimeCards serves a critical role in ensuring interoperability among diverse implementations. By defining a common framework, different vendors can develop TimeCards with varying features, performance levels, and technologies, while still maintaining compatibility with any compliant host system.

At its core, a TimeCard is built around a high-stability oscillator that serves as the fundamental source of precise timing. This oscillator is coupled with one or more interfaces that enable the TimeCard to both receive and distribute time and frequency information to the host system.

The receive interface may take many forms depending on the deployment environment and required accuracy. Common options include Global Navigation Satellite System (GNSS) receivers (e.g., GPS, Galileo, GLONASS, BeiDou), or other precision time synchronization mechanisms such as Precision Time Protocol (PTP), Network Time Protocol (NTP), White Rabbit (WR), WiWi, WWVB, or Pulse-Per-Second (PPS) inputs. These interfaces allow the TimeCard to discipline its oscillator and maintain alignment with an external reference clock.

In some configurations, a TimeCard may operate without an external timing input—designated as “NONE” for its receive interface. In this case, the device functions in holdover mode, relying solely on the stability of its internal oscillator to maintain accurate time over a defined interval. Such configurations are useful in environments where external signals are unavailable, intermittent, or intentionally excluded for security or operational reasons.

This flexible architecture enables TimeCards to support a wide range of applications—from GNSS-disciplined primary time sources to autonomous holdover systems, while maintaining a consistent and standardized interface to the host platform. While the receive interface enables the TimeCard to synchronize with an external reference, the providing interface ensures that the synchronized time and frequency are accurately distributed to the host system.

A providing interface is an essential and mandatory component of every TimeCard. It defines the mechanism through which the TimeCard delivers precise time, frequency, or both to the host. In practice, this interface forms the primary communication and synchronization channel between the TimeCard and the host platform.

Depending on system requirements, the providing interface may consist of a single interface or a combination of multiple interfaces operating simultaneously. Typical examples include system bus interfaces such as ISA, MCA, PCI, and PCI Express (PCIe), as well as peripheral and communication interfaces such as Serial Bus, USB, SCSI, PCMCIA or LPT. The selection of interface type directly impacts both the data transfer characteristics and the temporal precision achievable in the host system.

To ensure the conservation of timing precision and mitigate latency uncertainty, it is strongly recommended that the providing interface support hardware-based timestamping. Hardware timestamping allows the timing information to be captured or generated directly at the hardware level, eliminating variations introduced by software stacks or interrupt handling.

Timestamping may be realized through dedicated physical signals, such as a Pulse-Per-Second (PPS) output, or through in-bus implementations such as Precision Time Measurement (PTM) in PCIe architectures. These mechanisms enable deterministic, high-accuracy time delivery and foster interoperability across diverse TimeCard and host system implementations.  

In addition to the receive and providing interfaces, it is recommended that a TimeCard include one or more management and control interfaces. These interfaces enable configuration, monitoring, firmware management, diagnostics, and status reporting between the TimeCard and the host system. A TimeCard without a managment interface is still accepted if the functionality is predetermined and no monitoring is needed. 

The management interface serves as the control plane of the TimeCard, distinct from the data plane functions that deliver timing and frequency. Through this interface, the host can read and modify operational parameters such as oscillator state, synchronization source selection, disciplining mode, holdover performance, temperature compensation, and alarm or fault conditions.

Common examples of management and control interfaces include: SMBus or I²C, typically used for basic configuration and telemetry access in hardware environments. IPMI (Intelligent Platform Management Interface), often employed in server-class systems for out-of-band monitoring and control. PCIe Configuration Space Registers, which may expose time-related status and configuration parameters directly over the host bus. Serial or USB interfaces, for more advanced interaction, firmware updates, or detailed telemetry collection via vendor-supplied tools. Network-based interfaces such as REST, gRPC, or SNMP, when the TimeCard is part of a larger distributed or remote-managed timing infrastructure.

To promote interoperability and cross-vendor compatibility, it is recommended that all TimeCards expose a minimum common set of registers and attributes in a standardized format. This may include fields for:

- Current synchronization source and state
- Clock disciplining status
- Phase and frequency offset statistics
- Holdover duration and expected drift
- Alarm or fault codes
- Firmware version and build metadata

Furthermore, the management interface should support secure firmware update and integrity verification mechanisms to ensure reliability and prevent unauthorized modification. Together, these management and control capabilities provide the operational transparency necessary for effective integration, remote management, and lifecycle maintenance of TimeCards in large-scale deployments, such as data centers, telecom infrastructure, or AI back-end clusters.

#### 4.1 Architectural Principles (Normative)



# 6 References (Normative)

[G8620] ITU-T G.8260 "Definitions and terminology for synchronization in packet networks"
and especially "Definitions and terminology for synchronization in packet networks –
Amendment 2", both 2015 issue or later. Available gratis.
<https://www.itu.int/en/Pages/default.aspx>.
[IEEE 1139] "IEEE Standard Definitions of Physical Quantities for Fundamental Frequency and
Time Metrology" defines ADEV and TDEV.
[MTIE] "Measurement of Maximum Time Interval Error for Telecommunications Clock
Stability Characterization", Stefano Bregni, IEEE Transactions on Instrumentation and
Measurement, Vol. 45, No. 5, October 1996, pages 900-906. Cites ITU G810 "Definitions and
terminology for synchronization networks", Appendix II.5 "Maximum Time Interval Error
(MTIE)".
[PTPv2.1] IEEE 1588-2019 "Precision Time Protocol"
7 Bibliography (Informative)
< https://en.wikipedia.org/wiki/Precision\_Time\_Protocol>

ComSoc article on PTP? << Need precise cite. >>
[IRS\_DID] DI-IPSC-81434A, "Interface Requirements Specification Data Item Description",
approved 1999-12-15, 20 pages. This defines the kinds of data that are required, but leaves their
detailed format to design. DIDs may be obtained gratis from the US Defense Acquisition
University website <https://www.dau.edu/> by searching for "DI-IPSC" (without quotes).
[IDD\_DID] DI-IPSC-81436A, "Interface Design Description Data Item Description",
approved 1999-12-15, 6 pages. This defines the exact format what every bit means and
exactly where it is located. This is essential for interoperability between various TimeCard
makes and models.
[SSDD] DI-IPSC-81432A, "System/Subsystem Design Description", approved 10 August 1999,
9 pages. The SSDD describes the system- or subsystem-wide design and the architectural design
of a system or subsystem.
[SSS] DI-IPSC-81431A, "System/Subsystem Specification", approved 1 October 2000,
11 pages. The SSS specifies the requirements for a system or subsystem and the methods to be
used to ensure that each requirement has been met.
8 Notes
The present P3335 standard formal text document was started on 25 April 2025, largely based on
"TimeCard Architecture (Section 5) Draft (20250424).docx".
9 Acronyms
**1PPS** = One Pulse Per Second, **ADEV** = Allen Deviation, **AM** = Amplitude Modulation, **ASIC**
= Application Specific Integrated Circuit, **DDS** = Direct Digital Synthesis, **FPGA** = Field
Programmable Gate Array, **GHz** = Gigahertz (10^9 Hz), **IDD** = Interface Definition Document
[IDD\_DID], **IRIG** = Inter-Range Instrumentation Group, **IRS** = Interface Requirements
Specification [IRS\_IDD], **ITU** = International Telecommunications Union, **MTIE** = Maximum
time interval error, **PCIe** = Peripheral Component Interconnect Express, **PLL** = Phase Locked
Loop, **PM** = Phase Modulation, **PN** = Phase Noise, **PTP** = Precision Time Protocol [PTPv2.1],
**RT** = Radar Time, **SI** = International Metric System (French abbreviation), **SoC** = System on a
Chip, **SSDD** = System/Subsystem Design Document (DI-IPSC-81432A), **SWaP** = Size, Weight
and Power, **TAI** = International Atomic Time (French abbreviation), **TC** = PTP Transparent
Clock, **TDEV** = Time Deviation, **UTC** = Coordinated Universal Time (French abbreviation),
**WG** = Working Group
