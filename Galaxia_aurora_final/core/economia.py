import math

class SistemaEconomia:
    def __init__(self):
        self.recursos = {"Ouro": 10000, "Mana": 50000}
        self.taxa_eficiencia = 1.0

    def calcular_rendimento(self, base_recurso, nivel_tech):
        """
        Cálculo de rendimento complexo:
        R = B * (1 + eta) * log10(T)
        """
        if nivel_tech <= 0: nivel_tech = 1
        return base_recurso * self.taxa_eficiencia * math.log10(nivel_tech + 1)

    def processar_producao(self, nivel_base):
        renda = self.calcular_rendimento(1000, nivel_base)
        self.recursos["Ouro"] += renda

    def get(self, recurso):
        return self.recursos.get(recurso, 0)

class ArvoreTecnologica:
    def __init__(self):
        self.nivel = 1
        self.arvore_tech = ["Mineração", "Energia Estelar", "Sintetização de Mana"]

    def upgrade_tecnologia(self, economia, recurso):
        custo = self.nivel * 1500
        if economia.recursos.get(recurso, 0) >= custo:
            economia.recursos[recurso] -= custo
            self.nivel += 1
            return True
        return False
