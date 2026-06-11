# 8. Control Interfaces (Normative)

This chapter defines the physical, logical, and protocol-level **control interfaces** used to configure, monitor, and manage TimeCard devices.

---

## 8.1 Overview

Control interfaces form the out-of-band and in-band **management plane** of the TimeCard architecture. Unlike the timing interfaces defined in Clause 7, which operate strictly within the data plane to deliver phase and frequency synchronization, control interfaces are responsible for:
- Configuration of synchronization parameters and state machines.
- Status monitoring, health telemetry, and fault reporting.
- Firmware provisioning and lifecycle security management.
- Traceability reporting and calibration operations.

Every compliant TimeCard implementation shall provide at least one accessible control interface. This interface may be exposed through a physical baseboard connector, a host-exposed bus interface, or a network-based protocol suite.

---

## 8.2 Control Interface Classes

Control interfaces are categorized based on their communication topology and data granularity.

| Class | Description | Typical Use |
|--------|--------------|--------------|
| **Local Hardware Control** | Direct access via SMBus, I²C, I3C, or GPIO. | Baseboard-level configuration, power sequencing, or low-level telemetry by a BMC. |
| **Host-Integrated Control** | In-band access via PCIe MMIO or USB. | Runtime synchronization control by host OS software or drivers. |
| **Out-of-Band (OOB) Control** | NC-SI, IPMI, or dedicated serial interface. | Independent platform management regardless of the host OS state. |
| **Remote Network Control** | REST, gRPC, Redfish, or SNMP. | Distributed system orchestration or cloud-scale management. |

A TimeCard may implement one or more of these control classes simultaneously to support sophisticated datacenter abstraction models.

---

## 8.3 Minimum Functional Requirements

Where a control interface is implemented, it shall expose at least the following minimum common set of capabilities, restricted by the bandwidth and constraints of the specific medium:

| Function | Description |
|-----------|--------------|
| **Source Selection** | Select, prioritize, or configure the active synchronization reference (e.g., GNSS, PTP, PPS). |
| **Mode Control** | Read and modify the current operational state machine (e.g., Locked, Holdover, Free-running, Warm-up). |
| **Clock Discipline Settings** | Adjust PLL or disciplining loop time constants and bandwidth parameters. |
| **Telemetry Access** | Retrieve metrics such as fractional frequency offset, internal temperatures, instantaneous phase error, and stability statistics. |
| **Alarm and Event Logs** | Report critical operational events such as loss of reference, spoofing detection, or firmware integrity faults. |
| **Firmware Management** | Support cryptographic firmware update triggers, version reporting, and rollback. |

---

## 8.4 Communication Protocols

### 8.4.1 SMBus / I²C / I3C
- Provides low-speed, low-latency configuration and sensor access, typically used by a Baseboard Management Controller (BMC).
- The address space and register map should be modeled consistently across compliant implementations to ease integration.
- Bus arbitration, clock stretching, and timing compliance shall follow the respective SMBus or MIPI I3C specifications.

### 8.4.2 PCIe Configuration and MMIO
- Allows in-band, high-speed access to TimeCard control registers directly from the host CPU.
- The register layout should comply with recognized industry standard memory maps (such as the OCP-TAP Control Register Map) where applicable.
- If the TimeCard supports PCIe Precision Time Measurement (PTM), the control interface shall present the necessary standard capability structures to the host to enable PTM negotiation.

### 8.4.3 IPMI / NC-SI
- Enables robust out-of-band control independent of the host processor or operating system.
- IPMI implementations shall conform to DMTF DSP0236 for the claimed IPMI version and command scope.
- TimeCard devices establishing IPMI communication should implement an extended command set for time synchronization management (e.g., querying clock state, initiating reference failover).
- IPMI commands may support authenticated sessions utilizing pre-shared platform credentials.

### 8.4.4 REST / gRPC / SNMP / Redfish
- Used for high-level, network-based management and large-scale telemetry aggregation.
- REST, Redfish, and gRPC APIs should conform to established management schemas where such schemas apply.
- SNMP implementations shall conform to the SNMP architecture defined by IETF RFC 3411 for the claimed SNMP version and management scope.
- SNMP implementations should expose standard OIDs for timing health, synchronization source, and hardware/firmware versions.

