import random
from datetime import datetime
from typing import Dict, List, Any

class EntidadeJogo:
    def __init__(self, nome, nivel_forca=10, saude_max=100):
        self.nome = nome
        self.nivel_forca = nivel_forca
        self.saude_max = saude_max
        self.saude = saude_max
        self.ativo = True
        self.criado_em = datetime.now()
    def receber_dano(self, dano):
        self.saude -= max(0, dano)
        if self.saude <= 0: self.saude = 0; self.ativo = False; return True
        return False
    def to_dict(self): return {"nome": self.nome, "nivel_forca": self.nivel_forca}

class Protagonista(EntidadeJogo):
    def __init__(self, nome, nivel=1, forca_base=100, poderes=None, lealdade=100):
        super().__init__(nome, forca_base, 200)
        self.nivel = nivel
        self.poderes = poderes or ["Comando Estratégico"]
        self.lealdade = lealdade
        self.xp = 0
        self.pontos_retribuicao = 0
        self.moral = 100
        self.pontos_romance = {}
        self.pontos_talento = 0
    def ganhar_xp(self, xp_ganho):
        self.xp += xp_ganho
        if self.xp >= self.nivel * 100: self.nivel += 1; return True
        return False

class Aliado(EntidadeJogo):
    def __init__(self, nome, nivel_forca=80, tipo_poder="Apoio", lealdade=95):
        super().__init__(nome, nivel_forca)
        self.tipo_poder = tipo_poder
        self.lealdade = lealdade
    def dar_suporte(self, protagonista): print(f"{self.nome} dando suporte!")

class InimigoComandante(EntidadeJogo):
    def __init__(self, nome, nivel_forca=150, tipo_poder="Ofensivo", chance_contra_ataque=0.3):
        super().__init__(nome, nivel_forca)
        self.tipo_poder = tipo_poder
        self.chance_contra_ataque = chance_contra_ataque

class PersonagemRomance(EntidadeJogo):
    def __init__(self, nome, genero="Feminino", personalidade="Doce", lealdade=85):
        super().__init__(nome, 50)
        self.genero = genero
        self.personalidade = personalidade
        self.lealdade = lealdade

class Batalhao:
    def __init__(self, nome, tipo="Assalto", unidades=None):
        self.nome = nome
        self.tipo = tipo
        self.unidades = unidades or {}
        self.ativo = True

class BaseMilitar:
    def __init__(self, nome, nivel=1, dominio=10):
        self.nome = nome
        self.nivel = nivel
        self.dominio = dominio
