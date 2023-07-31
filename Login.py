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
    entrada_elo = ""  # NOVO: Caixa "Elo"
    
    caixa_usuario_ativa = False
    caixa_elo_ativa = False  # NOVO: Ativa a caixa "Elo"
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Captura o evento de clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                # Verifica se o clique foi dentro da caixa "Elo"
                if not existente and caixa_elo.collidepoint(x, y):
                    caixa_usuario_ativa = False
                    caixa_elo_ativa = True  # NOVO: Ativa a caixa "Elo"

                # Verifica se o clique foi dentro da caixa do usuário
                elif caixa_usuario.collidepoint(x, y):
                    caixa_usuario_ativa = True
                    caixa_elo_ativa = False  # NOVO: Desativa a caixa "Elo"
                    
                # Verifica se o clique foi dentro do botão "Entrar"
                elif botao_entrar.collidepoint(x, y):
                    return entrada_usuario, entrada_elo  # NOVO: Altera para retornar também a entrada do "Elo"
                # Verifica se o clique foi dentro do botão "Sair"
                elif botao_sair.collidepoint(x, y):
                    return
                else:
                    caixa_usuario_ativa = False
                    caixa_elo_ativa = False  # NOVO: Desativa a caixa "Elo"
                   

            # Captura eventos de teclado
            if event.type == pygame.KEYDOWN:
                if not existente:
                    if caixa_elo_ativa :  # NOVO: Adiciona as verificações para a caixa "Elo"
                        if event.key == pygame.K_RETURN:
                            caixa_usuario_ativa = False
                            caixa_elo_ativa = False
                            
                        elif event.key == pygame.K_BACKSPACE:
                            entrada_elo = entrada_elo[:-1]
                        else:
                            entrada_elo += event.unicode

                if caixa_usuario_ativa:
                    if event.key == pygame.K_RETURN:
                        caixa_usuario_ativa = False
                        caixa_elo_ativa = True  # NOVO: Ativa a caixa "Elo"
                        
                    elif event.key == pygame.K_BACKSPACE:
                        entrada_usuario = entrada_usuario[:-1]
                    else:
                        entrada_usuario += event.unicode
                

        janela.fill(BRANCO)

        # Calcule a posição central da janela
        centro_x = resolucao[0] // 2
        centro_y = resolucao[1] // 2

        # Define a largura e altura das caixas de texto
        largura_caixa = 250
        altura_caixa = 40

        if not existente:
            # Cria a caixa "Elo" (retângulo) e centraliza na tela  # NOVO
            caixa_elo = pygame.Rect(centro_x - largura_caixa // 2, centro_y - altura_caixa // 2 - 100, largura_caixa, altura_caixa)
            pygame.draw.rect(janela, PRETO, caixa_elo, 2)

            # Texto "Elo" ao lado da caixa do "Elo"  # NOVO
            renderizar_texto(janela, fonte, "Elo:", PRETO, (centro_x - 370, centro_y - 110))

            # Texto de entrada do "Elo"  # NOVO
            renderizar_texto(janela, fonte, entrada_elo, PRETO, (centro_x - 115, centro_y - 110))

        # Cria a caixa do usuário (retângulo) e centraliza na tela
        caixa_usuario = pygame.Rect(centro_x - largura_caixa // 2, centro_y - altura_caixa // 2 -30, largura_caixa, altura_caixa)  # Modificado para ajustar a posição
        pygame.draw.rect(janela, PRETO, caixa_usuario, 2)

        # Texto "Usuário" ao lado da caixa de usuário
        renderizar_texto(janela, fonte, "Usuário:", PRETO, (centro_x - 370, centro_y - 40))

        # Texto de entrada do usuário
        renderizar_texto(janela, fonte, entrada_usuario, PRETO, (centro_x - 115, centro_y - 40))

        # Cria o botão "Sair" e posiciona mais à esquerda
        botao_sair = pygame.Rect(centro_x - 165, centro_y + 200, 80, 30)  # Modificado para ajustar a posição
        pygame.draw.rect(janela, VERMELHO, botao_sair)
        renderizar_texto(janela, fonte, "Sair", BRANCO, (centro_x - 150, centro_y + 205))  # Modificado para ajustar a posição

        # Cria o botão "Entrar" e posiciona mais à esquerda
        botao_entrar = pygame.Rect(centro_x -45, centro_y + 200, 100, 30)  # Modificado para ajustar a posição
        pygame.draw.rect(janela, AZUL, botao_entrar)
        renderizar_texto(janela, fonte, "Entrar", BRANCO, (centro_x -30, centro_y + 205))  # Modificado para ajustar a posição

        pygame.display.flip()

if __name__ == "__main__":
    usuario, elo = caixas_texto()  # NOVO: Altera as variáveis retornadas para "elo"
    print("Elo:", elo)  # NOVO: Imprime o "Elo"
    print("Usuário:", usuario)