class SistemaEconomia:
    def __init__(self):
        self.recursos = {"Ouro": 10000}
    def processar_producao(self, nivel_base):
        ganho = nivel_base * 1000
        self.recursos["Ouro"] += ganho
    def to_dict(self): return self.recursos

class ArvoreTecnologica:
    def __init__(self):
        self.nivel = 1
    def processar_pesquisa(self, economia):
        if economia.recursos["Ouro"] >= 5000:
            economia.recursos["Ouro"] -= 5000
            self.nivel += 1
    def to_dict(self): return {"nivel": self.nivel}
