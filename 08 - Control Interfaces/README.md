# 8. Control Interfaces (Normative)

This clause specifies the control-plane requirements used to discover, configure, monitor, update, and manage a TimeCard. Every conforming implementation provides at least one control interface. A control interface may be local, host-integrated, out-of-band, remotely networked, or a combination of these forms.

## 8.1 Control-interface classes

| Class | Examples | Principal use |
|-------|----------|---------------|
| Local hardware control | SMBus, I2C, I3C, GPIO | Board-level configuration and telemetry. |
| Host-integrated control | PCIe MMIO, command queues, driver APIs, USB | Host discovery, configuration, time access, and status. |
| Out-of-band control | IPMI, NC-SI, serial | Management independent of the host operating system. |
| Remote network control | REST, gRPC, Redfish, SNMP | Fleet management and remote telemetry. |

An implementation may expose the same baseline information through more than one class. The semantic value of an object **shall** not change solely because a different control interface is used.

## 8.2 Baseline control capabilities

At least one implemented control interface **shall** provide access to the required baseline objects in 8.10.2. Collectively, the implemented control interfaces **shall** provide the following capabilities:

- Read implementation identity, revision, profile, and capability information.
- Read the unified-timescale state and an atomic time value.
- Read active and available synchronization-source information.
- Read active alarm and security-state information.
- Discover whether conditional configuration, telemetry, event, update, and sanitization operations are supported.

A writable operation is required only when the corresponding configurable feature is implemented or a conformance profile explicitly requires it.

## 8.3 Protocol mappings

### 8.3.1 SMBus, I2C, and I3C

An SMBus implementation **shall** conform to the System Management Bus Specification, Version 3.2 [14]. An I3C implementation **shall** conform to the MIPI I3C Basic specification, Version 1.2 [12].

An I2C-only implementation **shall** identify the I2C specification and revision used. For each local hardware control mapping, the supplier **shall** document addressing, bus speed, transfer size, byte order, clock-stretching behavior, timeout behavior, reset behavior, and the mapping of baseline objects.

### 8.3.2 PCIe configuration and MMIO

Each implemented PCIe control mapping **shall** satisfy 8.9. If PCIe PTM is implemented, the PCIe function **shall** expose the PTM capability structures required by the PCI Express Base Specification, Revision 5.0, Version 1.0 [13].

### 8.3.3 IPMI and NC-SI

An implementation claiming IPMI control **shall** conform to DMTF DSP0236 [1] for the IPMI version and command scope identified in the conformance statement. Vendor or P3335-specific commands **shall** use an assigned or documented extension mechanism, **shall** have identifiers unique within the applicable command namespace, and **shall** not redefine, alias, or overlap standard command identifiers.

An NC-SI mapping **shall** identify the NC-SI specification revision, package and channel discovery behavior, command set, and mapping of baseline objects.

### 8.3.4 REST, gRPC, SNMP, and Redfish

A network API **shall** publish a machine-readable schema or object description that identifies its version and maps operations to the baseline objects in 8.10.

An implementation claiming SNMP control **shall** identify the SNMP version and **shall** implement the message-processing, security, access-control, and management-information elements of the IETF RFC 3411 [6] framework that apply to the claimed management scope. The supplier **shall** identify the management information base modules, object identifiers, security model, and access-control model used.

REST, gRPC, and Redfish mappings **shall** document resource or service discovery, schema versioning, error responses, authentication method, and update compatibility.

### 8.3.5 Serial and USB

A serial or USB mapping **shall** document physical or USB class behavior, framing, command syntax or schema, encoding, flow control, timeout behavior, and the mapping of baseline objects. A human-readable command interface may be provided in addition to a machine-readable mapping.

## 8.4 Common mapping requirements

Each control-interface mapping **shall** define:

- A mapping name and major and minor version.
- Discovery and enumeration behavior.
- Data encoding, byte order, alignment, transfer size, and string encoding.
- Mapping of required and conditional objects.
- Object support, validity, stale-data, unavailable, and fault reporting.
- Error responses for unsupported operations, invalid values, reserved values, malformed requests, and access denial.
- Concurrency and atomicity behavior for multi-field values and configuration changes.
- Reset, restart, and persistence behavior.
- Compatibility behavior for unknown objects, fields, enumeration values, and extensions.

A change that removes an object, changes its units or meaning, narrows its valid range, or changes its access semantics **shall** increment the mapping major version. A backward-compatible addition **shall** increment the mapping minor version.

A receiving implementation **shall** process every recognized object and field in a message. It **shall** leave an unknown optional object or field uninterpreted. When forwarding is supported, it **shall** preserve the unknown optional value. If an unknown element prevents the requested operation, the receiving implementation **shall** report an incompatibility. A receiving implementation **shall** not write a reserved value. An implementation receiving a reserved or invalid write value **shall** reject the operation without changing the prior value.

