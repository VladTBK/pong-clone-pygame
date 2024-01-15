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
    def __init__(self, color, pos_X, pos_Y, width, height, name):
        self.color = color
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.vx = cfg.player_speed
        self.vy = cfg.player_speed
        self.name = name
        self.width = width
        self.height = height

    def update_state(self, key):
        if self.name == "player1":
            if key[pygame.K_w] and self.pos_Y >= cfg.player_width:
                self.pos_Y -= self.vx
            if (
                key[pygame.K_s]
                and self.pos_Y <= cfg.height - cfg.player_height - cfg.player_width
            ):
                self.pos_Y += self.vx

        if self.name == "player2":
            if key[pygame.K_UP] and self.pos_Y >= cfg.player_width:
                self.pos_Y -= self.vx
            if (
                key[pygame.K_DOWN]
                and self.pos_Y <= cfg.height - cfg.player_height - cfg.player_width
            ):
                self.pos_Y += self.vx

    def draw_player(self):
        pygame.draw.rect(
            screen, self.color, (self.pos_X, self.pos_Y, self.width, self.height)
        )


class Ball:
    def __init__(
        self,
        color,
        pos_X,
        pos_Y,
        size,
    ):
        self.color = color
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.vx = cfg.ballspeed
        self.vy = cfg.ballspeed
        self.size = size
        self.player_num = 1

    def update_state(self, curr_player):
        global running
        self.pos_X += self.vx
        self.pos_Y += self.vy
        if self.player_num == 1:
            if (
                curr_player.pos_X - self.size / 2 < self.pos_X
                and curr_player.pos_Y < self.pos_Y
                and curr_player.pos_Y + cfg.player_height > self.pos_Y
            ):
                self.player_num = 2
                self.vx = -(self.vx + 1)
            if self.pos_X >= cfg.width:
                cfg.player2_score += 1
                running = False

        elif self.player_num == 2:
            if (
                curr_player.pos_X + 2 * self.size > self.pos_X
                and curr_player.pos_Y < self.pos_Y
                and curr_player.pos_Y + cfg.player_height > self.pos_Y
            ):
                self.player_num = 1
                self.vx = -(self.vx - 1)
            if self.pos_X <= 0:
                cfg.player1_score += 1
                running = False

        if self.pos_Y <= self.size / 2 or self.pos_Y >= cfg.height - self.size / 2:
            self.vy = -self.vy

    def draw_ball(self):
        pygame.draw.circle(screen, self.color, (self.pos_X, self.pos_Y), self.size)


games = int(input("Choose a score that will win: "))
pygame.init()
screen = pygame.display.set_mode((cfg.width, cfg.height), vsync=1)
clock = pygame.time.Clock()
running = True


def run_game():
    global running
    ball = Ball(cfg.color_dict[0], cfg.width / 2, cfg.height / 2, cfg.ball_size)
    player1 = Player(
        cfg.color_dict[2],
        cfg.width - cfg.player_width * 2,
        cfg.height / 2 - cfg.player_height / 2,
        cfg.player_width,
        cfg.player_height,
        "player1",
    )
    player2 = Player(
        cfg.color_dict[2],
        cfg.player_width,
        cfg.height / 2 - cfg.player_height / 2,
        cfg.player_width,
        cfg.player_height,
        "player2",
    )
    while running:
        running = refresh(running)
        ball.draw_ball()
        player1.draw_player()
        player2.draw_player()
        curr_key = pygame.key.get_pressed()
        if curr_key[pygame.K_q]:
            pygame.quit()
        if ball.player_num == 1:
            ball.update_state(player1)
        else:
            ball.update_state(player2)

        player1.update_state(curr_key)
        player2.update_state(curr_key)
        pygame.display.flip()
        clock.tick(60) / 1000


def main():
    global running
    run_game()
    print(f"Player1 has {cfg.player1_score} points")
    print(f"Player2 has {cfg.player2_score} points")
    running = True


while cfg.player1_score < games and cfg.player2_score < games:
    main()

if cfg.player1_score < cfg.player2_score:
    print("Player 2 WON")
else:
    print("Player 1 WON")
