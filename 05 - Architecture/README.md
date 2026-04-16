# TimeCard Architecture Specification

While Host Systems use TimeCards, host systems are generally not themselves timing systems.  One or more Time Sources provide Reference Signals to one or more TimeCard implementations within each Host System.  Each Time Card receives the Reference Signals from the external Time Sources (see _diagram_), and provides local reference signals to one or more consumers within the Host System. 

_Context:_  The intent of the following figure is to define the overall system from external time reference sources to the host system and the TimeCards within, and how they all fit together.  **<< A figure will go below >>**

The establishment of a standard architecture for TimeCards is critical to enabling interoperability among diverse implementations. Given a consistent framework, different vendors can design and manufacture TimeCards with varying capabilities, performance levels, and core technologies, while maintaining full plug-and-play compatibility with any compliant host. This standardization fosters an open ecosystem, simplifies hardware integration, and enables seamless substitution or generational upgrades of TimeCards without requiring significant redesign of the host systems.

## 5.1 - Architecture Overview

A **TimeCard** is a modular subsystem designed to interface with a computing host system through a standardized hardware and software interface. The TimeCard's primary purpose is to deliver a stable, accurate, and reliable source of time (in the form of time of day, phase, frequency, or any combination thereof) to a host system.

### 5.1.1 Rationale for Dedicated Timing Subsystems
Modern host systems (such as high-performance servers, edge compute nodes, and telecommunications routers) typically lack the internal capabilities required to maintain roughly sub-microsecond or nanosecond-scale synchronization.  Host limitations generally include unpredictable software and operating system scheduling latencies that interfere with precise clock steering.

The temperature dependence of all properties of physical components, like standard quartz oscillators, is always relevant. 

The lack of widely applicable, commercially available, specialized hardware for bounded-latency time transfer and/or hardware timestamping is also a driver.

The TimeCard overcomes these host limitations by moving critical timing functions—such as phase-locked loops (PLLs), holdover tracking, and signal timestamping—to a dedicated, physically isolated subsystem. By incorporating a TimeCard, a host system gains enhanced timekeeping and synchronization capabilities without requiring a fundamental redesign of the host's primary processing architecture.  This also supports incremental host system modernization by upgrading and re-integrating TimeCards.

### 5.1.2 Implementation Modularity
While a common physical manifestation of a TimeCard is a discrete add-in card (such as a PCI Express card) inserted into a server chassis, a TimeCard system is fundamentally defined by its logical interfaces and behaviors rather than its physical implementation and constraints.  

Alternate valid implementations include, but are not limited to:
* A dedicated Intellectual Property block directly embedded into a System-on-Chip (SoC) or integrated onto a server motherboard.  How to formally prove adherence using only black-box tests is defined in section **04 Conformance**.
* An external desktop or ruggedized module temporarily or permanently connected to the host system via a hot-pluggable or peripheral interface (e.g., USB, Thunderbolt).

Any host system subsystem that meets the architectural boundaries and interface definitions defined within this standard **SHALL** be deemed a TimeCard for the purposes of conformance.

### 5.1.3 Hardware Timestamping
To preserve the integrity and determinism of timing, it is strongly recommended that both the providing and receiving interfaces implement **hardware-based timestamping**. Hardware timestamping enables timing information to be generated and measured directly within hardware logic, avoiding random delays caused by software stacks, interrupt latencies, and/or operating system scheduling and the like.

Hardware timestamping can be achieved through dedicated physical signals, such as a Pulse-Per-Second (PPS) output, or through advanced in-bus implementations, such as Precision Time Measurement (PTM) within modern PCI Express (PCIe) architectures. By moving the clock boundaries directly into the hardware bus, these mechanisms enable low-latency, deterministic time delivery. This allows distributed databases and cellular packet schedulers to achieve sub-microsecond absolute precision, improving cross-vendor interoperability among TimeCard and host designs.

---

## 5.2 - Core Timing Architecture

At its core, every TimeCard is built around at least one **frequency source** (with quantified stability), which serves as the foundational source of precise timing. This source-oscillator function is complemented by one or more interfaces that enable the TimeCard to receive and/or generate and distribute time-of-day, phase, and frequency information to and from the host system.

---

## 5.3 - Inbound (Receiving) Signal Interface

