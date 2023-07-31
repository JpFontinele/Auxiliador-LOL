

from caracteristicas.Ficha import Ficha


class Invocador:
    def __init__(self, invocador, elo):
        self._invocador = invocador
        self._elo = elo
        self._fichas = []

    # Método getter para o atributo "invocador"
    def get_invocador(self):
        return self._invocador

    # Método setter para o atributo "invocador"
    def set_invocador(self, invocador):
        self._invocador = invocador

    # Método getter para o atributo "elo"
    def get_elo(self):
        return self._elo

    # Método setter para o atributo "elo"
    def set_elo(self, elo):
        self._elo = elo

    # Método para adicionar uma nova ficha à lista de fichas
    def adicionar_ficha(self, id, nome, data):
        ficha = Ficha(id, nome, data)
        self._fichas.append(ficha)

    # Método para exibir as informações do invocador
    def exibir_info(self):
        print(f"Invocador: {self._invocador}")
        print(f"Elo: {self._elo}")
        print("Fichas:")
        for ficha in self._fichas:
            print(f"ID: {ficha.get_id} , Tipo de treino: {ficha.get_nome}, Data da ficha: {ficha.get_data}")
    
