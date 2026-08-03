# Annex A: Metrics (Informative)

This annex summarizes timing and frequency metrics used by the normative performance declarations in Clause 6. The controlling definitions and calculation methods are those in the normative references cited by the applicable requirement. The environmental-sensitivity discussion in A.10 condenses concepts from IEEE Std 1193-2022 [3] for convenient application to TimeCards; IEEE Std 1193-2022 remains the controlling source where a normative requirement cites it.

## A.1 Metric selection

No single metric characterizes every aspect of a TimeCard. A useful declaration selects metrics according to the behavior being evaluated:

| Behavior | Common metric or result |
|----------|-------------------------|
| Offset from a reference timescale | Time error with a stated bound or statistic |
| Bounded time variation | MTIE |
| Stochastic time variation | TDEV |
| Fractional-frequency stability | ADEV or modified ADEV |
| Spectral purity of a periodic output | Phase noise |
| Short-term edge variation | A specifically defined time-jitter statistic |
| Reference-loss behavior | Time error or MTIE versus elapsed holdover time |

The metric name alone is insufficient. The measurement point, operating state, averaging or observation interval, bandwidth, environmental conditions, and uncertainty determine what a result means.

## A.2 Allan deviation

Allan deviation (ADEV) characterizes fractional-frequency stability as a function of averaging time $\tau$. For $N$ successive fractional-frequency averages $\bar{y}_i$ of duration $\tau$, the non-overlapping estimator is:

$$
\sigma_y(\tau) = \sqrt{\frac{1}{2(N-1)}\sum_{i=1}^{N-1}\left(\bar{y}_{i+1}-\bar{y}_i\right)^2}.
$$

Overlapping estimators use more of the available data and can provide better confidence, but the estimator, sampling interval, dead time, preprocessing, and confidence basis should be reported. ADEV values from different averaging intervals or estimator configurations are not directly interchangeable.

## A.3 Time deviation

Time deviation (TDEV) characterizes stochastic time variation as a function of averaging time. It is related to modified Allan deviation $\operatorname{mod}\sigma_y(\tau)$ by:

$$
\operatorname{TDEV}(\tau) = \frac{\tau}{\sqrt{3}}\operatorname{mod}\sigma_y(\tau).
$$

TDEV is useful when assessing time-transfer noise and wander. A report should identify the underlying time-error sequence, sampling interval, averaging factors, filtering, and treatment of gaps or outliers.

## A.4 Maximum time interval error

Maximum time interval error (MTIE) is the maximum peak-to-peak time-error variation in any observation window of duration $\tau$. For a time-error function $x(t)$ over the available record, it can be expressed as:

$$
\operatorname{MTIE}(\tau) = \max_{t_0}\left[\max_{t_0 \le t \le t_0+\tau}x(t)-\min_{t_0 \le t \le t_0+\tau}x(t)\right].
$$

MTIE is a worst-observed-window statistic. The total record length, sampling interval, treatment of missing data, and observation intervals should accompany a reported curve or limit.

## A.5 Phase noise

Single-sideband phase noise $\mathcal{L}(f)$ describes noise power in a 1 Hz bandwidth at offset frequency $f$ from a carrier, relative to carrier power, and is normally reported in dBc/Hz. A declaration should identify carrier frequency, offset-frequency range, resolution and measurement bandwidths, cross-correlation settings if used, instrument floor, and any spurs excluded from the noise trace.

Phase noise is a frequency-domain metric. It should not be substituted for a time-domain jitter, ADEV, TDEV, or MTIE result without a stated conversion method and integration limits.

## A.6 Time jitter

The word *jitter* has several domain-specific meanings. For a pulse or event stream, a TimeCard declaration should define:

- The ideal event model and any trend or deterministic component removed.
- The event or edge used as the measurement marker.
- Measurement bandwidth and observation interval.
- Sample count and handling of missing or invalid events.
- Statistic, such as RMS, standard deviation, peak-to-peak observed range, percentile, or bounded maximum.
- Whether fixed offset is included or removed.

Peak-to-peak observed range depends strongly on sample count and observation time. RMS and standard deviation are equivalent only under the stated centering convention. These details are therefore part of the metric definition.

## A.7 Accuracy, precision, resolution, and granularity

| Term | Use in this standard |
|------|----------------------|
| Accuracy | Qualitative closeness to a reference value; numerical claims are expressed using a defined error and uncertainty. |
| Precision | Closeness of agreement among repeated indications under stated conditions. |
| Resolution | Smallest change in a measured quantity that produces a perceptible change in indication. |
| Granularity | Smallest step representable by an encoding or interface. |

A fine timestamp granularity does not by itself imply equally fine resolution, precision, or accuracy.

These terms define P3335 performance-declaration semantics and are aligned with the corresponding measurement concepts used by IEEE Std 1588-2019 [4]. When an implementation claims an IEEE 1588 mapping, IEEE Std 1588-2019 governs the protocol fields and state-machine behavior, while the definitions in Clause 3 govern P3335 conformance and performance declarations. Under 4.7 and 7.3.3, an implementation-specific departure is identified in the conformance statement and is not represented as IEEE 1588 conformance.

P3335 uses *accuracy* qualitatively and requires a quantitative claim to be expressed as a defined error or uncertainty bound. An IEEE 1588 `clockAccuracy` value is a protocol encoding that is mapped to the applicable measured or declared range under 6.4. P3335 uses *precision* for repeatability, *resolution* for the smallest perceptible change in indication, and *granularity* for the smallest representable encoding step. These four terms are not interchangeable, and an IEEE 1588 timestamp field width or scaling does not, by itself, establish P3335 resolution, precision, or accuracy.

## A.8 Holdover time error

During holdover, time error can be represented conceptually as:

$$
x_H(t)=x_0+y_0t+\frac{1}{2}Dt^2+\int_0^t n_y(u)\,du,
$$

where $x_0$ is time error at holdover entry, $y_0$ is initial fractional-frequency offset, $D$ is a linear fractional-frequency drift rate, and $n_y$ represents residual frequency fluctuations. Temperature, aging, retrace, supply sensitivity, and the quality of the pre-holdover estimate can alter these terms.

A holdover declaration should therefore identify the prior lock duration and source, entry condition, elapsed holdover interval, temperature profile, initial error treatment, and behavior on reference restoration.

## A.9 Ensemble and correlation considerations

For $N$ independent sources with equal variance, ideal averaging reduces standard deviation by a factor of $\sqrt{N}$, giving an ensemble deviation proportional to $1/\sqrt{N}$. Real sources can share environmental, receiver, antenna, power, or network errors, so correlation reduces or eliminates that benefit.

An ensemble result should identify the source population, weighting or selection method, correlation assumptions, rejection criteria, and behavior as sources become unavailable or degraded.

## A.10 Environmental sensitivity

Common environmental sensitivity quantities include fractional-frequency change per degree of temperature, fractional-frequency change per unit acceleration, supply sensitivity, and aging rate. Reports should distinguish static sensitivity from transient response and should identify axis, stimulus frequency, rate of change, settling time, and hysteresis when relevant.

Concurrent logging of environmental quantities and timing error helps separate environmental sensitivity from reference or measurement-system noise.
