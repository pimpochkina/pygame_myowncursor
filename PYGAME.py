import pygame

# Инициализация Pygame
pygame.init()


screen = pygame.display.set_mode((600, 600))


running = True
cursor_image = pygame.image.load('data/arrow.png')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    if pygame.mouse.get_focused():
        pygame.mouse.set_visible(False)
        screen.blit(cursor_image, (pygame.mouse.get_pos()))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()