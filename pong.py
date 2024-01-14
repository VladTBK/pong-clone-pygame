import pygame
from constants import cfg


def check_key(key):
    if key[pygame.K_q]:
        pygame.quit()


class Ball:
    def __init__(self, color, pos_X, pos_Y):
        self.color = color
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        pygame.draw.circle(screen, self.color, (self.pos_X, self.pos_Y), 40)

    def fall(self):
        self.pos_Y += 1
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, self.color, (self.pos_X, self.pos_Y), 40)


pygame.init()
screen = pygame.display.set_mode((cfg.height, cfg.width), vsync=1)
clock = pygame.time.Clock()

running = True
screen.fill(cfg.color_dict[1])


def main():
    global running
    ball = Ball(cfg.color_dict[0], cfg.height / 2, cfg.width / 2)
    while running:
        pygame.time.delay(10)
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        curr_key = pygame.key.get_pressed()
        check_key(curr_key)
        ball.fall()
        # update_ball()
        pygame.display.flip()
        clock.tick(60) / 1000


main()
