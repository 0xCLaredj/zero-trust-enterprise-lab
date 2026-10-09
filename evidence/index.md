# Evidence index

| Result | Source and date | Public artifact | Limits |
|---|---|---|---|
| Employee/admin RBAC | October 7 browser and journal records, proxy/native VPC source 10.0.20.3 | [RBAC](rbac.md) | Observed accounts/routes, not all authorization paths |
| Eight TCP pairs open to filtered | October 7 Nmap, attacker 192.168.1.2, native VPC | [Network](network.md), [scan extracts](scans/) | Fixed matrix and targeted GCP deny |
| SQL least privilege | October 7 app-credential outputs and applied SQL | [Database](database.md) | Reads remain possible; some supplied results have no timestamp |
| Five correlated manager alerts | October 7 source and manager timestamps | [Wazuh](wazuh.md) | Descriptive sample, not a detection rate or containment latency |
| Synthetic active response and LDAPS | Recorded October 7 user-run campaign | [Later campaigns](later-campaigns.md) | Full raw traces not preserved in public package |
| Hybrid boundary | October 8 Windows and inspected configuration records | [Hybrid](hybrid.md) | Domain continuity unresolved; scope frozen |

Local offline checks of the portfolio code are separate from these historical lab results. No historical result is relabeled as a fresh test of the cleaned app.
