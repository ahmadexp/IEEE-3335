1. Architecture Overview

A TimeCard is a modular subsystem designed to interface with a host platform through a standardized hardware and software interface. Its primary purpose is to deliver a stable, accurate, and reliable source of time—in the form of phase, frequency, or both—to the host system.

The establishment of a standard architecture for TimeCards plays a critical role in ensuring interoperability among diverse implementations. By defining a consistent framework, different vendors can design and manufacture TimeCards with varying capabilities, performance levels, and technologies, while maintaining full compatibility with any compliant host. This standardization fosters innovation, simplifies integration, and enables seamless substitution or upgrade of TimeCards without requiring significant system redesign.

2. Core Timing Architecture

At its core, every TimeCard is built around a high-stability oscillator, which serves as the foundational source of precise timing. This oscillator is complemented by one or more interfaces that enable the TimeCard to both receive and distribute time and frequency information to and from the host system.

3. Receive Interface

The receive interface provides a means for the TimeCard to synchronize its oscillator to an external reference. Depending on the deployment environment and the required accuracy, this interface may take multiple forms. Common examples include Global Navigation Satellite System (GNSS) receivers (e.g., GPS, Galileo, GLONASS, BeiDou), or other precision synchronization methods such as Precision Time Protocol (PTP), Network Time Protocol (NTP), White Rabbit (WR), WiWi, WWVB, or Pulse-Per-Second (PPS) inputs. These interfaces allow the TimeCard to discipline its oscillator and maintain alignment with an external time source.

In some configurations, a TimeCard may operate without any external timing input—designated as “NONE” for its receive interface. In this mode, the TimeCard functions in holdover, relying solely on the stability of its internal oscillator to maintain accurate time over a defined interval. Such configurations are particularly useful in environments where external timing references are unavailable, intermittent, or deliberately excluded for security or operational isolation.

This flexible receive architecture enables TimeCards to support a wide spectrum of use cases—from GNSS-disciplined primary time sources to autonomous holdover systems—while preserving a common and interoperable interface standard.

4. Providing Interface

While the receive interface allows synchronization to an external reference, the providing interface ensures that the synchronized time and frequency are accurately distributed to the host system.

A providing interface is a mandatory component of every TimeCard. It defines the mechanism by which the TimeCard delivers time, frequency, or both to the host, forming the primary communication and synchronization channel between them.

Depending on system requirements, the providing interface may consist of a single interface or a combination of multiple concurrent interfaces. Common examples include system bus standards such as ISA, MCA, PCI, and PCI Express (PCIe), as well as peripheral and communication interfaces such as Serial Bus, USB, SCSI, PCMCIA, or LPT. The selection of interface type directly influences both the data exchange characteristics and the precision of temporal alignment achievable by the host.

To preserve the integrity and determinism of timing, it is strongly recommended that the providing interface implement hardware-based timestamping. Hardware timestamping enables timing information to be generated and measured directly within hardware logic, avoiding non-deterministic delays caused by software stacks, interrupt latencies, or operating system scheduling.

Timestamping can be realized through dedicated physical signals, such as a Pulse-Per-Second (PPS) output, or through in-bus implementations, such as Precision Time Measurement (PTM) within PCIe architectures. These mechanisms ensure low-latency, deterministic time delivery and improve cross-vendor interoperability among TimeCard and host designs.

5. Management and Control Interfaces

In addition to the receive and providing interfaces, it is recommended that each TimeCard include one or more management and control interfaces. These interfaces enable configuration, monitoring, diagnostics, firmware management, and status reporting between the TimeCard and the host. A TimeCard without a management interface remains acceptable when its operational parameters are fixed or pre-determined, and no runtime monitoring or control is required.

The management interface functions as the control plane of the TimeCard, distinct from the data plane used for delivering timing and frequency. Through this interface, the host can configure and observe operational parameters such as oscillator state, synchronization source selection, disciplining mode, holdover behavior, temperature compensation, and alarm or fault conditions.

Common examples of management and control interfaces include:

SMBus or I²C – typically used for low-level configuration and telemetry in embedded environments.

IPMI (Intelligent Platform Management Interface) – for out-of-band management in server-class or rack-scale systems.

PCIe Configuration Space Registers – providing time-related control and status directly over the host bus.

Serial or USB interfaces – enabling firmware updates, diagnostics, or advanced telemetry access.

Network-based interfaces such as REST, gRPC, or SNMP, for distributed or remotely managed timing systems.

To promote interoperability and consistency, all TimeCards SHOULD expose a minimum common set of registers and attributes in a standardized format, including (but not limited to):

Current synchronization source and state

Clock disciplining status

Phase and frequency offset metrics

Holdover duration and expected drift

Alarm and fault indicators

Firmware version and build metadata

Furthermore, the management interface SHOULD support secure firmware update and integrity verification mechanisms to ensure reliability and prevent unauthorized modification. Collectively, these management and control capabilities provide the operational transparency and lifecycle management required for seamless integration of TimeCards into data centers, telecom infrastructure, and AI back-end clusters.

6. Power, Mechanical, and Environmental Considerations
6.1 Power Delivery

TimeCards MUST define input rails and tolerances (e.g., 12 V, 3.3 V).

When powered via host bus, the TimeCard MUST meet that bus’s limits and sequencing.

If externally powered, protection against reverse polarity MUST be included.

