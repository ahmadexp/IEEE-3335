# What is a TimeCard?

A summary of the last few P3335 Plenary and System Architecture discussions
This may form the basis for an Introductory sub-clause to the Architecture section

A TimeCard is an element of a larger system
It is not required to be an add-in card, in spite of the name
It may be an IP block embedded in a larger system
Add-in cards provide one example of a subsystem
A TimeCard must have better timekeeping ability than its host
We need a good definition of "timekeeping"
Must take time from at least one external source (ideally multiple sources)
These will likely be signals that the Host cannot manage on its own
Must have an oscillator with defined performance characteristics
required to be "better" than the Host, but simply having defined performance 
It may transmit time directly to other sources via hardware signals that could not be controlled precisely enough form the Host alone.
A TimeCard is controlled by its host system through a control interface
Having a standard control interface will encourage interoperability
