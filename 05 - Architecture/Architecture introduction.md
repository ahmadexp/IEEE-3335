Proposal for "Time Card Overview" clause in Architecture section (or wherever else?)
Denis Reilly 11/18/2024 denis.reilly@gmail.com

---

The Time Card system defined in this standard exists to enhance the time-of-day synchronization performance of a larger computing system (defined as the Host system)  that it is incorporated into. While one example of this type of system could be an add-in card such as a PCI Express card, a Time Card system does not have to be an add-in card. It could be an IP block which is directly embedded into the Host, for instance, or a module that is temporarily connected to the Host system via a hot-pluggable interface. Any subsystem which meets the definition in this standard and is designed to be incorporated inside a larger system can meet the definition of the Time Card.

It is assumed that the Host system by itself typically does not have a sufficiently good local clock, clock steering, time-measurement capabilities and other time-transfer mechanisms to keep time to the desired time accuracy level. The Time Card can be incorporated into this Host system to enhance its timekeeping ability without redesigning the Host system itself. 

The Time Card will be designed to take time from at least one good external source, which the Host could not normally manage on its own. The Time Card will also be designed with an oscillator with defined performance characteristics. A Time Card can also be capable of transmitting time directly to other sources (including other Time Cards with the proper input capabilities) via hardware signals that could not be controlled precisely enough by the Host alone. 

Each Time Card system can include a different configuration of Time and Frequency input and output signals (collectively called Timing Interfaces). If a Time Card system includes a Timing Interface that is defined in this standard, it will implement it according to this standard.

A Time Card can be controlled and configured by its Host system through a Control Interface. If a Control Interface is present, it will be implemented according to the information model in this standard. The same physical interface can be used as both a Control Interface and a Timing Interface, but there will be separate logical mechanisms for these functions. (For instance, a PCIe-based Time Card may use the PCIe bus as both a Timing Interface and a Control Interface, but these two functions are separate).

----

Notes to self:
"Time Card" is always 2 words in the PAR

I intend to avoid the IEEE keywords for now in this text

(IEEE keywords **shall **(Required)**, should** (Recommended)**, may **(Allowed). )
**(Avoid: must **(unavoidable situation) is deprecated. **ensure, guarantee, always**)