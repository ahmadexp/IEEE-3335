# Annex E: Host Operating-System Integration (Informative)

## E.1 Purpose

This annex illustrates how the host-interface requirements in Clauses 5, 6, 8, and 9 can be applied on Windows, macOS, and Linux. It does not define an operating-system API, driver package, entitlement, device path, or command number, and it does not add to the conformance requirements.

The portable boundary is the P3335 discovery descriptor, baseline information model, mapping version, instance identity, host-time correlation record, lifecycle behavior, and time-control ownership. Operating-system mechanisms bind to that boundary. The Open Compute Project Time Appliances Project driver implementations provide useful implementation experience [B20].

## E.2 Portable driver architecture

A portable host stack can be divided into four layers:

1. The operating system enumerates the PCIe function and assigns resources.
2. A privileged driver validates the P3335 discovery descriptor, bounds-checks resources, and owns hardware access.
3. A versioned host API exposes P3335 objects, events, and bounded time operations without exposing arbitrary MMIO to applications.
4. Optional services perform oscillator discipline, host-clock integration, monitoring, or firmware maintenance under explicit authorization and time-control ownership.

This separation keeps board profiles, register layouts, interrupt handling, and power transitions inside the component that can validate them. Applications consume stable semantic objects and can remain portable even when the operating-system transport differs.

### E.2.1 Discovery and identity

The driver should obtain system-assigned PCI resources before reading the descriptor. It should validate the descriptor signature, version, lengths, generation, BAR bounds, resource spans, and capability indications before mapping or accessing an optional block.

One physical card can appear under a different enumeration index after reboot, removal, or inventory change. Configuration, calibration, and service selection should use `TC_INSTANCE_ID`, or `TC_SERIAL` when a persistent serial number is available. A device path can be retained as a secondary mapping-scoped selector, but its stability scope should be stated.

### E.2.2 API and ABI boundary

A binary host API should use transport-enforced exact lengths or explicit structure lengths and versions. New fields are most safely appended, reserved fields remain zero, and unknown optional trailing fields are ignored only when the mapping declares that behavior. Read responses containing optional telemetry should preserve field-level validity instead of turning an absent field into a plausible zero.

Read-only monitoring and timing-affecting operations should be separate in both API access rights and user experience. Raw register access is useful for controlled engineering diagnostics but should not be the interoperability interface or an ordinary application privilege.

### E.2.3 Time and discipline services

A host-time correlation should retain the two host bounds rather than only a derived midpoint. The correlation window, sample age, clock identity, timescales, card state, source validity, discontinuity generation, and uncertainty or dispersion policy are needed to decide whether the sample is suitable for host-clock discipline.

A background discipline service, command-line utility, monitoring application, and host time provider can otherwise compete for the same hardware. One component should own timing-affecting operations at a time, while read-only clients continue to observe state. Loss of the owner should lead to a bounded and observable ownership transition.

## E.3 Windows considerations

Windows PCIe integration can use a Windows Driver Framework function driver to receive system-assigned resources and participate in Plug and Play and power transitions [B27]. The working-state entry, working-state exit, hardware-release, orderly-removal, and surprise-removal paths are natural points to start or stop interrupts, queues, polling, and MMIO access.

A versioned device interface or I/O control ABI can map driver operations to the P3335 objects. Read and write access masks can separate monitoring from time setting, discipline, configuration, and firmware update. The driver can expose one interface per TimeCard instance while retaining `TC_INSTANCE_ID` as the durable selection key.

Windows host-clock representations can differ from the card epoch and timescale. The driver or service should either normalize both timestamps into the P3335 `timestamp` representation or declare the host representation and conversion without losing the original correlation bounds.

Windows Time Service supports pluggable time providers that can obtain samples from hardware or software sources [B28]. A TimeCard provider should submit only samples that are discipline-eligible under 8.10.4. A Windows system-time jump, service restart, or card removal should invalidate older associations before another sample is offered.

Driver signing, package installation, service accounts, protected local interprocess communication, and production-release policy remain platform and deployment concerns. They should be recorded in the conformance statement when they affect availability, authorization, or the evaluated configuration.

## E.4 macOS considerations