### 8.4.5 Serial and USB
- Serial (RS-232/RS-422/RS-485) interfaces should provide a human-readable command-line shell or SCPI-like syntax for localized debugging.
- USB connections may present as standardized Communications Device Class (CDC) / virtual COM ports to facilitate maintenance or localized firmware provisioning.

---

## 8.5 Control Register Structure

The logical control registers listed below represent the fundamental baseline for low-level interaction between the host/BMC and the TimeCard. While physical implementations differ (e.g., I2C addresses vs. PCIe MMIO offsets), the logical concepts shall be present:

| Logical Register Concept | Description | Access | Example Units |
|-----------|--------------|---------|----------------|
| `SYNC_SRC` | Active external synchronization source ID | R/W | Enumeration |
| `PLL_STATE` | Current disciplining state (Locked, Holdover, Free) | R | Enumeration |
| `PHASE_ERR` | Instantaneous phase error relative to the primary reference | R | nanoseconds |
| `TEMP` | Active local oscillator temperature | R | °C |
| `MTIE_EST` | Current estimated holdover drift/MTIE boundary | R | nanoseconds |
| `FIRMWARE_VER` | Active running firmware version string | R | ASCII / Hex |
| `UPDATE_CMD` | Trigger flag for firmware update sequences | W | Boolean |
| `SECURE_MODE` | Runtime security lockdown indicator | R/W | Boolean |

All registers should adhere to consistent endianness and word alignment across a vendor's product line.

Reserved values are reserved for future use by IEEE P3335. A reserved value shall not be configured by an implementation or management client. If a reserved value is read from a field, the management client shall ignore that value unless a later revision of this standard defines it.

---

## 8.6 Security and Access Control

*Note: The requirements in this subclause apply conditionally. They are required only for TimeCards marketed or designated for secure infrastructure deployments. For isolated or lab-grade physical environments, these features may be omitted to reduce complexity.*

Where security hardening is implemented, control interfaces operate as primary attack surfaces and require robust cryptographic protection.

### 8.6.1 Authentication and Authorization
- Networked control protocols shall support user or machine authentication.
- Privilege levels should distinguish between read-only monitoring access, operator configuration access, and administrator provisioning access.
- Access credentials and cryptographic keys should be stored securely within a hardware-backed enclave or discrete TPM.

### 8.6.2 Secure Firmware and Configuration
- Firmware payload images shall be digitally signed using verifiable certificates.
- A secure boot sequence should verify firmware integrity (cryptographic hash matches) at initialization before granting control to the TimeCard operating logic.

### 8.6.3 Network Security
- Remote IP-based interfaces (REST, Redfish, gRPC) should utilize encrypted transport layers (e.g., TLS).
- Replay and injection protection should be implemented for operations traversing shared networking environments.

---

## 8.7 Event and Telemetry Management

To facilitate continuous performance observability, the control interface should support structured event and telemetry generation.

### 8.7.1 Event Reporting
- Generated operational events shall include a local timestamp, a severity classification, and a source identifier.
- Critical events should include, but are not limited to:
  - Reference loss (LOS)
  - Phase lock achieved or lost
  - Holdover entry or exit
  - Temperature threshold alarms
  - Firmware update success or failure.

### 8.7.2 Telemetry Streaming
- Continuous telemetry may be streamed via IPMI, REST, or gRPC for integration into centralized infrastructure dashboards.
- Telemetry generation rates shall be configurable by the administrator.
- Time synchronization statistics (such as ADEV or instantaneous phase offsets) should be strictly timestamped and aligned to the TimeCard's unified timescale.

### 8.7.3 Logging and Traceability
- Critical alarm logs should be preserved in non-volatile memory across power cycles.
- Exported log files may include cryptographic signatures to validate log integrity during forensic analysis.
- Traceability metadata (such as calibration constants and firmware build hashes) should be accessible to support operational compliance audits.

---

## 8.8 Interoperability and Extensions

All implemented control interfaces shall comply with the baseline schema defined by the overarching IEEE P3335 architecture.

