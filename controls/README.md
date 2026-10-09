# Control provenance

- `database-least-privilege.sql`: copied from the preserved October 7 applied transaction; scoped to the lab database and known tables/sequences. PUBLIC revocations affect other roles depending on those grants. This is not a migration for arbitrary databases.
- `wazuh-portal-rule.xml`: reconstructed reference matching recorded rule 100510 semantics, not a byte-for-byte manager export.
- `wazuh-reference-fragments.xml`: documented collection/response settings and recorded shared-source exclusions. One response block is shown for clarity; the last inspected live configuration still had two identical response blocks. No duplicate cleanup was applied.
- `network-policy.md`: recorded policy summary, not a deployable live export.

The active-response demonstration used an injected synthetic event. Expiry and client-specific containment behind proxies/SNAT remain unverified. Shared-source exclusions preserve a business path at the cost of blocking less broadly. Validate fragments offline/on a separate authorized environment before use; do not replace an entire manager configuration with these examples.
