# PostgreSQL least privilege — October 7

The preserved applied transaction revoked known table/sequence grants and database/schema creation rights, then granted SELECT on employees, clients and configs to app_user. Supplied app-connection output reported reads of 6 employees, 5 clients and 1 configuration; UPDATE, DELETE, CREATE and TEMP probes returned SQLSTATE 42501. Exact execution time was not supplied for that output.

Later user-run assumed-web-host-access records report UPDATE/DELETE/DROP/CREATE failures, with a screenshot showing InsufficientPrivilege. No actual host compromise or pre-hardening write attack was demonstrated. The app still needs SELECT, so stolen application credentials can expose readable records. See the copied [SQL control](../controls/database-least-privilege.sql).