Manufacturers may implement proprietary extensions, custom registers, or vendor-specific telemetry strings. These optional extensions shall not compromise or interfere with the baseline interoperability of the standardized registers and capabilities.

---

## 8.9 Baseline PCIe Host Interface Mapping

An implementation claiming the PCIe Host Mapping conformance profile shall expose a PCIe function that can be discovered by the host operating system and associated with the TimeCard control and timing functions.

The PCIe host mapping shall document:

- PCIe vendor ID, device ID, class code, subsystem identifiers, and revision identification.
- Discovery and enumeration behavior.
- Base Address Register (BAR) usage and memory type.
- Register block version, size, endianness, alignment, and access width.
- Interrupt mechanism, if interrupts are implemented.
- Reset behavior and persistence of configuration across reset.
- Error-reporting behavior for unsupported, reserved, or malformed accesses.
- Timestamp format, epoch, timescale, granularity, and rollover behavior.
- Correction terms required to relate PCIe/PTM timestamps to the unified timescale and to other providing interfaces.

If PCIe Precision Time Measurement (PTM) is implemented, the TimeCard shall expose the standard PCIe PTM capability structures required for host negotiation. The conformance statement shall identify the PCIe Base Specification revision used and the measurement point represented by PTM timestamps.

The baseline PCIe register block shall provide access to the baseline information model in 8.10. A PCIe implementation may provide additional vendor-specific BARs, registers, queues, or direct-memory-access mechanisms if those extensions do not alter the semantics of the baseline information model.

## 8.10 Baseline Control Information Model

The baseline information model defines semantic objects that shall be available through at least one implemented control interface. A physical register map, memory-mapped interface, command protocol, object model, schema, or API may be used to expose these objects, provided that the semantics, units, access modes, and reserved-value behavior are preserved.

### 8.10.1 Data Types and Access Modes

The following common data types are used by the baseline information model:

| Type | Description |
|------|-------------|
| `bool` | Boolean value, encoded as false or true. |
| `uint8`, `uint16`, `uint32`, `uint64` | Unsigned integer of the indicated width. |
| `int64` | Signed integer of the indicated width. |
| `enum` | Unsigned integer value selected from a documented enumeration. |
| `ascii` | Printable ASCII string with documented maximum length. |
| `bitmap` | Unsigned integer where individual bits have documented meanings. |

Access modes are `R` for read-only, `W` for write-only, and `R/W` for read/write.

### 8.10.2 Required Baseline Objects

The following objects shall be exposed by at least one control interface:

| Object | Access | Type | Units | Description |
|--------|--------|------|-------|-------------|
| `TC_MODEL` | R | ascii | none | Product or implementation model identifier. |
| `TC_HW_REV` | R | ascii | none | Hardware revision or equivalent implementation revision. |
| `TC_FW_REV` | R | ascii | none | Active firmware, gateware, or software revision. |
| `TC_PROFILE` | R | bitmap | none | Claimed conformance profiles and optional feature groups. |
| `TC_CAPS` | R | bitmap | none | Implemented receive, providing, host, control, security, and telemetry capabilities. |
| `TC_STATE` | R | enum | none | Overall timing state: initializing, warming up, free-running, locked, holdover, degraded, fault, or reserved. |
| `TC_TIMESCALE` | R | enum | none | Unified timescale exposed by the TimeCard, such as TAI, UTC, PTP, or implementation-specific. |
| `TC_TIME_SEC` | R | uint64 | s | Integer seconds of the unified timescale at the declared read measurement point. |
| `TC_TIME_NS` | R | uint32 | ns | Nanosecond portion of the unified timescale at the declared read measurement point. |
| `TC_GRANULARITY` | R | uint32 | ps | Timestamp granularity. |
| `TC_RESOLUTION` | R | uint32 | ps | Declared timestamp resolution. |
| `SYNC_SRC_ACTIVE` | R/W | enum | none | Active synchronization source selection or configured source selector. |
| `SYNC_SRC_AVAIL` | R | bitmap | none | Available synchronization sources. |
| `SYNC_SRC_HEALTH` | R | bitmap | none | Health indication for implemented synchronization sources. |
| `PHASE_ERR` | R | int64 | ps | Instantaneous phase error relative to the selected reference, if available. |
| `FREQ_OFFSET` | R | int64 | 1e-15 | Fractional frequency offset relative to the selected reference, if available. |
| `MTIE_EST` | R | uint64 | ps | Estimated or measured MTIE boundary for the declared interval, if available. |
| `HOLDOVER_ELAPSED` | R | uint64 | s | Elapsed time since entry into holdover. |
| `TEMP_LOCAL` | R | int64 | millidegrees C | Local oscillator or timing-function temperature. |
| `ALARM_ACTIVE` | R | bitmap | none | Active alarm indications. |
| `EVENT_COUNT` | R | uint32 | count | Count of retained event-log entries. |
| `EVENT_READ` | R | implementation-specific | none | Mechanism to read timestamped event records. |
| `TRACEABILITY_STATE` | R | enum | none | Traceability state: unsupported, unknown, traceable, degraded, or reserved. |
| `UPDATE_CMD` | W | enum | none | Firmware or configuration update command. |
| `SECURITY_STATE` | R | bitmap | none | Authentication, secure boot, signed firmware, and sanitization state. |

