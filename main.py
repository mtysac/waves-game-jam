import sys, os
import pygame

pygame.init()

# ICON_PATH = "assets/images/icon.png"
# game_icon = pygame.image.load(os.path.join(ICON_PATH))
# pygame.display.set_icon(game_icon)
SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

def main():
    while True:
        pygame.display.set_caption("My Pygame Window")
        SCREEN.fill((158, 191, 219))

        MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit
                    sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()