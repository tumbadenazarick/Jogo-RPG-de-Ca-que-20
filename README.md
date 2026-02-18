# Jogo-RPG-de-Ca-que-20  provider "google" {
  project = var.project_id
  region  = "us-central1"
  # O Terraform busca automaticamente a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS
}
resource "google_compute_instance" "exercito_eclipse" {
  # Aqui expandimos o código para 1.000 unidades
  count = 1000 

  name         = "unidade-combatente-${count.index}"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
  }

  # Atributos de "Poder" (Metadata)
  metadata = {
    nivel_de_força = "Alpha"
    lealdade       = "Lord Eclipse"
  }
}
- name: Google Auth
  uses: 'google-github-actions/auth@v2'
  with:
    credentials_json: '${{ secrets.GCP_SA_KEY }}'
