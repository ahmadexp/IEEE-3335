# Precision Time Synchronization in Data Centers

Research Scientist, Meta Ahmad Byagowi

*Why* to have precision time synchronization in Data Centers?

*How* to have precision time synchronization in Data Centers?

## Background

- Speed of light and speed of electricity are finite!
  - Speed of Light is slower in fiber (2.14 x 10^8m/s) than in vacuum (2.99 x 10^8m/s)
  - Latency in data transfer over the network
- Hyperscale cloud services serve people across the globe
  - Geographical distribution of customers
  - Necessity of distribution due to safety, robustness and regulations
- The demand for hardware resources is always increasing
  - Increase in users, data and multi dimensional contents
  - Interactivity with the data like multi-user and VR
  - Big data and AI

## Solution to Address the Hyperscale Demand

- Horizontal Scaling
  - Expansion of resources

![](_page_3_Picture_3.jpeg)

- Geographical expansion
  - Reduction of latency

![](_page_3_Figure_6.jpeg)

## Challenges with Expansion

- Distributed Systems
  - Consistency vs Availability
  - Propagation of Information
  - Need for Redundancy
- Distribution of Clock
  - A common reference between all machines
  - Latency vs Clock Skewness

## Categories of use cases

#### Use cases of Precision Time Sync in Distributed Systems:

- Synchronization (Phase)
  - Active (1)
    - Running Events at specific time
      - Sync or desync
  - Reactive (2)
    - Measure latency, time or intervals
- Syntonization (Frequency)
  - Active (3)
    - Calibrate speed and align runtime to reduce tail latency
  - Reactive (4)
    - Measure heterogeneity or provide binning

|          | Phase | Frequency |
|----------|-------|-----------|
| Active   | 1     | 2         |
| Reactive | 3     | 4         |

## Associate Events Between Multiple Machines

![](_page_6_Figure_1.jpeg)

## Precision Requirement

- CPU level
- OS (Kernel) level
- Distributed System level

## Precision Requirement at CPU level

- Nyquist sampling theorem
  - Sampling interval required to avoid aliasing
  - Sampling frequency should be at least twice the highest frequency contained in the signal
- Frequency in event occurrence
  - Instruction Latency
  - Instruction Throughput

```
// mov = 1 CPU cycle 
// xchg = 3 CPU cycles
// rdtsc = 1 CPU cycle
```

## Precision Requirement at OS level

#### • dmesg

System Logging is based on clock\_boottime (clock\_minotone\_RAW) with a quanta on 1us Events occur faster than the quanta of 1us (aliasing)

## Challenges and the Precision Requirement

• Vernier acuity

![](_page_10_Picture_2.jpeg)

• Compounding of Events

$$1^n = 1$$

![](_page_10_Picture_5.jpeg)

## Precision Requirement for Distributed Systems

![](_page_11_Picture_1.jpeg)

## What comes out of Precision Time Sync?

![](_page_12_Picture_1.jpeg)

Machine X and Y are any two machines across the globe or inside a local network

Pseudo Entanglement: Probabilistic Entanglement of two Registers (Machine Y and Y) within the Windows of Uncertainty

Window of Uncertainty: An ongoing estimation of a time interval that UTC (or TAI) sits inside it (with a given probability)

![](_page_12_Picture_5.jpeg)

## Tangle

![](_page_13_Figure_1.jpeg)

![](_page_14_Figure_0.jpeg)

#### **Functions**

- Identify concurrent event in another machine[s]
- Find the timestamp of an event in another machine[s]
- Chronologically Rank a given event across machines
- Measure the one-way-latency between machines
- Identify concurrent events with one-way-latency consideration
- Trace chronological order for sequence of events
- Benchmark machines by precise runtime measurement
- Directly utilize RDTSC for maximum precision in event timestamping

## Runtime Difference in a Pipeline

![](_page_16_Figure_1.jpeg)

## Runtime Difference in a Pipeline

![](_page_17_Figure_1.jpeg)

## Align and Calibrate Machines in a Pipeline

![](_page_18_Figure_1.jpeg)

## Precision Time Sync Across Different Domains

![](_page_19_Picture_1.jpeg)

![](_page_19_Picture_2.jpeg)

![](_page_19_Picture_3.jpeg)

## Time Precision and Applications

![](_page_20_Figure_1.jpeg)

## Open Time Server

How to sync a Datacenter?

![](_page_21_Figure_2.jpeg)

![](_page_22_Picture_0.jpeg)

![](_page_22_Picture_1.jpeg)

## Time Card

- Concept (2020)
- First Prototype (2021)
- Industry Adoption (2022)

![](_page_23_Picture_4.jpeg)

![](_page_23_Picture_5.jpeg)

![](_page_23_Picture_6.jpeg)

## Time Card Family

![](_page_24_Picture_1.jpeg)

![](_page_24_Picture_2.jpeg)

![](_page_24_Picture_3.jpeg)

![](_page_24_Picture_4.jpeg)

![](_page_24_Picture_5.jpeg)

![](_page_24_Picture_6.jpeg)

## Latest Time Card

![](_page_25_Picture_1.jpeg)

## Simplified Objectives for P3335

Produce a guide to improve interoperability, compatibility and comparability between Time Cards manufactured by different vendors.

- Set a structure to define various sub systems
- Set some sub standards for plug-in modules (like GNSS and OSC)
- Define interfaces (hardware: memory addresses, drivers …)
- Suggest testing methods and comparable benchmark metrics
- Provide blueprints to assist further development of Time Cards
- Do all this work in a structure that maximizes people's engagement

## Proposed Approach

- We already have something that works (various Time Cards)
- Turn the Time Card to a general case
- Study the general case
- Dissect the work in subgroups (Diverge)
- Work in parallel
- Bring things together (Converge)
- Combing through the work (coherence)

![](_page_27_Picture_8.jpeg)

Goal: Embrace Diversity, Ensure Interoperability

## Current Time Card

• Dual GNSS PCIe card with a MAC

![](_page_28_Picture_2.jpeg)

## Time Card Concept

• All possible pathways

![](_page_29_Figure_2.jpeg)

## Focus Areas

![](_page_30_Figure_1.jpeg)

## Thank you

#### Find out more on:

[www.ocptap.com](http://www.ocptap.com/) [www.timecard.ch](http://www.timecard.ch/) [www.timingcard.com](http://www.timingcard.com/) [www.opentimeserver.com](http://www.opentimeserver.com/)