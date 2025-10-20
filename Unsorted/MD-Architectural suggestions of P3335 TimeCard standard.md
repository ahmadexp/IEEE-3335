# Architectual suggestion of P3335 TimeCard standard

Magnus Danielson – Net Insight

## Re-occurring problems

Traditionally dedicated hardware have been developed for specific uses, enables tailor made designs, but comes at a hard start cost
More designs builds upon Commercially Of The Shelfs (COTS) producs, standard platforms onto which designs is adapted, cheaper base price, but may lack key features
For many synchronization and timing needs, COTS servers does neither have good clocks or good interfaces
To enable better performance, adding missing key features is needed
To enable COTS to be used in certain applications, it is a needed capability

## Usage scenario 1 – timing source to network

For a network to have good time, it needs one or more timing sources that take time, and is able to convey it
Need for timing input interfaces
Need for good hold-over performance to increase resilience to disturbances
Need for timing output interfaces
Need for monitoring port to validate time accuracy
Need for management interface to monitor, steer and maintain behaviours
=> Looks very much like TimeCards we seen

## Usage scenario 2 – timing network distributor and consumer

To build a network one not only input time, but distribute time and have receivers of time
A distributor receives time, but also conveys it
A receiver of time just do not happen to distribute it further in network
Performance of received time depends on quality of clock in receiver
Holdover performance increase resilience and performance for network events like re-routes, losses, re-selection of source etc
Much the same ability to monitor, steer and I/O remains
External time input can be benefit for monitoring, but not always practical to achieve

## Usage scenario 3 – Mobile base-station

- Server for processing
- NIC with switching and sync capabilities
- ITU-T speced oscillator requirements
- COTS server with NICs
- Needs clock and clock steering to integrate
- The TimeCard functionality may integrate into either server or NIC boards to optimize cost, size and power

#### Benefits of having common solution

- Much of the basic clock, steering etc. is needed by all solutions
- Having a common solution platform reduces need to re-invent these solutions
- Add needed features from option list as needed to meet particular applications
- A structured way for interfaces on TimeCard sub-system and also other interfaces on other sub-systems to be included and managed, dynamically appear and disappear, is to be expected today
- Ability to learn capabilities from interface can allow software developers to adapt higher layers to available features
- Structured way of advertising capabilities with specifications for what minimum performance to expect for each such basic or optional performance enable vendors to articulate capabilities such that users can procure the right features and be sure they get needed performance

## Division of properties 1

- Timing source inputs
  - PPS & 10 MHz
  - GNSS
- Timing outputs
  - PPS & 10 MHz
- Clocks and steering
  - Internal clock with known good performance
  - Ability to select different source
  - Ability to steer lock/holdover
  - Ability to combine sources (for ensemble clock)
  - Ability to select one or more network interfaces

## Division of properties 2

- Network Interfaces
  - On board
  - Separate NICs
- System usage
  - TimeCard a sub-system of a system, enhancing the capability of the system
  - NICs get steered to TimeCard time aids both receiving and distribution
  - Traditional CPU processing get access to time
  - GPUs get access to time
  - Other usage including clock synthesis in measurement instruments

#### A few words on clock performance

- Clock performance breaks up into systematics, random noise processes and environmental sensitivites
- Random noise limits uncertainty achieveable, as it adds a basic uncertainty to any locked source
- Systematic performance limits both free-running performance and ability to maintain holdover performance
- Environmental sensitivity is designed into the clock to match how hard other requirements are
- A SEC/Stratum 3 clock in TCXO costs about 10-20 USD
- Performance metrics of oscillators and steered clocks has already been established and standardized to become COTS products by themselves – ITU-T standards and methods can be recycled

## Sketches of architectural features 1

- Core functionality (mandatory)
  - Clock (see clock-options)
  - Basic inputs
  - Basic outputs
  - Management interface to steer
- Input enhancements (i.e. optional)
  - GNSS boards
  - Any other clock / time source, embedded or external
- Output enhancements (i.e. optional)
  - IRIG-B
- Network Interfacing enhancements (i.e. optional)
  - NIC interface embedded on TimeCard
  - NIC interfacing, over PCIx or other interfaces (thus, NIC is on other sub-system)

## Sketches of architectural features 2

- Physical manifestations (alternative options)
  - Separate sub-system board
  - Integrated to another sub-system (CPU or NIC)
- PCI-x interfacing (optional)
  - PTM timing interface
- Clock options (alternative options)
  - SEC/EEC clock (most basic minimal required)
  - eEEC, SSU-A/B etc. (improved performance options)