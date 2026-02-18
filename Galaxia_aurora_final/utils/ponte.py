import os

class PonteNexus:
    """
    Sistema de Conexão 'Ponte' - Lord Eclipse.
    Conecta módulos independentes sem unificar o código físico.
    """
    def __init__(self):
        self.conexoes = {}
        self.mascaras = {}

    def registrar_modulo(self, nome, modulo_obj):
        """Registra um sistema na ponte para que outros possam consultá-lo."""
        self.conexoes[nome] = modulo_obj
        print(f"🔗 [PONTE]: Módulo '{nome}' conectado à rede Nexus.")

    def executar_comando_cruzado(self, modulo_origem, modulo_destino, comando, *args):
        """
        Permite que um módulo execute funções em outro sem dependência direta.
        Ex: Economia pedindo dados para a Base Militar.
        """
        if modulo_destino in self.conexoes:
            target = self.conexoes[modulo_destino]
            if hasattr(target, comando):
                func = getattr(target, comando)
                return func(*args)
        print(f"⚠️ [AVISO]: Comando '{comando}' não encontrado no destino '{modulo_destino}'.")
        return None

    def aplicar_mascara_conflito(self, nome_identico, contexto):
        """Aplica a máscara OP_ se houver sobreposição de nomes."""
        novo_nome = f"OP_{contexto.upper()}_{nome_identico}"
        self.mascaras[nome_identico] = novo_nome
        return novo_nome

# Instância Global da Ponte
ponte_nexus = PonteNexus()
