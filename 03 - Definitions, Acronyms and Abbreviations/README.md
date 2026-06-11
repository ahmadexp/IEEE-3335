# 3. Definitions, Acronyms, and Abbreviations

This chapter defines the specialized terms, acronyms, and abbreviations utilized throughout the IEEE P3335 specification.

## 3.1 Definitions

For the purposes of this document, the following terms and definitions apply. The *IEEE Standards Dictionary Online* should be consulted for terms not defined in this clause.

- **Accuracy:** The degree of conformance or closeness of a measured time or frequency value to a defined primary reference (e.g., UTC).
- **Asymmetry Calibration:** The process of calculating and correcting unequal signal propagation delays in bi-directional timing links.
- **Control Plane:** The logical communication path dedicated to configuration, telemetry, and operations management rather than active time distribution.
- **Conformance Statement:** Supplier documentation identifying the IEEE P3335 clauses, optional features, interfaces, environmental limits, and performance declarations for which an implementation claims conformance.
- **Data Plane:** The logical or physical communication path strictly responsible for carrying phase, frequency, and time signals to or from the host or network.
- **Data Plane Latency:** The deterministic or variable propagation delay between a time source and its destination hardware.
- **Deterministic Behavior:** A system characteristic where the timing response under specified operational conditions is highly predictable and repeatable.
- **Disciplining:** The continuous process of steering a local oscillator's frequency and phase to align with a superior external reference signal.
- **Ensemble Clock:** A highly stable composite time source created by mathematically combining multiple independent references via weighting or consensus algorithms.
- **Environmental Chamber:** A specialized testing enclosure used to strictly control ambient temperature, humidity, and atmospheric conditions for hardware thermal testing.
- **Frequency Counter:** A measurement instrument used to determine the exact signal frequency or period over a defined averaging interval.
- **Granularity:** The minimum distinguishable or settable unit of change in a time-domain or frequency-domain output.
- **Hitless Switching:** The ability of a timing device to execute a reference failover or changeover without inducing a measurable phase discontinuity to the downstream consumers.
- **Holdover:** A mode of operation where a timing subsystem continues to maintain accurate time based solely on the historical stability of its internal oscillator after losing its external reference.
- **Holdover Error:** The progressively increasing deviation or drift of the subsystem’s timescale from an ideal reference while operating in a holdover state.
- **Host System:** The overarching computing, telecommunications, or networking platform that integrates a TimeCard through a standardized interface boundary.
- **Loop Bandwidth:** The effective frequency range over which a disciplining Phase-Locked Loop (PLL) tracks the reference, determining how fast the loop responds to changes.
- **Lock Time:** The duration required for the subsystem to acquire a reference and assert phase/frequency lock after a cold startup or reference transition.
- **Management Interface:** The designated control channel (e.g., SMBus, IPMI, REST) used strictly for configuration, diagnostics, and firmware management.
- **Measurement Point:** The physical connector, logical interface, register, packet timestamp, or other defined boundary at which a performance value is measured or declared.
- **Optional Feature:** A feature, interface, protocol, environmental profile, or security function that is not required for base conformance but that becomes subject to all applicable mandatory requirements when claimed by an implementation.
- **Oscilloscope (TIE Mode):** Measurement equipment configured to capture the Time Interval Error (TIE) of repetitive high-frequency signals.
- **Phase Alignment:** The absolute difference in timing between the corresponding edges of two separate signals; typically measured in nanoseconds or picoseconds.
- **Power Analyzer:** An instrument deployed to measure precise current draw, power sequencing, and consumption events over time.
- **Precision:** The statistical repeatability, resolution, or variance of a measurement under identical operating conditions.
- **Primary Reference Clock:** The highest-stability, autonomous time or frequency source in a synchronization hierarchy (as defined by ITU-T G.811).
- **Providing Interface:** The outbound physical or logical mechanism through which the TimeCard distributes precise time, phase, and frequency representations to the host or downstream devices.
- **Receive Interface:** The inbound physical or logical mechanism through which the TimeCard acquires an external reference representation.
- **Reference Signal:** Any external, traceable timing input actively utilized to discipline the local oscillator.
- **Resolution:** The absolute smallest incremental step, quantization, or granularity of a time or frequency measurement that the system can distinguish.
- **Rubidium Oscillator:** A highly stable atomic oscillator utilizing rubidium-87 vapor transitions to provide exceptional long-term frequency stability.
- **TimeCard:** A modular, hardware-based timing subsystem that abstracts synchronization complexity to deliver standardized phase, frequency, and time services to a host system.
- **Time Interval Counter (TIC):** A highly precise laboratory instrument designed to measure time differences between distinct electrical signal edges with picosecond-level resolution.
- **Time Jitter:** The short-term variation or instability of a time-domain signal (such as a 1PPS edge) from its ideal position, frequently reported as an RMS or peak-to-peak value.
- **Traceability:** A documented, unbroken mathematical chain of calibrations linking a local measurement back to recognized primary international standards (e.g., UTC).
- **Unified Timescale:** A single internal temporal scale actively maintained by the TimeCard, from which all separate outbound interfaces derive coherent, phase-aligned realizations.
- **Unspecified:** A characteristic intentionally not assigned a universal value by this standard. An unspecified characteristic may still be required to be declared by the supplier for a particular implementation or optional feature.

