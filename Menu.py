import pygame
import sys
import Login 

# Inicializa o Pygame
pygame.init()

# Definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)


# Definir fonte
fonte = pygame.font.Font(None, 40)

# Define a resolução da janela
resolucao = (1280, 720)

# Cria a janela
janela = pygame.display.set_mode(resolucao)

# Define o nome da janela
pygame.display.set_caption("AuxiliaLOL")

# Função para desenhar texto do botão
def desenhar_texto(texto, cor, x, y):
    texto_surface = fonte.render(texto, True, cor)
    texto_retangulo = texto_surface.get_rect()
    texto_retangulo.center = (x, y)
    janela.blit(texto_surface, texto_retangulo)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o clique do mouse ocorreu dentro do botão "Login"
            if pos_x_login - largura_botao//2 <= evento.pos[0] <= pos_x_login + largura_botao//2 and \
               pos_y_login - altura_botao//2 <= evento.pos[1] <= pos_y_login + altura_botao//2:
                #caixas_texto()
                Login.caixas_texto()
                print("Login")
            # Verifica se o clique do mouse ocorreu dentro do botão "Cadastrar"
            elif pos_x_login - largura_botao//2 <= evento.pos[0] <= pos_x_login + largura_botao//2 and \
                 pos_y_cadastrar - altura_botao//2 <= evento.pos[1] <= pos_y_cadastrar + altura_botao//2:
                print("Cadastro")
            # Verifica se o clique do mouse ocorreu dentro do botão "Help"
            elif pos_x_login - largura_botao//2 <= evento.pos[0] <= pos_x_login + largura_botao//2 and \
                 pos_y_help - altura_botao//2 <= evento.pos[1] <= pos_y_help + altura_botao//2:
                print("Help")
            # Verifica se o clique do mouse ocorreu dentro do botão "Sobre"
            elif pos_x_sobre - largura_botao//2 <= evento.pos[0] <= pos_x_sobre + largura_botao//2 and \
                 pos_y_sobre - altura_botao//2 <= evento.pos[1] <= pos_y_sobre + altura_botao//2:
                print("Sobre")

    # Limpar a janela
    janela.fill(BRANCO)

    # Desenhar botão "Login" centralizado e um pouco abaixo
    largura_botao, altura_botao = 150, 50
    pos_x_login, pos_y_login = resolucao[0] // 2, resolucao[1] // 2
    pos_y_login += 50  # Deslocamento para baixo
    pygame.draw.rect(janela, AZUL, (pos_x_login - largura_botao//2, pos_y_login - altura_botao//2, largura_botao, altura_botao))
    desenhar_texto("Login", BRANCO, pos_x_login, pos_y_login)

    # Desenhar botão "Cadastrar" logo abaixo do botão "Login"
    pos_y_cadastrar = pos_y_login + altura_botao + 20
    pygame.draw.rect(janela, AZUL, (pos_x_login - largura_botao//2, pos_y_cadastrar - altura_botao//2, largura_botao, altura_botao))
    desenhar_texto("Cadastrar", BRANCO, pos_x_login, pos_y_cadastrar)

    # Desenhar botão "Help" logo abaixo do botão "Cadastrar"
    pos_y_help = pos_y_cadastrar + altura_botao + 20
    pygame.draw.rect(janela, AZUL, (pos_x_login - largura_botao//2, pos_y_help - altura_botao//2, largura_botao, altura_botao))
    desenhar_texto("Help", BRANCO, pos_x_login, pos_y_help)

    # Desenhar botão "Sobre" no canto inferior direito
    largura_botao_sobre, altura_botao_sobre = 100, 40
    pos_x_sobre = resolucao[0] - largura_botao_sobre - 20
    pos_y_sobre = resolucao[1] - altura_botao_sobre - 20
    pygame.draw.rect(janela, AZUL, (pos_x_sobre, pos_y_sobre, largura_botao_sobre, altura_botao_sobre))
    desenhar_texto("Sobre", BRANCO, pos_x_sobre + largura_botao_sobre//2, pos_y_sobre + altura_botao_sobre//2)

    # Atualiza a janela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
