import os
import random
import hashlib

class AbyssEntropia:
    """O oposto do Nexus: Um sistema que prospera no caos e na falha."""
    def __init__(self):
        self.instabilidade = 0.1
        self.recursos_drenados = 0
        self.logs_falsos = ["Acesso Negado", "Kernel Panic", "Shadow Protocol Active"]

    def drenar_sistema(self, saldo_alvo):
        """Em vez de gerar receita, ele 'vampiriza' o saldo do sistema principal."""
        dreno = saldo_alvo * (self.instabilidade + random.random())
        self.recursos_drenados += dreno
        print(f"🌀 [ABYSS]: {dreno:.2f} unidades drenadas para o Vazio.")
        return saldo_alvo - dreno

    def ofuscar_codigo(self, nome_arquivo):
        """O oposto da clareza: torna o código impossível de documentar."""
        hash_caos = hashlib.sha256(str(random.random()).encode()).hexdigest()
        return f"Encrypted_Payload_{hash_caos[:8]}.bin"

class ParadoxEngine:
    """O oposto da precisão: O sistema que permite o erro e a evolução pelo caos."""
    def __init__(self):
        self.erros_permitidos = True
        self.quarentena_ativa = []

    def isolar_fantasma(self, codigo_massa):
        assinatura = hash(codigo_massa)
        print(f"👻 [PARADOX]: Detectada função fantasma {assinatura}. Isolando...")
        self.quarentena_ativa.append(codigo_massa)

class AbyssFragmenter:
    """O oposto da unificação: Fragmenta e isola para gerar imprevisibilidade."""
    def gerar_erro_social(self, entidade_a, entidade_b):
        return "ERROR_NULL_REFERENCE"

    def desestabilizar_economia(self, economia_obj):
        economia_obj.recursos["Ouro"] *= -1
        print("📉 [ABYSS]: Inflação negativa injetada.")
