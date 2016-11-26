import os
import pygame

def main():
    #inicjalizacja ekranu
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Game')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Display some text
    font = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 100)
    font2 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 60)
    font3 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 80)
    font4 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 120)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #dzwieki
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('sounds', 'menu.wav'))
    pygame.mixer.music.play(loops = -1)
    
    
    
    text = font.render("About", 1, (10, 10, 10))
    background.blit(text, (300,5))
    
    text = font4.render("Author:", 1, (255, 100, 0))
    background.blit(text, (250,200))
    text = font4.render("Alicja Gosiewska", 1, (255, 100, 0))
    background.blit(text, (50,300))
    

   

    text = font3.render("Press ESC to back to  menu", 1, (255, 10, 10))
    background.blit(text, (50,700))  
    
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    game_active = 1
    # Event loop
    while game_active == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE) or (event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN):
                
                return #wyjscie z petli
                
       



        pygame.display.flip()
    current_game.close()
    
if __name__ == '__main__': 
    main()
