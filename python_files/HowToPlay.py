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
    
    screen.blit(background, (0, 0))
    pygame.display.flip()

    przycisk = pygame.image.load(os.path.join('images/HowToPlay', 'przycisk.png'))
    background.blit(przycisk,(780,325))
    background.blit(przycisk,(780,420))
    background.blit(przycisk,(880,420))
    background.blit(przycisk,(680,420))
    space = pygame.image.load(os.path.join('images/HowToPlay', 'SPACE.png'))
    background.blit(space,(150,520))
    up = pygame.image.load(os.path.join('images/HowToPlay', 'up.png'))
    background.blit(up,(380,325))
    down = pygame.image.load(os.path.join('images/HowToPlay', 'down.png'))
    background.blit(down,(380,420))
    right = pygame.image.load(os.path.join('images/HowToPlay', 'right.png'))
    background.blit(right,(480,420))
    left = pygame.image.load(os.path.join('images/HowToPlay', 'left.png'))
    background.blit(left,(280,420))
    
    text = font2.render("space", 1, (10, 10, 10))
    background.blit(text, (180,530))
    text = font2.render("w", 1, (10, 10, 10))
    background.blit(text, (815,345))
    text = font2.render("s", 1, (10, 10, 10))
    background.blit(text, (820,440))
    text = font2.render("d", 1, (10, 10, 10))
    background.blit(text, (920,440))
    text = font2.render("a", 1, (10, 10, 10))
    background.blit(text, (720,440))
    
    
    
    
    text = font.render("How to play", 1, (10, 10, 10))
    background.blit(text, (300,5))
    
    text = font2.render("Your task is to survive the attack of", 1, (10, 10, 10))
    background.blit(text, (10,105))
    text = font2.render("the zombie horde for 5 minutes.", 1, (10, 10, 10))
    background.blit(text, (10,165))
    text = font2.render("If you do this, you'll get", 1, (10, 10, 10))
    background.blit(text, (10,225))
    text = font2.render("a suprising prize.", 1, (10, 10, 10))
    background.blit(text, (10,270))
        
    text = font2.render("movement:", 1, (10, 10, 10))
    background.blit(text, (30,400))
    
    text = font2.render("or:", 1, (10, 10, 10))
    background.blit(text, (600,400))
    
    text = font2.render("fire:", 1, (10, 10, 10))
    background.blit(text, (30,520))
    
    text = font2.render("you get cois for killing zombies.", 1, (10, 10, 10))
    background.blit(text, (30,600))
    text = font2.render("Coins allow you to buy upgrades.", 1, (10, 10, 10))
    background.blit(text, (30,650))

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
    
