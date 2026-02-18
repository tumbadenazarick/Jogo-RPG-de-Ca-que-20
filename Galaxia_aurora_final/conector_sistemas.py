from core.economia import SistemaEconomia
from core.entidades import BaseMilitar
from utils.ponte import ponte_nexus

# 1. Inicializar Sistemas
economia = SistemaEconomia()
base_militar = BaseMilitar(nome="Fortaleza Nexus", nivel=5)

# 2. Registrar na Ponte (Criando a conexão sem unificar arquivos)
ponte_nexus.registrar_modulo("ECONOMIA", economia)
ponte_nexus.registrar_modulo("MILITAR", base_militar)

# 3. Teste de Conexão (Ponte)
# A Base Militar agora pode 'perguntar' o saldo para a Economia via Ponte
saldo = ponte_nexus.executar_comando_cruzado("MILITAR", "ECONOMIA", "get", "Ouro") # Exemplo simplificado
print(f"📡 [CONEXÃO]: Saldo acessado via ponte: {saldo}")

# 4. Demonstração de Máscara (Conflito de Nomes)
# Se tivéssemos duas 'BaseMilitar', uma seria mascarada
nome_seguro = ponte_nexus.aplicar_mascara_conflito("BaseMilitar", "Abyss")
print(f"🛡️ [MÁSCARA]: Nome em conflito resolvido: {nome_seguro}")
