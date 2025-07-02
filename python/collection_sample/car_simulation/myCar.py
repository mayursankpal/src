#!/usr/bin/python3
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
#declare a variable
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car settings
car_width, car_height = 50, 30
car_x, car_y = WIDTH // 2, HEIGHT // 2
car_speed = 5

# Load car image
car_image = pygame.Surface((car_width, car_height))
car_image.fill(BLACK)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
    if keys[pygame.K_UP]:
        car_y -= car_speed
    if keys[pygame.K_DOWN]:
        car_y += car_speed

    # Boundary conditions
    if car_x < 0:
        car_x = 0
    elif car_x > WIDTH - car_width:
        car_x = WIDTH - car_width
    if car_y < 0:
        car_y = 0
    elif car_y > HEIGHT - car_height:
        car_y = HEIGHT - car_height

    # Drawing
    screen.fill(WHITE)
    screen.blit(car_image, (car_x, car_y))
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()