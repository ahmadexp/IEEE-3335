# P3335 Performance specifications: A start

Doug Arnold

2024-02-16

## Time Accuracy

- Required specifications
  - Identify source of standard time, e.g. GPS
  - Time accuracy to source (e.g. GPS system time)
    - For "Maximum" error specify percentage of time error is less than the stated value, e.g. 99%
    - Stated error shall include static error and dynamic error
  - Measurement point (e.g. 1PPS output)
  - Valid temperate range
  - Minimum necessary lock time interval to be in spec
- Optional specifications
  - Maximum transient error
  - RMS error (shall include static and dynamic error)
  - Maximum and/or RMS error to UTC or TAI (must include published estimate of maximum error from time source to UTC or TA)
  - Maximum and/or RMS disagreement among same model timecards

## Time Precision/stability

- Required specifications
  - MTIE, including averaging time(s)
  - Measurement point (e.g. 1PPS output)
  - Valid temperate range
  - Minimum necessary lock time interval to be in spec
- Optional specifications
  - TDEV, including averaging time(s)
  - Phase noise

## Frequency Precision/stability

- Optional specifications
  - Double sideband spectral density as a function of deviation from the carrier frequency in dBc/Hz
  - Measurement point (e.g. 10 MHz output)
  - Valid temperate range
- For both time and frequency domain performance specifications the term jitter shall not be used
  - This is due to jitter having multiple definitions in common use

## Holdover

- Required specifications
  - Minimum time interval that output does not exceed error threshold
  - Error threshold
  - Measurement point (e.g. 1PPS output)
  - Valid temperate range
  - Minimum necessary lock time interval prior to holdover to be in spec
- Optional specification
  - RMS holdover time interval