If a required object is not meaningful for a specific implementation, it shall be readable and shall return an unsupported or unavailable value from its documented enumeration.

### 8.10.3 GNSS Optional Objects

If a GNSS receive interface is implemented, the following objects shall be exposed:

| Object | Access | Type | Units | Description |
|--------|--------|------|-------|-------------|
| `GNSS_PRESENT` | R | bool | none | Indicates whether at least one GNSS receiver is present. |
| `GNSS_INSTANCES` | R | uint8 | count | Number of GNSS receiver instances. |
| `GNSS_ENABLE` | R/W | bool array | none | Enable state for each GNSS receiver instance. |
| `GNSS_CONST_AVAIL` | R | bitmap | none | Available GNSS constellations for each receiver instance. |
| `GNSS_CONST_ENABLE` | R/W | bitmap | none | Enabled GNSS constellations for each receiver instance. |
| `GNSS_LOCK_STATE` | R | enum | none | Receiver lock state. |
| `GNSS_ANTENNA_STATE` | R | enum | none | Antenna state, including unknown, valid, open, short, degraded, or reserved. |

Constellation enumeration values 0 and 9 through 191 are reserved for future standardization. Values 192 through 255 are implementation-specific.

## 8.11 Security Profiles

### 8.11.1 Baseline Security Profile

All conforming implementations shall document the security state of each implemented control interface. The documentation shall state whether authentication, authorization, secure boot, signed firmware update, encrypted transport, protected key storage, tamper response, and sanitization are supported.

### 8.11.2 Managed Security Profile

An implementation claiming the Managed TimeCard conformance profile shall meet the following requirements:

- Networked or remotely reachable control interfaces shall require authentication.
- The implementation shall distinguish read-only monitoring from configuration operations.
- Firmware update payloads shall be integrity-checked before installation.
- Security-relevant events shall be recorded in the event log.
- Default credentials, if present, shall be changeable.

### 8.11.3 Secure Infrastructure Profile

An implementation claiming the Secure Infrastructure TimeCard conformance profile shall meet the Managed Security Profile requirements and the following additional requirements:

- Firmware update payloads shall be digitally signed.
- A secure boot or measured boot mechanism shall verify firmware or gateware integrity before timing service enters the locked state.
- Private keys and credentials shall be stored in hardware-backed storage or another documented protected storage mechanism.
- Remote IP-based management shall use encrypted transport.
- Privileged operations shall provide replay or injection protection.
- A sanitization command shall erase sensitive keys, credentials, and security-relevant configuration.
- Sanitization completion or failure shall be reported through the control interface.

## 8.12 Summary

Control interfaces provide the framework for secure, consistent, vendor-neutral lifecycle management of TimeCard systems.

By standardizing configuration and telemetry logic, this framework facilitates integrating diverse TimeCards across heterogeneous server fleets and telecommunications infrastructures. This architectural consistency promotes long-term maintainability, traceability, and operational reliability throughout the lifespan of precision time synchronization networks.

---

**End of Chapter – Control Interfaces**
