# Infrastructure provenance

The sole Terraform root is [`terraform/`](terraform/). Its required project_id variable is supplied locally via the example tfvars. No state, real tfvars, credentials or provider cache is included.

This is the historical baseline infrastructure, including the intentionally broad allow-internal-vpc rule. It is **not** a codification of the final hardened live policy. The copied compute configuration declares terminated instance status. No terraform apply, live drift reconciliation or clean-room cloud reproduction was performed from this package.

Recorded hardened ingress controls and the October 8 AD exception are summarized in [network-policy.md](../controls/network-policy.md). Do not apply baseline Terraform against the hardened lab as a synchronization step. Format/validation checks are local source checks only; any future apply needs a reviewed plan and an isolated project.

Local checks on October 8: Terraform formatting and `terraform validate` passed with the existing Google 5.45.2 provider and backend disabled. The local mirror initialization reported the provider as unauthenticated; these checks do not establish provider provenance, live drift or cloud reproduction. No plan/apply was run.
