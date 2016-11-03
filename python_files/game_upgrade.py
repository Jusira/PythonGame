import os
import pygame

def main():
    #inicjalizacja ekranu
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Game')
    #dzwieki
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('sounds', 'menu.mp3'))
    pygame.mixer.music.play(loops = -1)
    
    last = pygame.time.get_ticks()
    first_enter = True
    enter = pygame.time.get_ticks()
    #kolor tla
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    
    rectangle = pygame.Surface(screen.get_size())
    rectangle = rectangle.convert()

    # Display some text
    font = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 50)
    font2 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 40)
    font3 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 80)
    
    
    text_coins = font3.render("UPGRADES", 1, (255, 10, 10))
    background.blit(text_coins, (10,10)) 
    
    text_coins = font3.render("Press ESC to back to  menu", 1, (255, 10, 10))
    background.blit(text_coins, (10,700)) 
    
    text_coins = font2.render("Coins:", 1, (10, 10, 10))
    background.blit(text_coins, (400,10)) 
    
   
    #wczytanie stanu gry
    game_status = open(os.path.join('other_data', 'game_status.txt'),'r')
    coins_value = game_status.readline().strip('\n\r') #wczytuje linie z pliku bez znaku konca linii
    
             
    #tabelka pozycji w menu 0-buy 1-select 2-selected 3-maxed, 4-menu
    positions = [["selected","buy for 50"],["selected","buy for 50","buy for 50"],["selected","buy for 50"],["upgrade for 10"],["upgrade for 10"],["upgrade for 10"]]
    
    settings = open(os.path.join('other_data', 'settings.txt'),'r')
    settings_values = [settings.readline().strip('\n\r') for i in range(11)]
    settings.close()
    
    def read_values():
        """aktualizuje wyswietlane napisy"""
        i = 0
        for j in range(len(positions)):
            for k in range(len(positions[j])):
                positions[j][k] = settings_values[i]
                i += 1
        return positions
    
   
    def save_changes():
        """zapisuje zmiany w ustawieniach do plików"""
        settings = open(os.path.join('other_data', 'settings.txt'),'w')
        for el in settings_values:
            settings.write(el + '\n')
        settings.close()
        
        game_status = open(os.path.join('other_data', 'game_status.txt'),'w')
        game_status.write(str(coins_value))
        game_status.close()
        
        upgrades = open(os.path.join('other_data', 'upgrades.txt'),'w')
        for el in upgrades_values:
            upgrades.write(str(el) + '\n')
        upgrades.close()
    
        
        

    act_pos = [0,0]
    
    upgrades = open(os.path.join('other_data', 'upgrades.txt'),'r')
    upgrades_values = [upgrades.readline().strip('\n\r') for i in range(3)]
    upgrades.close()
    positions_desc = [["GRASS","SNOW",],["ROBOT","NINJA 1","NINJA 2"],["ZOMBIES","CATS"],[upgrades_values[0]],[upgrades_values[1]],[upgrades_values[2]]]
    
    #tabelka niezmienialnych napisów
    caption_table = ["BACKGROUND", "PLAYER", "ENEMIES", "SHOOT SPEED", "LIFES", "MOVEMENT SPEED"]
    
      # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    screen.fill((0,0,0))
    last = pygame.time.get_ticks()
    
    def change_active_button(side,last):
        now = pygame.time.get_ticks()
        if now - last > 250: 
            last = pygame.time.get_ticks()
            if side == "down":
                if act_pos[0] < len(positions) - 1:
                    if act_pos[1] < len(positions[act_pos[0] + 1]):
                        return (act_pos[0] + 1, act_pos[1], last)
                    return (act_pos[0] + 1, len(positions[act_pos[0] + 1]) - 1, last)
            if side == "up":
                if act_pos[0] > 0:
                    if act_pos[1] < len(positions[act_pos[0] - 1]):
                        return (act_pos[0] - 1, act_pos[1], last)
                    return (act_pos[0] - 1, len(positions[act_pos[0] - 1]) - 1, last)
            if side == "right":
                if act_pos[1] < len(positions[act_pos[0]]) - 1:
                    return (act_pos[0], act_pos[1] + 1, last)
            if side == "left":
                if act_pos[1] >0:
                    return (act_pos[0], act_pos[1] - 1, last)
        return (act_pos[0], act_pos[1], last)
    
    def buy_upgrade(coins_value,last):
        now = pygame.time.get_ticks()
        if now - last > 300 and (int(coins_value)>=((int(upgrades_values[act_pos[0]-3])-1) * (10 + 15 * int(upgrades_values[act_pos[0] - 3])) + 10)) and int(upgrades_values[act_pos[0]-3]) < 7: # (x-1)*10 + 10 
            last = now
            coins_value = int(coins_value) - ((int(upgrades_values[act_pos[0]-3])-1) * (10 + 15 * int(upgrades_values[act_pos[0] - 3]))  + 10)
            upgrades_values[act_pos[0]-3] = int(upgrades_values[act_pos[0]-3]) + 1
        return (upgrades_values,coins_value, last)
    
    def update_values():
        """aktualizuje values biorac napisy z positions"""
        i = 0
        for j in range(len(positions)):
            for k in range(len(positions[j])):
                settings_values[i] = positions[j][k]
                i += 1
        return settings_values
    
    positions = read_values()
    
    game_active = 1
    # Event loop
    while game_active == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                return
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN and act_pos[0] == 6:
                return
                
        screen.blit(background, (0, 0))    
        keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
       
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                (act_pos[0], act_pos[1], last) = change_active_button("down", last)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
                (act_pos[0], act_pos[1], last) = change_active_button("up", last)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                (act_pos[0], act_pos[1], last) = change_active_button("right", last)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                (act_pos[0], act_pos[1], last) = change_active_button("left", last)
                
        if keys[pygame.K_RETURN]:
            now = pygame.time.get_ticks()
            if now - enter >250: #po to, zeby nie wciskal nam sie enter na poczatku
                if act_pos[0] <=2:
                    if positions[act_pos[0]][act_pos[1]] == "buy for 50" and int(coins_value) >= 50:
                        coins_value = int(coins_value) - 50
                        positions[act_pos[0]][act_pos[1]] = "select"
                    elif positions[act_pos[0]][act_pos[1]] == "select":
                        for j in range(len(positions[act_pos[0]])):
                            if positions[act_pos[0]][j] == "selected":
                                positions[act_pos[0]][j] = "select"
                        positions[act_pos[0]][act_pos[1]] = "selected"

                if 3 <= act_pos[0] :
                        (upgrades_values, coins_value, last) = buy_upgrade(coins_value,last)
            
        settings_values = update_values()        
                
    
        
        screen.fill((255,255,255))  
        pygame.draw.rect(screen,(10,10,255),(390,100 +act_pos[0]* 100,600,100),2)
        #stan coinsow
        text_coins = font2.render(str(coins_value), 1, (10, 10, 10))
        screen.blit(text_coins, (530,10))                 
        
        text_coins = font3.render("UPGRADES", 1, (255, 10, 10))
        screen.blit(text_coins, (10,10)) 
        text_coins = font3.render("Press ESC to go back to  menu", 1, (255, 10, 10))
        screen.blit(text_coins, (10,700)) 
        text_coins = font2.render("Coins:", 1, (10, 10, 10))
        screen.blit(text_coins, (400,10)) 
        
        
        j = 0
        for el in caption_table:
            text = font.render(str(el), 1, (10, 10, 255))
            screen.blit(text, (10 ,120 + j * 100))
            j += 1
            
        j = 0
        
        positions_desc = [["GRASS","SNOW",],["ROBOT","NINJA 1","NINJA 2"],["ZOMBIES","CATS"],[upgrades_values[0]],[upgrades_values[1]],[upgrades_values[2]]]
        
        for el in positions_desc:
            i = 0
            for cpt in el:
                text = font2.render(str(cpt), 1, (100, 100, 100))
                screen.blit(text, (400 + i* 200,120 + j * 100))
                i += 1
            j += 1
        if int(upgrades_values[0]) == 7:
            positions[3][0] = 'maxed'
        else:
            positions[3][0] = 'buy for %d' % ((int(upgrades_values[0])-1) * (10 + 15 * int(upgrades_values[0])) + 10)
        if int(upgrades_values[1]) == 7:
            positions[4][0] = 'maxed'
        else:
            positions[4][0] = 'buy for %d' % ((int(upgrades_values[1])-1) * (10 + 15 * int(upgrades_values[1])) + 10)
        if int(upgrades_values[2]) == 7:
            positions[5][0] = 'maxed'
        else:
            positions[5][0] = 'buy for %d' % ((int(upgrades_values[2])-1) * (10 + 15* int(upgrades_values[2])) + 10)
        
        j = 0
        for el in positions:
            i = 0
            for cpt in el:
                text = font2.render(str(cpt), 1, (10, 10, 10))
                screen.blit(text, (400 + i* 200,150 + j * 100))
                i += 1
            j += 1
            
        text = font2.render(str(positions[act_pos[0]][act_pos[1]]), 1, (255, 10, 255))
        screen.blit(text, (400 + act_pos[1]* 200, 150 + act_pos[0] * 100))
        
        setting_values = update_values()
       
        save_changes()
        
       
        pygame.display.flip()

    for event in pygame.event.get():   
        return
    
if __name__ == '__main__': 
    main()