DriverKit provides user-space driver infrastructure, and PCIDriverKit provides access to custom PCI and PCIe hardware [B29], [B30]. A macOS implementation can package a DriverKit system extension with a host application and expose a versioned user-client API to authorized applications.

The DriverKit extension should validate the PCI identity, system-assigned BAR length, P3335 descriptor, and resource ranges before MMIO access. The user-client method dispatch can enforce exact input and output sizes, while the shared ABI preserves the same P3335 object semantics used on other operating systems.

A read-only control application can enumerate multiple driver services, select by `TC_INSTANCE_ID`, and display only fields marked valid. Driver activation, user-client authorization, and application signing are separate from the TimeCard information model and are best documented as platform bindings rather than encoded into the normative object vocabulary.

When macOS realtime readings bracket a card read, the mapping should identify that host clock and preserve both readings. Raw card time should remain labeled with its actual or unknown timescale until a trusted card-to-host timescale relationship and leap correction are available.

Sleep, wake, extension replacement, host-app removal, Thunderbolt or other tunneled-PCIe disconnection, and reconnection should be included in physical validation. Reconnection should produce a new discovery validation and discontinuity generation before time-control operations resume.

## E.5 Linux considerations

The Linux PTP clock infrastructure provides a standard PHC abstraction and user-space clock operations [B31]. A Linux driver can map P3335 clock access to a PHC while exposing control, telemetry, events, and the discovery descriptor through documented kernel interfaces.

A `/dev/ptpN` number is an enumeration result and should not replace `TC_INSTANCE_ID` or `TC_SERIAL` in persistent configuration. Sysfs names, device nodes, and PCI paths can be useful secondary selectors when their stability scope is understood.

Linux cross-timestamp facilities can bind to `HOST_TIME_CORRELATION` by preserving the host clock identifier, bounds or measured interval, card timestamp, and uncertainty information. User-space tools should verify timescale and state before using a PHC to discipline the system clock.

Runtime power management, driver unbind and rebind, PCIe error recovery, hot plug, and host reboot should follow the same lifecycle rules as other platforms. Re-probing a known device identity does not remove the need to revalidate the active image and resource descriptor.

## E.6 Cross-platform mapping summary

| P3335 concept | Windows example | macOS example | Linux example |
|---------------|-----------------|---------------|---------------|
| PCIe discovery | Framework-assigned resources plus validated descriptor | PCIDriverKit provider plus validated descriptor | PCI core resources plus validated descriptor |
| Instance selection | Device interface plus `TC_INSTANCE_ID` | Driver service plus `TC_INSTANCE_ID` | PHC or PCI path plus `TC_INSTANCE_ID` |
| Binary interface | Versioned device interface or I/O control ABI | Versioned DriverKit user-client ABI | Kernel API, ioctl, netlink, sysfs, or documented combination |
| Card time | Driver clock operation | DriverKit user-client clock operation | PHC operation |
| Host-time correlation | Bracketed host clock and card reading | Bracketed host clock and card reading | PTP cross-timestamp facility or equivalent |
| Host discipline | Eligible sample supplied to a Windows time provider | Privileged service using eligible samples | `phc2sys`-style service or equivalent |
| Time-control ownership | Driver or service lease | User-client or service claim | Kernel or daemon arbitration |
| Lifecycle | Plug and Play and power callbacks | DriverKit and system-extension lifecycle | PCI probe, remove, power-management, and error-recovery paths |

## E.7 Integration review checklist

Before a platform binding is used for a performance or conformance claim, an integrator should confirm:

- The exact hardware, firmware or gateware, driver, service, API or ABI, and operating-system revisions.
- Descriptor validation and fail-closed handling of unknown or ambiguous optional resources.
- Stable per-card selection and separation of per-card calibration and configuration.
- Atomic TimeCard reads and bounded host-time correlations with explicit timescales.
- Rejection of stale, discontinuous, source-invalid, or excessive-window discipline samples.
- Single-owner behavior for time setting and discipline.
- Bounded cancellation and resource revalidation through supported lifecycle transitions.
- Least-privilege separation of monitoring, time control, configuration, update, and security administration.
- Physical-card validation coverage for every claimed board profile and host connection type.
