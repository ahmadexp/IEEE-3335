# TimeCard Architecture Specification

## 5.1 -  Architecture Overview

A **TimeCard** is a modular subsystem designed to interface with a host system through a standardized hardware and software interface. Its primary purpose being to deliver a stable, accurate, and reliable source of time (in the form of time of day, phase, frequency, or all) to the host system.

The establishment of a standard architecture for TimeCards plays a critical role in ensuring interoperability among diverse implementations. By defining a consistent framework, different vendors can design and manufacture TimeCards with varying capabilities, performance levels, and technologies, while maintaining full compatibility with any compliant host. This standardization fosters innovation, simplifies integration, and enables seamless substitution or upgrade of TimeCards without requiring significant host system redesign.

---

## 5.2 - Core Timing Architecture

At its core, every TimeCard is built around an **frequency source** (with quantified stability), which serves as the foundational source of precise timing. This source oscillator function is complemented by one or more interfaces that enable the TimeCard to both **receive** and **distribute** time, phase, and frequency information to and from the host system.

---

## 5.3 - Inbound Signal Interface

The **receive interface** provides a means for the TimeCard to synchronize its oscillator to an external reference. Depending on the deployment environment and the required accuracy, this interface may take multiple forms.  Common examples include **Global Navigation Satellite System (GNSS)** receivers (e.g., GPS, Galileo, GLONASS, BeiDou), or other precision synchronization methods such as **Precision Time Protocol (PTP)**, **Network Time Protocol (NTP)**, **White Rabbit (WR)**, **WiWi**, **WWVB**, or **Pulse-Per-Second (PPS)** inputs. These interfaces allow the TimeCard to discipline its oscillator function and maintain alignment with an external time source.  The external references may or may not be more stable or of lower noise than this oscillator function.

In some configurations, a TimeCard may operate without any external timing input. In this mode, the TimeCard functions in **holdover**, relying solely on the stability of its internal oscillator to maintain accurate time over a defined interval. Such configurations are particularly useful in environments where external timing references are unavailable, intermittent, or deliberately excluded for security or operational isolation.

This flexible receive architecture enables TimeCards to support a wide use-case spectrum — from GNSS-disciplined primary time sources to autonomous holdover systems — while preserving a common and interoperable interface standard.

---

## 5.4 - Outbound Signal Interface

While the receive interface allows synchronization to an external reference, the **providing interface** ensures that the synchronized time and frequency are accurately distributed to the host system.

A providing interface is a **mandatory component** of every TimeCard. It defines the mechanism by which the TimeCard delivers time, frequency, or both to the host, forming the synchronization channel between them.

Depending on system requirements, the providing interface may consist of a single interface or a combination of multiple concurrent interfaces. Common examples include system bus standards such as **ISA**, **MCA**, **PCI**, and **PCI Express (PCIe)**, as well as peripheral and communication interfaces such as **Serial Bus**, **USB**, **SCSI**, **PCMCIA**, or **LPT**. The selection of interface type directly influences both the data exchange characteristics and the precision of temporal alignment achievable by the host.

To preserve the integrity and determinism of timing, it is strongly recommended that the providing interface implement **hardware-based timestamping**. Hardware timestamping enables timing information to be generated and measured directly within hardware logic, avoiding non-deterministic delays caused by software stacks, interrupt latencies, and/or operating system scheduling.

Timestamping can be realized through dedicated physical signals, such as a **Pulse-Per-Second (PPS)** output, or through in-bus implementations, such as **Precision Time Measurement (PTM)** (for Intel processors) within **PCIe** architectures. These mechanisms enable low-latency, deterministic time delivery and improve cross-vendor interoperability among TimeCard and host designs.

---

## 5.5  Management and Control Interface (M&CI)

In addition to the inbound and outbound signal interfaces, it is recommended that each TimeCard include at least one **management and control interface**. These interfaces enable configuration, monitoring, diagnostics, firmware management, and status reporting between the TimeCard and the host. A TimeCard without a management interface is acceptable if its operational parameters are fixed or pre-determined, and no runtime monitoring or control is required.

The management interface functions as the **control plane** of the TimeCard, distinct from the **data plane** used for delivering timing and frequency. Through this interface, the host can configure and observe operational parameters such as oscillator state, synchronization source selection, disciplining mode, holdover behavior, temperature compensation, and alarm or fault conditions.

