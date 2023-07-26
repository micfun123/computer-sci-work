import pygame
import sys

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (255, 255, 255)

# Ball properties
BALL_RADIUS = 20
BALL_COLOR = (0, 0, 255)
INITIAL_SPEED_X = 5
DAMPING_FACTOR = 0.9

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Bouncing with Damping")

# Initialize the ball
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_speed_x, ball_speed_y = INITIAL_SPEED_X, 0

# Initialize the font
font = pygame.font.Font(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the ball's position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collisions with the screen edges
    if ball_x + BALL_RADIUS >= SCREEN_WIDTH:
        ball_x = SCREEN_WIDTH - BALL_RADIUS
        ball_speed_x *= -DAMPING_FACTOR

    if ball_x - BALL_RADIUS <= 0:
        ball_x = BALL_RADIUS
        ball_speed_x *= -DAMPING_FACTOR

    if ball_y + BALL_RADIUS >= SCREEN_HEIGHT:
        ball_y = SCREEN_HEIGHT - BALL_RADIUS
        ball_speed_y *= -DAMPING_FACTOR

    if ball_y - BALL_RADIUS <= 0:
        ball_y = BALL_RADIUS
        ball_speed_y *= -DAMPING_FACTOR

    # Draw the ball and the screen
    screen.fill(SCREEN_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    # Display speed in the top left corner
    speed_text = font.render("Speed: {:.2f}".format(abs(ball_speed_x)), True, (0, 0, 0))
    screen.blit(speed_text, (10, 10))

    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
