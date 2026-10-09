# =============================================================================
# ALL VMs are created in STOPPED state (desired_status = "TERMINATED")
# This means: disk cost only (~$0.04/GB/month), NO compute cost.
# Start them with: gcloud compute instances start VM_NAME --zone=europe-west1-b
# =============================================================================

# 1. Active Directory Domain Controller (Windows Server 2022)
resource "google_compute_instance" "vm_ad" {
  name         = "vm-ad"
  machine_type = "e2-medium"
  zone         = "europe-west1-b"
  # desired_status added after creation to stop the VM
  desired_status = "TERMINATED"

  boot_disk {
    initialize_params {
      image = "windows-cloud/windows-2022"
      size  = 50
      type  = "pd-ssd"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_servers.id
  }

  tags = ["allow-iap"]
}

# NOTE: vm-sysmon runs LOCALLY on VMware Workstation (Windows 10 Pro),
# connected to GCP via Tailscale VPN. No GCP instance needed.

# 3. Web Server (Ubuntu 22.04)
resource "google_compute_instance" "vm_web" {
  name           = "vm-web"
  machine_type   = "e2-micro"
  zone           = "europe-west1-b"
  desired_status = "TERMINATED"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 20
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_servers.id
  }

  tags = ["allow-iap"]
}

# 4. Database Server (Ubuntu 22.04)
resource "google_compute_instance" "vm_db" {
  name           = "vm-db"
  machine_type   = "e2-micro"
  zone           = "europe-west1-b"
  desired_status = "TERMINATED"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 20
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_servers.id
  }

  tags = ["allow-iap"]
}

# 5. Keycloak Server (Ubuntu 22.04)
resource "google_compute_instance" "vm_keycloak" {
  name           = "vm-keycloak"
  machine_type   = "e2-medium"
  zone           = "europe-west1-b"
  desired_status = "TERMINATED"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 20
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_servers.id
  }

  tags = ["allow-iap"]
}

# 6. Wazuh / SIEM (Ubuntu 22.04)
resource "google_compute_instance" "vm_wazuh" {
  name           = "vm-wazuh"
  machine_type   = "e2-standard-2"
  zone           = "europe-west1-b"
  desired_status = "TERMINATED"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 50
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_mgmt.id
  }

  tags = ["allow-iap"]
}

# 7. GCP attacker VM (Debian 11 boot image; offensive tools are configured separately)
# NOT a Spot instance anymore so it can be stopped/started on demand
resource "google_compute_instance" "vm_attacker" {
  name           = "vm-attacker"
  machine_type   = "e2-medium"
  zone           = "europe-west1-b"
  desired_status = "TERMINATED"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 20
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_attacker.id
  }

  tags = ["allow-iap"]
}
