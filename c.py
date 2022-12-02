import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 20  # пикселей в секунду
    drawing = False
    
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
        if drawing == True:
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, ("green"), (x1, y1, 100, 100))
            x_pos += v * clock.tick() / 1000  # v * t в секундах
        pygame.display.flip()
    pygame.quit()