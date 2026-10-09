# Historical unauthenticated baseline

This source demonstrates the original authorization weakness. It has no OIDC or route authorization. Credentials now come from DB_HOST, DB_NAME, DB_USER and DB_PASSWORD. Debug is disabled and direct launch binds loopback only. It is not the hardened app and must not be exposed as a public service.
