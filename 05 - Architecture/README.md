# TimeCard Architecture Specification

## 5.1 Architecture Overview

A **TimeCard** is a modular timing subsystem designed to interface with a larger host system through standardized hardware and software boundaries. Its primary objective is to deliver a stable, accurate, and reliable source of time—typically comprising time of day (ToD), phase alignment, and frequency stability—to the host system. By abstracting complex timing and synchronization tasks away from the host's general-purpose processing workload, the TimeCard enables bounded-latency timekeeping without requiring host system modifications.

The establishment of a standard architecture for TimeCards is critical for establishing broad interoperability among diverse implementations. By adhering to a consistent architectural framework, hardware vendors can design and manufacture TimeCards with varying capabilities, performance tiers, and underlying oscillator technologies while preserving full compatibility with any compliant host. This standardization fosters innovation, simplifies integration, and allows for the seamless substitution or upgrading of TimeCards across different generations of host systems, data centers, telecom platforms, and industrial infrastructure.

---

## 5.2 Core Timing Architecture

At its core, every TimeCard is built around an **internal frequency source** (an oscillator with quantified stability characteristics), which serves as the foundational reference for precise timekeeping. This internal oscillator function operates in conjunction with one or more interfaces that enable the TimeCard to **receive**, **process**, and **distribute** phase, frequency, and time-of-day information. 

The TimeCard maintains an internal unified timescale, continuously disciplined by the inbound references (when available) to correct for phase and frequency drift. If no inbound references are available, the oscillator transitions into a holdover state, utilizing its native stability to maintain the timescale autonomously.

---

## 5.3 Inbound Signal Interface

The **receive interface** provides the mechanism for the TimeCard to synchronize its internal oscillator to an external, traceable reference. Depending on the deployment environment and the accuracy objectives, this interface takes various physical and logical forms, ranging from direct radio frequency (RF) reception to network-based packet timing. 

Common inbound references include:
- **Global Navigation Satellite System (GNSS)** signals (e.g., GPS, Galileo, GLONASS, BeiDou).
- Packet-based synchronization protocols, such as **Precision Time Protocol (PTP)**, **Network Time Protocol (NTP)**, or **White Rabbit (WR)**.
- Direct localized RF/optical inputs like **WWVB**, **WiWi**, or **Pulse-Per-Second (PPS)** and **10 MHz** references.

These interfaces allow the TimeCard to discipline its internal oscillator and maintain phase alignment with a primary reference clock. The external references used for disciplining may possess different noise characteristics than the local oscillator; typically, the local oscillator provides superior short-term stability (low phase noise), while the external reference provides superior long-term accuracy and traceability.

In configurations where an external timing input is lost, intermittent, or deliberately disabled for security isolation, the TimeCard operates in **holdover**. During holdover, the TimeCard relies entirely on the stability of its internal frequency source (e.g., a TCXO, OCXO, or atomic rubidium element) to accurately maintain time over a specified duration before the time error exceeds allowable margins. Flexible receive architectures permit TimeCards to function across a vast spectrum of use cases—from distributed edge nodes relying on GNSS to fully isolated autonomous datacenters.

---

## 5.4 Outbound Signal Interface

While the receive interface facilitates external synchronization, the **providing interface** (or outbound interface) distributes the synchronized time and frequency domains to the host system and, optionally, to downstream peripheral devices.

A providing interface is a **mandatory component** of the TimeCard architecture. It establishes the temporal synchronization channel by which the TimeCard delivers localized time, frequency, or both, to the operating environment.

Depending on application requirements, this distribution may occur across a single interface or a combination of concurrent interfaces. Typical outbound links include system buses such as **PCI Express (PCIe)**, **Compute Express Link (CXL)**, and legacy buses, alongside peripheral interfaces (e.g., **USB**, **Serial**). The selection of the interface dictates the temporal resolution, achievable accuracy, and bandwidth of the synchronization channel.

To preserve timing integrity and deterministic behavior, it is strongly recommended that the providing interface implement **hardware-based timestamping**. Hardware timestamping measures and stamps events directly within the physical or link-layer logic, bypassing significant and unpredictable software stack delays, interrupt latencies, and operating system scheduling jitter. 

