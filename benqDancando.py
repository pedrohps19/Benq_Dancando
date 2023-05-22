import pygame
import os

pygame.init()

largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))

benq_imagem1 = os.path.join("benq.png")
benq_imagem2 = os.path.join("benq_1braço_baixo.png")
benq_imagem3 = os.path.join("benq_1outrobraço_baixo.png")
benq_imagem4 = os.path.join("benq_2braços_baixo.png")

#Fazendo o redimensionamento das imagens do benq para todas terem o tamanho de 200x200 
imagem1 = pygame.image.load(benq_imagem1).convert_alpha()
imagem1 = pygame.transform.scale(imagem1, (200, 200))

imagem2 = pygame.image.load(benq_imagem2).convert_alpha()
imagem2 = pygame.transform.scale(imagem2, (200, 200))

imagem3 = pygame.image.load(benq_imagem3).convert_alpha()
imagem3 = pygame.transform.scale(imagem3, (200, 200))

imagem4 = pygame.image.load(benq_imagem4).convert_alpha()
imagem4 = pygame.transform.scale(imagem4, (200, 200))

#Array com todas as imagens do benq já redimensionadas e disponiveis para usar na hora da animação
lista_imagens = [imagem1, imagem2, imagem3, imagem4]

# Velocidade em segundos
velocidade_animacao = 0.5  

# Posição inicial de x e y do centro da imagem
posicao_x = largura / 2 - 50  
posicao_y = altura / 2 - 50

# Velocidade de movimento no eixo x
velocidade_x = 1  

# Direção do movimento "1 segue para direita e -1 segue para esquerda"
direcao_x = 1  

# Controlando o espelhamento das imagens
espelhado = False  


#Fazendo a busca da musica que será usada e passando para o Pygame
musica = os.path.join("musica_wandinha.wav")
pygame.mixer.music.load(musica)

#Volume da música de 0.0 até 1.0
pygame.mixer.music.set_volume(0.5)

#"-1" deixará a música tocando em loop
pygame.mixer.music.play(-1)  


#Por qual imagem do Array a animação irá começar, no caso o primerio elemento/indice "0"
i_imagem = 0  
#Buscando o tempo que acaba a animação anterior para poder passar para a proxima animação/imagem
tempo_anterior = pygame.time.get_ticks()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            quit()

    
    janela.fill((255, 255, 255))

    # Fazendo a verificação para saber quando passar para a próxima imagem
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_anterior >= velocidade_animacao * 1000:
        i_imagem = (i_imagem + 1) % len(lista_imagens)

        tempo_anterior = tempo_atual

        # Trocando o espelhamento depois de cada imagem trocada
        espelhado = not espelhado

    # Imagem atual
    imagem_atual = lista_imagens[i_imagem]

    # Fazendo o transformação de "Translação"
    posicao_x += velocidade_x * direcao_x

    # Limitando o movimento para o tamanho da tela
    if posicao_x <= 100 or posicao_x >= largura - 100:
        # Mover para o lado contrário
        direcao_x *= -1 

    # Fazendo o espelhamento das imagens
    if espelhado:
        imagem_atual = pygame.transform.flip(imagem_atual, True, False)

    # Buscando tamanho da tela para saber quando colidiu
    retangulo_imagem = imagem_atual.get_rect(center=(posicao_x, posicao_y))

    # Por fim colocamos os elementos na tela
    janela.blit(imagem_atual, retangulo_imagem)

    pygame.display.update()