The following M&CI busses are independent of one another, and a TimeCard may utilize more than one kind of bus.  Common examples of management and control interfaces include but are not limited to:
- **SMBus or I²C** – typically used for low-level configuration and telemetry in embedded environments.  
- **IPMI** (Intelligent Platform Management Interface) – for out-of-band management in server-class or rack-scale systems.  
- **PCIe Configuration Space Registers** – providing time-related control and status directly over the host bus, including direct memory access to the hardware control registers.  
- **Serial or USB interfaces** – enabling firmware updates, diagnostics, or advanced telemetry access.  
- **Network-based interfaces** such as REST, gRPC, or SNMP, for distributed or remotely managed timing systems.

To promote interoperability and consistency, all TimeCards **SHOULD** expose a minimum common set of registers and attributes in a standardized format, including (but not limited to):
- Current synchronization source and state  
- Clock disciplining status  
- Phase and frequency offset metrics  
- Holdover duration and expected drift  
- Alarm and fault indicators  
- Firmware version and build metadata  

Furthermore, the management interface **SHOULD** support secure firmware update and integrity verification mechanisms to ensure reliability and prevent unauthorized modification. Collectively, these management and control capabilities provide the operational transparency and lifecycle management required for seamless integration of TimeCards into data centers, telecom infrastructure, and AI back-end clusters.

---

## 5.6 - Power, Mechanical, and Environmental Considerations
The subsections apply only if the TimeCard is implemented physically, versus for instance as a firmware function within a larger system.
### 5.6.1 - Power Delivery
- TimeCards **SHALL** define and document input power rail voltages and tolerances (e.g., 12 V, 3.3 V).    
- If externally powered, protection against reverse polarity **SHALL** be included.  
- Deterministic power-up sequencing and optional energy storage for holdover **SHOULD** be supported.

### 5.6.2 - Mechanical Form Factor
- The physical envelope **SHALL** be documented.  
- Acceptable envelope forms include add-in cards (low-profile/full-height), mezzanine, or embedded.  
- Mounting **SHALL** withstand insertion/removal; strain relief for all cable ports (electrical or optical) **SHOULD** be included.  
- Faceplates **SHOULD** label at least GNSS, PPS, 10 MHz, ToD, and management ports and include indicator LEDs.

### 5.6.3 - Connectors and I/O
- RF/timing reference signal ports **SHALL** be impedance-matched.  
- PPS/10 MHz electrical levels, impedance, and edge polarity (trigger on rising versus falling edge) **SHALL** be specified.  
- Data and management ports **SHOULD** have ESD protection and mechanically locking connectors.

### 5.6.4 - Thermal Design
- Operating temperature range **SHALL** be defined; oscillator drift vs. temperature **SHOULD** be characterized and documented.  
- Host airflow assumptions **SHOULD** be documented; heat load during warm-up **SHALL** be specified.  
- Over/under-temperature thresholds **SHALL** be reported via a management and control interface, if such an interface is provided.

### 5.6.5 - Environmental and Reliability
- Shock, vibration, and humidity limits **SHOULD** be stated.  
- EMC/ESD compliance **SHOULD** meet target-market standards.  
- MTBF and wear-out items **SHOULD** be documented and published.  
- Safety, labeling, and disposal requirements **SHOULD** be provided.

---

## 5.7 - Reference Signals and Performance Metrics (Normative)
- IEEE 1139 and IEEE 1193 (39 and 93 are both correct) **SHOULD** be used for performance-metric definitions.
- NIST Special Publication 1065 by Riley is informative.
- Requirements **SHOULD** be conditioned on the physical type of signal, including but not limited to: electrical balanced or unbalanced, voltage and/or current levels, optical fiber type or free-space, frequency band, and so on.
- ITU G.703 Clause 19 **MAY** be used.
- ITU G.8271, Amendment 1, Annex A, **MAY** be used.  << **Verify - Annex A not found** >>
- Measurement bandwidths **SHALL** be reported.
  
### 5.7.1 - Unified Timescale (Normative)
A unified timescale comes from a single oscillator function which is published in multiple distribution formats each approximating the ideal of the timescale to the capabilities of that format.

