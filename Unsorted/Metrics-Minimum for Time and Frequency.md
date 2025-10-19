# **METRICS: TIME & FREQUENCY ACCURACY**

**MINIMUM ACCURACY**

DECEMBER 12, 2023 GREG ARMSTRONG RENESAS ELECTRONICS CORPORATION

![](_page_0_Picture_3.jpeg)

## **TIME & FREQUENCY ACCURACY**

### **MINIMUM FREQUENCY ACCURACY**

Highly recommend to follow ITU-T clock recommendations, specifically ITU-T G.812

- G.812 provides metric and targets for frequency accuracy, noise generation, noise tolerance and noise transfer
  - Can also be used for hold-over performance

For minimum frequency accuracy, recommend using Type III – also maps to OCP-TAP oscillator minimum recommendations

- Frequency accuracy: 4.6 × 10–6 (1 year)
- Noise Generation (recommend using both MTIE & TDEV for metrics)

| MTIE limit (ns)        | Observation interval τ<br>(s) |
|------------------------|-------------------------------|
| 40                     | $0.1 < \tau \le 1$            |
| $40 \times \tau^{0.4}$ | 1 < τ ≤ 10                    |
| 100                    | τ > 10                        |

| TDEV limit<br>(ns)       | Observation interval τ (s) |
|--------------------------|----------------------------|
| $3.2 \times \tau^{-0.5}$ | 0.1 < τ ≤ 2.5              |
| 2                        | 2.5 < τ ≤ 40               |
| $0.32\times\tau^{0.5}$   | 40 < τ ≤ 1000              |
| 10                       | τ > 1000                   |

- For noise transfer, recommend using a bandwidth of 0.001 Hz and maximum gain peaking of 0.2 dB
  - Again, allows reuse of metrics and performance targets from G.812
  - Existing test equipment that can be used to measure may place requirements at faceplate for measurement output (i.e. SMA (10MHz), ETH (SyncE), …)

## **TIME & FREQUENCY ACCURACY**

### **MINIMUM TIME ACCURACY**

The OCP-TAP Oscillator Workstream defined a Class G1 Oscillator Normative Specifications

• Target was to provide minimum 250ns (when locked to GNSS)

Recommend to follow IEEE 1588-2019 *clockAccuracy* for reporting accuracy

Recommend following ITU-T for time accuracy metrics

For minimum time accuracy:

| Value (hex) | Specification                         |
|-------------|---------------------------------------|
| 00 to 16    | Reserved                              |
| 17          | The time is accurate to within 1 ps   |
| 18          | The time is accurate to within 2.5 ps |
| 19          | The time is accurate to within 10 ps  |
| 1A          | The time is accurate to within 25 ps  |
| 1B          | The time is accurate to within 100 ps |
| 1C          | The time is accurate to within 250 ps |
| 1D          | The time is accurate to within 1 ns   |
|             |                                       |

- When locked to GNSS input source, recommend using wander generation from G.8272 but extending MTIE to 250 ns (i.e. OCP-TAP target)
  - Minimum time accuracy would be 0x22 (meaning accuracy range of 100 ns ~ 250 ns)

|      | 818 |
|------|-----|
| 0.25 | 818 |

- When locked to non-GNSS time sources, recommend using metric max|TE| (like ITU-T G.8273.x recommendations)
  - Minimum time accuracy would be 0x23 (meaning accuracy range of 250 ns ~ 1 μs)
  - Recommend defining max|TE| of 1 μs as a minimum
  - Metrics may want to also look at sub-components, cTE and dTE
  - Again, there is existing test equipment that can be used to measure max|TE|, cTE, dTE

![](_page_2_Picture_18.jpeg)

**Renesas.com**

![](_page_3_Picture_1.jpeg)