## 8.5 Atomic reads and configuration changes

Values representing a single logical observation **shall** be returned atomically. In particular, a timestamp split across multiple transport words **shall** use a latch, snapshot command, sequence counter, retry rule, or equivalent mechanism that prevents fields from different seconds or update cycles from being combined.

For background on transaction atomicity, see [B22].

For a configuration operation affecting timing behavior, the interface **shall** report whether the operation was accepted, when it became effective, and whether it caused or can cause a phase step, frequency transient, loss of lock, restart, or interruption of a providing interface.

Configuration writes **shall** either complete as one documented operation or report partial completion and the resulting state. A failed write **shall** not silently leave an indeterminate state or configuration.

## 8.6 Access control and security state

Every control interface **shall** document its authentication, authorization, transport protection, update authorization, audit, key-storage, and sanitization capabilities. The `SECURITY_STATE` object **shall** report the mechanisms supported and their current verified or active state. If no security mechanism is implemented for a control interface, the documentation and `SECURITY_STATE` object **shall** state `none` and **shall** identify the physical-access or deployment assumptions on which that choice depends.

Requirements for the Managed TimeCard and Secure Infrastructure TimeCard profiles are specified in 8.11. A control interface not claiming either profile may omit authentication only when the omission is declared in the conformance statement.

Security failure **shall** not be reported as normal successful completion. Authentication failures, authorization denials, firmware verification failures, and sanitization failures **shall** be distinguishable to an authorized operator.

## 8.7 Events and telemetry

If event reporting is implemented, each event record **shall** include a timestamp or an explicit indication that valid time was unavailable, a severity, a source, an event type, and event-specific data. The event timestamp measurement point and timescale **shall** be documented.

The following state changes **shall** generate an event when the corresponding function and event reporting are implemented:

- Reference acquired, rejected, selected, degraded, or lost.
- Lock acquired or lost.
- Holdover entered or exited.
- Time step, frequency step, or discontinuity detected.
- Environmental or power threshold crossed.
- Firmware update, boot-integrity check, authentication, authorization, or sanitization completed or failed.

If telemetry streaming is implemented, the supplier **shall** document rate limits, timestamp behavior, dropped-sample indication, ordering, backpressure, and the relationship between streamed values and on-demand reads.

## 8.8 Extensions

An implementation may provide vendor-specific objects, commands, registers, messages, and telemetry. Extensions **shall** use a documented namespace or identifier range and **shall** not change the meaning of baseline objects.

A receiving implementation that does not advertise support for an extension **shall** be able to process the baseline object or message without interpreting that extension. Reserved P3335 identifiers and values **shall** not be assigned to vendor-specific behavior.

## 8.9 PCIe host interface profile

An implementation claiming the PCIe Host Mapping conformance profile **shall** expose a discoverable PCIe function associated with the TimeCard timing and control functions.

The PCIe mapping **shall** document:

- Vendor ID, device ID, class code, subsystem identifiers, and revision identifier.
- PCIe Base Specification revision and discovery behavior.
- BAR, capability, command-queue, or driver-API resources used by the mapping.
- Mapping signature and major and minor version at a documented discovery location.
- Interrupt or polling behavior.
- Function-level, fundamental, and software-reset behavior.
- Persistence of configuration and time state across each reset type.
- Error reporting for unsupported, malformed, reserved, or unauthorized accesses.
- Timestamp format, epoch, timescale, granularity, rollover, and atomic-read mechanism.
- Measurement point and correction terms relating PCIe or PTM time to the unified timescale and other providing interfaces.

The PCIe mapping **shall** expose all required baseline objects in 8.10.2 through MMIO, a command or queue interface, a driver API, or a documented combination thereof. The conformance statement **shall** identify which mapping is the interoperable baseline for the implementation.

If PCIe PTM is implemented, the TimeCard **shall** expose the standard PTM capability structures and **shall** document the PTM measurement point and correction model.

## 8.10 Baseline control information model

The baseline information model defines transport-neutral object names, data semantics, access modes, and units. A protocol mapping may use registers, messages, resources, attributes, or API calls, provided that it preserves these semantics and satisfies 8.4 and 8.5.

### 8.10.1 Data types and object status

| Type | Description |
|------|-------------|
| `bool` | Boolean false or true. |
| `uint8`, `uint16`, `uint32`, `uint64` | Unsigned integer of the indicated width. |
| `int64` | Signed 64-bit integer. |
| `enum` | One value from a defined symbolic set. |
| `string` | UTF-8 string with a mapping-defined maximum length. |
| `set` | Unordered set of defined symbolic values. |
| `timestamp` | Atomic structure containing seconds, nanoseconds, timescale, validity, and optional uncertainty. |
| `record` | Structure whose fields are defined by the object or mapping. |

