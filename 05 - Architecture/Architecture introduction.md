Proposal for "Time Card Overview" clause in Architecture section (or wherever else?)
Denis Reilly 11/18/2024 denis.reilly@gmail.com

---

# Time Card Architecture Overview

## 1. Scope and Purpose
The Time Card system defined in this standard exists to enhance the time-of-day synchronization and frequency distribution performance of a larger computing system (defined as the *Host system*) into which it is incorporated. The primary objective is to offload critical timing functions from the Host to a dedicated subsystem designed specifically for high-accuracy and high-precision timekeeping.

While one common example of this system is a discrete add-in card (such as a PCI Express card) inserted into a server chassis, a Time Card system does not need to be a physical card. Alternate implementations include, but are not limited to:
* A dedicated intellectual property (IP) block directly embedded or integrated into the Host system's silicon or motherboard.
* An external module temporarily or permanently connected to the Host system via a hot-pluggable or peripheral interface.

Any subsystem that meets the architectural definitions in this standard and is designed to be incorporated inside a larger system meets the definition of the Time Card.

## 2. Rationale for Dedicated Timing Subsystems
It is assumed that the Host system by itself typically lacks a sufficiently good local clock, clock steering, time-measurement capabilities, and other time-transfer mechanisms to keep time to the desired accuracy level. Typical Host limitations include unpredictable software and operating system latencies that interfere with precise clock steering, and an absence of specialized hardware for bounded-latency time transfer or hardware timestamping.

The Time Card can be incorporated into this Host system to enhance its timekeeping ability without redesigning the Host system itself. By incorporating a Time Card, a Host system gains enhanced, deterministic timekeeping and synchronization capabilities.

## 3. Core Capabilities
To overcome Host limitations, a Time Card architecture incorporates several critical timing components:

### 3.1 External Time Sources
The Time Card will be designed to take time from at least one good external source, which the Host could not normally manage on its own. Common external sources include Global Navigation Satellite Systems (GNSS), Precision Time Protocol (PTP) network feeds, or direct hardware signals such as Pulse Per Second (PPS). The Time Card processes these inputs with dedicated hardware to achieve high-precision synchronization.

### 3.2 Local Oscillator
The Time Card will also be designed with an onboard local oscillator (e.g., a TCXO, OCXO, or atomic clock) with defined performance characteristics. This oscillator provides the stable frequency reference needed to filter short-term jitter from external sources and to continue tracking time accurately (holdover) when external references are temporarily lost or degraded.

### 3.3 Time Distribution
A Time Card can also be capable of transmitting time directly to other sources (including other Time Cards with the proper input capabilities) via hardware signals that could not be controlled precisely enough by the Host alone. Implementing these signals entirely within the Time Card's hardware domain bypasses the unpredictable latencies associated with Host software intervention.

## 4. Interfaces
Each Time Card system can include a different configuration of Time and Frequency input and output signals (collectively called *Timing Interfaces*). If a Time Card system includes a Timing Interface that is defined in this standard, the Time Card will implement the interface according to this standard.

A Time Card can be controlled and configured by its Host system through a *Control Interface*. If a Control Interface is present, it will be implemented according to the information model in this standard. It is common for a single physical connection to serve as both a Control Interface and a Timing Interface, but the architecture maintains separate logical mechanisms for these functions. For instance, a PCIe-based Time Card uses the PCIe bus as both a Timing Interface and a Control Interface, but these two functions operate on distinct logical planes.

---

Notes to self:
"Time Card" is always 2 words in the PAR

I intend to avoid the IEEE keywords for now in this text

(IEEE keywords **shall **(Required)**, should** (Recommended)**, may **(Allowed). )
**(Avoid: must **(unavoidable situation) is deprecated. **ensure, guarantee, always**)
