class Invocador:
    def __init__(self, invocador, elo):
        self._invocador = invocador
        self._elo = elo

class Cadastro:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def cadastrarInvocador(self, invocador):
        with open(self.arquivo, 'a') as file:
            file.write(f"{invocador._invocador},{invocador._elo}\n")

    def VerificaInvocador(self, nome_invocador):
        with open(self.arquivo, 'r') as file:
            for line in file:
                invocador, elo = line.strip().split(',')
                if invocador == nome_invocador:
                    return True
        return False

# Exemplo de uso:
cadastro = Cadastro("invocadores.txt")

# Cadastrando um invocador
invocador1 = Invocador("Player123", "Diamante")
cadastro.cadastrarInvocador(invocador1)

# Verificando se um invocador está salvo
nome_invocador = "Player123"
if cadastro.VerificaInvocador(nome_invocador):
    print(f"O invocador {nome_invocador} está cadastrado.")
else:
    print(f"O invocador {nome_invocador} não está cadastrado.")
