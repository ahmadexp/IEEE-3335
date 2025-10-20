This appendix provides example workflows, command snippets, and pseudo-scripts to facilitate repeatable testing and automation of TimeCard devices.
All commands and examples are illustrative; implementers may substitute equivalent utilities or frameworks as appropriate.

A.1 Environment Setup and Prerequisites

Host Requirements:

Linux kernel 6.0 or later (PTP/PTM support enabled)

Root or elevated permissions for hardware access

Installed packages:

sudo apt install linuxptp hwclock i2c-tools lm-sensors python3-numpy python3-matplotlib


Instrument Connectivity:

SCPI-capable phase noise analyzer and time-interval counter connected via USB or LAN

Serial, USB, or network access to TimeCard management interface

A.2 Basic TimeCard Discovery and Initialization
1. PCIe Bus Enumeration
lspci | grep -i time
# Example output:
# 02:00.0 Precision TimeCard Controller: Turba Inc. Model TC-100 (rev 01)

2. Read PCIe PTM Capability (if supported)
sudo lspci -vvv -s 02:00.0 | grep -A5 "PTM"

3. I²C/SMBus Telemetry (for power, temperature, oscillator status)
sudo i2cdetect -y 1
sudo i2cget -y 1 0x68 0x10 w  # Example register read for oscillator status

A.3 GNSS Receiver Validation
1. GNSS Lock Detection
sudo cat /dev/ttyACM0 | grep -E "GPGGA|GPRMC"
# Look for valid fix (GGA with nonzero quality) and UTC time output.

2. PPS Verification
sudo ppstest /dev/pps0
# Observe timestamps and verify steady 1 Hz output, <50 ns jitter preferred.

3. GNSS Lock/Unlock Cycle
# Simulate antenna disconnect
sudo ip link set eth0 down   # If GNSS via network-fed PTP
# Or physically disconnect antenna


Monitor TimeCard telemetry for “Holdover” state transition:

sudo i2cget -y 1 0x68 0x22
# Expected: Bit flag changes from LOCKED (0x01) to HOLDOVER (0x02)

A.4 PTP/PTM Host Synchronization
1. Enable PTP Service
sudo systemctl stop chronyd
sudo ptp4l -i enp5s0f0 -m -S -2 &

2. Query Offset and Delay Statistics
phc2sys -s CLOCK_REALTIME -c /dev/ptp0 -O 0 -m
# Observe phase offset convergence to <100 ns steady-state.

3. PTM Measurement (PCIe Time Measurement)
sudo cat /sys/kernel/debug/ptm/ptm_report
# Example fields: Local_Timestamp, Remote_Timestamp, Delta_ps

A.5 PPS and 10 MHz Phase Alignment Measurement
1. Using Time Interval Counter (SCPI)
# Measure PPS-to-PPS offset between two TimeCards
:MEAS:TINT? CH1,CH2
# Repeat 1e6 times and compute mean ± RMS jitter

2. Using Oscilloscope (Python/SCPI Automation)
import pyvisa, numpy as np
rm = pyvisa.ResourceManager()
scope = rm.open_resource('TCPIP0::192.168.1.100::inst0::INSTR')
scope.write(":ACQ:MODE SAM")
scope.write(":MEAS:DEL? CH1,CH2")
delay = float(scope.read())
print(f"PPS phase offset = {delay*1e9:.2f} ns")

3. Continuous Logging
for i in {1..10000}; do
  echo "$(date +%s),$(sudo cat /sys/class/pps/pps0/assert)"
  sleep 1
done > pps_log.csv

A.6 Frequency Stability (ADEV/TDEV) Analysis
1. Collect Frequency Samples
sudo chronyc tracking | grep "Last offset"
# Or capture oscillator output using counter and export timestamps.

2. Compute ADEV using Python
import allantools as at, numpy as np
data = np.loadtxt("freq_data.txt")
tau, adev, adev_err, _ = at.adev(data, rate=1.0, data_type='freq')
for t,a in zip(tau, adev):
    print(f"{t:.1f} s : {a:.3e}")

A.7 Holdover and MTIE Testing
1. Enter Holdover

Disconnect all references (GNSS/PTP). Wait for status flag:

sudo i2cget -y 1 0x68 0x22  # HOLDOVER = 0x02

2. Log Phase Deviation Over Time
while true; do
  echo "$(date +%s),$(sudo phc_ctl /dev/ptp0 get | grep 'offset')"
  sleep 60
