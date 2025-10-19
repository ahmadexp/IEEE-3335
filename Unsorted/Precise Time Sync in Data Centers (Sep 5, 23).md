# Slide 1

## Precision Time Synchronization in Data Centers

Research Scientist, Meta Ahmad Byagowi

---

# Slide 2

Why to have precision time synchronization in Data Centers?

How to have precision time synchronization in Data Centers?

---

# Slide 3

## Background

Speed of light and speed of electricity are finite!
Speed of Light is slower in fiber (2.14 x 10^8m/s) than in vacuum (2.99 x 10^8m/s)
Latency in data transfer over the network
Hyperscale cloud services serve people across the globe
Geographical distribution of customers
Necessity of distribution due to safety, robustness and regulations
The demand for hardware resources is always increasing
Increase in users, data and multi dimensional contents
Interactivity with the data like multi-user and VR
Big data and AI

---

# Slide 4

## Solution to Address the Hyperscale Demand

Geographical expansion
Reduction of latency

Horizontal Scaling
Expansion of resources

![Image 1](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_4_image_1.jpg)

![Image 2](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_4_image_2.png)

---

# Slide 5

## Challenges with Expansion

Distributed Systems
Consistency vs Availability
Propagation of Information
Need for Redundancy
Distribution of Clock
A common reference between all machines
Latency vs Clock Skewness

---

# Slide 6

## Categories of use cases

Use cases of Precision Time Sync in Distributed Systems:
Synchronization (Phase)
Active (1)
Running Events at specific time
Sync or desync
Reactive (2)
Measure latency, time or intervals
Syntonization (Frequency)
Active (3)
Calibrate speed and align runtime to reduce tail latency
Reactive (4)
Measure heterogeneity or provide binning


|  | Phase | Frequency |
| --- | --- | --- |
| Active | 1 | 2 |
| Reactive | 3 | 4 |

---

# Slide 7

## Associate Events Between Multiple Machines

---

# Slide 8

## Precision Requirement

CPU level
OS (Kernel) level
Distributed System level

---

# Slide 9

## Precision Requirement at CPU level

Nyquist sampling theorem
Sampling interval required to avoid aliasing
Sampling frequency should be at least twice the highest frequency contained in the signal
Frequency in event occurrence
Instruction Latency
Instruction Throughput
// mov = 1 CPU cycle 
// xchg = 3 CPU cycles
// rdtsc = 1 CPU cycle

A CPU with a clock speed of 3.2 GHz executes 3.2 billion cycles per second
That is a period of about 310ps

---

# Slide 10

## Precision Requirement at OS level

dmesg

System Logging is based on clock_boottime (clock_minotone_RAW) with a quanta on 1us
Events occur faster than the quanta of 1us (aliasing)

![Image 3](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_10_image_3.png)

---

# Slide 11

## Challenges and the Precision Requirement

![Image 4](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_11_image_4.gif)

---

# Slide 12

## Precision Requirement for Distributed Systems

1

---

# Slide 13

## What comes out of Precision Time Sync?

Pseudo Entanglement

Machine X

Machine Y

Machine X and Y are any two machines across the globe or inside a local network

Pseudo Entanglement: Probabilistic Entanglement of two Registers (Machine Y and Y) within the Windows of Uncertainty

Window of Uncertainty: An ongoing estimation of a time interval that UTC (or TAI) sits inside it (with a given probability)

UTC of TAI

WOU

Time

---

# Slide 14

## Tangle

Event 1234
Event 1235
Event 1236
Event 1237
Event 1238
Event 1239
Event 1240

Event 1282
Event 1283
Event 1284

Machine A

Machine Local Time

NIC

CPU

ART

PTM

PTP

Network

OTS

![Image 5](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_14_image_5.png)

![Image 6](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_14_image_6.png)

![Image 7](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_14_image_7.png)

PTP

GNSS

UTC

Local OSC

m(UTC)
 c(UTC)

Tangle

Local Time

Circular Buffers

PHC

Window of Uncertainty

WOU(UTC)

Query Engine

RDTSC

---

# Slide 15

## Multiple Systems

Event 1234
Event 1235
Event 1236
Event 1237
Event 1238
Event 1239
Event 1240

Event 1282
Event 1283
Event 1284

Event 2044
Event 2045
Event 2046
Event 2047
Event 2048
Event 2049
Event 2050
Event 2051

Event 2077
Event 2078

Machine A

Machine B

Machine Local Time

Machine Local Time

Tangle

Tangle

…

2:00pm

2:00pm

2:00pm

---

# Slide 16

## Functions

Identify concurrent event in another machine[s]
Find the timestamp of an event in another machine[s]
Chronologically Rank a given event across machines
Measure the one-way-latency between machines
Identify concurrent events with one-way-latency consideration
Trace chronological order for sequence of events
Benchmark machines by precise runtime measurement
Directly utilize RDTSC for maximum precision in event timestamping

---

# Slide 17

## Runtime Difference in a Pipeline

Machine A

Time Axis

Machine B

