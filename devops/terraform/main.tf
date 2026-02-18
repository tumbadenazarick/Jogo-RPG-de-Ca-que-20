resource "local_file" "nexus_config" {
  content  = "nexus_enabled = true"
  filename = "${path.module}/nexus.cfg"
}