Access modes are `R` for read-only, `W` for write-only, and `R/W` for read/write. Every read response **shall** distinguish `valid`, `unavailable`, `unsupported`, `unspecified`, `stale`, and `fault` when those states can occur in the mapping.

For a `timestamp`, nanoseconds **shall** be in the range 0 through 999 999 999. The seconds and nanoseconds fields **shall** represent the same measurement instant and **shall** satisfy the atomic-read requirement in 8.5.

Each mapping **shall** define the response when a value would exceed the representable range of its declared type. For every accumulating counter, the mapping **shall** define whether the value saturates or rolls over, its maximum or modulus, its reset conditions, and the indication used to detect rollover or lost counts. An accumulating counter **shall** not wrap without an observable indication.

### 8.10.2 Required baseline objects

The following objects **shall** be exposed through at least one control interface:

| Object | Access | Type | Units | Semantics |
|--------|--------|------|-------|-----------|
| `TC_MODEL` | R | string | none | Product or implementation model identifier. |
| `TC_HW_REV` | R | string | none | Hardware or implementation revision; `not-applicable` for an implementation without hardware. |
| `TC_FW_REV` | R | string | none | Active firmware, gateware, or software revision; `not-applicable` when none exists. |
| `TC_INFO_MODEL_REV` | R | string | none | P3335 information-model revision implemented. |
| `TC_PROFILE` | R | set | none | Conformance profiles claimed by the active configuration. |
| `TC_CAPS` | R | set | none | Implemented interface and feature capabilities. |
| `TC_STATE` | R | enum | none | Overall unified-timescale operating state. |
| `TC_TIMESCALE` | R | enum | none | Timescale represented by `TC_TIME` and timing telemetry. |
| `TC_TIME` | R | timestamp | s, ns | Atomic unified-timescale value at the declared read measurement point. |
| `SYNC_SRC_ACTIVE` | R | string | none | Identifier of the source currently used to discipline or validate the unified timescale; `none` when no source is active. |
| `SYNC_SRC_AVAIL` | R | set | none | Identifiers of synchronization sources currently available for selection or monitoring. |
| `ALARM_ACTIVE` | R | set | none | Active alarm identifiers; an empty set indicates no active alarm. |
| `SECURITY_STATE` | R | record | none | Supported and active security mechanisms and the result of the most recent integrity verification. |

A required baseline object **shall** not report `unsupported` or `unspecified` as its object-level status. An optional field within that object may report `unspecified` when the mapping permits it. A required baseline object may report `unavailable`, `stale`, or `fault` only when that state is meaningful and distinguishable from a valid value.

### 8.10.3 Conditional baseline objects

The following objects are required when the corresponding capability is advertised in `TC_CAPS`:

| Object | Access | Type | Units | Applicability and semantics |
|--------|--------|------|-------|-----------------------------|
| `SYNC_SRC_SELECT` | R/W | string | none | Implementations supporting operator source selection; selected source or selection policy. |
| `SYNC_SRC_HEALTH` | R | record | none | Implementations with receive interfaces; health and rejection reason for each source. |
| `PHASE_ERR` | R | int64 | ps | Implementations reporting phase error; value relative to the identified source and measurement point. |
| `FREQ_OFFSET` | R | int64 | 1e-15 | Implementations reporting fractional frequency offset; value relative to the identified source. |
| `MTIE_EST` | R | uint64 | ps | Implementations reporting estimated or measured MTIE; paired with `MTIE_INTERVAL`. |
| `MTIE_INTERVAL` | R | uint64 | s | Observation interval associated with `MTIE_EST`. |
| `HOLDOVER_ELAPSED` | R | uint64 | s | Implementations supporting holdover; elapsed time since holdover entry. |
| `TEMP_LOCAL` | R | int64 | mdeg C | Implementations reporting a local timing-function temperature in millidegrees Celsius; sensor location is declared. |
| `EVENT_COUNT` | R | uint32 | count | Implementations with an event log; number of readable retained events. Behavior at the `uint32` limit and indication of event loss or overwrite follow the mapping declaration required by 8.10.1. |
| `EVENT_READ` | R | record | none | Implementations with an event log; next or selected event record. |
| `REFERENCE_EVIDENCE` | R | record | none | Implementations reporting reference-chain evidence; identifiers and availability of source, calibration, measurement-point, and uncertainty information without asserting end-to-end traceability. |
| `UPDATE_CMD` | W | record | none | Implementations supporting controlled firmware, gateware, or software update. |
| `SANITIZE_CMD` | W | record | none | Implementations claiming sanitization; scope and authorization parameters. |

A conditional object advertised in `TC_CAPS` **shall** not report `unsupported`. An unadvertised conditional object may report `unsupported` when addressed through a mapping that permits object probing.

