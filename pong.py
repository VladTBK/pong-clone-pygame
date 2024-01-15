import pygame
from constants import cfg


def refresh(check_run):
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check_run = False
    screen.fill(cfg.color_dict[1])
    return check_run


class Player:
    def __init__(self, color, pos_X, pos_Y, width, height, turn):
        self.color = color
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.vx = cfg.player_speed
        self.vy = cfg.player_speed
        self.turn = turn
        self.width = width
        self.height = height
        pygame.draw.rect(
            screen, self.color, (self.pos_X, self.pos_Y, self.width, self.height)
        )

    def update_state(self, key):
        if self.turn:
            if key[pygame.K_w] and self.pos_Y >= cfg.player_width:
                self.pos_Y -= self.vx
            if (
                key[pygame.K_s]
                and self.pos_Y <= cfg.height - cfg.player_height - cfg.player_width
            ):
                self.pos_Y += self.vx

        pygame.draw.rect(
            screen, self.color, (self.pos_X, self.pos_Y, self.width, self.height)
        )


class Ball:
    def __init__(self, color, pos_X, pos_Y, size):
        self.color = color
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.vx = cfg.ballspeed
        self.vy = cfg.ballspeed
        self.size = size
        pygame.draw.circle(screen, self.color, (self.pos_X, self.pos_Y), self.size)

    def update_state(self):
        self.pos_X += self.vx
        self.pos_Y += self.vy
        if self.pos_X >= cfg.width - self.size / 2 or self.pos_X <= self.size / 2:
            self.vx = -self.vx

        if self.pos_Y <= self.size / 2 or self.pos_Y >= cfg.height - self.size / 2:
            self.vy = -self.vy

        pygame.draw.circle(screen, self.color, (self.pos_X, self.pos_Y), self.size)


pygame.init()
screen = pygame.display.set_mode((cfg.width, cfg.height), vsync=1)
clock = pygame.time.Clock()


def main():
    running = True
    ball = Ball(cfg.color_dict[0], cfg.width / 2, cfg.height / 2, cfg.ball_size)
    player1 = Player(
        cfg.color_dict[2],
        cfg.width - cfg.player_width * 2,
        cfg.height / 2 - cfg.player_height / 2,
        cfg.player_width,
        cfg.player_height,
        False,
    )
    player2 = Player(
        cfg.color_dict[2],
        cfg.player_width,
        cfg.height / 2 - cfg.player_height / 2,
        cfg.player_width,
        cfg.player_height,
        True,
    )
    while running:
        running = refresh(running)
        curr_key = pygame.key.get_pressed()
        if curr_key[pygame.K_q]:
            pygame.quit()

        ball.update_state()
        player1.update_state(curr_key)
        player2.update_state(curr_key)
        pygame.display.flip()
        clock.tick(60) / 1000


main()
