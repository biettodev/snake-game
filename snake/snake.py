import pygame

from random import randrange

# Declaração das cores
branco =(255, 255, 255)
preto =(0, 0, 0)
vermelho =(255, 0, 0)
verde =(0, 255, 0)
azul =(0, 0, 255)

# Tratamento de erros na importação
try:
    pygame.init()
except:
    print('O módulo pygame não foi inicializado com sucesso.')

# Definição de algumas propriedades do jogo
largura =320
altura =280
tamanho =10
placar =40
relogio =pygame.time.Clock()

fundo =pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake')

# Função que configura um texto
def texto(msg, cor, tam, x, y):
    fonte =pygame.font.SysFont(None, tam)
    texto1 =fonte.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

# Função que cria e configura a cobra como uma lista
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo,  preto,  (XY[0],  XY[1],  tamanho,  tamanho))

# Função que cria a maçã
def maca(pos_x, pos_y):
    pygame.draw.rect(fundo,  vermelho,  (pos_x, pos_y, tamanho, tamanho))

# Função principal 
# Em que ocorre o loop do jogo e as interações      
def jogo():
    # Definição das variáveis de fim da execução
    sair =True
    fimdejogo =False
    
    # Definição das variáveis de posicionamento dos objetos na tela
    pos_x =randrange (0, largura-tamanho, 10)
    pos_y =randrange (0, altura-tamanho-placar, 10)
    maca_x =randrange (0, largura-tamanho, 10)
    maca_y =randrange (0, altura-tamanho-placar, 10)
    velocidade_x =0
    velocidade_y =0
    CobraXY =[ ]
    CobraComp =1
    
    # Declaração da pontuação inicial do jogador
    pontos =0
    
    # Loop de execução principal em que ocorre o jogo
    while sair:
    
        # Loop de saída em caso de derrota que exibe tela de Game Over
        while fimdejogo:
                    
            # Laço que captura todos os eventos no jogo
            for event in pygame.event.get():
            
                # Verifica se o evento é para sair da execução
                if event.type == pygame.QUIT:
                    sair =False
                    fimdejogo =False
                        
                # Verifica se o evento é uma tecla pressionada
                if event.type == pygame.KEYDOWN:
                        
                    # Se a tecla pressionada for C, o jogo continua
                    if event.key == pygame.K_c:
                        sair =True
                        fimdejogo =False
                        pos_x =randrange (0, largura-tamanho, 10)
                        pos_y =randrange (0, altura-tamanho-placar, 10)
                        maca_x =randrange (0, largura-tamanho, 10)
                        maca_y =randrange (0, altura-tamanho-placar, 10)
                        velocidade_x =0
                        velocidade_y =0
                        CobraXY =[ ]
                        CobraComp =1
                        pontos =0
                    
                    # Se a tecla pressionada for S, o jogo encerra
                    if event.key == pygame.K_s:
                        sair =False
                        fimdejogo =False
                        
                # Verifica se o evento vem do mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x =pygame.mouse.get_pos()[0]
                    y =pygame.mouse.get_pos()[1]
                            
                    # Se o clique for sobre a posição abaixo, o jogo continua
                    if (x >= 45 and y >= 120) and (x <= 180 and y <= 150):
                        sair =True
                        fimdejogo =False
                        pos_x =randrange (0, largura-tamanho, 10)
                        pos_y =randrange (0, altura-tamanho-placar, 10)
                        maca_x =randrange (0, largura-tamanho, 10)
                        maca_y =randrange (0, altura-tamanho-placar, 10)
                        velocidade_x =0
                        velocidade_y =0
                        CobraXY =[ ]
                        CobraComp =1
                        pontos =0
                        
                    # Senão, se o clique for sobre a posição abaixo, o jogo encerra
                    elif (x > 190 and y > 120) and (x < 265 and y < 150):
                        sair =False
                        fimdejogo =False
                    
            # Desenha a tela de Game Over
            fundo.fill(branco)
            texto('GAME OVER', vermelho, 50, 50, 30)
            texto('PONTUAÇÃO FINAL: '+str(pontos), preto, 30, 50, 80)
            
            # Retângulo e texto que simulam botão para continuar a jogar
            pygame.draw.rect(fundo, preto, [45, 120, 135, 30])
            texto('Continuar(C)', branco, 20, 72, 128)
            
            # Retângulo e texto que simulam botão para sair do jogo
            pygame.draw.rect(fundo, preto, [190, 120, 75, 30])
            texto('Sair(S)', branco, 20, 206, 128)
            
            pygame.display.update()
            
        # Laço que captura todos os eventos no jogo
        for event in pygame.event.get():
        
            # Verifica se o evento é para sair da execução
            if event.type == pygame.QUIT:
                    sair =False
            
            # Verifica se o evento vem do teclado
            if event.type == pygame.KEYDOWN:
                    
                # Vericações das teclas pressionadas
                # Verifica cada seta do teclado pressionada
                # Muda a direção de acordo com a seta
                
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y =0
                    velocidade_x =-10
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y =0
                    velocidade_x =10
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x =0
                    velocidade_y =-10
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x =0
                    velocidade_y =10
        
        # Preenche o fundo com branco
        fundo.fill(branco)
        
        # Adiciona movimento a cobra, mudando a posição de acordo com a velocidade, quadro a quadro
        pos_x +=velocidade_x
        pos_y +=velocidade_y
        
        # Verificação de adição de pontos e comprimento da cobra ao comer a maçã
        if sair:
            if pos_x == maca_x and pos_y == maca_y:
                maca_x =randrange (0, largura-tamanho, 10)
                maca_y =randrange (0, altura-tamanho-placar, 10)
                CobraComp += 1
                pontos +=1
                
            # Retorna a cobra, caso atravesse uma borda, à borda inversa
            if pos_x + tamanho > largura:
                pos_x =0
            if pos_x < 0:
                pos_x =largura-tamanho
            if pos_y + tamanho > altura-placar:
                pos_y =0
            if pos_y < 0:
                pos_y =altura-tamanho-placar
        
        # Define a cabeça da cobra e acrescenta ao comprimento dela
        CobraInicio =[ ]
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        
        # Se o comprimento da cobra
        if len(CobraXY) > CobraComp:
            del CobraXY[0]
        
        # Se a cabeça da cobra colidir com qualquer parte do resto do corpo, o jogador perde
        if any(Bloco == CobraInicio for Bloco in CobraXY[: -1]):
            fimdejogo =True
        
        # Renderização dos principais objetos do jogo na tela
        pygame.draw.rect(fundo,  preto,  [0, altura-placar ,  largura,  placar])        
        texto('PONTUAÇÃO: '+str(pontos), branco, 20, 10, altura-30)     
        cobra(CobraXY)
        maca(maca_x, maca_y)
        
        # Função interna do Pygame que atualiza a tela a cada frame
        pygame.display.update()
        
        # Chama o relógio, renderizando 10 frames por segundo
        relogio.tick(10)

# Chamada da função do jogo 
# E saída da execução do programa        
jogo()
pygame.quit()