Hardware-assisted delivery mechanisms include:
- Dedicated physical signaling such as a **Pulse-Per-Second (PPS)** discrete wire alongside a serial Time-of-Day message.
- In-band bus implementations such as **Precision Time Measurement (PTM)** within modern **PCIe** architectures. 

These explicit hardware mechanisms establish sub-microsecond or nanosecond-class deterministic time delivery, establishing cross-vendor interoperability.

---

## 5.5 Management and Control Interface (M&CI)

In addition to the inbound and outbound signal interfaces, every TimeCard SHOULD include at least one **Management and Control Interface**. These interfaces facilitate configuration, monitoring, diagnostics, state machine transitions, firmware provisioning, and health reporting between the TimeCard and the overarching management plane. (A TimeCard completely lacking a management interface is acceptable only for fixed-function, static-configuration systems requiring no runtime telemetry).

The M&CI serves as the **control plane** of the TimeCard, kept logically (and sometimes physically) distinct from the time **data plane**. Through this interface, host applications or external baseboard management controllers (BMCs) configures parameters such as source prioritization, PLL bandwidth, disciplining modes, and holdover thresholds, while monitoring real-time metrics including phase offsets and oscillator temperatures.

Common M&CIs include:
- **SMBus / I²C** or **I3C**: Frequently used for out-of-band telemetry and low-level configuration by BMCs.
- **PCIe Configuration Space and Memory-Mapped I/O (MMIO)**: Providing low-latency, in-band access to hardware control registers directly via the host CPU.
- **Serial (UART) or USB**: Standardized methods for diagnostics, debug, and localized firmware updates.
- **Network-based APIs**: Such as REST, gRPC, Redfish, or SNMP for distributed, network-managed timing appliances.

To promote multi-vendor interoperability, TimeCards SHOULD expose a standardized data model (e.g., utilizing Yang models or standardized MMIO register maps) containing:
- Selected synchronization source and operational state machine.
- Clock disciplining active status and PLL lock indication.
- Phase and frequency offset measurements relative to the reference.
- Holdover duration, projected drift, and current internal temperature.
- Active alarm definitions, threshold faults, and health indicators.
- Firmware version, hardware revision, and manufacturer metadata.

Furthermore, the management interface SHOULD support cryptographic firmware update mechanisms and secure boot validation to prevent unauthorized runtime modification and protect critical infrastructure timing integrity.

---

## 5.6 Power, Mechanical, and Environmental Considerations

The following subsections apply to physically realized TimeCards (e.g., PCIe add-in cards, mezzanine modules) rather than software-only or deeply integrated embedded firmware functions.

### 5.6.1 Power Delivery
- TimeCards SHALL define and document input power rail voltages, acceptable ripple, and absolute tolerances (e.g., 12 V, 3.3 V).    
- If powered by external discrete connections, reverse polarity protection SHALL be included.  
- Deterministic power-up sequencing, inrush current limiting, and optional supercapacitor/battery energy storage for bridging power interruptions SHOULD be documented.

### 5.6.2 Mechanical Form Factor
- The exact physical envelope and bounding box SHALL be documented.  
- Acceptable envelope forms include standard server add-in cards (low-profile, full-height, half-length), OCP NIC 3.0, mezzanine forms, or standardized embedded modules.  
- Mounting mechanics SHALL withstand repeated insertion and removal. Strain relief mechanisms for fragile cable ports (such as coaxial RF drops or optical fiber) SHOULD be included.  
- Faceplates physical limits permitting, SHOULD visibly label external ports (e.g., GNSS, PPS, 10 MHz, ToD) and include status indicator LEDs.

### 5.6.3 Connectors and I/O
- RF and analog timing reference ports SHALL be impedance-matched (typically 50 ohms).  
- For PPS and 10 MHz electrical interfaces, the voltage levels, input/output impedance, edge speed, and polarity (e.g., triggering on the rising edge) SHALL be specified explicitly.  
- Exposed data and management ports SHOULD implement adequate Electrostatic Discharge (ESD) protection and utilize mechanically locking connectors where feasible.

### 5.6.4 Thermal Design
- The nominal and absolute maximum operating temperature ranges SHALL be defined. The oscillator's frequency drift across this temperature spectrum (temperature coefficient) SHOULD be characterized and documented.  
- Assumptions regarding host-provided airflow (Linear Feet per Minute - LFM) SHOULD be documented. The maximum thermal dissipation (heat load) during cold-start warm-up SHALL be specified.  
- Out-of-bounds thermal events (over/under-temperature thresholds) SHALL trigger configurable alerts via the Management and Control Interface.

