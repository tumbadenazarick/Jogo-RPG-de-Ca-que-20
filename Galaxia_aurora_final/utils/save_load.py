import json
import os

class SaveSystem:
    def __init__(self, directory="saves"):
        self.directory = directory
        if not os.path.exists(directory): os.makedirs(directory)
    def salvar(self, nome, dados):
        with open(os.path.join(self.directory, f"{nome}.json"), "w") as f:
            json.dump(dados, f)
        return True
    def carregar(self, nome):
        path = os.path.join(self.directory, f"{nome}.json")
        if os.path.exists(path):
            with open(path, "r") as f: return json.load(f)
        return None
    @staticmethod
    def listar_saves(): return []
