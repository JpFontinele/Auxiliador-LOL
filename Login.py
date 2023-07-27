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

def renderizar_texto(surface, fonte, texto, cor, posicao):
    texto_renderizado = fonte.render(texto, True, cor)
    surface.blit(texto_renderizado, posicao)

def caixas_texto():
    fonte = pygame.font.Font(None, 32)
    entrada_usuario = ""
    entrada_senha = ""
    caixa_usuario_ativa = False
    caixa_senha_ativa = False

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
                # Verifica se o clique foi dentro da caixa da senha
                elif caixa_senha.collidepoint(x, y):
                    caixa_senha_ativa = True
                    caixa_usuario_ativa = False
                else:
                    caixa_usuario_ativa = False
                    caixa_senha_ativa = False

            # Captura eventos de teclado
            if event.type == pygame.KEYDOWN:
                if caixa_usuario_ativa:
                    if event.key == pygame.K_RETURN:  # Se o usuário pressionar ENTER na caixa do usuário
                        caixa_usuario_ativa = False
                        caixa_senha_ativa = True
                    elif event.key == pygame.K_BACKSPACE:  # Se o usuário pressionar BACKSPACE, remove o último caractere
                        entrada_usuario = entrada_usuario[:-1]
                    else:
                        entrada_usuario += event.unicode  # Adiciona o caractere digitado à entrada do usuário
                elif caixa_senha_ativa:
                    if event.key == pygame.K_RETURN:  # Se o usuário pressionar ENTER na caixa da senha
                        return entrada_usuario, entrada_senha
                    elif event.key == pygame.K_BACKSPACE:  # Se o usuário pressionar BACKSPACE, remove o último caractere
                        entrada_senha = entrada_senha[:-1]
                    else:
                        entrada_senha += event.unicode  # Adiciona o caractere digitado à entrada da senha

        janela.fill(BRANCO)

        # Calcule a posição central da janela
        centro_x = resolucao[0] // 2
        centro_y = resolucao[1] // 2

        # Cria a caixa do usuário (retângulo) e centraliza na tela
        largura_caixa = 200
        altura_caixa = 40
        caixa_usuario = pygame.Rect(centro_x - largura_caixa // 2, centro_y - 50, largura_caixa, altura_caixa)
        pygame.draw.rect(janela, PRETO, caixa_usuario, 2)

        # Texto "Usuário" ao lado da caixa de usuário
        renderizar_texto(janela, fonte, "Usuário:", PRETO, (centro_x - 250, centro_y - 40))

        # Texto de entrada do usuário
        renderizar_texto(janela, fonte, entrada_usuario, PRETO, (centro_x - 90, centro_y - 40))

        # Cria a caixa da senha (retângulo) e centraliza na tela
        caixa_senha = pygame.Rect(centro_x - largura_caixa // 2, centro_y + 50, largura_caixa, altura_caixa)
        pygame.draw.rect(janela, PRETO, caixa_senha, 2)

        # Texto "Senha" ao lado da caixa de senha
        renderizar_texto(janela, fonte, "Senha:", PRETO, (centro_x - 250, centro_y + 60))

        # Texto de entrada da senha (mostrando asteriscos)
        renderizar_texto(janela, fonte, '*' * len(entrada_senha), PRETO, (centro_x - 90, centro_y + 60))

        pygame.display.flip()

if __name__ == "__main__":
    usuario, senha = caixas_texto()
    print("Usuário:", usuario)
    print("Senha:", senha)