Machine C

Machine D

Epoch #1

Pipelines

Machine A

Machine B

Machine C

Machine D

Machine A

Machine B

Machine C

Machine D

Machine A

Machine B

Machine C

Machine D

Epoch #2

Epoch #3

Epoch #4

---

# Slide 18

## Runtime Difference in a Pipeline

Machine A

Time Axis

Machine B

Machine C

Machine D

Pipelines

Machine A

Machine B

Machine C

Machine D

Machine A

Machine B

Machine C

Machine D

Machine A

Machine B

Machine C

Machine D

Epoch #1

Epoch #2

Epoch #3

Epoch #4

---

# Slide 19

## Align and Calibrate Machines in a Pipeline

Machine A

Time Axis

Machine B

Machine C

Machine D

Pipelines

Machine A

Machine B

Machine C

Machine D

Machine A

Machine B

Machine C

Machine D

Machine A

Machine B

Machine C

Machine D

Epoch #1

Epoch #2

Epoch #3

Epoch #4

---

# Slide 20

## Precision Time Sync Across Different Domains

![Image 8](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_20_image_8.png)

Data Center

![Image 9](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_20_image_9.png)

PTM

Global

Local Network

Inside Machines

IEEE P3335

IEEE 1588

![Image 10](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_20_image_10.png)

![Image 11](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_20_image_11.png)

![Image 12](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_20_image_12.png)

![Image 13](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_20_image_13.png)

RDTSC

![Image 14](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_20_image_14.png)

TPAUSE

CPU’s
TSC

---

# Slide 21

## Time Precision and Applications

WR

PTP+PTM

NTP

Industry Standard Physical Clocks

UserlandOS

Packet Latency (Globally)

Disk Operations

PTP+PTM

Real Time Linux

1ns

PTP w/o PTM

100ps

10ps

1ps

100ms

20ms

2ms

1ms

500us

250us

100us

50us

20us

5us

1us

100ns

500ns

500ms

10ns

One way Latency (P2P)

WR+PTM

NTP

INT

MMU

DC like a PC

DDP

CCP

PTP

Tangle

---

# Slide 22

## Open Time ServerHow to sync a Datacenter?

Software

Time Appliance

![Image 15](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_22_image_15.png)

Open Time Server

Traditional

COTS Server

Monitoring

Drivers

Time Card

NIC

Mgmt.

Tools

![Image 16](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_22_image_16.png)

---

# Slide 23

![Image 17](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_23_image_17.jpg)

![Image 18](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_23_image_18.jpg)

---

# Slide 24

## Time Card

Concept (2020)
First Prototype (2021)
Industry Adoption (2022)

![Image 19](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_24_image_19.png)

![Image 20](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_24_image_20.png)

![Image 21](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_24_image_21.png)

---

# Slide 25

## Time Card Family

![Image 22](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_25_image_22.png)

![Image 23](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_25_image_23.png)

![Image 24](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_25_image_24.png)

![Image 25](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_25_image_25.png)

![Image 26](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_25_image_26.png)

Broadcom’s Time Card

ADVA’s Time Card

![Image 27](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_25_image_27.png)

Celestica’s Time Card

---

# Slide 26

## Latest Time Card

![Image 28](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_26_image_28.jpg)

---

# Slide 27

## Simplified Objectives for P3335

Produce a guide to improve interoperability, compatibility and comparability between Time Cards manufactured by different vendors.
Set a structure to define various sub systems
Set some sub standards for plug-in modules (like GNSS and OSC)
Define interfaces (hardware: memory addresses, drivers …)
Suggest testing methods and comparable benchmark metrics
Provide blueprints to assist further development of Time Cards
Do all this work in a structure that maximizes people’s engagement

---

# Slide 28

## Proposed Approach

We already have something that works (various Time Cards)
Turn the Time Card to a general case
Study the general case
Dissect the work in subgroups (Diverge)
Work in parallel
Bring things together (Converge)
Combing through the work (coherence)

Goal: Embrace Diversity, Ensure Interoperability

![Image 29](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_28_image_29.png)

![Image 30](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_28_image_30.png)

![Image 31](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_28_image_31.png)

![Image 32](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_28_image_32.png)

![Image 33](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_28_image_33.png)

![Image 34](Precise Time Sync in Data Centers (Sep 5, 23)_images/slide_28_image_34.png)

---

# Slide 29

## Current Time Card

Dual GNSS PCIe card with a MAC

PCIe

SMA

GNSS1

GNSS2

Time Engine

MAC

---

# Slide 30

## Time Card Concept

All possible pathways

PCIe

SMA

GNSS1

GNSS2

Time Engine

MAC

1

2

3

4

5

---

# Slide 31

## Focus Areas

Time Engine

Local Oscillator

Physical Interface

Host Interface

Receiver

1

2

3

4

5

7

6

Metrics and Performance

---

# Slide 32

## Thank you

Find out more on:

www.ocptap.com
www.timecard.ch
www.timingcard.com
www.opentimeserver.com

---
