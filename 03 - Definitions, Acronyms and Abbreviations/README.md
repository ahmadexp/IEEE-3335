# 3. Definitions, Acronyms, and Abbreviations

## 3.1 Definitions

For the purposes of this document, the following terms and definitions apply. The IEEE Standards Dictionary Online should be consulted for terms not defined in this clause.

- **accuracy:** Qualitative closeness of agreement between a measured quantity value and a reference quantity value. A numerical accuracy claim is expressed in this standard as time error, frequency offset, uncertainty, or another defined metric.
- **conformance profile:** Named set of mandatory requirements that applies when the profile is claimed by an implementation.
- **conformance statement:** Supplier documentation identifying the P3335 clauses, profiles, optional features, interfaces, limits, and evidence for which an implementation claims conformance.
- **control interface:** Logical or physical interface used to configure, monitor, update, or manage a TimeCard.
- **data plane:** Logical or physical path that conveys time, phase, frequency, or event-timestamp information.
- **declared:** Stated in the conformance statement or in supplier documentation referenced by that statement.
- **disciplining:** Steering a local timing function using observations of one or more reference signals.
- **ensemble operation:** Selection or combination of multiple references to produce the reference used by the unified timescale.
- **granularity:** Smallest step in the representation or encoding of a reported value.
- **holdover:** Operating state in which a TimeCard maintains its timescale after loss or rejection of the external reference used for synchronization, using its local timing function and available historical information.
- **host system:** Computing, telecommunications, measurement, or control platform that integrates or consumes the services of a TimeCard.
- **lock time:** Elapsed time from a declared starting condition until a TimeCard enters the declared locked state.
- **measurement point:** Physical connector, logical boundary, register access point, packet event, or other defined location to which a measured or declared value applies.
- **measurement uncertainty:** Non-negative parameter characterizing the dispersion of quantity values attributed to a measurand.
- **optional feature:** Feature, interface, protocol, environmental profile, or security function not required for base conformance that becomes subject to its applicable mandatory requirements when claimed.
- **phase alignment:** Specified phase relationship between corresponding timing markers on two interfaces. Alignment error is the measured difference from that relationship.
- **providing interface:** Outbound physical or logical interface through which a TimeCard distributes time, phase, frequency, or timestamp information.
- **receive interface:** Inbound physical or logical interface through which a TimeCard acquires a reference representation.
- **reference signal:** External signal or data stream used to initialize, discipline, validate, or monitor the unified timescale.
- **resolution:** Smallest change in a measured quantity that causes a perceptible change in the corresponding indication.
- **time error:** Difference between the time indicated by the TimeCard at a specified measurement point and the time of the declared reference timescale at the corresponding instant.
- **TimeCard:** Modular timing subsystem that maintains a unified timescale and provides time, phase, frequency, or timestamp services through one or more interfaces.
- **time jitter:** Short-term variation of a specified timing event from its ideal position after removal of the trend or deterministic components identified by the declared measurement method.
- **timescale:** Ordered system of time values with a defined reference, epoch, and rules for forming time intervals.
- **traceability:** Property of a measurement result by which the result can be related to a stated reference through a documented, unbroken chain of calibrations, each contributing to measurement uncertainty.
- **unavailable:** Status indicating that a supported object or measurement does not currently have a valid value.
- **unified timescale:** Single timescale maintained by a TimeCard instance from which all of that instance's providing interfaces derive their time, phase, frequency, or timestamp information.
- **unsupported:** Status indicating that an object, operation, or feature is not implemented.
- **valid:** Status indicating that a value satisfies the freshness, state, and integrity conditions defined by its interface mapping.

## 3.2 Acronyms and Abbreviations

- **1PPS:** one pulse per second
- **ADEV:** Allan deviation
- **API:** application programming interface
- **ASIC:** application-specific integrated circuit
- **BMC:** baseboard management controller
- **CFM:** cubic feet per minute
- **CSAC:** chip-scale atomic clock
- **DCLS:** direct current level shift
- **DDS:** direct digital synthesizer
- **EMC:** electromagnetic compatibility
- **EMI:** electromagnetic interference
- **ESD:** electrostatic discharge
- **FPGA:** field-programmable gate array
- **GNSS:** global navigation satellite system
- **GPIO:** general-purpose input/output
- **gRPC:** Google Remote Procedure Call
- **I2C:** Inter-Integrated Circuit
- **I3C:** Improved Inter-Integrated Circuit
- **IPMI:** Intelligent Platform Management Interface
- **IRIG:** Inter-Range Instrumentation Group
- **LFM:** linear feet per minute
- **LOS:** loss of signal
- **MMIO:** memory-mapped input/output
- **MTBF:** mean time between failures
- **MTIE:** maximum time interval error
- **NC-SI:** Network Controller Sideband Interface
- **NMI:** national metrology institute
- **NTP:** Network Time Protocol
- **OCP TAP:** Open Compute Project Time Appliances Project
- **OCXO:** oven-controlled crystal oscillator
- **PCIe:** Peripheral Component Interconnect Express
- **PHC:** PTP hardware clock
- **PLL:** phase-locked loop
- **PTM:** Precision Time Measurement
- **PTP:** Precision Time Protocol
- **REST:** representational state transfer
- **RF:** radio frequency
- **RMS:** root mean square
- **SMA:** SubMiniature version A connector
- **SMBus:** System Management Bus
- **SNMP:** Simple Network Management Protocol
- **TAI:** International Atomic Time
- **TCXO:** temperature-compensated crystal oscillator
- **TDEV:** time deviation
- **TIC:** time interval counter
- **TIE:** time interval error
- **TLS:** Transport Layer Security
- **ToD:** time of day
- **USB:** Universal Serial Bus
- **UTC:** Coordinated Universal Time
- **WR:** White Rabbit