A TimeCard **SHALL** generate a single unified timescale and **SHALL** publish it across all Outbound Interfaces.    

All boundaries between adjacent seconds of signals from the the providing interface of the same TimeCard instance **SHALL** align to within a time tolerance that is documented and published.

### 5.7.2 - Output Signal Classes (Informative)
Typical outputs include ToD, 1 PPS, 10 MHz/5 MHz, packetized time (PTP), and host-bus time (PTM).  
Electrical characteristics and limits **SHOULD** be published for each.

### 5.7.3 - Stability, Accuracy, Precision (Normative Reporting)
Qualities sought include adequate stability (ADEV/TDEV/MTIE), low phase noise, high accuracy, high precision, and fine resolution.  
Numeric targets are intentionally unspecified; vendors **SHALL** report measurements using:
- ADEV/TDEV versus tau  
- Time/frequency offset to reference  
- Timestamp granularity  
- Physical synchronization extent and conditions
- And any other measurement the manufacturer chooses to include

### 5.7.4 - Phase Noise and Time Jitter (Normative Reporting)
Periodic outputs (e.g., 10 MHz) **SHOULD** include PN spectrum vs. offset frequency.  
Pulse outputs (e.g., PPS), **SHALL** specify RMS and peak-to-peak time jitter and measurement bandwidth in Hertz.
These requirements **MAY** be conditioned on intended signal and intended use.

### 5.7.5 - Holdover Performance (Normative)
Vendors **SHALL** publish maximum holdover error vs. time, warm-up conditions, and test range.  
Holdover requirements apply to 1 PPS outputs assuming a perfect inbound reference.  
MTIE per ITU-T G.8260 (G.810 App II.5) **SHALL** be used as the holdover metric. Other holdover metrics may also be measured and documented.
Note that ITU G.8262.1 is very loose.  << **Need to explain "very loose".** >>

### 5.7.6 - Ensemble References (Normative)
Implementations **SHALL** support combining multiple references into one unified "Ensemble" reference.  
Ensemble logic **MAY** provide source weights, health, and alarms via management telemetry.

### 5.7.7 - Large-Extent Synchronization (Informative)
For data-hall or campus deployments, the intent is to achieve a specified maximum end-to-end time error while implementing calibration as needed, and meeting cable/optical constraints as a function of the physical dimensions (in meters) of the extent.  Many independent vendors are involved, so this is a matter of overall system design, and not of TimeCard design per se.

### 5.7.8 - Time-Flow Narrative (Informative)  
A TimeCard receives zero or more references, selects one via a policy, and disciplines its internal hardware clock using a PLL.  
The TimeCard can operate as a PTP Ordinary Clock.  A traversal narrative linked to a notional system block diagram will go here.

### 5.7.9 - Implementation Flexibility (Informative)
The “oscillator” NEED NOT be or contain a discrete resonator.  A nuclear frequency source may be used for applications requiring extremenly good performasnce.  A DDS or similar digital source may suffice for cost-sensitive designs.  
SWaP-C trade-offs are left to the market.

### 5.7.10 - Conformance and Interface Definitions (Normative Guidance)
Undefined interfaces **SHOULD** normatively cite approved Interface Definition Documents (IDDs) for interoperability.

Conformance testing **SHOULD** cover:
- ADEV/TDEV measurement methodology  
- PN masks and spectra  
- PPS alignment across all outputs  
- PTM latency/asymmetry characterization  
- Holdover MTIE verification  
- Ensemble behavior under reference loss
- Plus anything else the manufacturer chooses

---

## 5.8 - Documentation Requirements (Normative)

Manufacturers **SHALL** provide publicly available datasheets specifying at least the following:
- Which architectural principles and constraints are implemented  
- PLL/disciplining type and loop bandwidth  
- All performance metrics defined in §7 (for instance stability, accuracy, PN/jitter, holdover, ensemble)  
- Traceability data sufficient for analysis, or an explicit “traceability not supported” statement  
- All optional or conditional features provided in the implementation

---

## 5.9 - Vendor Datasheet Checklist (Informative)