The **receive interface** provides a means for the TimeCard to synchronize its oscillator function to an external reference. Depending on the deployment environment and the required accuracy, this interface may take multiple forms.  Common examples include **Global Navigation Satellite System (GNSS)** receivers (e.g., GPS, Galileo, GLONASS, BeiDou), or other precision synchronization methods such as **Precision Time Protocol (PTP)**, **Network Time Protocol (NTP)**, **White Rabbit (WR)**, **WiWi**, **WWVB**, or **Pulse-Per-Second (PPS)** inputs. These interfaces allow the TimeCard to discipline its oscillator function and maintain alignment with an external time source.  The external references may or may not be more stable or of lower noise than this oscillator function.

In some configurations, a TimeCard may operate without any inbound external timing input. In this mode, the TimeCard functions in **holdover**, relying solely on the stability of its internal oscillator function to maintain accurate time over a defined interval. Such configurations are particularly useful in environments where external timing references are unavailable, intermittent, or deliberately excluded for security or operational isolation to support redundancy.

This flexible receive architecture enables TimeCards to support a wide use-case spectrum - from GNSS-disciplined primary time sources at the edge of the network, to boundary clocks that lack access to any PTPv2 *Grand Master*, to autonomous isolated holdover systems - while preserving a common and interoperable host interface standard. (Boundary Clocks are required to have at least two PTP inbound ports.)  

In datacenters having a large number of servers, this flexible architecture allows a single common application (not I/O driver) executable binary to be installed in all servers (a great simplification), each server determining its role and the specific external timing source to be used.  

IEEE 1588-2019 [PTPv2.1] (Hybrid) Mixed Multicast Unicast Operation **MAY** be required for physically large host systems.

---

## 5.4 - Outbound (Providing) Signal Interface

While the receive interface allows synchronization to an external reference, the **providing interface** supports distribution of accurate synchronized time and frequency within the associated host system.

At least one providing interface **SHALL** be present on every TimeCard.  This interface defines the mechanism by which the TimeCard delivers time-of-day, phase, and/or frequency to the host in any combination, thereby forming the synchronization channel between the TimeCard and the host.

Depending on system requirements, the provided interface may consist of a single interface or a combination of multiple concurrent interfaces. Common examples include system bus standards such as **ISA**, **MCA**, **PCI**, and **PCI Express (PCIe)**, as well as peripheral and communication interfaces such as **Serial Bus**, **USB**, **SCSI**, **PCMCIA**, or **LPT**. The selection of interface type directly influences both the data exchange characteristics and the precision of temporal alignment achievable by the host.

---

## 5.5  Management and Control Interface (M&CI)

In addition to the inbound and outbound signal interfaces, it is recommended that each TimeCard include at least one **Management and Control Interface (M&CI)**. These interfaces enable configuration, monitoring, diagnostics, firmware management, and status reporting between the TimeCard and the host. A TimeCard without a management interface is acceptable if no runtime monitoring or control is required.

The concept of control and data planes arose decades ago **( details lost, circa 1970? Good reference? May have come from IBM, in the midst of the realization that using special data values for control caused endless problems)**, originally in hardware design, later in the design of networking hardware, where it was observed that things were simplified if one separates data from control.  A few layers carried the data being processed, and a few other layers carried control signals to implement the processing algorithm.  Those same algorithms and controls are now implemented in firmware et al, but the general concepts of control and data planes endure.

The management interface functions as (or is part of) the **control plane** of the TimeCard, distinct from the **data plane** used for delivering timing and frequency. Through this interface, the host can configure and observe operational parameters such as oscillator state, synchronization source selection, disciplining mode, holdover behavior, temperature compensation, and alarm or fault conditions.

The following M&CI buses are independent of one another, and a TimeCard may utilize more than one kind of bus simultaneously.  Common examples of management and control interfaces include, but are not limited to:
- **SMBus or I²C** – typically used for low-level configuration and telemetry in embedded environments.  
- **IPMI** (Intelligent Platform Management Interface) – for out-of-band management in server-class or rack-scale systems.  
- **PCIe Configuration Space Registers** – providing time-related control and status directly over the host bus, including direct memory access to the hardware control registers.  
- **Serial or USB interfaces** – enabling firmware updates, diagnostics, or advanced telemetry access.  
- **Network-based interfaces** such as REST, gRPC, or SNMP, for distributed or remotely managed timing systems.

To promote interoperability and consistency, all TimeCards **SHOULD** expose a minimum common set of registers and attributes in a standardized format, including (but not limited to):  **(MAP != API, not interchangeable, need both.  Lots of existing base requires MAPs.  Have APIs be wrappers on underlying MAPs? Looking for a better approach.)**
- Current synchronization sources and their states  
- Clock disciplining status  
- Phase and frequency offset metrics  
- Holdover duration and expected drift  
- Alarm and fault indicators  
- Firmware version and build metadata  

