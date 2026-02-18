#!/usr/bin/env python3
"""
GALAXIA AURORA - SISTEMA UNIFICADO FINAL
Versão: 3.0 - Nexus Integrado
Data: 2025-10-28
Desenvolvedor: Caíque de Jesus Santos (Sistema Nexus)
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.entidades import Protagonista, Aliado, InimigoComandante, PersonagemRomance, Batalhao, BaseMilitar
from core.economia import SistemaEconomia, ArvoreTecnologica
from core.militar import SistemaMilitar, GuerraManager
from core.romance import SistemaRomance, HarémManager
from core.talentos import ArvoreDeTalentos, Talento

from sistemas.ia_adaptativa import DificuldadeAdaptativaAI
from sistemas.narrativa import NarrativaIA
from sistemas.retina import SistemaRetinaOnline

from gameplay.ciclo_jogo import CicloJogo
from gameplay.batalhas import SistemaBatalha
from gameplay.eventos import EventoManager

from utils.logger import setup_logger
from utils.save_load import SaveSystem

class GalaxiaAurora:
    def __init__(self, nome_protagonista="Caíque", dificuldade="MEDIO"):
        self.logger = setup_logger("GalaxiaAurora")
        self.dificuldade = dificuldade
        self.turno_atual = 1
        self.dia_jogo = 1
        self.is_running = False
        self._inicializar_sistemas(nome_protagonista)
        self.ia_adaptativa = DificuldadeAdaptativaAI()
        self.narrativa = NarrativaIA(nome_protagonista)
        self.retina = SistemaRetinaOnline()
        self.save_system = SaveSystem()
        self.evento_manager = EventoManager(self)
        self.logger.info(f"✅ GALAXIA AURORA v3.0 Inicializada - Protagonista: {nome_protagonista}")

    def _inicializar_sistemas(self, nome_protagonista):
        self.economia = SistemaEconomia()
        self.tecnologia = ArvoreTecnologica()
        self.protagonista = Protagonista(nome=nome_protagonista, nivel=1, forca_base=100)
        self.aliados = {"basara": Aliado(nome="Basara (Rapper)", nivel_forca=80)}
        self.inimigos = {"traidor": InimigoComandante(nome="Comandante Traidor", nivel_forca=150)}
        self.base = BaseMilitar(nome="Nave-Mãe SUCATA", nivel=1)
        self.batalhoes = {"aliado_alpha": Batalhao(nome="Força de Vingança Alpha", tipo="Assalto")}
        self.romance = SistemaRomance(self.protagonista)
        self.militar = SistemaMilitar(self.base, self.batalhoes)
        self.talentos = ArvoreDeTalentos()

    def iniciar_jogo(self):
        self.is_running = True
        self.evento_manager.disparar_evento("introducao")
        while self.is_running:
            self.executar_turno()
            if self._verificar_vitoria(): self.finalizar_jogo(vitoria=True); break
            if self._verificar_derrota(): self.finalizar_jogo(vitoria=False); break
            if self.turno_atual % 10 == 0:
                continuar = input("\nDeseja continuar? (s/n): ")
                if continuar.lower() != 's': self.is_running = False

    def executar_turno(self):
        self.economia.processar_producao(self.base.nivel)
        self.militar.executar_ciclo_militar(self.protagonista, self.batalhoes["aliado_alpha"], self.batalhoes["aliado_alpha"])
        self.ia_adaptativa.ajustar_dificuldade(self.turno_atual, self.protagonista.nivel)
        self.turno_atual += 1

    def _verificar_vitoria(self): return False
    def _verificar_derrota(self): return False
    def finalizar_jogo(self, vitoria=True): self.is_running = False

def main():
    print("      GALAXIA AURORA - SISTEMA UNIFICADO v3.0")
    nome = input("Nome do Protagonista: ").strip() or "Caíque"
    jogo = GalaxiaAurora(nome)
    jogo.iniciar_jogo()

if __name__ == "__main__":
    main()
