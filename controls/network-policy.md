# Recorded network controls

October 7 records five server ingress slices: priority 800 service allows and priority 850 internal denies. DB accepts web TCP 5432; Keycloak accepts web TCP 8080; web accepts Keycloak TCP 80, with its internal deny scoped to TCP; Wazuh permits four server agents TCP 1514/1515 and Keycloak dashboard TCP 443; AD initially permits Keycloak directory/DNS/Kerberos traffic. Broad `allow-internal-vpc` was disabled. These are ingress slices, not universal traffic isolation.

A separate attacker-specific priority 900 GCP deny covers the fixed eight-pair scan. Do not attribute that scan solely to the later service slices or to Tailscale.

October 8 inspected AD exception: both Keycloak 10.0.20.3/32 and web/router 10.0.20.2/32 allowed TCP 53/88/636 and UDP 53/88/389. This relaxes earlier web-to-AD isolation. Explicit Windows AD DNS later succeeded; default resolution/domain discovery remained unresolved. No frozen-scope repair is required.