Furthermore, the management interface **SHOULD** support secure firmware update and integrity verification mechanisms to enable reliability and prevent unauthorized modification. Together, these management and control capabilities give you the operational transparency and lifecycle management you need to integrate TimeCards into data centers, telecom infrastructure, and AI back-end clusters. In distributed environments, centralized management software can poll these M&CI endpoints to establish a global view of timing health, rapidly identifying degraded oscillators or spoofed GNSS signals to support mitigation. 

---

## 5.6 - Power, Mechanical, and Environmental Considerations
The subsections herein apply only if the TimeCard is implemented physically, versus, for instance, as a firmware function within a larger system.
Requirements stated in this section may normatively reference other standards.  This approach is preferred to listing numerical values to prevent conflicts arising between independently updated standards.

### 5.6.1 - Power Delivery
- TimeCard vendors **SHALL** define and document input power rail voltages and tolerances (e.g., 12 V, 3.3 V).    
- If externally powered, the TimeCard **SHALL** survive reverse polarity without damage or permanent degradation for any length of time, but need not work during reverse polarity.  
- Such things as deterministic power-up sequencing and optional energy storage for holdover **SHOULD** be supported and documented.

### 5.6.2 - Mechanical Form Factor
- The per-unit weight and physical envelope expressed in standard Metric or Imperial numerical physical units **SHALL** be documented.  
- Acceptable envelope forms include add-in cards (low-profile/full-height), mezzanine, or embedded.  
- Mounting **SHALL** withstand insertion/removal and strain relief for all cable ports (electrical or optical) **SHOULD** be included.  
- Faceplates **SHOULD** label at least GNSS, PPS, 10 MHz, ToD, and management ports and include visual status indicators.

### 5.6.3 - Connectors and I/O
- Analog RF/timing reference signal ports **SHALL** be impedance-matched to drive a transmission line at least ten meters in length.  
- PPS/10 MHz electrical levels, impedance, and edge polarity (trigger on the rising or the falling edge) **SHALL** be specified.  
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
- The details are left to design, and are often governed by local laws and regulations, or such things as local and/or national electrical and fire safety regulations.

---

## 5.7 - Reference Signals and Performance Metrics (Normative)
- Methods defined in **Annex A (Metrics)** of the present standard, which align with IEEE 1139, IEEE 1193, and ITU-T G.810 / G.8260, **SHOULD** be used for performance-metric definitions and analysis.  
- NIST Special Publication 1065 by Riley [NIST-1065]
- Requirements **SHOULD** be conditioned on the physical characteristics of the interface type, including but not limited to: electrical balanced or unbalanced signaling, voltage and/or current thresholds, optical fiber classification, and frequency band.
- ITU-T G.703 Clause 19 **MAY** be used as a reference for synchronous signaling.
- Measurement equipment bandwidths in Hertz and trace averaging settings **SHALL** be explicitly documented alongside all reported performance results.
  
### 5.7.1 - Unified Timescale (Normative)
A unified timescale is derived from a single oscillator function and is published simultaneously in multiple distribution formats, each format approximating the ideal timescale to the capabilities of that distribution format.

A TimeCard **SHALL** generate exactly one unified timescale and **SHALL** publish this timescale across all Outbound Interfaces.  _Note that multiple TimeCards are needed to implement multiple unified timescales_.

All boundaries between adjacent seconds of signals from the providing interface of the same TimeCard instance **SHALL** align to within a specified time tolerance that is documented and published.  This is necessary for Ensemble reference signals (§5.7.6 herein) to be generated and used.

All analog reference signal forms of a unified timescale **SHALL** have continuous time phase, although the time derivatives of the phase need not be continuous.  

### 5.7.2 - Output Signal Classes (Normative)
Typical outputs include ToD, 1 PPS, 10 MHz/5 MHz, packetized time (PTP), and host-bus time (PTM).  Electrical characteristics and limits **SHOULD** be published for each.  This may be done using normative references to formal standards.

### 5.7.3 - Stability, Accuracy, Precision (Normative Reporting)
Qualities sought include adequate stability (ADEV/TDEV/MTIE), low phase noise, high accuracy, high precision, and fine resolution.  
Numerical targets aren't set; they're determined by design and the current market. 

