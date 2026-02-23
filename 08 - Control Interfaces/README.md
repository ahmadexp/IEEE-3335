# 8. Control Interfaces (Normative)

This chapter defines the physical, logical, and protocol-level **control interfaces** used to configure, monitor, and manage TimeCard devices.

---

## 8.1 Overview

Control interfaces form the out-of-band and in-band **management plane** of the TimeCard architecture. Unlike the timing interfaces defined in Clause 7, which operate strictly within the data plane to deliver phase and frequency synchronization, control interfaces are responsible for:
- Configuration of synchronization parameters and state machines.
- Status monitoring, health telemetry, and fault reporting.
- Firmware provisioning and lifecycle security management.
- Traceability reporting and calibration operations.

Every compliant TimeCard implementation SHALL provide at least one accessible control interface. This interface MAY be exposed through a physical baseboard connector, a host-exposed bus interface, or a network-based protocol suite.

---

## 8.2 Control Interface Classes

Control interfaces are categorized based on their communication topology and data granularity.

| Class | Description | Typical Use |
|--------|--------------|--------------|
| **Local Hardware Control** | Direct access via SMBus, I²C, I3C, or GPIO. | Baseboard-level configuration, power sequencing, or low-level telemetry by a BMC. |
| **Host-Integrated Control** | In-band access via PCIe MMIO or USB. | Runtime synchronization control by host OS software or drivers. |
| **Out-of-Band (OOB) Control** | NC-SI, IPMI, or dedicated serial interface. | Independent platform management regardless of the host OS state. |
| **Remote Network Control** | REST, gRPC, Redfish, or SNMP. | Distributed system orchestration or cloud-scale management. |

A TimeCard MAY implement one or more of these control classes simultaneously to support sophisticated datacenter abstraction models.

---

## 8.3 Minimum Functional Requirements

Where a control interface is implemented, it SHALL expose at least the following minimum common set of capabilities, restricted by the bandwidth and constraints of the specific medium:

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
- The address space and register map SHOULD be modeled consistently across compliant implementations to ease integration.
- Bus arbitration, clock stretching, and timing compliance SHALL follow the respective SMBus or MIPI I3C specifications.

### 8.4.2 PCIe Configuration and MMIO
- Allows in-band, high-speed access to TimeCard control registers directly from the host CPU.
- The register layout SHOULD comply with recognized industry standard memory maps (such as the OCP-TAP Control Register Map) where applicable.
- If the TimeCard supports PCIe Precision Time Measurement (PTM), the control interface SHALL present the necessary standard capability structures to the host to enable PTM negotiation.

### 8.4.3 IPMI / NC-SI
- Enables robust out-of-band control independent of the host processor or operating system.
- TimeCard devices establishing IPMI communication SHOULD implement an extended command set for time synchronization management (e.g., querying clock state, initiating reference failover).
- IPMI commands MAY support authenticated sessions utilizing pre-shared platform credentials.

### 8.4.4 REST / gRPC / SNMP / Redfish
- Used for high-level, network-based management and large-scale telemetry aggregation.
- REST, Redfish, and gRPC APIs SHOULD conform to established Open Management Schemas (OMS).
- SNMP implementations SHOULD expose standard OIDs for timing health, synchronization source, and hardware/firmware versions.

### 8.4.5 Serial and USB
- Serial (RS-232/RS-422/RS-485) interfaces SHOULD provide a human-readable command-line shell or SCPI-like syntax for localized debugging.
- USB connections MAY present as standardized Communications Device Class (CDC) / virtual COM ports to facilitate maintenance or localized firmware provisioning.

---

## 8.5 Control Register Structure

The logical control registers listed below represent the fundamental baseline for low-level interaction between the host/BMC and the TimeCard. While physical implementations differ (e.g., I2C addresses vs. PCIe MMIO offsets), the logical concepts SHALL be present:

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

All registers SHOULD adhere to consistent endianness and word alignment across a vendor's product line.

---

## 8.6 Security and Access Control

*Note: The requirements in this subclause apply conditionally. They are REQUIRED only for TimeCards marketed or designated for secure infrastructure deployments. For isolated or lab-grade physical environments, these features MAY be omitted to reduce complexity.*

Where security hardening is implemented, control interfaces operate as primary attack surfaces and require robust cryptographic protection.

### 8.6.1 Authentication and Authorization
- Networked control protocols SHALL support user or machine authentication.
- Privilege levels SHOULD distinguish between read-only monitoring access, operator configuration access, and administrator provisioning access.
- Access credentials and cryptographic keys SHOULD be stored securely within a hardware-backed enclave or discrete TPM.

### 8.6.2 Secure Firmware and Configuration
- Firmware payload images SHALL be digitally signed using verifiable certificates.
- A secure boot sequence SHOULD verify firmware integrity (cryptographic hash matches) at initialization before granting control to the TimeCard operating logic.

### 8.6.3 Network Security
- Remote IP-based interfaces (REST, Redfish, gRPC) SHOULD utilize encrypted transport layers (e.g., TLS).
- Replay and injection protection SHOULD be implemented for operations traversing shared networking environments.

---

## 8.7 Event and Telemetry Management

To facilitate continuous performance observability, the control interface SHOULD support structured event and telemetry generation.

### 8.7.1 Event Reporting
- Generated operational events SHALL include a local timestamp, a severity classification, and a source identifier.
- Critical events SHOULD include, but are not limited to: 
  - Reference loss (LOS)
  - Phase lock achieved or lost
  - Holdover entry or exit
  - Temperature threshold alarms
  - Firmware update success or failure.

### 8.7.2 Telemetry Streaming
- Continuous telemetry MAY be streamed via IPMI, REST, or gRPC for integration into centralized infrastructure dashboards.
- Telemetry generation rates SHALL be configurable by the administrator.
- Time synchronization statistics (such as ADEV or instantaneous phase offsets) SHOULD be strictly timestamped and aligned to the TimeCard's unified timescale.

### 8.7.3 Logging and Traceability
- Critical alarm logs SHOULD be preserved in non-volatile memory across power cycles.
- Exported log files MAY include cryptographic signatures to validate log integrity during forensic analysis.
- Traceability metadata (such as calibration constants and firmware build hashes) SHOULD be accessible to support operational compliance audits.

---

## 8.8 Interoperability and Extensions

All implemented control interfaces SHALL comply with the baseline schema defined by the overarching IEEE P3335 architecture. 

Manufacturers MAY implement proprietary extensions, custom registers, or vendor-specific telemetry strings. However, as an architectural objective, these optional extensions SHOULD NOT compromise or interfere with the baseline interoperability of the standardized registers and capabilities.

---

## 8.9 Summary

Control interfaces construct the necessary framework for secure, consistent, and vendor-neutral lifecycle management of TimeCard systems.

By standardizing configuration and telemetry logic, this framework facilitates the integration of diverse TimeCards into heterogeneous server fleets and telecommunications infrastructures. This architectural consistency promotes long-term maintainability, traceability, and operational reliability throughout the lifespan of precision time synchronization networks.

---

**End of Chapter – Control Interfaces**
