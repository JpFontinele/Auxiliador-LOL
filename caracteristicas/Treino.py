class Treino:
    def __init__(self, dificuldade, tempo, qtdDeMinions, scoreDeMinions):
        self._dificuldade = dificuldade
        self._tempo = tempo
        self._qtdDeMinions = qtdDeMinions
        self._scoreDeMinions = scoreDeMinions

    # Getter para o atributo "dificuldade"
    def get_dificuldade(self):
        return self._dificuldade

    # Setter para o atributo "dificuldade"
    def set_dificuldade(self, dificuldade):
        self._dificuldade = dificuldade

    # Getter para o atributo "tempo"
    def get_tempo(self):
        return self._tempo

    # Setter para o atributo "tempo"
    def set_tempo(self, tempo):
        self._tempo = tempo

    # Getter para o atributo "qtdDeMinions"
    def get_qtdDeMinions(self):
        return self._qtdDeMinions

    # Setter para o atributo "qtdDeMinions"
    def set_qtdDeMinions(self, qtdDeMinions):
        self._qtdDeMinions = qtdDeMinions

    # Getter para o atributo "scoreDeMinions"
    def get_scoreDeMinions(self):
        return self._scoreDeMinions

    # Setter para o atributo "scoreDeMinions"
    def set_scoreDeMinions(self, scoreDeMinions):
        self._scoreDeMinions = scoreDeMinions

# Exemplo de uso:
treino1 = Treino("Alto", "30 minutos", 200, 4500)
print("Dificuldade:", treino1.get_dificuldade())
print("Tempo:", treino1.get_tempo())
print("Quantidade de Minions:", treino1.get_qtdDeMinions())
print("Score de Minions:", treino1.get_scoreDeMinions())

treino1.set_dificuldade("Médio")
treino1.set_tempo("45 minutos")
treino1.set_qtdDeMinions(150)
treino1.set_scoreDeMinions(3500)

print("\nNovos valores:")
print("Dificuldade:", treino1.get_dificuldade())
print("Tempo:", treino1.get_tempo())
print("Quantidade de Minions:", treino1.get_qtdDeMinions())
print("Score de Minions:", treino1.get_scoreDeMinions())
