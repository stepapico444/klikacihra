import pygame
pygame.init()
okno = pygame.display.set_mode((400, 300))
pygame.display.set_caption("klikací hra")
font = pygame.font.SysFont("Arial", 30)
skore = 0
bezi = True

while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            skore += 1
            okno.fill((0, 0, 0))
            text = font.render(f"klikni! Skóre: {skore}", True, (255, 255, 255))
            okno.blit(text, (80, 130))
            pygame.display.update()

pygame.quit()
