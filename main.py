import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up window dimensions
width, height = 1000, 700  # Adjusted for a larger window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Lights")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
RED = (255, 0, 0)
yellow = (255, 255, 0)
YELLOW = (255, 255, 0)
green = (0, 255, 0)
GREEN = (0, 255, 0)

# Set up line position and dimensions
line_y = height // 2
line_width = width

# Set up rectangles for parts A and B
rect_a = pygame.Rect(0, 0, width, line_y)
rect_b = pygame.Rect(0, line_y, width, height - line_y)

# Set up traffic lights in part A
rectangle_gap = 300  # Adjust the gap between the rectangles
traffic_light_a1 = pygame.Rect(50, 50, 250, 100)
traffic_light_a2 = pygame.Rect(traffic_light_a1.right + rectangle_gap, 50, 250, 100)

# Traffic light states in part A
current_state_a1 = RED
current_state_a2 = RED
timer_a1 = 0
timer_a2 = 0

# Traffic light timers
switch_time = 60  # frames

# Set up traffic lights in part B
traffic_light_b1 = pygame.Rect(50, line_y + 50, 250, 100)
traffic_light_b2 = pygame.Rect(traffic_light_b1.right + rectangle_gap, line_y + 50, 250, 100)

# Traffic light states in part B
current_state_b1 = RED
current_state_b2 = RED
timer_b1 = 0
timer_b2 = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update traffic light states in part A based on timers
    timer_a1 += 1
    timer_a2 += 1

    if current_state_a1 == RED and timer_a1 >= switch_time:
        current_state_a1 = GREEN
        timer_a1 = 0
    elif current_state_a1 == GREEN and timer_a1 >= switch_time:
        current_state_a1 = YELLOW
        timer_a1 = 0
    elif current_state_a1 == YELLOW and timer_a1 >= switch_time:
        current_state_a1 = RED
        timer_a1 = 0

    if current_state_a2 == RED and timer_a2 >= switch_time:
        current_state_a2 = GREEN
        timer_a2 = 0
    elif current_state_a2 == GREEN and timer_a2 >= switch_time:
        current_state_a2 = YELLOW
        timer_a2 = 0
    elif current_state_a2 == YELLOW and timer_a2 >= switch_time:
        current_state_a2 = RED
        timer_a2 = 0

    # Update traffic light states in part B based on timers
    timer_b1 += 1
    timer_b2 += 1

    if current_state_b1 == RED and timer_b1 >= switch_time:
        current_state_b1 = GREEN
        timer_b1 = 0
    elif current_state_b1 == GREEN and timer_b1 >= switch_time:
        current_state_b1 = YELLOW
        timer_b1 = 0
    elif current_state_b1 == YELLOW and timer_b1 >= switch_time:
        current_state_b1 = RED
        timer_b1 = 0

    if current_state_b2 == RED and timer_b2 >= switch_time:
        current_state_b2 = GREEN
        timer_b2 = 0
    elif current_state_b2 == GREEN and timer_b2 >= switch_time:
        current_state_b2 = YELLOW
        timer_b2 = 0
    elif current_state_b2 == YELLOW and timer_b2 >= switch_time:
        current_state_b2 = RED
        timer_b2 = 0

    # Clear the screen
    screen.fill(white)

    # Draw rectangles for parts A and B
    pygame.draw.rect(screen, black, rect_a, 2)
    pygame.draw.rect(screen, black, rect_b, 2)

    # Draw traffic lights in part A
    pygame.draw.rect(screen, green, traffic_light_a1, 2)
    pygame.draw.rect(screen, black, traffic_light_a2, 2)

    # Draw traffic light colors in part A
    pygame.draw.circle(screen, red if current_state_a1 == RED else black, (traffic_light_a1.left + 50, 125), 20)
    pygame.draw.circle(screen, yellow if current_state_a1 == YELLOW else black, (traffic_light_a1.left + 125, 125), 20)
    pygame.draw.circle(screen, green if current_state_a1 == GREEN else black, (traffic_light_a1.right - 50, 125), 20)

    pygame.draw.circle(screen, red if current_state_a2 == RED else black, (traffic_light_a2.left + 50, 125), 20)
    pygame.draw.circle(screen, yellow if current_state_a2 == YELLOW else black, (traffic_light_a2.left + 125, 125), 20)
    pygame.draw.circle(screen, green if current_state_a2 == GREEN else black, (traffic_light_a2.right - 50, 125), 20)

    # Draw traffic lights in part B
    pygame.draw.rect(screen, black, traffic_light_b1, 2)
    pygame.draw.rect(screen, black, traffic_light_b2, 2)

    # Draw traffic light colors in part B
    pygame.draw.circle(screen, red if current_state_b1 == RED else black, (traffic_light_b1.left + 50, line_y + 125), 20)
    pygame.draw.circle(screen, yellow if current_state_b1 == YELLOW else black, (traffic_light_b1.left + 125, line_y + 125), 20)
    pygame.draw.circle(screen, green if current_state_b1 == GREEN else black, (traffic_light_b1.right - 50, line_y + 125), 20)

    pygame.draw.circle(screen, red if current_state_b2 == RED else black, (traffic_light_b2.left + 50, line_y + 125), 20)
    pygame.draw.circle(screen, yellow if current_state_b2 == YELLOW else black, (traffic_light_b2.left + 125, line_y + 125), 20)
    pygame.draw.circle(screen, green if current_state_b2 == GREEN else black, (traffic_light_b2.right - 50, line_y + 125), 20)

    # Update the display
    pygame.display.flip()

    # Control the frames per second
    pygame.time.Clock().tick(60)
