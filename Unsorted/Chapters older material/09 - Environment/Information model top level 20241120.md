Proposal on top level of information model
Doug Arnold
2024-11-20

So far this is just the top level for GNSS to see if anyone likes this approach


Add to 3.1 Acronyms

GNSS	Global Navigation Satellite System
GPS	Global Positioning System
IRNSS	Indian Regional Navigation Satellite System
PNT 	Position Navigation and Timing
QZSS	Quasi-Zenith Satellite System

8. Control Interfaces

The information model does not have to be implemented as long as the timecard driver makes the attributes available in the data formats described in this clause.

A reserved value is for future use by the IEEE 3335 working group.  It shall not be configured.  If read it shall be ignored.

8.1 Timing Inputs

8.1.1 GNSS receivers

**Table 1 - GNSS receiver attributes**

8.1.1.1 GNSSpresent 

Attribute type: read
Data type: Boolean

8.1.1.2 GNSSinstances

Attribute type: read
Data type: Uint8

8.1.1.3 GNSSinstanceNumber

Attribute type: argument
Data type: Uint8

8.1.1.4 GNSSenable

Attribute type: read, write
Argument: GNSSinstanceNumber
Data type: Boolean[GNSSinstances]

8.1.1.5 GNSSconsellationsAvailable

Attribute type: read
Argument: GNSSinstanceNumber
Data type: Boolean[Uint8]

**Table 2 – GNSS constellations**

8.1.1.6 GNSSconstellationNumber

Attribute type: argument
Data type: Uint8

8.1.1.7 GNSSconsellationEnable

Attribute type: read, write
Arguments: 
GNSSinstanceNumber
GNSSconstellationNumber
Data type: Boolean[Uint8, Uint8]















| Attribute | Attribute type | Description |
| --- | --- | --- |
| GNSSpresent | Read | Reports presence of at least one GNSS receiver |
| GNSSinstances | Read | Number of GNSS instances present |
| GNSSinstanceNumber | Argument | GNSS instance index |
| GNSSenable | Read, write | Configures or reports enablement of GNSS instances |
| GNSSconstellationsAvailable | Read | Reports which GNSS constellations the receiver can use in the PNT solution |
| GNSSconsellationNumber | Argument | GNSS constellation index |
| GNSSconsellationEnable | Read, write | Configures or reports enablement of GNSS Constellations withing a specific GNSS instance |


| GNSSconstellationNumber | GNSS constellation |
| --- | --- |
| 0 | reserved |
| 1 | GPS |
| 2 | Galileo |
| 3 | GLONASS |
| 4 | BeiDou |
| 5 | QZSS |
| 6 | IRNSS |
| 7 | Iridium |
| 8 | AtomiChron |
| 9-191 | reserved |
| 192-255 | Implementation specific |
