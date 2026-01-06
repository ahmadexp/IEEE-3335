# Performance Metrics (Normative)

This clause defines the performance reporting and characterization requirements for TimeCard implementations. The intent is to enable measurable, transparent, and comparable timing behavior across vendors. Performance metrics shall be reported in vendor documentation. 

---

## 6.1 Overview

TimeCard performance must quantify the precision, stability, and accuracy with which the device maintains and delivers time and / or frequency in a contect aligned with the performance requirements of the intend application/

Performance metrics for the oscillator/s utilized within the Timecard shall be provided. These shall include frequency accuracy and temperature stability.

Performance metrics applicable for the characterization of the operation within the applicable use case should be provided. Those metrics should be characterized under both locked (synchronized/syntonized) and holdover operating conditions.

Manufacturers may report the following metrics:
- Frequency stability (ADEV, TDEV)
- Maximum Time Interval Error (MTIE)
- Phase noise (PN)
- Jitter and alignment (PPS and ToD)
- Accuracy and drift relative to reference
- Holdover behavior
- Environmental sensitivity (to temperature, voltage, vibration)

All measurements shall be made by testing equipement traceabke to the relevant standards, such as UTC(NIST), and conform to relevant methodologies e.g. ITU-T G.810/G.8260.
