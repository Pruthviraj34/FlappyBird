import pygame
import random

pygame.init()

# -----------------------------
# Screen
# -----------------------------

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# -----------------------------
# Colours
# -----------------------------

SKY = (135, 206, 235)
WHITE = (255, 255, 255)
GREEN = (55, 175, 65)
DARK_GREEN = (35, 125, 45)
LIGHT_GREEN = (95, 205, 85)
YELLOW = (255, 220, 50)
ORANGE = (240, 145, 30)
BLACK = (30, 30, 30)
BROWN = (120, 80, 40)
GROUND = (210, 180, 80)
GRASS = (70, 180, 70)

# -----------------------------
# Fonts
# -----------------------------

score_font = pygame.font.SysFont("arial", 40, bold=True)
game_over_font = pygame.font.SysFont("arial", 65, bold=True)
small_font = pygame.font.SysFont("arial", 28, bold=True)


# -----------------------------
# Bird drawing
# -----------------------------

def draw_bird(surface, x, y):

    # Body
    pygame.draw.ellipse(
        surface,
        YELLOW,
        (x, y, 42, 32)
    )

    # Body shading
    pygame.draw.ellipse(
        surface,
        (235, 185, 30),
        (x + 5, y + 18, 27, 12)
    )

    # Wing
    pygame.draw.ellipse(
        surface,
        (245, 190, 35),
        (x + 7, y + 14, 22, 13)
    )

    # Wing detail
    pygame.draw.line(
        surface,
        ORANGE,
        (x + 12, y + 20),
        (x + 23, y + 23),
        3
    )

    # Eye
    pygame.draw.circle(
        surface,
        WHITE,
        (x + 31, y + 9),
        7
    )

    pygame.draw.circle(
        surface,
        BLACK,
        (x + 33, y + 9),
        3
    )

    # Beak
    pygame.draw.polygon(
        surface,
        ORANGE,
        [
            (x + 40, y + 14),
            (x + 54, y + 19),
            (x + 40, y + 23)
        ]
    )


# -----------------------------
# Cloud drawing
# -----------------------------

def draw_cloud(surface, x, y, size=1):

    cloud_color = (255, 255, 255)

    pygame.draw.circle(
        surface,
        cloud_color,
        (int(x), int(y)),
        int(25 * size)
    )

    pygame.draw.circle(
        surface,
        cloud_color,
        (int(x + 30 * size), int(y - 10 * size)),
        int(32 * size)
    )

    pygame.draw.circle(
        surface,
        cloud_color,
        (int(x + 65 * size), int(y)),
        int(25 * size)
    )

    pygame.draw.rect(
        surface,
        cloud_color,
        (
            int(x - 5 * size),
            int(y),
            int(75 * size),
            int(25 * size)
        )
    )


# -----------------------------
# Pipe drawing
# -----------------------------

def draw_pipe(surface, x, height, gap):

    pipe_width = 80

    # Top pipe body
    pygame.draw.rect(
        surface,
        GREEN,
        (x, 0, pipe_width, height)
    )

    # Dark side of top pipe
    pygame.draw.rect(
        surface,
        DARK_GREEN,
        (x, 0, 10, height)
    )

    # Highlight on top pipe
    pygame.draw.rect(
        surface,
        LIGHT_GREEN,
        (x + 15, 0, 12, height)
    )

    # Top pipe cap
    pygame.draw.rect(
        surface,
        DARK_GREEN,
        (x - 5, height - 5, pipe_width + 10, 25)
    )

    pygame.draw.rect(
        surface,
        GREEN,
        (x, height - 3, pipe_width, 18)
    )

    # Bottom pipe
    bottom_y = height + gap

    pygame.draw.rect(
        surface,
        GREEN,
        (x, bottom_y, pipe_width, HEIGHT - bottom_y)
    )

    # Dark side
    pygame.draw.rect(
        surface,
        DARK_GREEN,
        (x, bottom_y, 10, HEIGHT - bottom_y)
    )

    # Highlight
    pygame.draw.rect(
        surface,
        LIGHT_GREEN,
        (x + 15, bottom_y, 12, HEIGHT - bottom_y)
    )

    # Bottom pipe cap
    pygame.draw.rect(
        surface,
        DARK_GREEN,
        (x - 5, bottom_y - 15, pipe_width + 10, 25)
    )

    pygame.draw.rect(
        surface,
        GREEN,
        (x, bottom_y - 13, pipe_width, 18)
    )


# -----------------------------
# Ground
# -----------------------------

def draw_ground(surface):

    # Dirt
    pygame.draw.rect(
        surface,
        GROUND,
        (0, HEIGHT - 45, WIDTH, 45)
    )

    # Grass
    pygame.draw.rect(
        surface,
        GRASS,
        (0, HEIGHT - 50, WIDTH, 12)
    )

    # Small grass lines
    for x in range(0, WIDTH, 25):

        pygame.draw.line(
            surface,
            DARK_GREEN,
            (x, HEIGHT - 38),
            (x + 8, HEIGHT - 28),
            3
        )


# -----------------------------
# Reset game
# -----------------------------