### 5.6.5 Environmental and Reliability
- Operational limits for physical shock, vibration, and relative humidity SHOULD be published.  
- EMC (Electromagnetic Compatibility) and ESD emission/immunity levels SHOULD meet the regulatory standards of the intended target market.  
- Reliability metrics (e.g., Mean Time Between Failures - MTBF) and components susceptible to wear-out (such as flash memory or oscillators) SHOULD be documented.  
- Safe handling, labeling, and hazardous material disposal instructions (e.g., RoHS, REACH) SHOULD be provided.

---

## 5.7 Reference Signals and Performance Metrics (Normative)

- IEEE Std 1139 and IEEE Std 1193 SHOULD be used as authoritative references for defining phase noise, frequency stability, and general performance metrics.
- NIST Special Publication 1065 (Riley) provides informative guidance on frequency stability analysis.
- Specified performance constraints SHOULD be conditioned upon the physical signal type (e.g., electrical balanced/unbalanced, single-ended voltages, optical properties).
- ITU-T G.703 Clause 19 MAY be referenced for standard electrical characteristics of synchronization interfaces.
- Measurement bandwidths and respective integration times SHALL be reported for all specified jitter and stability data.
  
### 5.7.1 Unified Timescale (Normative)
A unified timescale originates from a single, continuously operating oscillator function. This internal timescale is synthesized and translated into various outbound distribution formats, each approximating the core timescale within the physical limits of that specific interface.

A TimeCard SHALL generate a single, continuous unified timescale and SHALL publish coherent translations of this timescale across all active Outbound Interfaces.    

All second boundaries (e.g., the rising edge of a 1 PPS signal) output from any providing interface of the same physical TimeCard instance SHALL align with each other. The maximum allowable time divergence (skew) between these outputs SHALL be tested, documented, and published by the manufacturer.

### 5.7.2 Output Signal Classes (Informative)
Standard synchronization outputs from a TimeCard frequently include Time of Day (ToD) serial streams, 1 PPS discrete signals, 10 MHz / 5 MHz continuous sine or square waves, packetized synchronization networks (e.g., PTP), and host-bus signaling (e.g., PCIe PTM). Detailed electrical parameters, slew rates, and load limits SHOULD be published for each individual class.

### 5.7.3 Stability, Accuracy, Precision (Normative Reporting)
High-performance timekeeping is characterized by stability (measured via ADEV, TDEV, or MTIE), low phase noise, high absolute accuracy relative to UTC, high precision, and nanosecond/picosecond resolution.  

Specific numerical thresholds are intentionally omitted from this standard to allow for market innovation; instead, manufacturers SHALL characterize and report performance by providing:
- Allan Deviation (ADEV) and Time Deviation (TDEV) plots versus observation time (tau).  
- Bounded worst-case time and frequency offset relative to the primary reference input.  
- Timestamp granularity and quantization error.  
- The exact test conditions and synchronization configurations utilized during performance validation.

### 5.7.4 Phase Noise and Time Jitter (Normative Reporting)
For continuous periodic outputs (e.g., 10 MHz), manufacturers SHOULD provide a Phase Noise (PN) spectral density plot (dBc/Hz) across standard offset frequencies (e.g., 1 Hz to 1 MHz).  

For pulsed time outputs (e.g., 1 PPS), manufacturers SHALL specify the root-mean-square (RMS) and peak-to-peak time jitter, explicitly noting the measurement bandwidth. These disclosures MAY be conditioned on the intended environmental profile.

### 5.7.5 Holdover Performance (Normative)
When inbound references are lost, the system relies on holdover. Vendors SHALL publish the maximum projected holdover error drift profile over time, accounting for specific initial warm-up conditions and external temperature variations.  

Holdover limits generally apply to the 1 PPS outputs extrapolated from a nominally perfect prior inbound reference.  

Maximum Time Interval Error (MTIE) configured per ITU-T G.8260 SHALL be used as the primary holdover metric. Furthermore, it is acknowledged that baseline networking standards, such as ITU-T G.8262.1 (which focuses on telecom boundary clock requirements for SyncE), often permit holdover drifts that are significantly looser than the nanosecond-level tolerances required by advanced TimeCard implementations. Consequently, TimeCards intended for extreme precision applications SHOULD document MTIE against far more stringent, application-specific boundaries than standard telecom profiles.

