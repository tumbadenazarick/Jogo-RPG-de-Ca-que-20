import os
import shutil
import time

class GerenciadorQuarentena:
    """
    Sistema avançado para isolar códigos defeituosos, repetidos ou
    com falhas sem apagar o sistema original.
    """
    def __init__(self, pasta_quarentena="quarentena"):
        self.pasta_quarentena = pasta_quarentena
        if not os.path.exists(pasta_quarentena):
            os.makedirs(pasta_quarentena)

    def isolar(self, caminho_arquivo, motivo="Falha detectada"):
        if not os.path.exists(caminho_arquivo):
            return False, "Arquivo não encontrado."

        nome_base = os.path.basename(caminho_arquivo)
        timestamp = int(time.time())
        novo_nome = f"ISOLADO_{timestamp}_{nome_base}"
        destino = os.path.join(self.pasta_quarentena, novo_nome)

        try:
            shutil.copy2(caminho_arquivo, destino)
            with open(f"{destino}.log", "w") as log:
                log.write(f"Data: {time.ctime()}\nMotivo: {motivo}\nOriginal: {caminho_arquivo}")

            print(f"📁 [NEXUS]: Código isolado com segurança em: {destino}")
            return True, destino
        except Exception as e:
            return False, str(e)

gerenciador_quarentena = GerenciadorQuarentena()
