
import pygame
import sys

# Inicializando Pygame
pygame.init()

# Configurações da janela
largura, altura = 1200, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bloquinhos")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Tamanho e espaçamento dos blocos
tamanho_bloco = 40
espacamento = 5

# Criar uma matriz de blocos
bloquinhos = [[BRANCO for _ in range(largura // (tamanho_bloco + espacamento))] for _ in range(altura // (tamanho_bloco + espacamento))]

def desenhar_bloquinhos():
    for y, linha in enumerate(bloquinhos):
        for x, cor in enumerate(linha):
            rect = (x * (tamanho_bloco + espacamento), y * (tamanho_bloco + espacamento), tamanho_bloco, tamanho_bloco)
            pygame.draw.rect(janela, cor, rect)

def main():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x = mouse_x // (tamanho_bloco + espacamento)
                y = mouse_y // (tamanho_bloco + espacamento)
                bloquinhos[y][x] = PRETO
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    print("Bloquinhos Pretos:")
                    for y, linha in enumerate(bloquinhos):
                        for x, cor in enumerate(linha):
                            if cor == PRETO:
                                print(f"({x}, {y}, 1)", end=",")
                    print()

        janela.fill(BRANCO)
        desenhar_bloquinhos()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