### 5.7.6 Ensemble References (Normative)
Advanced implementations SHALL support algorithms combining multiple diverse references into a single, unified "Ensemble" reference.  
Ensemble logic MAY provide dynamic source weighting, individual source health monitoring, and boundary alarms accessible via the management telemetry.

### 5.7.7 Large-Extent Synchronization (Informative)
For extensive datacenter or campus-wide deployments, maintaining synchronization implies establishing a specified maximum end-to-end time error budget. This involves system-level calibration, compensating for cable/fiber propagation delays (roughly 5 nanoseconds per meter), and handling thermal shifts in long cable runs. Because these variables depend heavily upon facility dimensions and multi-vendor integrations, large-extent architectural design sits outside the direct scope of the individual TimeCard's hardware specification.

### 5.7.8 Time-Flow Narrative (Informative)  
In a typical sequence, a TimeCard receives zero or more external references, subjects them to a selection algorithm or policy (e.g., Best Master Clock Algorithm), and disciplines its local hardware clock utilizing a Phase Locked Loop (PLL). 
*(Note: A traversal narrative linked to a system block diagram is expected to be integrated in future revisions.)*

### 5.7.9 Implementation Flexibility (Informative)
The internal "oscillator" acts as a functional block and need not consist of a single discrete quartz resonator. Implementations span from Direct Digital Synthesis (DDS) derived from low-cost Silicon-based MEMS, to local atomic frequency standards (e.g., Rubidium or Cesium vapor cells) for ultra-high-stability. The selection strictly governs Size, Weight, Power, and Cost (SWaP-C) trade-offs driven by end-user requirements.

### 5.7.10 Conformance and Interface Definitions (Normative Guidance)
If physical or logical interfaces are implemented that are not fully defined within this specification, manufacturers SHOULD normatively cite approved external Interface Definition Documents (IDDs) to maintain predictable interoperability.

Recommended conformance verification SHOULD cover:
- Empirical ADEV/TDEV testing methodology.  
- Phase Noise masks and verification metrics.  
- Skew alignment testing across divergent output pins.  
- Hardware-assisted baseline latency and asymmetric delay characterization (e.g., PCIe PTM).  
- MTIE holdover verification across temperature cycles.  
- Deterministic failover and ensemble behavior during abrupt reference loss.

---

## 5.8 Documentation Requirements (Normative)

Manufacturers SHALL provide publicly available technical documentation (datasheets or user manuals) specifying:
- The architectural subset and optional constraints implemented by the specific hardware model.  
- The structural type of the disciplining mechanism (e.g., DPLL, analog PLL) and corresponding loop bandwidths/time constants.  
- Comprehensive testing results addressing the performance metrics defined in §5.7.
- Traceability data establishing a chain of measurement to international primary standards, or a clear "traceability not supported" notice.  
- Operating parameters for all optional features provided.

---

## 5.9 Vendor Datasheet Checklist (Informative)

| Category | Requirement Level | Example Documentation Objects |
|-----------|------------------------|------------------|
| **Electrical & Power** | REQUIRED | Input rails, required tolerances, peak/idle current draw, power sequencing, inrush limits. |
| **Mechanical** | REQUIRED | Dimensional bounding box, connector types, faceplate layout, mass. |
| **Thermal** | REQUIRED | Operating and storage temperature range, required airflow (LFM), max thermal dissipation. |
| **Timing Performance** | REQUIRED | ADEV/TDEV plots, local oscillator PN spectra, holdover MTIE bounds over time. |
| **Synchronization Inputs** | REQUIRED | Supported protocols: GNSS bands/constellations, PTP/NTP capability, WR compatibility, 1PPS input specs. |
| **Outputs** | REQUIRED | Signal voltages, impedance, PPS/10 MHz/ToD alignments, and measurable output skew. |
| **Management** | RECOMMENDED | Remote interface type, supported telemetry vectors, SNMP/REST support, secure firmware update method. |
| **Compliance** | REQUIRED | Safety (UL/CSA), EMC/EMI limits, ESD tolerances, RoHS/REACH compliance, CE/FCC markings. |
| **Reliability** | RECOMMENDED | Specified MTBF, service intervals, oscillator aging rates, backup power retention lifecycle. |
| **Documentation** | REQUIRED | Implementation/integration guide, status indicator LED matrices, baseline calibration methodologies. |

