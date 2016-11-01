import os
import pygame

def main():
    #inicjalizacja ekranu
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Game')
    
    #wczytanie stanu gry
    game_status = open(os.path.join('other_data', 'game_status.txt'),'r')
    coins_value = game_status.readline().strip('\n\r') #wczytuje linie z pliku bez znaku konca linii
    
    #kolor tla
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Display some text
    font = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 100)
    font2 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 50)
    
    text_coins = font2.render("Coins:", 1, (10, 10, 10))
    background.blit(text_coins, (400,10)) 
     
    win_status = open(os.path.join('other_data', 'w.txt'),'r')
    win_value = win_status.readline().strip('\n\r') 
    win_status.close()
    
    
    #tworzymy buttony
    captions = ["Play","Upgrades","How to play", "Reset progress", "Credits", "Quit"]
    buttons = [0] * 6
    for i in range(6):
        buttons[i] = font.render(captions[i], 1, (10,10,10)) #napis + kolor    
        background.blit(buttons[i], (50,100+100*i)) #tekst + pozycja
    
    #zapamietujemy, ktory button jest aktywny
    active_button = 0
    
    #zapamietujey czas w grze
    last = pygame.time.get_ticks()
    
    def change_active_button(up_or_down,last):
        now = pygame.time.get_ticks()
        if now - last > 250: 
            last = pygame.time.get_ticks()
            if up_or_down == "down":
                if active_button < 5:
                    return (active_button + 1, last)
            else:
                if active_button > 0:
                    return (active_button - 1, last)
            return (active_button, last)
        return (active_button, last)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    
    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                return #wyjscie z petli
            
        keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            (active_button, last) = change_active_button("down", last)  # ruch w dol
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            (active_button, last) = change_active_button("up",last)# ruch w gore
            
        if keys[pygame.K_RETURN]:
            if active_button == 0:
                exec(open(os.path.join('python_files', 'playgame.py')).read())
            if active_button == 1:
                exec(open(os.path.join('python_files', 'game_upgrade.py')).read())
            if active_button == 2:
                exec(open(os.path.join('python_files', 'HowToPlay.py')).read())
            if active_button == 3:
                win_status = open(os.path.join('other_data', 'w.txt'),'w')
                win_value = win_status.write('0') 
                win_status.close()
                game_status.close()
                game_status = open(os.path.join('other_data', 'game_status.txt'),'w')
                game_status.write('0')
                game_status.close()
                game_status = open(os.path.join('other_data', 'game_status.txt'),'r')
                coins_value = game_status.readline().strip('\n\r') #wczytuje linie z pliku bez znaku konca linii
                settings_values = ["selected","buy for 50",   "selected", "buy for 50", "buy for 50" ,"selected","buy for 50", "upgrade for 10","upgrade for 10","upgrade for 10"]
                settings = open(os.path.join('other_data', 'settings.txt'),'w')
                for el in settings_values:
                    settings.write(el + '\n')
                settings.close()
                upgrades = open(os.path.join('other_data', 'upgrades.txt'),'w')
                for i in range(3):
                    upgrades.write('1' + '\n')
                upgrades.close()
            if active_button == 4:
                #wyswietli creditsy
                exec(open(os.path.join('python_files', 'credits.py')).read())
            if active_button == 5:
                return                 
        if keys[pygame.K_s]:
            if keys[pygame.K_p]:
                if keys[pygame.K_a]:
                    if keys[pygame.K_m]:
                        exec(open(os.path.join('python_files','cong.py')).read())
                        exit()
        
        
        #tlo
        screen.blit(background, (0, 0))
        #aktywny button
        buttons[active_button] = font.render(captions[active_button], 1, (255,10,255)) #napis + kolor    
        screen.blit(buttons[active_button], (50,100+100*active_button)) #tekst + pozycja
        #stan coinsow
        text_coins = font2.render(coins_value, 1, (10, 10, 10))
        screen.blit(text_coins, (530,10))
        
        if win_value == '1':
            text_s = font2.render("Press together keys", 1, (10, 10, 255))
            screen.blit(text_s, (500,70))
            text_s = font2.render("s + p + a + m", 1, (10, 10, 255))
            screen.blit(text_s, (600,100))            
            text_s = font2.render("to watchthe ending again", 1, (10, 10, 255))
            screen.blit(text_s, (450,130))
         

        pygame.display.flip()
        
    game_status.close()


if __name__ == '__main__': main()