Vendors **SHALL** report measurements using:
- ADEV/TDEV versus tau  
- Time/frequency offset to reference  
- Timestamp granularity  
- Physical synchronization extent and conditions
- And any other measurement the manufacturer or vendor chooses to include

### 5.7.4 - Phase Noise and Time Jitter (Normative Reporting)
Periodic outputs (e.g., 10 MHz) **SHOULD** include PN spectrum vs. offset frequency.  
Pulse outputs (e.g., PPS) SHALL specify RMS and peak-to-peak time jitter, and measurement bandwidth in Hertz.
These requirements **MAY** be conditioned on signal kind and the intended use or uses.

### 5.7.5 - Holdover Performance (Normative)
Holdover performance measures the stability of the TimeCard when all external synchronization references are unavailable.
- Vendors **SHALL** publish the maximum holdover error bounds versus elapsed time (e.g., drift in microseconds over 4, 12, and 24 hours).
- Vendors **SHALL** publish the warm-up conditions required before the oscillator's holdover stability guarantees become valid, and the test temperature range the holdover specification assumes.  
- Holdover requirements apply to the continuous physical drift of the 1PPS output, assuming the TimeCard was previously locked to a perfect, zero-noise inbound reference prior to disconnection for some specified minimum period of time.  
- Maximum Time Interval Error (MTIE) per ITU-T G.8260 (or G.810 App II.5) **SHALL** be used as the definitive mathematical holdover metric. Other auxiliary holdover metrics (such as frequency aging rate) **MAY** also be measured and documented.

*Informative Note:* Implementers should be cautious when relying solely on generic telecommunications boundaries (such as certain relaxed profiles within ITU G.8262.1), as those bounds are often too loose for the nanosecond-class strictness required by modern distributed host systems. P3335 TimeCards often require significantly tighter phase-drift boundaries.

### 5.7.6 - Ensemble References (Normative)
Implementations **SHALL** support combining multiple inbound references into one unified "Ensemble" inbound reference.  

Ensemble logic **MAY** provide source weights, health, and alarms via management telemetry.

One example of an Ensemble Clock is one in which the local Primary Reference provides phase and frequency, and an incoming external reference signal defines the boundaries between adjacent SI Seconds and labels those seconds according to a standard timescale such as TAI or UTC.

### 5.7.7 - Large-Extent Synchronization (Informative)
For data-hall or campus deployments, the intent is to achieve a specified maximum end-to-end time error while implementing calibration as needed, and meeting cable/optical constraints as a function of the three-dimensional physical dimensions (in meters) of the deployment extent.  Many independent vendors are involved, so this is a matter of overall host system design, and not of TimeCard design per se.

### 5.7.8 - Time-Flow Narrative (Informative)  
The logical flow of time through the TimeCard architecture generally follows these stages:

1. **Ingress:** The TimeCard receives zero or more external references (e.g., GNSS, PTP, or PPS, or an Ensemble of external references).
2. **Selection:** The system evaluates the health, stability, and configured priority of the incoming references and selects the most optimal source using a defined policy (e.g., [PTPv2.1] Best Master Clock Algorithm).
3. **Disciplining (PLL):** The selected reference is fed into a phase-locked loop (PLL), which stably and smoothly disciplines the TimeCard's internal local oscillator. This loop filters out short-term jitter from the reference, relying on the local oscillator's high short-term stability to provide a clean signal.
4. **Timescale Generation:** The disciplined oscillator drives a hardware counter, generating a _single_, unified timescale implementing a timescale such as TAI or UTC.
5. **Egress:** The unified timescale is published across all Outbound Interfaces simultaneously. This includes generating physical PPS edges, updating memory-mapped Time of Day registers, scaling frequency outputs (e.g., 10 MHz), and serving host PCIe PTM requests—all originating from the exact same hardware counter.

If the last ingress reference is lost, the TimeCard enters **Holdover** (the PLL stops updating), keeping the unified timescale running based purely on the uncorrected drift behavior of the local oscillator function.

### 5.7.9 - Implementation Flexibility (Informative)
The “oscillator function” need not be or contain a discrete resonator.  A direct atomic primary frequency reference source may be used for applications requiring extremely good performance.  A DDS or similar digital source may suffice for cost-sensitive designs.  
SWaP-C trade-offs are left unspecified to allow design to follow the then-current market.

