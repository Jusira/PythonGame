import os
import pygame



def main():
    #inicjalizacja ekranu
    pygame.init()
    
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Game')
    start = pygame.time.get_ticks()
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
    win_status = open(os.path.join('other_data', 'w.txt'),'w')
    win_value = win_status.write('1') 
    win_status.close()
    
    #dzwieki
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('sounds', 'win.mp3'))
    pygame.mixer.music.play()

    #obrazek
    image = pygame.image.load(os.path.join('images/cong', '3.jpg'))
    pygame.transform.scale(image, (800, 600))
      # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    play = False
    play2 = False
    game_active = 1
    # Event loop
    while game_active == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE) or (event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN):
                
                return #wyjscie z petli
                
        screen.blit(background, (0, 0))    
        keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
        
        now = pygame.time.get_ticks()
                             
        
        text = font.render("Congratulations", 1, (255, 10, 10))
        screen.blit(text, (200,20))
        if 2500< now - start:
            text = font.render("It's time for:", 1, (255, 10, 10))
            screen.blit(text, (100,120)) 
        if 5000< now - start :
            text = font.render("unexpected prize", 1, (255, 10, 10))
            screen.blit(text, (300,220))
            
        if 6500 < now - start and play == False:
            pygame.mixer.music.load(os.path.join('sounds', 'cong.mp3'))
            pygame.mixer.music.play(0)
            play = True
        if 7500< now - start:
            screen.blit(image,(200,300))
        if 12000< now - start:
            text = font.render("That's all.", 1, (255, 10, 10))
            screen.blit(text, (100,650)) 
        if 13500< now - start and play2 == False:    
            pygame.mixer.music.load(os.path.join('sounds', 'win.mp3'))
            pygame.mixer.music.play(0)
            play2 = True
        if 14500< now - start:
            text = font.render("Thank you for playing.", 1, (255, 10, 10))
            screen.blit(text, (0,720)) 
        if 18000< now - start:
            exec(open('game.py').read())
            return

            
     
                   
        pygame.display.flip()
    current_game.close()
    
if __name__ == '__main__': 
    main()
    