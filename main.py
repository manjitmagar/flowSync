# main.py
import pygame
import sys
from traffic_lights import TrafficLights

# Initialize Pygame
pygame.init()

# Set up window dimensions
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Lights")

# Set up TrafficLights object
traffic_lights = TrafficLights(screen, width, height)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update and render traffic lights
    traffic_lights.update()
    traffic_lights.render()

    # Control the frames per second
    pygame.time.Clock().tick(60)
