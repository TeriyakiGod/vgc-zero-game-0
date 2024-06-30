from vgc_zero_lcd.vgc import VGC
import pygame

def main():
    vgc = VGC()
    pygame.init()
    
    screen = pygame.display.set_mode(vgc.display_size)
    pygame.display.set_caption("VGC Zero LCD")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        if vgc.input.key1():
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 255, 0))
        
        screen = pygame.transform.rotate(screen, 90)
        screen = pygame.transform.flip(screen, False, True)
        vgc.draw(screen)
        
        clock.tick(60)
        
    pygame.quit()
    vgc.quit()
    
if __name__ == "__main__":
    main()
        