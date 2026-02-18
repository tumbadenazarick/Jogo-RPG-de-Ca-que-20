class EventoManager:
    def __init__(self, jogo):
        self.jogo = jogo
    def disparar_evento(self, nome):
        print(f"Evento {nome} disparado!")