done > holdover_phase.csv

3. Compute MTIE (ITU-T G.8260)
import allantools as at
phase = np.loadtxt("holdover_phase.csv", delimiter=",")[:,1]
tau, mtie = at.mtie(phase, rate=1)

A.8 Ensemble Reference Validation
1. Configure Dual References

Reference A: GNSS PPS

Reference B: PTP Grandmaster

2. Apply Offset and Observe Convergence
sudo ptp4l -i enp5s0f1 -m -S -2 --offset 100ns &
# Monitor ensemble source weights:
sudo i2cget -y 1 0x68 0x40 w


Expected: Ensemble output converges within nominal stability (<20 ns) after re-weighting.

A.9 Management Telemetry via REST/gRPC
Example REST Query
curl -X GET http://192.168.1.10:8080/api/v1/timecard/status
# Returns:
# {
#   "sync_source": "GNSS",
#   "lock_state": "LOCKED",
#   "discipline_mode": "AUTO",
#   "phase_offset_ns": 0.7,
#   "temperature_C": 42.3,
#   "firmware_version": "1.2.3"
# }

Example gRPC Client (Python)
import grpc, timecard_pb2, timecard_pb2_grpc
channel = grpc.insecure_channel('192.168.1.10:50051')
stub = timecard_pb2_grpc.TimeCardStub(channel)
status = stub.GetStatus(timecard_pb2.StatusRequest())
print(status)

A.10 Automated Regression Example (Shell)

A minimal nightly validation loop for CI/CD environments:

#!/bin/bash
LOG=nightly_test_$(date +%F).log
echo "=== TimeCard Nightly Test ===" > $LOG

# GNSS lock test
gnss_fix=$(grep -c "GPGGA" /dev/ttyACM0)
[[ $gnss_fix -gt 0 ]] && echo "GNSS OK" >> $LOG || echo "GNSS FAIL" >> $LOG

# PPS jitter check
rms=$(sudo ppstest /dev/pps0 | awk '{sum+=$7; n++} END {print sqrt(sum/n)}')
echo "PPS RMS jitter: $rms ns" >> $LOG

# ADEV computation
python3 compute_adev.py >> $LOG

# Push logs to CI server
scp $LOG ci@lab-server:/results/

A.11 Example Lab Instrument SCPI Summary
Function	Example SCPI Command	Notes
Start measurement	:INIT:IMM	Begins immediate measurement
Read time interval	:MEAS:TINT? CH1,CH2	Returns time delta in seconds
Measure frequency	:MEAS:FREQ? CH1	Frequency in Hz
Get phase noise	:CALC:MARK1:Y?	Read marker value (dBc/Hz)
Reset	*RST	Reset instrument
Identify	*IDN?	Device identity
A.12 Data Normalization and Reporting

After measurements:

Convert all timestamps to TAI or UTC reference.

Store results in JSON/CSV format:

{
  "device": "Turba TC-100",
  "firmware": "1.2.3",
  "ADEV": {"tau_s": [1,10,100], "adev": [1e-10, 2e-11, 6e-12]},
  "Holdover_MTIE_ns": 150,
  "PPS_Jitter_ns": 0.8
}


Use a unified schema across all test runs for easy ingestion by dashboards (Grafana, Elastic, etc.).

Publish datasets to OCP TAP Interoperability Database (recommended format: CSV + metadata JSON).

A.13 Suggested Automation Frameworks
Framework	Use Case	Integration Example
Robot Framework	Structured regression suites	robot --variable HOST:192.168.1.10 tests/
PyTest	Unit-level API validation	pytest tests/test_timecard_api.py
Jenkins/GitLab CI	Continuous integration	Nightly ADEV, jitter, holdover tests
Prometheus + Grafana	Live telemetry visualization	REST scraping of /status endpoints
Ansible	Multi-device orchestration	Apply config and collect logs from multiple hosts
A.14 Summary

This appendix provides practical command-line and scripting examples to support consistent, traceable, and automatable testing of TimeCard devices.
By leveraging standard Linux utilities, SCPI-capable instruments, and open-source analysis tools, laboratories and vendors can ensure that all performance metrics—ADEV, MTIE, PN, jitter, and alignment—are reproducible and comparable across implementations.
These procedures form the backbone of OCP-TAP continuous conformance verification, ensuring ongoing interoperability, transparency, and confidence in the TimeCard ecosystem.