### 8.10.4 Common symbolic values

`TC_PROFILE` **shall** use the profile names `base`, `physical-timing-output`, `pcie-host-mapping`, `managed-timecard`, and `secure-infrastructure-timecard` for the corresponding profiles in 4.4.

`TC_STATE` **shall** distinguish at least the following states: `unknown`, `initializing`, `warming-up`, `free-running`, `acquiring`, `locked`, `holdover`, `degraded`, and `fault`.

`TC_TIMESCALE` **shall** distinguish at least `unknown`, `TAI`, `UTC`, `PTP`, and `other-declared`. If `other-declared` is used, the mapping to a declared reference timescale **shall** be documented.

Unknown symbolic values received by a receiving implementation **shall** be preserved when forwarding and otherwise treated as unknown. A mapping that encodes symbolic values numerically **shall** document the numeric assignments and reserve an extension range.

### 8.10.5 GNSS conditional objects

If a GNSS receive capability is advertised in `TC_CAPS`, the following objects **shall** be exposed:

| Object | Access | Type | Units | Semantics |
|--------|--------|------|-------|-----------|
| `GNSS_INSTANCES` | R | uint8 | count | Number of GNSS receiver instances. |
| `GNSS_ENABLE` | R/W | set | none | Enabled receiver-instance identifiers, when receiver enable control is supported. |
| `GNSS_CONST_AVAIL` | R | record | none | Available constellations for each receiver instance. |
| `GNSS_CONST_ENABLE` | R/W | record | none | Enabled constellations for each receiver instance, when configuration is supported. |
| `GNSS_LOCK_STATE` | R | record | none | Acquisition or lock state for each receiver instance. |
| `GNSS_ANTENNA_STATE` | R | record | none | Antenna state for each receiver instance, including unknown, valid, open, short, or degraded when detectable. |

The common constellation identifiers are `GPS`, `Galileo`, `GLONASS`, `BeiDou`, `QZSS`, and `NavIC`. Additional constellation identifiers **shall** use the extension mechanism defined by the control mapping.

### 8.10.6 Other satellite timing sources

Non-GNSS satellite services, including large low-Earth-orbit constellations such as Starlink, are not assigned common GNSS identifiers by P3335. If an implementation uses such a service as a timing source, the supplier **shall** identify the service, document vehicle selection and handover behavior, and expose source identity and health through the extension mechanism defined by the control mapping.

## 8.11 Security profiles

### 8.11.1 Baseline security declaration

All conforming implementations **shall** document the security properties of each control interface, including physical-access assumptions. The documentation **shall** state whether authentication, authorization, encrypted transport, signed update, boot integrity verification, protected key storage, anti-rollback protection, event auditing, tamper response, and sanitization are supported. This declaration requirement does not require a security mechanism unless the implementation claims a profile or feature whose applicable requirements specify that mechanism. When no security mechanism is implemented, the documentation **shall** state `none` and identify the deployment assumptions.

### 8.11.2 Managed TimeCard profile

An implementation claiming the Managed TimeCard profile **shall** meet the following requirements:

- A networked or remotely reachable control interface **shall** authenticate the user or machine before permitting configuration or update operations.
- Authorization **shall** distinguish monitoring, configuration, update, security-administration, and sanitization privileges when those operations are implemented.
- Default shared credentials **shall** be replaced or changed before remote configuration is enabled.
- An update payload **shall** be integrity-checked before installation.
- Security-relevant successes and failures **shall** be recorded when event logging is implemented.
- The security protocol, version, credential lifecycle, and recovery procedure **shall** be documented.

### 8.11.3 Secure Infrastructure TimeCard profile

An implementation claiming the Secure Infrastructure TimeCard profile **shall** meet the Managed TimeCard profile and the following additional requirements:

- Firmware, gateware, and other executable update payloads **shall** be digitally signed and verified against an authorized trust anchor before activation.
- The update mechanism **shall** prevent installation of an unauthorized rollback version unless an explicitly authorized recovery procedure is used.
- Secure boot or measured boot **shall** verify executable integrity before the timing service enters the locked state.
- Private keys and credentials **shall** be stored in hardware-backed or equivalently protected storage whose protection mechanism is documented.
- Remote IP-based management **shall** use an encrypted, peer-authenticated transport.
- Privileged operations **shall** provide replay and message-injection protection.
- Sanitization **shall** erase the sensitive keys, credentials, and security-relevant configuration identified in the sanitization scope.
- Sanitization completion or failure **shall** be reported, and a failed sanitization **shall** not be reported as successful.

## 8.12 Summary

This clause defines a transport-neutral baseline control model and the requirements that each protocol binding preserves. The model supports common integration while allowing transport-specific and vendor-specific extensions to evolve through explicit versioning and namespaces.
