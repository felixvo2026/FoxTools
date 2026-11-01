def main_close():
    """
        Überwacht die Schließung eines Pygame-Fenster, z.B. :
        import pygame
        import foxtools

        pygame.init()
        foxtools.center_window()
        screen = pygame.display.set_mode((800, 600))

        running = True
        while running:
            running = foxtools.main_close()
            pygame.display.update()

        pygame.quit()

    """
    import pygame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

    return True

def center_window():
    """Zentriert ein Pygame-Fenster"""
    import os
    os.environ["SDL_VIDEO_CENTERED"] = "1"