**P3335 Timecard Hardware Interfaces**


**Add to clause 2 Normative References**
IEC 60169-15:2121, “Radio-frequency connectors - Part 15: Sectional specification - RF coaxial connectors with inner diameter of outer conductor 4,13 mm (0,163 in) with threaded coupling - Characteristic impedance 50 Ω (type SMA)”

IRIG Standard 200-16, “IRIG Serial Time Code Formats”

ITU-T G.703 Amendment 1 (05/2021), “Physical/Electrical Characteristics of Hierarchical
Digital Interfaces”

**Add to subclause 3.****1 Definitions**
N/A

**Add to subclause 3.2 Acronyms and Abbreviations**
AM	Amplitude Modulated
DCLS	Direct Current Level Shift
IRIG	Inter-Range Instrumentation Group
PCIe	Peripheral Component Interface express
PPS	Pulse Per Second
PTM	Precise Time Measurement
SFP	Small Form-factor Pluggable
SMA	Subminiature version A

**Add to Annex A – Bibliography**
N/A


**1.0 ****Inputs****	**<editors note: change clause/subclause numbers to fit overall draft>

The time card shall be able to successfully interpret inputs which meet the specifications listed in this clause

**1.1 ****GNSS receiver**
SMA female connector (50 Ohm), Standard: IEC 60169-15:2121
Antenna power (TBD)

**1.2 ****Pulse Per Second**** (PPS)**
Input level into 50 ohms (Low is -0.3 to 0.3V, high is 1.2 to 5.5V)
Tolerate pulse width range of: 100 ns – 500 ms
On-time mark is 50% on rising edge
The maximum rise time (10%-90%) 5 ns.  Implementations may accept longer rise times.
SMA female connector (50 Ohm)

**1.3 ****10 MHZ sine wave **
Specifications TBD
SMA female connector

**1.4 ****IRIG ****t****ime ****c****ode AM sine wave**
2.0-5.5 V peek-to-peek
Signal format conformant to IRIG Standard 200-16
SMA female connector

**1.5 ****IRIG time code DCLS**
Input level into 50 ohms (Low is -0.3 to 0.3V, high is 1.2 to 5.5V)
Active high required, Configurable active low (optional)
SMA female connector


**2.0 ****Outputs**

The output signals, if present, shall meet the specifications in this clause.

**2.1 PPS**
This interface shall be implemented
As specified in ITU-T G703 Amendment 1, Clause 19, and Annex A except that the connector shall be an SMA female connector

**2.2 ****Pulse****s**** (optional)**
1 PPS to 1 MPPS (fixed or programable)
Output level into 50 ohms (Low is -0.3 to 0.3V, high is 1.2 to 5.5V)
On-time mark is 50% on rising edge
Available pulse rates are implementation specific
SMA female connector

**2.3 ****10 MHZ sine**** ****wave ****(optional)**
Specifications TBD
SMA female connector

**2.4 ****IRIG ****t****ime ****c****ode AM sine wave**** ****(optional)**
2.0 – 5.5 V peek-to-peek (MARK) into 50 ohms, 
Signal format conformant to IRIG Standard 200-16
SMA female connector

**2.5 ****IRIG time code DCLS**** ****(optional)**
Output level into 50 ohms (Low is -0.3 to 0.3V, high is 1.2 to 5.5V)
Signal format conformant to IRIG Standard 200-16
Active high required, Configurable active low (optional)
SMA female connector

**3.0 ****Bi-directional interfaces**

**3.1 ****PCIe**
This interface is required when the PCIe mapping is implemented
Any of the standard form factors may be implemented: Full-length, half-length, low-profile
Precise Time Measurement (PTM) support is required
Standards: PCI-SIG PCIe 

**3.2 S****mall ****F****orm-factor ****P****luggable (SFP)**** ****(optional)**
TBD: Which SFF interface to call out
Standards: Storage Networking Industry Association SFF committee

**4.0 Alternative connectors**** (optional)**

Except for the host connector, an implementation may have different connectors, if the manufacturer supplies an adaptor cable to convert to the connectors specified.





| Date | Author(s) | Comments |
| --- | --- | --- |
| 2024-05-4 | Doug Arnold | First cut including inputs: GNSS, PPS, 10 MHz, IRIG
Outputs: PPS, pulses, 10 MHz, IRIG
Bidirectional: PCIe, SFP |
| 2024-12-09 | Doug Arnold | Added lists for acronyms, and normative references.  Changed PPS to match ITU-T requirements for simple PPS, except connector |
