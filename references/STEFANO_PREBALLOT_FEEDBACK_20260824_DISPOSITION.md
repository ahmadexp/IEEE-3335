# Stefano Pre-Ballot Feedback Disposition, August 24, 2026

Source reviewed: Feedback from Stefano on the unofficial IEEE P3335 draft, transcribed by the Chair.

All five technical points are addressed in the active manuscript sources. Because the changes clarify scope and add normative performance declarations, they remain draft candidate text until Working Group review.

## Action summary

| Area | Resolution |
|------|------------|
| Scope and deployment model | Clause 1.1 now distinguishes the core directly attached TimeCard application from optional upstream packet timing recovery and optional downstream network distribution. |
| Performance categories | Clause 5.7 now includes noise transfer and noise tolerance for applicable receive and providing interfaces. |
| Time-error terminology | Clause 6.3 and Clause 3 now use constant time error and dynamic time error consistently with the terminology of ITU-T Recommendation G.8260. |
| Reproducible declarations | Clause 6.4 defines required stimulus, measurement-point, operating-state, result, acceptance-criteria, and uncertainty content for noise transfer and noise tolerance. |
| Supporting guidance and tests | Annexes A and B explain the metrics and provide reproducible example procedures; the 6.11 documentation checklist includes both categories. |

## Detailed disposition

| ID | Comment topic | Disposition |
|----|---------------|-------------|
| ST-01 | State the primary local-reference application and optional PTP recovery and downstream distribution in 1.1. | Accepted with clarification. Clause 1.1 explicitly identifies direct attachment as the core application, a directly coupled local reference as the common deployment, and upstream packet recovery and downstream network distribution as optional functions. The text preserves the primary-reference and free-running implementation cases permitted by 5.3.4 rather than silently creating a new mandatory external receive interface. |
| ST-02 | Add noise transfer to the 5.7 performance categories. | Accepted. Clause 5.7 requires the category to be addressed from each synchronization receive interface to each applicable providing interface. |
| ST-03 | Add noise tolerance to the 5.7 performance categories. | Accepted. Clause 5.7 requires the category to be addressed for each receive interface used for synchronization. |
| ST-04 | Replace the final 6.3 reference to time jitter with time error, including constant and dynamic components. | Accepted. Clause 6.3 distinguishes constant time error and dynamic time error from phase noise, MTIE, TDEV, ADEV, noise transfer, and noise tolerance. Clause 6.4.1 requires separately estimated cTE and dTE components when the declared method permits separation. |
| ST-05 | Add noise transfer and noise tolerance under 6.4. | Accepted and expanded for testability. Clauses 6.4.2 and 6.4.3 define bounded, reproducible declaration content. Clause 6.11 and Annexes A and B carry those declarations into documentation and example testing. |

## Remaining action

AI-027 in `PUBLICATION_READINESS.md` tracks reviewer confirmation and Working Group ratification of this draft candidate text before official ballot.
