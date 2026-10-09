# Known hybrid architectural limitation — October 8

The Windows workstation reached the portal root (HTTP 200) and failed to connect to the actual DB endpoint 10.0.20.4: 5432. Later explicit DNS queries to AD 10.0.20.5 succeeded while default DNS-only/no-hosts LDAP SRV lookup timed out and forced DC discovery returned 1355. Secure-channel checks were false; successful current domain authentication was not established.

Supplied effective NRPT had no corp.local namespace, and hosts entries masked hostname lookup symptoms. SNAT through the shared web/router changes the source presented to GCP; inspected AD policy was expanded to admit 10.0.20.2 alongside Keycloak 10.0.20.3. This weakens earlier web-to-AD isolation. These resolver and routing observations do not prove a single complete causal chain or an inherent Tailscale defect.

Technical scope froze on October 8. Further Windows DNS/domain-continuity repair is future work, not a portfolio completion gate.