Deterministic power-up sequencing and optional energy storage for holdover SHOULD be supported.

6.2 Mechanical Form Factor

The physical envelope MUST be documented.

Acceptable forms include add-in cards (low-profile/full-height), mezzanine, or embedded.

Mounting MUST withstand insertion/removal; strain relief for RF ports SHOULD be included.

Faceplates SHOULD label GNSS, PPS, 10 MHz, ToD, and management ports and include indicator LEDs.

6.3 Connectors and I/O

RF/timing ports MUST be impedance-matched and rated.

PPS/10 MHz electrical levels, impedance, and edge polarity MUST be specified.

Data and management ports SHOULD have ESD protection and locking connectors.

6.4 Thermal Design

Operating temperature range MUST be defined; oscillator drift vs. temperature SHOULD be characterized.

Host airflow assumptions SHOULD be documented; heat load during warm-up MUST be specified.

Over/under-temperature thresholds MUST be reported via management.

6.5 Environmental and Reliability

Shock, vibration, and humidity limits SHOULD be stated.

EMC/ESD compliance MUST meet target-market standards.

MTBF and wear-out items SHOULD be published.

Safety, labeling, and disposal requirements MUST be provided.

7. Reference Signals and Performance Metrics
7.1 Unified Timescale (Normative)

A TimeCard SHALL generate a single unified timescale and MUST publish it identically across all outputs.
All second boundaries from the same TimeCard instance MUST align exactly.

7.2 Output Signal Classes (Informative)

Typical outputs include ToD, 1 PPS, 10 MHz/5 MHz, packetized time (PTP), and host-bus time (PTM).
Electrical characteristics and limits SHOULD be published for each.

7.3 Stability, Accuracy, Precision (Normative Reporting)

Qualities sought include adequate stability (ADEV/TDEV/MTIE), low phase noise, high accuracy, high precision, and fine resolution.
Numeric targets are intentionally unspecified; vendors SHALL report measurements using:

ADEV/TDEV vs. τ,

Time/frequency offset to reference,

Timestamp granularity,

Physical synchronization extent and conditions.

7.4 Phase Noise and Time Jitter (Normative Reporting)

Periodic outputs (e.g., 10 MHz) SHOULD include PN spectrum vs. offset frequency.

For pulse outputs (e.g., PPS), SHALL specify RMS and peak-to-peak jitter and measurement bandwidth.

7.5 Holdover Performance (Normative)

Vendors SHALL publish maximum holdover error vs. time, warm-up conditions, and test range.

Holdover requirements apply to 1 PPS outputs assuming perfect reference.

MTIE per ITU-T G.8260 (G.810 App II.5) SHALL be used as the holdover metric.

7.6 Ensemble References (Normative)

Implementations SHALL support combining multiple references into one unified Ensemble reference.

Ensemble logic SHOULD expose source weights, health, and alarms via management telemetry.

7.7 Large-Extent Synchronization (Informative)

For data-hall or campus deployments, vendors SHOULD report achievable end-to-end time error, calibration needs, and cable/optical constraints.

7.8 Time-Flow Narrative (Informative)

A TimeCard receives zero or more references, selects one via a policy, and disciplines its internal hardware clock using a PLL.
PLL type and bandwidth materially affect behavior and SHOULD be disclosed.
The TimeCard can operate as a PTP Ordinary Clock toward the host or network.

7.9 Implementation Flexibility (Informative)

The “oscillator” NEED NOT be a discrete resonator; a DDS or similar digital source may suffice for cost-sensitive designs.
SWaP-C trade-offs are left to the market.

7.10 Conformance and Interface Definitions (Normative Guidance)

Undefined interfaces SHOULD normatively cite approved Interface Definition Documents (IDDs) for interoperability.

Conformance testing SHOULD cover:

ADEV/TDEV measurement methodology,

PN masks and spectra,

PPS alignment across all outputs,

PTM latency/asymmetry characterization,

Holdover MTIE verification,

Ensemble behavior under reference loss.

8. Documentation Requirements (Normative)

Manufacturers SHALL provide publicly available datasheets specifying:

Which architectural principles and constraints are implemented.

PLL/disciplining type and loop bandwidth or range.

All performance metrics in §7 (stability, accuracy, PN/jitter, holdover, ensemble).

Traceability data sufficient for analysis, or an explicit “traceability not supported” statement.

All optional or conditional features exercised in the implementation.

9. Vendor Datasheet Checklist (Informative)
Category	Required / Recommended	Example Contents
Electrical & Power	REQUIRED	Input rails, tolerance, current draw, sequencing
Mechanical	REQUIRED	Dimensions, connectors, faceplate layout
Thermal	REQUIRED	Operating/storage temp, airflow, warm-up load
Timing Performance	REQUIRED	ADEV/TDEV plots, PN spectra, holdover MTIE
Synchronization Inputs	REQUIRED	GNSS/PTP/NTP/WR interface specs
Outputs	REQUIRED	PPS, 10 MHz, ToD specs, alignment accuracy
Management	RECOMMENDED	Interface type, telemetry fields, firmware update method
Compliance	REQUIRED	Safety, EMC, ESD, RoHS, CE/FCC marks
Reliability	RECOMMENDED	MTBF, service intervals, backup power retention
Documentation	REQUIRED	Quick start guide, LED legend, calibration method

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
