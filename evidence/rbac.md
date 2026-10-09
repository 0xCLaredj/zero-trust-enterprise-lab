# RBAC — October 7, 2026

Source: preserved manual RBAC observations and evening business-flow records; browser traffic via the Keycloak/IAP proxy into the native VPC. Before loading the role guard, the employee session reached /admin with HTTP 200 (14: 12: 33 UTC). After restart, the journal recorded /admin 403 at 14: 14: 45 and /employee 200 at 14: 16: 29. The authorized-admin positive case returned /admin 200 at 14: 26: 35; direct portal-admin assignment was captured.

The evening journal corroborated employee /employee 200 at 19: 55: 10 and /admin 403 at 19: 56: 19, plus authorized-admin /admin 200 at 20: 00: 10. The observed browser OTP path is separate from a complete audit of alternate/recovery flows.
