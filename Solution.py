import pygame
import random

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill("black")
    screen.fill(pygame.Color('green'), pygame.Rect(0, 0, 100, 100))
    
    running = True
    drawing = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill("black")
                drawing = True
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
        if drawing:
            x2, y2 = event.pos
            screen.fill("black")
            pygame.draw.rect(screen, ('green'), (x2 - x1, y2 - y1, 100, 100))
        pygame.display.flip()
    pygame.quit()