import os

class PonteNexus:
    """
    Sistema de ponte para conectar o código original ao oposto
    e resolver conflitos de nomes usando a máscara 'OP_'.
    """
    def __init__(self):
        self.mapa_de_identidade = {}

    def verificar_sobreposicao(self, nome_original, novo_codigo):
        if nome_original in novo_codigo:
            print(f"⚠️ Detectado nome idêntico: {nome_original}")
            print("🛠️ Aplicando máscara 'OP_' para evitar quebra de sistema...")
            return novo_codigo.replace(nome_original, f"OP_{nome_original}")
        return novo_codigo

    def criar_ponte(self, original, oposto):
        self.mapa_de_identidade[original] = oposto
        print(f"🔗 Ponte estabelecida: {original} <-> {oposto}")

ponte_global = PonteNexus()
