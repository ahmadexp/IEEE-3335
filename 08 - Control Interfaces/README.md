# Control Interfaces (Normative)

This chapter defines the **control interfaces** used to configure, monitor, and manage TimeCard devices. Control interfaces provide the logical communication and operational management mechanisms necessary to ensure consistency, security, and interoperability across TimeCard implementations.

---

## 1 - Overview

Control interfaces form the **management plane** of the TimeCard architecture. Unlike timing interfaces, which operate within the data plane and deliver phase and frequency information, control interfaces are responsible for:
- Configuration of synchronization parameters
- Status monitoring and fault reporting
- Firmware and security management
- Calibration and traceability operations

Every TimeCard implementation **SHALL** provide at least one accessible control interface, either through a physical connector, a host-exposed interface, or a network-based protocol.

---

## 2 - Control Interface Classes

Control interfaces are categorized based on **communication scope** and **data granularity**:

| Class | Description | Typical Use |
|--------|--------------|--------------|
| **Local Hardware Control** | Direct access through SMBus, I²C, or GPIO. | Board-level configuration or telemetry. |
| **Host-Integrated Control** | In-band via PCIe or USB. | Runtime synchronization control by host software or drivers. |
| **Out-of-Band Control** | IPMI or serial interface. | Platform management independent of host OS. |
| **Remote Network Control** | REST, gRPC, or SNMP. | Distributed system or cloud management. |

A TimeCard **MAY** implement one or more of these control classes simultaneously, provided that concurrency and security are properly managed.

---

## 3 - Minimum Functional Requirements

All control interfaces **SHALL** expose a minimum common set of functionality:

| Function | Description |
|-----------|--------------|
| **Source Selection** | Select or prioritize active synchronization reference (GNSS, PTP, PPS, etc.). |
| **Mode Control** | Switch between locked, holdover, and free-running states. |
| **Clock Discipline Settings** | Adjust PLL or disciplining loop bandwidth and parameters. |
| **Telemetry Access** | Retrieve metrics such as frequency offset, temperature, phase error, and ADEV statistics. |
| **Alarm and Event Logs** | Report critical events such as loss of reference, GNSS failure, or firmware errors. |
| **Firmware Management** | Support update, rollback, and signature validation. |
| **Security Management** | Handle authentication, encryption, and access control. |

---

## 4 - Communication Protocols

### 4.1 - SMBus / I²C
- Provides low-speed configuration and sensor access.  
- **Address space** and **register map** SHALL be standardized across compliant implementations.  
- **Bus arbitration** and **timing compliance** SHALL follow SMBus 3.2 specification.  
- Typical use cases include reading oscillator telemetry and alarm flags.

### 4.2 - PCIe Configuration Registers
- Allows in-band access to TimeCard control registers directly from the host.  
- Register layout **SHALL** comply with the OCP-TAP Control Register Map.  
- **Capabilities:** enable/disable timing outputs, report PTM timestamps, and read clock state.  
- PCIe PTM extensions **MUST** be supported for timestamp correlation.

### 4.3 - IPMI
- Enables out-of-band control independent of host software.  
- TimeCard devices **SHOULD** implement an IPMI command set extension for time synchronization management (e.g., `GET_CLOCK_STATE`, `SET_REFERENCE_SOURCE`).  
- Commands **MUST** support authenticated sessions using platform credentials.

### 4.4 - REST / gRPC / SNMP
- Used for network-based management and telemetry aggregation.  
- REST and gRPC APIs **SHALL** conform to the OCP-TAP Open Management Schema (OMS).  
- SNMP **SHOULD** expose OIDs for timing health, synchronization source, and firmware version.  
- All remote communications **MUST** support TLS encryption and authentication tokens.

### 4.5 - Serial and USB
- Serial (RS-232/RS-422) interfaces **SHOULD** provide a command-line shell or SCPI-like control syntax.  
- USB connections **MAY** present as virtual COM ports for maintenance or firmware updates.  
- Firmware update procedures **MUST** include integrity verification before flashing.

---

## 5 - Control Register Structure

Control registers form the fundamental mechanism for low-level interaction between the host and the TimeCard.

| Register | Description | Access | Example Units |
|-----------|--------------|---------|----------------|
| `SYNC_SRC` | Active synchronization source ID | R/W | Enum |
| `PLL_STATE` | Locked / Holdover / Free | R | Boolean |
| `PHASE_ERR` | Instantaneous phase error | R | ns |
| `TEMP` | Oscillator temperature | R | °C |
| `MTIE_MAX` | Current holdover MTIE estimate | R | ns |
| `FIRMWARE_VER` | Firmware version string | R | ASCII |
| `UPDATE_CMD` | Trigger firmware update | W | Boolean |
| `SECURE_MODE` | Security enable flag | R/W | Boolean |

All registers **SHALL** have consistent endianness, alignment, and versioning per the OCP-TAP TimeCard Control Register Map (TCRM).

---

## 6 - Security and Access Control

Control interfaces represent potential attack surfaces; therefore, robust protection is **MANDATORY**.

### 6.1 - Authentication and Authorization
- All control protocols **MUST** support user authentication.  
- Privilege levels **SHALL** distinguish between read-only, operator, and administrator access.  
- Access credentials **MUST** be stored securely, preferably in a TPM or hardware security enclave.

### 6.2 - Secure Firmware and Configuration
- Firmware images **MUST** be digitally signed using vendor-issued certificates.  
- Secure boot **SHOULD** verify firmware integrity at initialization.  
- Configuration changes **MUST** be logged and cryptographically signed when remote.

### 6.3 - Encryption and Network Security
- Remote interfaces (REST, SNMP, gRPC) **MUST** use encrypted transport (TLS 1.3 or higher).  
- Session keys **SHALL** be refreshed periodically.  
- Replay and injection protection **MUST** be implemented for critical operations.

---

## 7 - Event and Telemetry Management

The control interface **SHOULD** support structured telemetry reporting for continuous monitoring.

### 7.1 - Event Reporting
- All events **SHALL** include a timestamp, severity, and source.  
- Events **MUST** include: Reference loss, Lock achieved/lost, Holdover entry/exit, Temperature alarm, and Firmware update success/failure.

### 7.2 - Telemetry Streaming
- Continuous telemetry **MAY** be streamed over IPMI, REST, or gRPC for real-time monitoring.  
- Sampling rate **SHALL** be configurable.  
- Time synchronization statistics **SHOULD** be timestamped and aligned to the unified timescale.

### 7.3 - Logging and Traceability
- Logs **MUST** be preserved across power cycles.  
- Exported logs **SHALL** include cryptographic signatures to ensure integrity.  
- Traceability to test conditions and firmware build **SHOULD** be maintained for certification purposes.

---

## 8 - Compliance and Interoperability

All control interfaces **SHALL** comply with the OCP-TAP and IEEE P3335 control schema.  
Optional extensions **MAY** be implemented, provided that they do not compromise baseline interoperability.  
Compliance testing **SHALL** verify register access, authentication, firmware update flow, and telemetry accuracy.

---

## 9 - Summary

Control interfaces are essential for secure, consistent, and vendor-neutral management of TimeCard systems.  
By standardizing control mechanisms, OCP-TAP ensures that all TimeCards—regardless of design origin—can be configured, monitored, and maintained uniformly across heterogeneous infrastructures.  
This guarantees long-term maintainability, traceability, and security compliance throughout the lifecycle of time synchronization systems.

---

**End of Chapter – Control Interfaces**

