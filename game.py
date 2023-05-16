import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Alien Shooter")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the player
player_width = 50
player_height = 50
player_x = (window_width - player_width) // 2
player_y = window_height - player_height - 10
player_speed = 5

# Set up the bullet
bullet_width = 5
bullet_height = 15
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_state = "ready"  # "ready" - ready to be fired, "fire" - bullet is currently moving

# Set up the alien
alien_width = 50
alien_height = 50
alien_x = random.randint(0, window_width - alien_width)
alien_y = 50
alien_speed = 3

# Set up the score
score = 0
font = pygame.font.Font('freesansbold.ttf', 24)
text_x = 10
text_y = 10

# Game loop
running = True
while running:
    window.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Player controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_state = "fire"

    # Update the player
    if player_x < 0:
        player_x = 0
    elif player_x > window_width - player_width:
        player_x = window_width - player_width
    
    # Update the bullet
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        pygame.draw.rect(window, white, (bullet_x, bullet_y, bullet_width, bullet_height))
        
        if bullet_y < 0:
            bullet_state = "ready"
            bullet_y = player_y
    
    # Update the alien
    alien_x += alien_speed
    if alien_x < 0 or alien_x > window_width - alien_width:
        alien_speed *= -1
        alien_y += alien_height
    
    # Collision detection
    if bullet_y < alien_y + alien_height and bullet_state == "fire":
        if bullet_x > alien_x and bullet_x < alien_x + alien_width or bullet_x + bullet_width > alien_x and bullet_x + bullet_width < alien_x + alien_width:
            bullet_state = "ready"
            bullet_y = player_y
            score += 1
            alien_x = random.randint(0, window_width - alien_width)
            alien_y = 50
    
    # Render the player, alien, and score
    pygame.draw.rect(window, white, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, white, (alien_x, alien_y, alien_width, alien_height))
    score_text = font.render("Score: " + str
