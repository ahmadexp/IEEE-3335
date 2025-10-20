## Architecture

A TimeCard is a subsystem to a bigger system with a standardized interface to the system.  to provide time and frequency. 

set of functions, interface definitions1 , and TimeCard behaviors, not necessarily
implemented as a tangible physical object. For instance, a TimeCard may be implemented as a
function of some kind within an FPGA, ASIC, or SoC in a system that requires a time reference
but is not itself a time reference or clock.

#### 4.1 Architectural Principles (Normative)

Qualities sought include *adequately* high stability (quantified using ADEV or TDEV or MTIE as
appropriate), low phase noise, high accuracy, high precision, fine granularity, high resolution,
ability to synchronize TimeCard instances over a specified large physical extent while meeting
some pre-specified performance requirements, ability to create Ensemble clocks from multiple
time reference inputs, et al. The definition of *adequately* depends on the relevant use cases.
A TimeCard generates a single unified timescale and may publish this simultaneously in multiple
forms. There is exactly one timescale, not one per reference signal output.
All outputs **shall** publish the single *unified* timescale, approximating the timescale's ideal to fit
the capabilities of the output media. A major implication is that the boundaries between seconds
seen on the various output media from the same TimeCard instance always align exactly.
In addition to stability requirements, there are often maximum Phase Noise (PN) requirements.
PN is very weak amplitude (AM) and/or phase modulation (PM) of a periodic carrier whose

 If not defined within the present standard, interface definitions are usually incorporated by normatively citing a set of formally approved IDDs standards. This is needed for interoperability spanning various TimeCard makes and models.

frequency exceeds about one megahertz. While PN is not defined for slow pulse trains like
1PPS, time jitter is defined. PN is specified as a pair of power spectra of some kind (covering
AM and PM, if both are important) versus offset frequency. Each reference signal output will
likely have its own PN spectrum.
Low SWaP and cost (either absolute or relative to the host system being served, as appropriate
for specific use cases).
Manufacturers will be required to measure and publish their guaranteed maximum holdover
errors as a function of holdover time, along with required minimum warmup conditions and
times, et al. Holdover requirements apply only to 1PPS outputs and assume that the chosen
incoming reference is perfect. MTIE is widely used
The ITU G810 Appendix II.5 definition [G8260] of MTIE **shall** be the holdover metric for
TimeCards.
Alternately, multiple independent incoming time-reference signals may be combined into a
single unified *ensemble* time-reference signal that may be chosen as an incoming time reference.
TimeCard implementations **shall** be capable of combining multiple incoming reference signals
into a single unified *Ensemble* reference signal that may be used in the same manner as an
individual reference signal.
4.2 What's Common to all Implementations (Informative)
The architecture, constraints, and interfaces are common to all TimeCard implementations; all
else can vary. TimeCard implementations need not support all architecture objectives and/or
constraints. Manufacturers will specify exactly what they do and do not offer, and customers
will choose those offerings that best suit their specific application use case or cases.
In some use cases, the sole purpose of the TimeCard is to provide a standard interface to provide
a time reference to bespoke hardware, often with minimal to no technical requirements.
Cost sensitivity varies by orders of magnitude. One size does not fit all. So, numerical
performance requirements are explicitly defined as *unspecified* in the standard, meaning that the
WG deliberated and decided to leave this issue to the market to segment and settle2 .
Although we usually think of an oscillator as being a physical object perhaps containing a very
good resonator of some kind, this is not necessarily true in a TimeCard. For some use cases, a
DDS implemented in FPGA firmware controlled by a low-end commodity digital logic clock or
a wristwatch crystal oscillator or the like suffices.
TimeCards are a kind of PTP "Ordinary Clock".
4.3 Time-Flow Narrative (Informative)
The following is an informative traversal narrative, proceeding from the time-inputs to the time-
outputs in the direction of reference-time flow:
There is at least one input time reference signal available, and there may be multiple
simultaneously connected and available time references. If more than one signal is available,
there will be a pre-configured scheme to select which signal to use, what to do if and when the

*Unspecified* will be formally defined in the Nomenclature section of the P3335 standard. Also, officially define "out of scope", and update the definition of Traceable and Optional (conditional) Shall.

chosen reference signal degrades or ceases, and just how fussy and impatient to be in this
decision.
A TimeCard may have its own integral or dedicated Primary Reference Clock oscillator and
have no need of any incoming time reference, so the earlier rule would change to zero or more
incoming time reference signals. More commonly, there could be an ensemble clock
implemented where the local Primary Reference provides phase and frequency, plus external
incoming reference signals that define the boundaries between adjacent SI Seconds and label
those seconds according to TAI or UTC or some other time scale.
The TimeCard's internal Hardware Clock is steered into synchronism with the chosen incoming
time reference signal using a PLL of some kind; details vary, as does how tightly the PLL
synchronizes to the chosen incoming time reference, and the specific PLL type and loop
bandwidth. Knowledge of the specific PLL Type and Loop Bandwidth is necessary for the
design of the embedding system. Loop bandwidths range from millihertz (very loose
synchronization) to tens of kilohertz (very tight synchronization).

#### 5 Documentation Requirements (Normative)

Many Architectural Principles and Constraints are optional, which ones to support being left to
the market on the theory that customers will choose what's best for them. This implies that the
necessary data for publicly available products must be freely available to the public.
Manufacturers **shall** specify in publicly available datasheets exactly which of the listed
Architectural Principles and Constraints they do and do not meet or implement.
Manufacturers **shall** specify in publicly available datasheets the PLL Type and Loop Bandwidth.
Manufacturers **shall** provide in publicly available documents all data needed to perform
traceability analysis, or state that traceability is not supported.
All exercised optional (conditional) requirements **shall** be documented.

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
