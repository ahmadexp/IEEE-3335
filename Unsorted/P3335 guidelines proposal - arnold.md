# Some Proposed Guidelines for Normative Clauses in P3335

Doug Arnold

2023-11-07

## Contents

- 1. Absolute requirements and options
- 2. Host interface mappings
- 3. Performance metrics

#### Absolute requirements and options

- A time card is not compliant to P3335 unless all absolute requirements are met
- A time card can be compliant to P3335 without implementing options
- Options might have requirements (shall statements)
  - To claim that a time card implements a P3335 option, it must implement all requirements that we define for that option
- A compliant time card implementation may include some options, and not others
- A statement of compliance to P3335 should list included options. Not mentioning an option should be interpreted as the option is not included

### Users of P3335 standard

- 1. Operators of systems that need precise timing
- 2. System architects/integrators designing systems that need precise timing
- 3. Open source projects that develop drivers for P3335 time cards
- 4. Time card designers
- 5. Component designers (i.e. time card subsystem designers)
- Users 1-3 care only about properties of the time card observable at the host interface and i/o port interfaces
- Users 4 and 5 also care about internal interfaces
- Time card designers might want to implement a proprietary internal time card architecture
- Proposal:
  - host and i/o ports interface requirements are absolute
  - Internal interfaces are options

## Time card block diagram

![](_page_4_Figure_1.jpeg)

## Host interface mappings

- A P3335 time card can use different host interface mappings
- We define a PCIe mapping
- We define what has to be specified for a new host interface mapping
  - Deviations from the PCIe mapping will be the minimum change that is needed to work with the host interface protocol and hardware
  - So that a driver can be ported to a new host technology easily

## Performance requirements

- We do not specify performance requirements for compliance
  - This is needed to allow cards to work in different use cases
- But we specify performance metrics
  - So that performance claims by manufacturers are clear and unambiguous
    - Reduce marketing weasel wording
  - Our ability to enforce this might be limited to educating the end users and system integrators