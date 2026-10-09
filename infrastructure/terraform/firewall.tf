# Allow IAP access for SSH and RDP
# Google's IAP IP range is 35.235.240.0/20
resource "google_compute_firewall" "allow_iap" {
  name    = "allow-iap-ssh-rdp"
  network = google_compute_network.vpc_zt_lab.name

  allow {
    protocol = "tcp"
    ports    = ["22", "3389"]
  }

  source_ranges = ["35.235.240.0/20"]
  target_tags   = ["allow-iap"]
}

# Allow internal traffic within the VPC
# In a true Zero Trust model we would restrict this, but for Phase 1 baseline we allow it
resource "google_compute_firewall" "allow_internal" {
  name    = "allow-internal-vpc"
  network = google_compute_network.vpc_zt_lab.name

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
  }

  allow {
    protocol = "udp"
  }

  source_ranges = ["10.0.10.0/24", "10.0.20.0/24", "10.0.99.0/24", "192.168.1.0/24"]
}

# Explicitly deny internet inbound to everything else (default behavior, but good to codify)