---

## 3.2 Acronyms and Abbreviations

- **1PPS:** One Pulse Per Second
- **ADEV:** Allan Deviation
- **API:** Application Programming Interface
- **ASIC:** Application Specific Integrated Circuit
- **BC:** Boundary Clock
- **BMC:** Baseboard Management Controller
- **CDC:** Communications Device Class
- **CXL:** Compute Express Link
- **CSAC:** Chip-Scale Atomic Clock
- **DCLS:** Direct Current Level Shift
- **DDS:** Direct Digital Synthesizer
- **EMC:** Electromagnetic Compatibility
- **EMI:** Electromagnetic Interference
- **ESD:** Electrostatic Discharge
- **FPGA:** Field Programmable Gate Array
- **GNSS:** Global Navigation Satellite System (e.g., GPS, Galileo, GLONASS)
- **GM:** Grandmaster
- **gRPC:** Google Remote Procedure Call
- **GPS:** Global Positioning System
- **I2C:** Inter-Integrated Circuit
- **I3C:** Improved Inter-Integrated Circuit
- **IPMI:** Intelligent Platform Management Interface
- **IRIG:** Inter-Range Instrumentation Group
- **IRNSS:** Indian Regional Navigation Satellite System
- **MAC:** Media Access Control
- **MMIO:** Memory-Mapped Input/Output
- **MTBF:** Mean Time Between Failures
- **MTIE:** Maximum Time Interval Error
- **NC-SI:** Network Controller Sideband Interface
- **NTP:** Network Time Protocol
- **OCP TAP:** Open Compute Project Time Appliances Project
- **OCXO:** Oven-Controlled Crystal Oscillator
- **OC:** Ordinary Clock
- **PCIe:** Peripheral Component Interconnect Express
- **PHC:** PTP Hardware Clock or Physical Hardware Clock
- **PHY:** Physical Layer
- **PLL:** Phase-Locked Loop
- **PN:** Phase Noise
- **PTM:** Precision Time Measurement
- **PTP:** Precision Time Protocol
- **QZSS:** Quasi-Zenith Satellite System
- **REST:** Representational State Transfer
- **RoHS:** Restriction of Hazardous Substances
- **SCPI:** Standard Commands for Programmable Instruments
- **SEC:** Securities and Exchange Commission
- **SMA:** SubMiniature version A (connector)
- **SMBus:** System Management Bus
- **SNMP:** Simple Network Management Protocol
- **SFP:** Small Form-factor Pluggable
- **SWaP-C:** Size, Weight, Power, and Cost
- **TC:** Transparent Clock
- **TAI:** International Atomic Time
- **TCXO:** Temperature-Compensated Crystal Oscillator
- **TDEV:** Time Deviation
- **TIC:** Time Interval Counter
- **TIE:** Time Interval Error
- **TPM:** Trusted Platform Module
- **ToD:** Time of Day
- **USB:** Universal Serial Bus
- **UTC:** Coordinated Universal Time
- **WiWi:** Wireless two-Way interferometry
- **WR:** White Rabbit
- **WWVB:** Radio Station WWVB (NIST)

---

**End of Chapter – Definitions, Acronyms, and Abbreviations**
