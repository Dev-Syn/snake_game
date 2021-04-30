import pygame

azul = (50, 100, 213)
laranja = (205, 102, 0)

dimensoes = (600, 600)


### valores iniciais

x = 300
y= 300
d = 10

snake_list = [[x,y]]

tela = pygame.display.set_mode((dimensoes))

pygame.display.set_caption('Snake do syn')

tela.fill(azul)

clock = pygame.time.Clock()


def draw_snake(s_list):
    tela.fill(azul)
    for unity in snake_list:
        pygame.draw.rect(tela, laranja, [unity[0], unity[1], d, d])

def snake_move(s_list):
    delta_x = 0
    delta_y = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -d
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = d
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = - d
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = d
    
    x_new = snake_list[-1][0] + delta_x
    y_new = snake_list[-1][1] + delta_y

    snake_list.append([x_new, y_new])

    del snake_list[0]

    return snake_list

while True:
    pygame.display.update()
    draw_snake(snake_list)
    snake_list = snake_move(snake_list)
    clock.tick(60)