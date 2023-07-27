import pygame
import sys

pygame.init()

# Define a resolução da janela
resolucao = (1280, 720)

# Cria a janela
janela = pygame.display.set_mode(resolucao)
pygame.display.set_caption('AuxiliaLOL')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

def renderizar_texto(surface, fonte, texto, cor, posicao):
    texto_renderizado = fonte.render(texto, True, cor)
    surface.blit(texto_renderizado, posicao)

def caixas_texto(existente=True):
    fonte = pygame.font.Font(None, 32)
    entrada_usuario = ""
    entrada_senha = ""
    entrada_nickname = ""  # NOVO
    entrada_repita_senha = ""  # NOVO
    caixa_usuario_ativa = False
    caixa_senha_ativa = False
    caixa_nickname_ativa = False  # NOVO
    caixa_repita_senha_ativa = False  # NOVO

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Captura o evento de clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o clique foi dentro da caixa do usuário
                if caixa_usuario.collidepoint(x, y):
                    caixa_usuario_ativa = True
                    caixa_senha_ativa = False
                    caixa_nickname_ativa = False  # NOVO
                    caixa_repita_senha_ativa = False  # NOVO
                # Verifica se o clique foi dentro da caixa da senha
                elif caixa_senha.collidepoint(x, y):
                    caixa_usuario_ativa = False
                    caixa_senha_ativa = True
                    caixa_nickname_ativa = False  # NOVO
                    caixa_repita_senha_ativa = False  # NOVO
                # Verifica se o clique foi dentro da caixa do nickname  # NOVO
                elif caixa_nickname.collidepoint(x, y) and not existente:
                    caixa_usuario_ativa = False
                    caixa_senha_ativa = False
                    caixa_nickname_ativa = True
                    caixa_repita_senha_ativa = False
                # Verifica se o clique foi dentro da caixa "Repita senha"  # NOVO
                elif caixa_repita_senha.collidepoint(x, y) and not existente:
                    caixa_usuario_ativa = False
                    caixa_senha_ativa = False
                    caixa_nickname_ativa = False
                    caixa_repita_senha_ativa = True
                # Verifica se o clique foi dentro do botão "Entrar"
                elif botao_entrar.collidepoint(x, y) :
                    return entrada_usuario, entrada_senha, entrada_nickname
                # Verifica se o clique foi dentro do botão "Sair"
                elif botao_sair.collidepoint(x, y) :
                    pygame.quit()
                    sys.exit()
                else:
                    caixa_usuario_ativa = False
                    caixa_senha_ativa = False
                    caixa_nickname_ativa = False
                    caixa_repita_senha_ativa = False

            # Captura eventos de teclado
            if event.type == pygame.KEYDOWN:
                if caixa_usuario_ativa:
                    if event.key == pygame.K_RETURN:
                        caixa_usuario_ativa = False
                        caixa_senha_ativa = True
                        caixa_nickname_ativa = False  # NOVO
                        caixa_repita_senha_ativa = False  # NOVO
                    elif event.key == pygame.K_BACKSPACE:
                        entrada_usuario = entrada_usuario[:-1]
                    else:
                        entrada_usuario += event.unicode
                elif caixa_senha_ativa:
                    if event.key == pygame.K_RETURN:
                        caixa_usuario_ativa = False
                        caixa_senha_ativa = False
                        caixa_nickname_ativa = True  # NOVO
                        caixa_repita_senha_ativa = False  # NOVO
                    elif event.key == pygame.K_BACKSPACE:
                        entrada_senha = entrada_senha[:-1]
                    else:
                        entrada_senha += event.unicode
                elif caixa_nickname_ativa and not existente:  # NOVO
                    if event.key == pygame.K_RETURN:
                        caixa_usuario_ativa = False
                        caixa_senha_ativa = False
                        caixa_nickname_ativa = False
                        caixa_repita_senha_ativa = True  # NOVO
                    elif event.key == pygame.K_BACKSPACE:
                        entrada_nickname = entrada_nickname[:-1]
                    else:
                        entrada_nickname += event.unicode
                elif caixa_repita_senha_ativa and not existente:  # NOVO
                    if event.key == pygame.K_RETURN:
                        return entrada_usuario, entrada_senha, entrada_nickname
                    elif event.key == pygame.K_BACKSPACE:
                        entrada_repita_senha = entrada_repita_senha[:-1]
                    else:
                        entrada_repita_senha += event.unicode

        janela.fill(BRANCO)

        # Calcule a posição central da janela
        centro_x = resolucao[0] // 2
        centro_y = resolucao[1] // 2

        # Define a largura e altura das caixas de texto
        largura_caixa = 250
        altura_caixa = 40

        # Cria a caixa do usuário (retângulo) e posiciona à direita da tela
        caixa_usuario = pygame.Rect(centro_x - 120, centro_y - 50, largura_caixa, altura_caixa)
        pygame.draw.rect(janela, PRETO, caixa_usuario, 2)

        # Texto "Usuário" ao lado da caixa de usuário
        renderizar_texto(janela, fonte, "Usuário:", PRETO, (centro_x - 370, centro_y - 40))

        # Texto de entrada do usuário
        renderizar_texto(janela, fonte, entrada_usuario, PRETO, (centro_x - 115, centro_y - 40))

        # Cria a caixa da senha (retângulo) e posiciona à direita da tela
        caixa_senha = pygame.Rect(centro_x - 120, centro_y + 50, largura_caixa, altura_caixa)
        pygame.draw.rect(janela, PRETO, caixa_senha, 2)

        # Texto "Senha" ao lado da caixa de senha
        renderizar_texto(janela, fonte, "Senha:", PRETO, (centro_x - 370, centro_y + 60))

        # Texto de entrada da senha (mostrando asteriscos)
        renderizar_texto(janela, fonte, '*' * len(entrada_senha), PRETO, (centro_x - 115, centro_y + 60))
         # Cria o botão "Sair"  # NOVO
        botao_sair = pygame.Rect(centro_x - 100, centro_y + 200, 80, 30)
        pygame.draw.rect(janela, VERMELHO, botao_sair)
        renderizar_texto(janela, fonte, "Sair", BRANCO, (centro_x - 85, centro_y + 205))

        # Cria o botão "Entrar"  # NOVO
        botao_entrar = pygame.Rect(centro_x + 20, centro_y + 200, 100, 30)
        pygame.draw.rect(janela, AZUL, botao_entrar)
        renderizar_texto(janela, fonte, "Entrar", BRANCO, (centro_x + 35, centro_y + 205))
        
        if not existente:
            # Cria a caixa do nickname (retângulo) e posiciona à direita da tela  # NOVO
            caixa_nickname = pygame.Rect(centro_x - 120, centro_y - 120, largura_caixa, altura_caixa)
            pygame.draw.rect(janela, PRETO, caixa_nickname, 2)

            # Texto "Nickname" ao lado da caixa do nickname  # NOVO
            renderizar_texto(janela, fonte, "Nickname:", PRETO, (centro_x - 370, centro_y - 110))

            # Texto de entrada do nickname  # NOVO
            renderizar_texto(janela, fonte, entrada_nickname, PRETO, (centro_x - 115, centro_y - 110))

            # Cria a caixa "Repita senha" (retângulo) e posiciona à direita da tela  # NOVO
            caixa_repita_senha = pygame.Rect(centro_x - 120, centro_y + 120, largura_caixa, altura_caixa)
            pygame.draw.rect(janela, PRETO, caixa_repita_senha, 2)

            # Texto "Repita senha" ao lado da caixa "Repita senha"  # NOVO
            renderizar_texto(janela, fonte, "Repita senha:", PRETO, (centro_x - 370, centro_y + 130))

            # Texto de entrada do "Repita senha" (mostrando asteriscos)  # NOVO
            renderizar_texto(janela, fonte, '*' * len(entrada_repita_senha), PRETO, (centro_x - 115, centro_y + 130))

        pygame.display.flip()

if __name__ == "__main__":
    usuario, senha, nickname = caixas_texto()
    print("Nickname:", nickname)
    print("Usuário:", usuario)
    print("Senha:", senha)
