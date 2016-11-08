import os
import pygame

def main():
    #inicjalizacja ekranu
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game')
    
    enter = pygame.time.get_ticks()
    
    #wczytanie ilosci coinsow i wyzerownanie pliku
    current_game = open(os.path.join('other_data', 'current_game.txt'),'r')
    coins_value = current_game.readline().strip('\n\r') #wczytuje linie z pliku bez znaku konca linii
    current_game.close()
    current_game = open(os.path.join('other_data', 'current_game.txt'),'w')
    current_game.write(str(0))
    current_game.close()
    #dodanie zarobionych coinsow do wszystkich
    game_status = open(os.path.join('other_data', 'game_status.txt'),'r')
    coins_all = game_status.readline().strip('\n\r')
    
    game_status = open(os.path.join('other_data', 'game_status.txt'),'w')
    game_status.write(str(int(coins_value) + int(coins_all)))
    game_status.close()
    #kolor tla
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Display some text
    font = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 70)
    font2 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 50)
    font3 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 150)
    
    text_coins = font3.render("GAME OVER", 1, (255, 10, 10))
    background.blit(text_coins, (50,20)) 
    text_coins = font.render("Coins earned:", 1, (10, 10, 10))
    background.blit(text_coins, (50,220))
    text_coins = font.render(coins_value, 1, (10, 10, 10))
    background.blit(text_coins, (450,220)) 
    text_coins = font2.render("Press ENTER to play again", 1, (10, 10, 10))
    background.blit(text_coins, (100,400))
    text_coins = font2.render("Press ESC to return to menu", 1, (10, 10, 10))
    background.blit(text_coins, (100,480))
     
    
    
    
      # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    game_active = 1
    # Event loop
    while game_active == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                exec(open('game.py').read())
                return #wyjscie z petli
                
            
        keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
       
        if keys[pygame.K_RETURN]:
            now = pygame.time.get_ticks()
            if now - enter >250: #po to, zeby nie wciskal nam sie enter na poczatku                     
                exec(open('game.py').read())
                return
        
        #tlo
                   
        pygame.display.flip()
    current_game.close()
    
if __name__ == '__main__': 
    main()
    

