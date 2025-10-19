# Slide 1

## Financial Industry Time Synch Accuracy Regulations

Presentation for P3335 Systems Architecture SC

Steve Guendert, Ph.D.
IBM Corporation

---

# Slide 2

## Agenda

Government regulations:  US and EU
FINRA and MiFID 2
Single point of failure
Industry regulations
Payments industry

4/16/2025

2

---

# Slide 3

## Regulatory Background

Widespread proliferation and usage of electronic trading platforms with their automation
Advent of High Frequency Trading (HFT)
Increased the need for tighter synchronization and traceability to a common reference time scale
UTC
How does UTC really work?
What is traceability?  What does it really mean?
Calibration
Equipment monitoring

3

---

# Slide 4

## Government Regulations-US

NASD, OATS, FINRA, CAT
1996 SEC report: NASD/NASDAQ did not always act in best interest of customers
Led to new regulations in late 1990s
1998: NASD Order Audit Trail System (OATS) Rule 6953
Daily synchronization, within 3 seconds of NIST atomic clock
FINRA (Financial Industry Regulatory Authority)
FINRA is a not-for-profit entity that is responsible for overseeing virtually every US stock broker and brokerage firm. (The SEC is responsible for ensuring fairness for the individual investor.)
2008: FINRA OATS Rule 7430
Superseded Rule 6953
Tighter synchronization, (1 sec) maintained at all times when market is open

4

---

# Slide 5

## Government Regulations-US (Cont’d)

FINRA (Financial Industry Regulatory Authority)
2014: FINRA Regulatory Notice 14-47 out for comments
2016: FINRA Rule 4590 and SEC Regulatory Notice 16-23
What does this mean?  Effective 2018:
Requires synchronization of equipment to within 50ms of NIST(UTC)	
Also requires audit log capability to prove compliance
Log of all times when clocks are synchronized and the results
Includes notice of clock drift outside required tolerance

5

---

# Slide 6

## Government Regulations-US (Cont’d)

Consolidated Audit Trail (CAT)
Requires sending of complete documentation on all orders to a central repository by 8am Eastern Time the day following a trade.
Requires time stamps at ms resolution at five places in the audit trail:
The time of order origination
The time when the order is routed
The time when the order is received
The time when the order was modified and/or cancelled
The time when the order was executed

6

---

# Slide 7

## Fines

7

![Image 1](P3335 Preso on Financial Industry regulations_images/slide_7_image_1.wmf)

---

# Slide 8

## Government Regulations-EU

European Securities and Markets Authority (ESMA)
Ensures fair and equitable financial markets/protects investors
Closest European equivalent to the SEC in the U.S.
Empowered by the Market in Financial Instruments Directive (MiFID) to draft regulatory technical standards for EU financial markets and firms
ESMA began the process of updating MiFID with a new directive, MiFID II in 2011
MiFID II formally adopted by the EU parliament in June 2014
MiFID II requirements went into effect in January 2018
MiFID II clock synchronization requirements are more stringent that the latest U.S. requirements previously discussed
MiFID II applies to any organization dealing in European financial instruments
Commission Delegated Regulation (EU) 2017/574 
AKA Regulatory Technical Standard (RTS) 25
RTS-25 has four articles

8

---

# Slide 9

## RTS-25 Article 1: Reference Time

Business clocks that provide the timestamp for any reportable event should be coordinated to UTC, using either a link to one of the laboratories maintaining a UTC(k) realization of UTC, or the time signals disseminated by GPS or other satellite system. 
If using a satellite system, any offset from UTC must be accounted for and removed from the timestamp.

9

---

# Slide 10

## RTS-25 Article 2: Level of Accuracy for Operators of Trading Venues

Article 2 describes the level of accuracy, i.e. the maximum divergence from UTC, that should be achieved by the operators of financial trading venues, taking into account the gateway to gateway latency of their trading systems.

10

![Image 2](P3335 Preso on Financial Industry regulations_images/slide_10_image_2.wmf)

---

# Slide 11

## RTS-25 Article 3: Level of Accuracy for members/participants of a trading venue

Article 3 defines the level of accuracy that apply to business clocks of members or participants of financial trading venues.

11

![Image 3](P3335 Preso on Financial Industry regulations_images/slide_11_image_3.wmf)

---

# Slide 12

## RTS-25 Article 4: Compliance With Maximum Divergence Requirements

Article 4 specifies that operators of trading venues and their members or participants shall establish a system of traceability to UTC. 
They shall be able to demonstrate traceability to UTC by documenting the system design, functioning and specifications. 
They shall be able to identify the exact point at which a timestamp is applied and demonstrate that the point within the system where the timestamp is applied remains consistent. 
The traceability system should be reviewed at least once per year to ensure compliance with the regulations.

12

---

# Slide 13

## Government Regulations-EU (Cont’d)

Single Point of Failure
Requires banks to notify the government if their systems are running with a single point of failure
Loss of either the PTS or the BTS results in a single point of failure for the entire CTN
Banks do not like to report such problems to the government


MIFID II violation fines:  up to 5 million Euros, or 10% of firm’s turnover

13

---

# Slide 14

## Payment Industry Regulations

Payment Card Industry (PCI) Data Security Standard V 3.2.1

14

![Image 4](P3335 Preso on Financial Industry regulations_images/slide_14_image_4.wmf)

![Image 5](P3335 Preso on Financial Industry regulations_images/slide_14_image_5.wmf)

![Image 6](P3335 Preso on Financial Industry regulations_images/slide_14_image_6.wmf)

---

# Slide 15

## Payment Industry Regulations

Payment Card Industry (PCI) Data Security Standard V 3.2.1

15

![Image 7](P3335 Preso on Financial Industry regulations_images/slide_15_image_7.wmf)

![Image 8](P3335 Preso on Financial Industry regulations_images/slide_15_image_8.wmf)

---