def reset_game():

    bird_x = 200
    bird_y = 280

    bird_width = 54
    bird_height = 32

    bird_velocity = 0
    gravity = 0.45

    pipe_width = 80
    pipe_gap = 180

    pipe_x = WIDTH
    pipe_height = random.randint(100, 330)

    pipe_speed = 4

    score = 0
    pipe_passed = False

    return (
        bird_x,
        bird_y,
        bird_width,
        bird_height,
        bird_velocity,
        gravity,
        pipe_width,
        pipe_gap,
        pipe_x,
        pipe_height,
        pipe_speed,
        score,
        pipe_passed
    )


# -----------------------------
# Starting values
# -----------------------------

(
    bird_x,
    bird_y,
    bird_width,
    bird_height,
    bird_velocity,
    gravity,
    pipe_width,
    pipe_gap,
    pipe_x,
    pipe_height,
    pipe_speed,
    score,
    pipe_passed
) = reset_game()


# -----------------------------
# Clouds
# -----------------------------

clouds = [
    [100, 100, 1.0, 0.3],
    [420, 150, 0.7, 0.2],
    [680, 80, 1.2, 0.25],
    [850, 230, 0.8, 0.3]
]


# -----------------------------
# Game variables
# -----------------------------

running = True
game_over = False


# -----------------------------
# Main game loop
# -----------------------------

while running:

    # -------------------------
    # Events
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Bird flap
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = -8

            # Restart
            if event.key == pygame.K_r and game_over:

                (
                    bird_x,
                    bird_y,
                    bird_width,
                    bird_height,
                    bird_velocity,
                    gravity,
                    pipe_width,
                    pipe_gap,
                    pipe_x,
                    pipe_height,
                    pipe_speed,
                    score,
                    pipe_passed
                ) = reset_game()

                game_over = False

            # Quit
            if event.key == pygame.K_q:
                running = False


    # -------------------------
    # Game logic
    # -------------------------

    if not game_over:

        # Gravity
        bird_velocity += gravity
        bird_y += bird_velocity

        # Move pipe
        pipe_x -= pipe_speed

        # Move clouds
        for cloud in clouds:

            cloud[0] -= cloud[3]

            if cloud[0] < -120:
                cloud[0] = WIDTH + random.randint(50, 200)
                cloud[1] = random.randint(60, 220)


        # New pipe
        if pipe_x < -pipe_width:

            pipe_x = WIDTH
            pipe_height = random.randint(100, 330)
            pipe_passed = False


        # Score
        if pipe_x + pipe_width < bird_x and not pipe_passed:

            score += 1
            pipe_passed = True


        # Bird collision rectangle
        bird_rect = pygame.Rect(
            bird_x + 5,
            bird_y + 4,
            bird_width - 8,
            bird_height - 8
        )


        # Pipe collision rectangles
        top_pipe = pygame.Rect(
            pipe_x,
            0,
            pipe_width,
            pipe_height
        )

        bottom_pipe = pygame.Rect(
            pipe_x,
            pipe_height + pipe_gap,
            pipe_width,
            HEIGHT
        )


        # Pipe collision
        if bird_rect.colliderect(top_pipe):
            game_over = True

        if bird_rect.colliderect(bottom_pipe):
            game_over = True


        # Top boundary
        if bird_y <= 0:

            bird_y = 0
            game_over = True


        # Ground collision
        if bird_y + bird_height >= HEIGHT - 45:

            bird_y = HEIGHT - 45 - bird_height
            game_over = True


    # -------------------------
    # Draw background
    # -------------------------

    screen.fill(SKY)


    # -------------------------
    # Draw clouds
    # -------------------------

    for cloud in clouds:

        draw_cloud(
            screen,
            cloud[0],
            cloud[1],
            cloud[2]
        )


    # -------------------------
    # Draw pipes
    # -------------------------

    draw_pipe(
        screen,
        pipe_x,
        pipe_height,
        pipe_gap
    )


    # -------------------------
    # Draw bird
    # -------------------------

    draw_bird(
        screen,
        bird_x,
        bird_y
    )


    # -------------------------
    # Draw ground
    # -------------------------

    draw_ground(screen)


    # -------------------------
    # Draw score
    # -------------------------

    score_text = score_font.render(
        str(score),
        True,
        BLACK
    )

    # Score with white shadow
    shadow_text = score_font.render(
        str(score),
        True,
        WHITE
    )

    screen.blit(
        shadow_text,
        (
            WIDTH // 2 - score_text.get_width() // 2 + 2,
            22
        )
    )

    screen.blit(
        score_text,
        (
            WIDTH // 2 - score_text.get_width() // 2,
            20
        )
    )


    # -------------------------
    # Game over
    # -------------------------

    if game_over:

        # Dark transparent-style box
        overlay = pygame.Surface(
            (500, 220),
            pygame.SRCALPHA
        )

        overlay.fill((255, 255, 255, 210))

        screen.blit(
            overlay,
            (150, 180)
        )


        game_over_text = game_over_font.render(
            "GAME OVER",
            True,
            BLACK
        )

        restart_text = small_font.render(
            "Press R to restart",
            True,
            BLACK
        )

        quit_text = small_font.render(
            "Press Q to quit",
            True,
            BLACK
        )


        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                205
            )
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                290
            )
        )

        screen.blit(
            quit_text,
            (
                WIDTH // 2 - quit_text.get_width() // 2,
                330
            )
        )


    # -------------------------
    # Update display
    # -------------------------

    pygame.display.update()

    clock.tick(60)


pygame.quit()