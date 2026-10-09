# vpc
resource "google_compute_network" "vpc_zt_lab" {
  name                    = "vpc-zt-lab"
  auto_create_subnetworks = false
}

# subnet-users
resource "google_compute_subnetwork" "subnet_users" {
  name          = "subnet-users"
  ip_cidr_range = "10.0.10.0/24"
  region        = "europe-west1"
  network       = google_compute_network.vpc_zt_lab.id
}

# subnet-servers
resource "google_compute_subnetwork" "subnet_servers" {
  name          = "subnet-servers"
  ip_cidr_range = "10.0.20.0/24"
  region        = "europe-west1"
  network       = google_compute_network.vpc_zt_lab.id
}

# subnet-mgmt
resource "google_compute_subnetwork" "subnet_mgmt" {
  name          = "subnet-mgmt"
  ip_cidr_range = "10.0.99.0/24"
  region        = "europe-west1"
  network       = google_compute_network.vpc_zt_lab.id
}

# subnet-attacker
resource "google_compute_subnetwork" "subnet_attacker" {
  name          = "subnet-attacker"
  ip_cidr_range = "192.168.1.0/24"
  region        = "europe-west1"
  network       = google_compute_network.vpc_zt_lab.id
}

# Cloud Router and NAT for outbound internet access for VMs without external IPs
resource "google_compute_router" "router" {
  name    = "zt-router"
  region  = "europe-west1"
  network = google_compute_network.vpc_zt_lab.id
}

resource "google_compute_router_nat" "nat" {
  name                               = "zt-nat"
  router                             = google_compute_router.router.name
  region                             = "europe-west1"
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
}