### 5.7.10 - Conformance and Interface Definitions (Normative Guidance)
Undefined interfaces **SHALL** normatively cite approved  **<< How good does this have to be?  Approved by whom, and how? >>** formal Interface Definition Documents (IDDs) for interoperability.

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
- PLL/disciplining loop type and bandwidth  
- All performance metrics defined in §7 (for instance, stability, accuracy, PN/jitter, holdover, ensemble)  
- Traceability data sufficient for analysis, or an explicit “traceability not supported” statement  
- All optional or conditional features provided in the implementation

---

## 5.9 - Vendor Datasheet Checklist (Informative)

**<< Explain the purpose of this section, update, disperse items herein, or delete entire section.  Does this really belong in _04-Conformance_?   >>**

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
| Documentation | REQUIRED | Quick start guide, visual indicator legend, calibration method |

---

## 5.10 - References (Normative)

- [G8620] ITU-T G.8260 *Definitions and terminology for synchronization in packet networks* (2015 or later).  
- [IEEE 1139] *IEEE Standard Definitions of Physical Quantities for Fundamental Frequency and Time Metrology*.
- [IEEE 1193] *IEEE Guide for Measurement of Environmental Sensitivities of Standard Frequency Generators*
- [MTIE] Stefano Bregni, *Measurement of Maximum Time Interval Error for Telecommunications Clock Stability Characterization*, IEEE Transactions on Instrumentation and Measurement, Vol. 45, No. 5, Oct 1996.  
- [PTPv2.1] IEEE 1588-2019 *Precision Time Protocol (PTP)*.  

---

## 5.11 - Bibliography (Informative)

-[IDD_DID] DI-IPSC-81436A, *Interface Design Description Data Item Description* (1999).  
-[IRS_DID] DI-IPSC-81434A, *Interface Requirements Specification Data Item Description* (1999).  
-[NIST-1065]  NIST Special Publication 1065 (by W.J. Riley) provides an informative foundation for frequency metrology.  
-[Precision Time Protocol] (https://en.wikipedia.org/wiki/Precision_Time_Protocol)  Wikipedia  
-[SSS] DI-IPSC-81431A, *System/Subsystem Specification* (2000).  
-[SSDD] DI-IPSC-81432A, *System/Subsystem Design Description* (1999).  

---

## 5.12 - Notes
The present P3335 standard document was initiated on 25 April 2025, largely based on “TimeCard Architecture (Section 5) Draft (20250424).docx”, and has since evolved.

---

## 5.13 - Acronyms  
**1PPS** = One Pulse Per Second  
**ADEV** = Allan Deviation  
**ARM** = Advanced RISC Machines Ltd (Acorn)  
**ASIC** = Application Specific Integrated Circuit  
**DDS** = Direct Digital Synthesis  
**EMC** = Electro Magnetic Compatibility  
**ESD** = Electro Static Discharge  
**FPGA** = Field Programmable Gate Array  
**gRPC** = Google Remote Procedure Call  
**GNSS** = Global Navigation Satellite System  
**I2C** = Inter-Integrated Circuit  
**IDD** = Interface Definition Document  
**I/O** = Input/Output  
**IRIG** = Inter-Range Instrumentation Group  
**ISA** = Industry Standard Architecture computer bus  
**ITU** = International Telecommunications Union  
**LPT** = Line Printer Terminal  
**M&CI** = Management and Control Interface  
**MCA** = Micro Channel Architecture  
**MHz** = Megahertz (10^6 Hertz)  
**MTBF** = Mean Time Between Failure  
**MTIE** = Maximum Time Interval Error  
**NTP** = Network Time Protocol  
**PCIe** = Peripheral Component Interconnect Express  
**PCMCIA** = Personal Computer Memory Card International Association  
**PLL** = Phase Locked Loop  
**PN** = Phase Noise  
**PTM** = Precision Time Measurement (Legacy Intel, now ARM)  
**PTP** = Precision Time Protocol  
**REST** = Representational State Transfer     
**RMS** = Root Mean Square  
**SCSI** = Small Computer System Interface  
**SI** = System International (Metric System)  
**SMB** = System Management Bus  
**SNMP** = Simple Network Management Protocol  
**SoC** = System on a Chip  
**SWaP-C** = Size, Weight, Power, and Cost  
**TAI** = International Atomic Time (in French)  
**TDEV** = Time Deviation  
**ToD** = Time of Day  
**USB** = Universal Serial Bus  
**UTC** = Coordinated Universal Time  
**V** = Volts or Voltage  
**WG** = Working Group  
**WiWi** = Wireless two-Way interferometry  
**WR** = White Rabbit [PTPv2.1 - High Accuracy]  
**WWVB** = Radio Station WWVB  

---

**End of Document**
