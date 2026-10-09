# Flask source and provenance

`app.py` is a portfolio adaptation of the historical `app_oidc_update.py`, with environment configuration, a fail-closed `portal-admin` guard, session expiry, JSON audit output and debug disabled. It is not the exact October 8 deployed source export. Recorded lab results refer to the deployed application, not a deployment of this cleaned adaptation.

Install `requirements.lock.txt` in a local virtual environment, export the variables listed in `../config/.env.example`, then run `python app.py`. Direct launch binds 127.0.0.1: 5000. Register the corresponding `/callback` URI on a confidential Keycloak client. HTTPS is the default cookie setting; isolated loopback HTTP requires `LAB_HTTP_ONLY=1`.

Configure Keycloak to include the realm `portal-admin` role in the **validated ID token** under `realm_access.roles`. Missing or malformed claims deny administrator access. Browser OTP is a Keycloak flow setting; this source alone does not prove every login/recovery path enforces MFA.

Logout clears the local Flask session only; global Keycloak logout is not reproduced in this adaptation. Audit JSON is emitted to the application logger; collect it into a JSON-only file before using the provided Wazuh collection fragment. Proxy source attribution and HTTPS deployment need explicit configuration. No production-readiness or fresh cloud end-to-end test is claimed.

`baseline/` contains the intentionally unauthenticated original lab source with credentials removed. It is separately labeled and binds loopback only.
