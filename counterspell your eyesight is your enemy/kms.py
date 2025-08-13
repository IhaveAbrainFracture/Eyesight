import pygame
import random
import sys

pygame.init()


screen_width = 800
screen_height = 600


white = (255,255,255)
black = (0, 0, 0)
grey = (10,10,10)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dhyan")


target_radius = 30
target_x = random.randint(target_radius, screen_width - target_radius)
target_y = random.randint(target_radius, screen_height - target_radius)
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance <= target_radius:
                score += 1
                target_x = random.randint(target_radius, screen_width - target_radius)
                target_y = random.randint(target_radius, screen_height - target_radius)

    screen.fill(black)
    pygame.draw.circle(screen, grey, (target_x, target_y), target_radius)

    score_text = font.render("your enemy is yourself (click the circles) score here  :" + str(score), True, white)
    screen.blit(score_text, (10, 10))
    score_text =("bottom text here", white)
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
sys.exit()

