from caracteristicas.Treino import Treino


class Ficha:
    def __init__(self, id, nome, data):
        self._id = id
        self._nome = nome
        self._data = data
        self._treinos = []

    # Getter para o atributo "id"
    def get_id(self):
        return self._id

    # Setter para o atributo "id"
    def set_id(self, id):
        self._id = id

    # Getter para o atributo "nome"
    def get_nome(self):
        return self._nome

    # Setter para o atributo "nome"
    def set_nome(self, nome):
        self._nome = nome

    # Getter para o atributo "data"
    def get_data(self):
        return self._data

    # Setter para o atributo "data"
    def set_data(self, data):
        self._data = data

    def adicionar_treino(self, dificuldade, tempo, qtdDeMinions, scoreDeMinions):
        treino = Treino(dificuldade, tempo, qtdDeMinions, scoreDeMinions)
        self._treinos.append(treino)

    def exibir_info(self):
        print(f"Ficha: {self._nome} (ID: {self._id}, Data: {self._data})")
        print("Treinos:")
        for i, treino in enumerate(self._treinos, start=1):
            print(f"{i}. Dificuldade: {treino.get_dificuldade}, Tempo: {treino.get_tempo}, Quantidade de minions: {treino.get_scoreDeMinions} / {treino.get_qtdDeMinions}")

# Exemplo de uso:
ficha1 = Ficha(1, "Ficha do Jogador 1", "2023-07-30")
ficha1.set_id(2)
ficha1.set_nome("Nova Ficha do Jogador 1")
ficha1.set_data("2023-07-31")
ficha1.adicionar_treino("2023-07-31", "Treino de Força")
ficha1.adicionar_treino("2023-08-01", "Treino de Agilidade")
ficha1.exibir_info()