---

## 5.10 References (Normative)

- [G8260] ITU-T G.8260 *Definitions and terminology for synchronization in packet networks* (2015 or later).  
- [IEEE 1139] IEEE Std 1139™, *IEEE Standard Definitions of Physical Quantities for Fundamental Frequency and Time Metrology*.
- [IEEE 1193] IEEE Std 1193™, *IEEE Guide for Measurement of Environmental Sensitivities of Standard Frequency Generators*.
- [MTIE] Stefano Bregni, *Measurement of Maximum Time Interval Error for Telecommunications Clock Stability Characterization*, IEEE Transactions on Instrumentation and Measurement, Vol. 45, No. 5, Oct 1996.  
- [PTPv2.1] IEEE Std 1588™-2019, *IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems*.  

---

## 5.11 Bibliography (Informative)

- [IDD_DID] DI-IPSC-81436A, *Interface Design Description Data Item Description* (1999).  
- [IRS_DID] DI-IPSC-81434A, *Interface Requirements Specification Data Item Description* (1999).  
- [SSDD] DI-IPSC-81432A, *System/Subsystem Design Description* (1999).  
- [SSS] DI-IPSC-81431A, *System/Subsystem Specification* (2000).
- NIST Special Publication 1065, W.J. Riley, *Handbook of Frequency Stability Analysis* (2008). 

---

## 5.12 Notes
The present P3335 standard document was initiated on 25 April 2025, largely based on *“TimeCard Architecture (Section 5) Draft (20250424).docx”*.

---

## 5.13 Acronyms  

*Note: The following acronyms are used within this section; they are intended to be gathered into a single comprehensive abbreviation appendix for the final publication of the standard.*

- **1PPS**: One Pulse Per Second  
- **ADEV**: Allan Deviation  
- **ASIC**: Application Specific Integrated Circuit
- **BMC**: Baseboard Management Controller
- **CXL**: Compute Express Link
- **DDS**: Direct Digital Synthesis  
- **EMC**: Electromagnetic Compatibility
- **EMI**: Electromagnetic Interference
- **ESD**: Electrostatic Discharge  
- **FPGA**: Field Programmable Gate Array  
- **GNSS**: Global Navigation Satellite System  
- **I2C**: Inter-Integrated Circuit
- **I3C**: Improved Inter-Integrated Circuit
- **IDD**: Interface Definition Document  
- **IPMI**: Intelligent Platform Management Interface
- **IRIG**: Inter-Range Instrumentation Group  
- **ISA**: Industry Standard Architecture
- **ITU**: International Telecommunication Union  
- **LED**: Light Emitting Diode  
- **LPT**: Line Printer Terminal  
- **MCA**: Micro Channel Architecture  
- **MEMS**: Micro-Electromechanical Systems
- **MHz**: Megahertz (10^6 Hertz)  
- **MMIO**: Memory-Mapped I/O
- **MTBF**: Mean Time Between Failures  
- **MTIE**: Maximum Time Interval Error  
- **NTP**: Network Time Protocol  
- **OCP**: Open Compute Project
- **OCXO**: Oven-Controlled Crystal Oscillator
- **PCIe**: Peripheral Component Interconnect Express  
- **PCMCIA**: Personal Computer Memory Card International Association  
- **PLL**: Phase-Locked Loop  
- **PN**: Phase Noise  
- **PTM**: Precision Time Measurement  
- **PTP**: Precision Time Protocol  
- **RMS**: Root Mean Square  
- **SCSI**: Small Computer System Interface  
- **SMBus**: System Management Bus  
- **SNMP**: Simple Network Management Protocol
- **SoC**: System on a Chip  
- **SWaP-C**: Size, Weight, Power, and Cost  
- **TCXO**: Temperature-Compensated Crystal Oscillator
- **TDEV**: Time Deviation  
- **ToD**: Time of Day  
- **USB**: Universal Serial Bus  
- **UTC**: Coordinated Universal Time  
- **WG**: Working Group  
- **WiWi**: Wireless two-Way interferometry  
- **WR**: White Rabbit  
- **WWVB**: Radio Station WWVB

---

**End of Document**
