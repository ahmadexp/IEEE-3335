## General Terms

| Term | Definition |
|------|-------------|
| **TimeCard** | A modular timing subsystem that provides standardized interfaces to deliver phase, frequency, and time synchronization services to a host system. |
| **Host System** | The computing or networking platform that integrates a TimeCard through a standardized interface (e.g., PCIe, USB). |
| **Unified Timescale** | A single internal timescale maintained by the TimeCard; all outputs are phase-aligned realizations of this same scale. |
| **Reference Signal** | Any external timing input used to discipline the TimeCard oscillator (e.g., GNSS, PTP, PPS). |
| **Holdover** | Operation without an external reference, relying on oscillator stability to maintain accurate time. |
| **Disciplining** | The process of steering the oscillator frequency and phase to align with an external reference. |
| **Ensemble Clock** | A composite time source created by combining multiple references via weighting or consensus algorithms. |
| **Management Interface** | Control channel used for configuration, telemetry, and firmware management (e.g., SMBus, IPMI, REST). |
| **Providing Interface** | The mechanism by which the TimeCard delivers time and frequency to the host (e.g., PPS, 10 MHz, PTM). |
| **Receive Interface** | The mechanism through which the TimeCard obtains an external reference signal. |
| **Control Plane** | Logical path for configuration and monitoring operations. |
| **Data Plane** | Logical path responsible for carrying time and frequency signals to or from the host. |

---

## Performance Metrics

| Metric | Definition / Reference |
|---------|------------------------|
| **ADEV (Allan Deviation)** | Statistical measure of frequency stability versus averaging time τ (ITU-T G.810 Annex I). |
| **TDEV (Time Deviation)** | Time-domain equivalent of Allan deviation, representing time stability (ITU-T G.810 Annex I). |
| **MTIE (Maximum Time Interval Error)** | Maximum time deviation observed between any two points in a measurement window; holdover metric defined in ITU-T G.8260 (Appendix II.5). |
| **PN (Phase Noise)** | Power spectral density of short-term phase fluctuations, expressed in dBc/Hz at specified offset frequencies. |
| **Time Jitter** | Short-term variation of a time-domain signal such as PPS, reported as RMS or peak-to-peak. |
| **Accuracy** | Degree of conformance of a measured time or frequency to a defined reference. |
| **Precision** | Repeatability or resolution of a measurement under identical conditions. |
| **Resolution** | Smallest incremental step or quantization of a time or frequency measurement. |
| **Granularity** | Minimum distinguishable unit of change in time or frequency output. |
| **Phase Alignment** | Difference in timing between corresponding edges of two signals; often measured in nanoseconds. |
| **Loop Bandwidth** | Effective frequency range over which the disciplining PLL tracks the reference. |
| **Lock Time** | Time required for the TimeCard to achieve synchronization after startup or reference change. |
| **Holdover Error** | Deviation of the TimeCard’s timescale from the ideal reference during holdover. |

---

## Protocols and Standards

| Acronym | Description |
|----------|--------------|
| **GNSS** | Global Navigation Satellite System (GPS, Galileo, GLONASS, BeiDou). |
| **PTP** | Precision Time Protocol (IEEE 1588). |
| **NTP** | Network Time Protocol (RFC 5905). |
| **WR** | White Rabbit — deterministic Ethernet-based time/frequency transfer. |
| **WiWi** | Wireless Wireline Synchronization Protocol (IEEE 802.1AS extensions). |
| **WWVB** | Low-frequency U.S. national time broadcast from NIST. |
| **PPS** | Pulse Per Second; 1 Hz reference pulse marking second boundaries. |
| **PTM** | Precision Time Measurement feature of PCI Express. |
| **PCIe** | Peripheral Component Interconnect Express bus standard. |
| **SMBus** | System Management Bus, based on I²C protocol. |
| **IPMI** | Intelligent Platform Management Interface for out-of-band management. |
| **REST** | Representational State Transfer — HTTP-based API model. |
| **gRPC** | Google Remote Procedure Call protocol for structured telemetry. |
| **SCPI** | Standard Commands for Programmable Instruments. |
| **ADEV/TDEV/MTIE** | Core stability metrics from ITU-T G.810 and G.8260. |

---

## Hardware and Clock Types

| Term | Definition |
|------|-------------|
| **OCXO** | Oven-Controlled Crystal Oscillator; provides high thermal stability. |
| **TCXO** | Temperature-Compensated Crystal Oscillator. |
| **CSAC** | Chip-Scale Atomic Clock; miniaturized atomic frequency standard. |
| **Rubidium Oscillator** | Atomic oscillator providing long-term frequency stability. |
| **PLL** | Phase-Locked Loop used for frequency/phase tracking. |
| **DDS** | Direct Digital Synthesizer generating precise frequencies from a digital reference. |
| **Primary Reference Clock** | Highest-stability source in a timing hierarchy (per ITU-T G.811). |

---

## Measurement Instruments

| Instrument | Description |
|-------------|-------------|
| **TIC (Time Interval Counter)** | Measures time differences between signal edges with ps-level resolution. |
| **PN Analyzer** | Instrument for single-sideband phase-noise measurement. |
| **Frequency Counter** | Measures signal frequency or period over an averaging interval. |
| **Oscilloscope (TIE Mode)** | Captures time-interval error of repetitive signals such as PPS. |
| **Power Analyzer** | Monitors current draw and consumption over time. |
| **Environmental Chamber** | Controls ambient temperature for thermal testing. |

---

## Miscellaneous Terms

| Term | Definition |
|------|-------------|
| **Traceability** | Documented, unbroken chain of calibrations linking measurements to national or international standards. |
| **SWaP-C** | Size, Weight, Power, and Cost — key design trade-off factors. |
| **Data Plane Latency** | Propagation delay between time source and destination. |
| **Asymmetry Calibration** | Correction of unequal path delays in bi-directional timing links. |
| **Hitless Switching** | Reference changeover without phase discontinuity. |
| **Deterministic Behavior** | Predictable, repeatable timing response under specified conditions. |
| **OCP TAP** | Open Compute Project Time Appliances Project — community defining open time/frequency standards. |

---

## References

1. **ITU-T G.810** – Definitions and terminology for synchronization networks.  
2. **ITU-T G.8260** – Definitions and test methods for synchronization performance.  
3. **IEEE 1588-2019** – Precision Time Protocol (PTP).  
4. **PCI-SIG PCI Express Base Specification 5.0, Annex PTM.**  
5. **OCP TAP TimeCard Specification (current document).**  
6. **NIST Special Publication 1065** – Time and Frequency Measurement.  

---

This glossary ensures that every acronym and concept used in the TimeCard Specification is **unambiguous**, **standardized**, and **traceable** to existing timing and synchronization frameworks.  
It completes the document as a **stand-alone, standards-compliant reference** suitable for publication, implementation, and certification.
