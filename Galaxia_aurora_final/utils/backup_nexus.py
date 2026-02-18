import os
import shutil
import time
import zipfile

class BackupNexus:
    """
    Sistema de Backup e Restauração de Emergência para o Lord Eclipse.
    Garante que nenhuma modificação seja permanente se causar falhas.
    """
    def __init__(self, raiz=".", pasta_backups="backups_emergencia"):
        self.raiz = raiz
        self.pasta_backups = pasta_backups
        if not os.path.exists(pasta_backups):
            os.makedirs(pasta_backups)

    def criar_snapshot(self, motivo="Backup Manual"):
        """Cria um arquivo ZIP com todo o estado atual do código."""
        timestamp = int(time.time())
        nome_arquivo = f"SNAPSHOT_{timestamp}.zip"
        caminho_zip = os.path.join(self.pasta_backups, nome_arquivo)

        with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.raiz):
                if self.pasta_backups in root or ".git" in root:
                    continue
                for file in files:
                    zipf.write(os.path.join(root, file))

        print(f"📦 [BACKUP]: Snapshot criado com sucesso: {caminho_zip}")
        print(f"📄 Motivo: {motivo}")
        return caminho_zip

    def restaurar_snapshot(self, nome_zip):
        """Restaura o código para o estado de um snapshot específico."""
        caminho_zip = os.path.join(self.pasta_backups, nome_zip)
        if not os.path.exists(caminho_zip):
            print(f"❌ [ERRO]: Snapshot {nome_zip} não encontrado.")
            return False

        print(f"⚠️ [RESTAURAÇÃO]: Restaurando sistema... Isto sobrescreverá arquivos atuais.")
        with zipfile.ZipFile(caminho_zip, 'r') as zipf:
            zipf.extractall(self.raiz)

        print(f"✅ [SUCESSO]: Sistema restaurado para o ponto {nome_zip}")
        return True

if __name__ == "__main__":
    backup = BackupNexus()
    backup.criar_snapshot("Snapshot Inicial de Segurança")
