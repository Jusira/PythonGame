

import pygame                # importujemy biblioteki pygame
import os 
import random

    
class IsoGame(object):
    import random
    
    
                            ##########################   KLASY  ################################    
    class Bullet_player:
        def __init__(self,x,y):
            self.position_x = x
            self.position_y = y
            self.speed = 10
            self.height = 70 
            self.width = 85
            self.image = 0
                          
        
    class Enemy_zombie_male():
        def __init__(self,x,y):
            self.position_x = x
            self.position_y = y
            self.speed = 20
            self.height = 195
            self.width = 161
            self.coins = 1
            self.hp = 1
            self.image = 0
            

    class Enemy_zombie_female():
        def __init__(self,x,y):
            self.position_x = x
            self.position_y = y
            self.speed = 15
            self.height = 195
            self.width = 161
            self.coins = 2
            self.hp = 2
            self.image = 1
            
            
    class Enemy_Jack():
        def __init__(self,x,y):
            self.position_x = x
            self.position_y = y
            self.speed = 60
            self.height = 195
            self.width = 161
            self.coins = 1
            self.hp = 1
            self.image = 2
            
    class Player():
        def __init__(self,x,y,lifes, img1, img2, img3,create_time):
            self.position_x = x
            self.position_y = y
            self.hp = 1
            self.image=[]
            self.lifes=lifes
            self.player_image_shoot = img1
            self.player_image_run = img2
            self.bullet_animations = img3
            self.player_frame = 1 
            #lista pociskow
            self.bullet_list = []
            self.last_shoot = create_time
            self.last_life = create_time
            self.licznik_strzalu = 0
            self.shoot_now = False 
            self.shoot_now2 = False
            self.dead = False
            self.licznik = 0 # zmienna pomocnicza do liczenia wejść do ifa i odświeżania
 
            
                        ##########################   INIT ################################               
                      
    def __init__(self):
        pygame.init()       # incjalizujemy biblioteke pygame
        screen = pygame.display.set_mode((100,100))
        flag = pygame.DOUBLEBUF    # wlaczamy tryb podwojnego buforowania
 

        #muzyka
        los = self.random.randrange(3)
        pygame.mixer.init(frequency=22050,size=-16,channels=4)
        pygame.mixer.music.load(os.path.join('sounds', 'game%d.wav' % (los)))
        pygame.mixer.music.play(loops = -1)

        #wczytujemy dane:
        settings = open(os.path.join('other_data', 'settings.txt'),'r')
        self.settings_values = [settings.readline().strip('\n\r') for i in range(11)]
        settings.close()
        upgrades = open(os.path.join('other_data', 'upgrades.txt'),'r')
        upgrades_values = [upgrades.readline().strip('\n\r') for i in range(3)]
        upgrades.close()
        
        #ustawiamy predkosci
        self.player_cooldown = 60 #szybkosc gry
        self.shoot_cooldown = 2000 - 250* int(upgrades_values[0])
        self.speed = 3 * int(upgrades_values[2])  #szybkosc poruszania gracza
        self.lifes = int(upgrades_values[1])
        self.life_image = pygame.image.load(os.path.join('images/life', 'life.png'))
        
        #ustawiamy czas
        self.clock = pygame.time.Clock()
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        
        # tworzymy bufor na  grafike
        self.surface = pygame.display.set_mode((1500,1000),flag)  # ustalamy rozmiar ekranu
         
        #lista przeciwnikow
        self.enemy_list = []
        #lista martwych przeciwnikow
        self.dead_enemy_list = []
        
            
        #tekstury tła
        if self.settings_values[1] == 'selected':
                self.grass_image = pygame.image.load(os.path.join('images/textures', 'snow.jpg')) #snieg
        else:
            self.grass_image = pygame.image.load(os.path.join('images/textures', 'grass.png')) #trawa
        self.grass_positions = [[0,0],[1000,0],[2000,0]] #pozycje trawy
        
        #panel
        self.panel_image = pygame.image.load(os.path.join('images', 'panel2.png')) #trawa
        
        
        #czcionka coins
        self.font2 = pygame.font.Font(os.path.join('other_data', 'From Cartoon Blocks.ttf'), 50)
        self.actual_coins_status = 0
        self.text_coins = self.font2.render("Coins:", 1, (255, 255, 255))
        
        #tablica animacji przeciwnikow:
        if self.settings_values[5] == 'selected':
            self.animations = [[pygame.image.load(os.path.join('images/zombie_male', 'Walk%d.png' % i)) for i in range(1,11)], #zombie_male_walk
                  [pygame.image.load(os.path.join('images/zombie_male', 'rsz_1rsz_dead%d.png' % i)) for i in range(1,13)], #zombie_male_dead
                  [pygame.image.load(os.path.join('images/zombie_female', 'rsz_1rsz_walk_%d.png' % i)) for i in range(1,11)], #zombie_female_walk
                  [pygame.image.load(os.path.join('images/zombie_female', 'rsz_1rsz_dead_%d.png' % i)) for i in range(1,13)],
                  [pygame.image.load(os.path.join('images/Jack', 'rsz_rsz_1rsz_run_%d.png' % i)) for i in range(1,9)],
                  [pygame.image.load(os.path.join('images/Jack', 'rsz_rsz_1rsz_dead_%d.png' % i)) for i in range(1,11)]]
        else:
            self.animations = [[pygame.image.load(os.path.join('images/Cat', 'rsz_1rsz_run_%d.png' % i)) for i in range(1,9)], 
                  [pygame.image.load(os.path.join('images/Cat', 'rsz_1rsz_dead_%d.png' % i)) for i in range(1,11)], 
                  [pygame.image.load(os.path.join('images/Dog', 'rsz_rsz_run_%d.png' % i)) for i in range(1,8)], 
                  [pygame.image.load(os.path.join('images/Dog', 'rsz_rsz_dead_%d.png' % i)) for i in range(1,11)],
                  [pygame.image.load(os.path.join('images/Jack', 'rsz_rsz_1rsz_run_%d.png' % i)) for i in range(1,9)],
                  [pygame.image.load(os.path.join('images/Jack', 'rsz_rsz_1rsz_dead_%d.png' % i)) for i in range(1,11)]]
            
            
                
        #odmierzamy fragmenty czasu
        self.last = pygame.time.get_ticks()
        self.last_enemy = pygame.time.get_ticks()
        self.now = pygame.time.get_ticks()
        
        # zmienna stanu gry
        self.gamestate = 1  # 1 - run, 0 - exit
        
        
        
        if self.settings_values[2] == 'selected':
            self.player_image_shoot = [pygame.image.load(os.path.join('images/robot_shoot', 'rsz_1rsz_runshoot%d.png' % i)) for i in range(5,10)]
            player_image_run = [pygame.image.load(os.path.join('images/robot_run', 'Run(%d).png' % i)) for i in range(1,9)] 
            self.bullet_animations = [pygame.image.load(os.path.join('images/bullet', 'rsz_bullet_00%d.png' % i)) for i in range(0,5)]
        
        if self.settings_values[3] == 'selected':
            self.player_image_shoot = [pygame.image.load(os.path.join('images/ninja_female', '/home/alicja/Alicja/PADPy2016/repozytoria/RiverRide_PythonGame/images/ninja_female/rsz_1rsz_throw__00%d.png' % i)) for i in range(5)]
            player_image_run = [pygame.image.load(os.path.join('images/ninja_female', 'rsz_1rsz_run__00%d.png' % i)) for i in range(10)] 
            self.bullet_animations = [pygame.image.load(os.path.join('images/kunai', 'Kunai.png')) for i in range(1)]   
        
        if self.settings_values[4] == 'selected':
            self.player_image_shoot = [pygame.image.load(os.path.join('images/ninja_male', 'rsz_rsz_throw__00%d.png' % i)) for i in range(5)]
            player_image_run = [pygame.image.load(os.path.join('images/ninja_male', 'rsz_rsz_run__00%d.png' % i)) for i in range(10)] 
            self.bullet_animations = [pygame.image.load(os.path.join('images/kunai', 'Kunai.png')) for i in range(1)]   
        
        
        
        self.Player_1 = self.Player(50, 500, self.lifes,
                          self.player_image_shoot,
                           player_image_run ,
                          self.bullet_animations,
                          pygame.time.get_ticks())
           
        
            
         
        self.licznik_przeciwnikow = 1
        self.licznik=0
        self.bl_rect= 0
        self.en_rect = 0
        
        
        self.loop()    # glowna petla gry
    
    
    
    
                        ##########################   FUNKCJE ################################    


    def coins_for_kill(self,en):
        self.actual_coins_status += en.coins
    
    def collision(self,x1,y1,w1,h1,x2,y2,w2,h2): #sprawdza kolizję z duszkiem
        if x1 >= x2+w2: return True
        if x1+w1 <= x2: return True
        if y1 >= y2+h2: return True
        if y1+h1 <= y2: return True
        return False
    
    def screen_collision(self, x,y): #sprawdza kolizję z końcem ekranu
        if x <= -50 or x >= 1320: return True
        if y <= -20 or y >= 800: return True
        return False
    
    def bullets_collisions(self,Player):
        for bl in Player.bullet_list:
            self.bl_rect = pygame.Rect(bl.position_x, bl.position_y, bl.width, bl.height)
            bl_used = False
            for en in self.enemy_list:
                if bl_used == False:
                    self.en_rect = pygame.Rect(en.position_x, en.position_y, en.width, en.height)
                    if self.bl_rect.colliderect(self.en_rect):
                        en.hp -= 1
                        Player.bullet_list.remove(bl)
                        bl_used = True
                        if en.hp == 0:
                            self.enemy_kill(en)
                            self.coins_for_kill(en)
                            current_game = open(os.path.join('other_data', 'current_game.txt'),'w')
                            current_game.write(str(self.actual_coins_status))
                            current_game.close()

                        
    def player_collisions(self,Player):
        self.pl_rect = pygame.Rect(Player.position_x, Player.position_y - 50, 100, 130)
        now = pygame.time.get_ticks()
        for en in self.enemy_list:
            self.en_rect = pygame.Rect(en.position_x, en.position_y - 50, en.width - 100, en.height - 60)
            if self.pl_rect.colliderect(self.en_rect) and now - Player.last_life > 500:
                self.enemy_kill(en)
                Player.last_life = now
                if Player.lifes == 1:
                    Player.lifes = 0
                    Player.dead = True
                    Player.position_y = - 500
                else:
                    Player.lifes -= 1
                    
                    

    def enemy_kill(self,en):
        los = self.random.randrange(6)
        sound = pygame.mixer.Sound(os.path.join('sounds', 'hit%d.wav' % (los)))
        chan1 = pygame.mixer.Channel(2)
        chan1.queue(sound)
        self.dead_enemy_list.append([0,en])
        self.enemy_list.remove(en)
        
    def death_animation(self):
        for en in self.dead_enemy_list:
            if en[0] < len(self.animations[2*en[1].image+1]):
                self.surface.blit(self.animations[2*en[1].image + 1][en[0]],(en[1].position_x - 10 * en[0],en[1].position_y))
                en[0] += 1
            else:
                self.dead_enemy_list.remove(en)
        
    
    def move(self,Player,dirx,diry):
        dx = Player.position_x + (dirx * self.speed)
        dy = Player.position_y + (diry * self.speed)
        if self.screen_collision(dx,dy):
            return
        Player.position_x = dx
        Player.position_y = dy
        
    def player_shoot(self,Player):
        if Player.licznik == 1:
            Player.player_frame = (Player.player_frame +1) % 1000
        else:
            Player.licznik = 1
        self.surface.blit(Player.player_image_shoot[Player.player_frame % 4],(Player.position_x,Player.position_y))
        if Player.licznik_strzalu == 4:
                Player.licznik_strzalu = 0
                Player.shoot_now2 = False
        Player.licznik_strzalu += 1
    
    def enemy_create(self):
        '''losowo tworzymy przeciwnika'''
        now = pygame.time.get_ticks()
        if now - self.last_enemy > 1500//(1 + 0.005 *self.licznik_przeciwnikow):
            self.last_enemy = now
            self.licznik_przeciwnikow += 1
            #tworzymy zwykle zombiaki
            for i in range(abs(int(self.random.normalvariate(1, min(self.licznik_przeciwnikow/100,2.5))))):
                self.enemy_list.append(self.Enemy_zombie_male(1500,self.random.randrange(0,800,80)))
            #tworzymy female zombie
            if self.minutes > 0:
                for i in range(abs(int(self.random.normalvariate(1, min(self.licznik_przeciwnikow/300,2))))):
                    self.enemy_list.append(self.Enemy_zombie_female(1500,self.random.randrange(0,800,80)))
            if self.minutes > 2:
                for i in range(abs(int(self.random.normalvariate(1, min(self.licznik_przeciwnikow/500,1))))):
                    self.enemy_list.append(self.Enemy_Jack(1500,self.random.randrange(0,800,80)))
                
    
    def enemy_move(self):
        """rusza przeciwnikiem"""
        for en in self.enemy_list:
            en.position_x -= en.speed
            
    def enemy_update(self):
        """usuwa przeciwnikow ktorzy wyszli poza plansze lub zostali zabici"""
        for en in self.enemy_list:
            if en.position_x < -200:
                self.enemy_list.remove(en)
        
    def enemy_refresh(self,Player):
        """odswieza przeciwnikow"""
        for en in self.enemy_list:
            self.surface.blit(self.animations[2*en.image][(Player.player_frame)% len(self.animations[2*en.image])],(en.position_x,en.position_y)) 

         
 
    def player_refresh(self,Player):
        ''' odswieza animacje gracza jezeli minelo wystarczajaco duzo czasu od ostatniego ticka'''
        if Player.licznik == 1:
            Player.player_frame = (Player.player_frame +1) % 1000
        else:
            Player.licznik = 1
        self.surface.blit(Player.player_image_run[Player.player_frame % 8],(Player.position_x,Player.position_y)) # umieszczamy gracza
    
    def grass_refresh(self):
        """odswieza pozycje trawy"""
        for i in self.grass_positions:
            self.surface.blit(self.grass_image,i)
            if i[0] > -1000:
                i[0] -= 10
            else:
                i[0] = 2000
                
    def bullet_move(self,Player):
        """rusza pociskiem"""
        for en in Player.bullet_list:
            en.position_x += 40
            
    def bullet_update(self,Player):
        """Usuwa pociski ktore poza plansze"""
        for en in Player.bullet_list:
            if en.position_x > 2500:
                Player.bullet_list.remove(en)
        
    def bullet_refresh(self,Player):
        """odswieza pociski"""
        for en in Player.bullet_list:
            self.surface.blit(Player.bullet_animations[(Player.player_frame)% len(Player.bullet_animations)],(en.position_x,en.position_y)) 
        
    
                
    def game_player_refresh(self,Player,now,life):      
        #sprawdzamy kolizje
        self.bullets_collisions(Player)
        self.enemy_refresh(Player)
        #odswiezamy gracza
        self.player_collisions(Player)
        if now - Player.last_shoot >= self.shoot_cooldown and Player.shoot_now == True:
            sound = pygame.mixer.Sound(os.path.join('sounds', 'gun.wav'))
            chan1 = pygame.mixer.Channel(1)
            chan1.queue(sound)
            Player.bullet_list.append(self.Bullet_player(Player.position_x + 100,Player.position_y + 60))
            Player.last_shoot = now
        Player.shoot_now = False    
        if Player.shoot_now2 == True:
            self.player_shoot(Player)
        else:
            self.player_refresh(Player)
        #odswiezamy pociski
        self.bullet_move(Player)
        self.bullet_update(Player)
        self.bullet_refresh(Player)
        for i in range(Player.lifes):
            self.surface.blit(self.life_image,(950 + i * 70, 60*(life-1)))
        text_life = self.font2.render("Player %d :" % (life), 1, (255, 255, 255))
        self.surface.blit(text_life,(700, 60*(life-1)))
        
    def game_refresh(self,now):
        """odświeża cały ekran gry"""
        self.surface.fill((0,0,0)) # czyscimy ekran, malo wydajne ale wystarczy 
            #odswiezamy tlo          
        self.grass_refresh()
        self.surface.blit(self.panel_image,(0,-5)) 
            #odswiezamy przeciwnikow
        self.enemy_move()
        self.enemy_update()
        self.death_animation()
            
        self.surface.blit(self.text_coins, (140,20))
            #odswiezamy coinsy
        self.coins_value = self.font2.render(str(self.actual_coins_status), 1, (255, 255, 255))
        self.surface.blit(self.coins_value, (280,20))
            #odswiezamy czas
            
        if self.seconds > 50:
            time = self.font2.render(str(4 - self.minutes) + ":0" + str(60 - self.seconds), 1, (255, 255, 255))
        else:
            time = self.font2.render(str(4 - self.minutes) + ":" + str(60 - self.seconds), 1, (255, 255, 255))
        self.surface.blit(time,(15,20))
            
    
    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()
 
    def loop(self):
        """ glowna petla gry """
        while self.gamestate==1:           
            for event in pygame.event.get():
                if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                    self.gamestate = 0
                    exec(open(os.path.join('python_files','game_end.py')).read())
                    exit()
           
            if self.Player_1.dead == True:
                 pygame.time.delay(1000)
                 self.gamestate=0
                 exec(open(os.path.join('python_files','game_end.py')).read())
                 exit()
            
            keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
 
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
               self.move(self.Player_1,0,1)  # ruch w dol
            if keys[pygame.K_UP] or keys[pygame.K_w]:
               self.move(self.Player_1,0,-1)   # ruch w gore
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
               self.move(self.Player_1,1,0)  # ruch w prawo
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
               self.move(self.Player_1,-1,0)   # ruch w lewo
               
            if keys[pygame.K_SPACE] or keys[pygame.K_l]:
                self.Player_1.shoot_now = True   # animacja strzalu
                self.Player_1.shoot_now2 = True 
                
                
            self.enemy_create()
            
            # odliczamy czas
            if self.milliseconds > 1000:
                self.seconds += 1
                self.milliseconds -= 1000
            if self.seconds > 60:
                self.minutes += 1
                self.seconds -= 60
                
            self.milliseconds += self.clock.tick_busy_loop(60)
          
            self.now = pygame.time.get_ticks()
            if self.now - self.last >= self.player_cooldown:
                self.game_refresh(self.now)
                if self.Player_1.dead==False:
                    self.game_player_refresh(self.Player_1,self.now, 1)
                self.last = self.now
            pygame.display.flip()  
            
            if self.minutes == 5:
                self.gamestate=0
                exec(open(os.path.join('python_files','cong.py')).read())
                exit()
            
                
 
        self.game_exit()
 


if __name__ == '__main__':
   IsoGame()
   