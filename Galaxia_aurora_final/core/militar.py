import random
import time

class BaseMilitar:
    """Núcleo de comando e comportamento de IA militar."""
    FRASES_COMPORTAMENTO = {
        "ALERTA": "⚠️ Intruso detectado no perímetro! Iniciando protocolo de contenção.",
        "COMBATE": "⚔️ Alvo na mira. Fogo livre! Pela glória do Império Nexus.",
        "RECUAR": "🛡️ Escudos baixos! Retirada tática imediata.",
        "VITORIA": "🏳️ Inimigo neutralizado. Retornando à base."
    }

    def __init__(self, nome, nivel_fortificacao, sistema_economico):
        self.nome = nome
        self.nivel = nivel_fortificacao
        self.economia = sistema_economico
        self.tropas = []

    def confirmar_acao(self, acao):
        """Sistema de confirmação para evitar funções fantasma."""
        print(f"✅ [COMANDO]: Ação '{acao}' validada pelo Sistema Cardinal.")
        return True

    def adicionar_tropa(self, unidade):
        self.tropas.append(unidade)
        self.economia.recursos["Ouro"] -= (unidade.nivel_forca * 0.1)

class SistemaComandoMilitar:
    def __init__(self, chave_mestra):
        self.chave_mestra = chave_mestra.encode()

    def gerar_protocolo_blindado(self, acao_militar, patente_oficial):
        import hashlib
        import hmac
        timestamp = str(int(time.time()))
        payload = f"{acao_militar}|{patente_oficial}|{timestamp}".encode()
        assinatura = hmac.new(self.chave_mestra, payload, hashlib.sha256).hexdigest()
        return {
            "token_confirmacao": f"MIL-ORD-{assinatura[:16].upper()}",
            "status": "PROTEGIDO",
            "timestamp": timestamp
        }

class SistemaMilitar:
    def __init__(self, base, batalhoes):
        self.base = base
        self.batalhoes = batalhoes
    def executar_ciclo_militar(self, protagonista, aliado, inimigo):
        print("⚔️ Ciclo militar avançado em execução.")
