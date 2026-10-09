# S 04 fixed TCP matrix — October 7, 2026

Native GCP VPC source: vm-attacker, 192.168.1.2. Nmap 7.80 used -sT -Pn -n --reason --max-retries 1 --host-timeout 30 s. Start before 14: 35: 41 UTC; after 14: 38: 24 UTC. Targeted rule deny-s 04-attacker-services: ingress priority 900, source 192.168.1.2/32, listed TCP ports denied, logging enabled.

| Target | TCP ports | Before | After |
|---|---|---|---|
| 10.0.20.2 | 80 | open | filtered |
| 10.0.20.3 | 8080 | open | filtered |
| 10.0.20.4 | 5432 | open | filtered |
| 10.0.20.5 | 53, 88, 389, 445, 3389 | all open | all filtered |

8/8 open became 0/8 open, 8/8 filtered. This does not prove a compromise, all-port isolation, Tailscale enforcement or Wazuh receipt of GCP deny logs. Machine-readable extracts preserve the source XML scan timestamps and port states.