| Category | Required / Recommended | Example Contents |
|-----------|------------------------|------------------|
| Electrical & Power | REQUIRED | Input rails, tolerance, current draw, sequencing |
| Mechanical | REQUIRED | Dimensions, connectors, faceplate layout |
| Thermal | REQUIRED | Operating/storage temp, airflow, warm-up load |
| Timing Performance | REQUIRED | ADEV/TDEV plots, PN spectra, holdover MTIE |
| Synchronization Inputs | REQUIRED | GNSS/PTP/NTP/WR interface specs |
| Outputs | REQUIRED | PPS, 10 MHz, ToD specs, alignment accuracy |
| Management | RECOMMENDED | Interface type, telemetry fields, firmware update method |
| Compliance | REQUIRED | Safety, EMC, ESD, RoHS, CE/FCC marks |
| Reliability | RECOMMENDED | MTBF, service intervals, backup power retention |
| Documentation | REQUIRED | Quick start guide, LED legend, calibration method |

---

## 5.10 - References (Normative)

- [G8620] ITU-T G.8260 *Definitions and terminology for synchronization in packet networks* (2015 or later).  
- [IEEE 1139] *IEEE Standard Definitions of Physical Quantities for Fundamental Frequency and Time Metrology*.
- [IEEE 1193] *IEEE Guide for Measurement of Environmental Sensitivities of Standard Frequency Generators*
- [MTIE] Stefano Bregni, *Measurement of Maximum Time Interval Error for Telecommunications Clock Stability Characterization*, IEEE Transactions on Instrumentation and Measurement, Vol. 45, No. 5, Oct 1996.  
- [PTPv2.1] IEEE 1588-2019 *Precision Time Protocol (PTP)*.  

---

## 5.11 - Bibliography (Informative)

- Wikipedia: [Precision Time Protocol] (https://en.wikipedia.org/wiki/Precision_Time_Protocol)  
- [IRS_DID] DI-IPSC-81434A, *Interface Requirements Specification Data Item Description* (1999).  
- [IDD_DID] DI-IPSC-81436A, *Interface Design Description Data Item Description* (1999).  
- [SSDD] DI-IPSC-81432A, *System/Subsystem Design Description* (1999).  
- [SSS] DI-IPSC-81431A, *System/Subsystem Specification* (2000).
- NIST Special Publication 1065 by Riley 

---

## 5.12 - Notes
The present P3335 standard document was initiated on 25 April 2025, largely based on *“TimeCard Architecture (Section 5) Draft (20250424).docx”*.

---

## 5.13 - Acronyms  
<< Cover all acronyms in the entire document here; later collect in a single section in the overall standard. >>
**1PPS** = One Pulse Per Second  
**ADEV** = Allan Deviation  
**ASIC** = Application Specific Integrated Circuit  
**DDS** = Direct Digital Synthesis  
**EMC** = Electro Magnetic Compatibility  
**ESD** = Electro Static Discharge  
**FPGA** = Field Programmable Gate Array  
**GNSS** = Global Navigation Satellite System  
**I2C** = Inter-Integrated Circuit  
**IDD** = Interface Definition Document  
**IRIG** = Inter-Range Instrumentation Group  
**ISA** = Industry Standard Architecture computer bus  
**ITU** = International Telecommunications Union  
**LED** = Light Emitting Diode  
**LPT** = Line Printer Terminal  
**MCA** = Micro Channel Architecture  
**MHz** = Megahertz (10^6 Hertz)  
**MTBF** = Mean Time Between Failure  
**MTIE** = Maximum Time Interval Error  
**NTP** = Network Time Protocol  
**PCIe** = Peripheral Component Interconnect Express  
**PCMCIA** = Personal Computer Memory Card International Association  
**PLL** = Phase Locked Loop  
**PN** = Phase Noise  
**PTM** = Precision Time Measurement (Intel)  
**PTP** = Precision Time Protocol  
**RMS** = Root Mean Square  
**SCSI** = Small Computer System Interface  
**SMB** = System Management Bus  
**SoC** = System on a Chip  
**SWaP-C** = Size, Weight, Power, and Cost  
**TDEV** = Time Deviation  
**ToD** = Time of Day  
**USB** = Universal Serial Bus  
**UTC** = Coordinated Universal Time  
**WG** = Working Group  
**WiWi** = Wireless two-Way interferometry  
**WR** = White Rabbit  
**WWVB** = Radio Station WWVB  

---

**End of Document**
