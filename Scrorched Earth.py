import pygame as pg
import random
from win32api import GetSystemMetrics as GSM
from math import cos, sin, radians, sqrt, atan2, pi
import time


#~~~~~~~~~~~~~~~Definitions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def draw_background():
        screen.fill((255, 160, 228))

        return

def draw_tank(player_number):
  # Tank is 25 pixels breed      
        p1 = (playersinfo[player_number]["Position"+str(i)], 711)
        p2 = (playersinfo[player_number]["Position"+str(i)] + 5, 714)
        p3 = (playersinfo[player_number]["Position"+str(i)] + 20, 714)
        p4 = (playersinfo[player_number]["Position"+str(i)]+ 25, 711)
        p5 = (playersinfo[player_number]["Position"+str(i)] + 25, 707)
        p6 = (playersinfo[player_number]["Position"+str(i)] + 20, 704)
        p10 = (playersinfo[player_number]["Position"+str(i)] + 5, 704)
        p11 = (playersinfo[player_number]["Position"+str(i)], 707)
        pointlist1 = [p1, p2, p3, p4, p5, p6, p10, p11]       
        pg.draw.polygon(screen, playersinfo[player_number]["Color"+str(i)], pointlist1, 0)

        #nozzle
        gamma = playersinfo[player_number]["Angle"+str(i)]
        p7 = (playersinfo[player_number]["Position"+str(i)] + 13, 704)
        a = 13 + 11*cos(radians(gamma))
        b = 704 - 11*sin(radians(gamma))
        p8 = (playersinfo[player_number]["Position"+str(i)] + a, b)
        
        pointlist2 = p7, p8      
        pg.draw.polygon(screen, playersinfo[player_number]["Color"+str(i)], pointlist2, 1)

        return p5, p11, p8


def draw_text(player_number):
        text = font.render("Player"+str(i)+":"+ playersinfo[player_number]["Name"+str(i)] +" Power:"+ str(playersinfo[player_number]["Power"+str(i)]) +" Angle:"+str(playersinfo[player_number]["Angle"+str(i)]), 1, (playersinfo[player_number]["Color"+str(i)]), None)
        screen.blit(text, (10,10))
       
        return

def draw_missle_traj(player_number):
        # Constants
        g = 9.81
        rho = 1.225
        Cd = 0.7
        S = 0.005
        m = 1.0
        const = 1
        dt = 0.01
        # Initial values
        gamma = playersinfo[player_number]["Angle"+str(i)]

        v = const * playersinfo[player_number]["Power"+str(i)]
        vx = v * cos(radians(gamma))
        vy = -v * sin(radians(gamma))
        
        tankBegin = draw_tank(player_number)[0][0]
        tankEnd = draw_tank(player_number)[1][0]
        nozzleEndx = draw_tank((player_number))[2][0]
        nozzleEndy = draw_tank((player_number))[2][1]
        
        x = nozzleEndx
        y = nozzleEndy
        coordinates = (x,y)

        while 0 < y < 714 :
                 Fg = m*g
                 Fdrag = Cd*0.5*rho* v**2 *S
                 Fx = -sin(radians(gamma)) * Fdrag
                 Fy = Fg + (cos(radians(gamma))*Fdrag)

                 ax = Fx / m
                 ay = Fy / m

                 vx = vx + (ax*dt)
                 vy = vy + (ay*dt)

                 v = sqrt(vx**2 + vy**2)
                 gamma = atan2(vy,vx)

                 x = x + (vx*dt)
                 y = y + (vy*dt)

                 position = (x,y)
                 traj_line = pg.draw.line(screen, (0,0,0), position, coordinates)
                 coordinates = position
                 pg.display.update()

                
        players = [len(playersinfo)]
        hit_player_number = -1
        for j in range(nplayers):
                if int(playersinfo[j].get("Position"+str(j))) <= x <= (int(playersinfo[j].get("Position"+str(j)) + 25)):
                        hit_player_number = j
                                                          
 
        return


        

#~~~~~~~~~~~~~~~MAIN PROGRAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Number and names of players
playersinfo = []
nplayers = int(input("Start game with how many players?"))

# State keeping
colorsneat = list(dict.values(pg.color.THECOLORS))

for i in range(nplayers):   
       player = {"Name"+str(i) : raw_input("Enter name for player"+str(i)+":"), "Color"+str(i):  random.choice(colorsneat), "Position"+str(i): random.randrange(0, 1511, 27), "Power"+str(i): 100, "Angle"+str(i): 30}
       playersinfo.append(player)
print(playersinfo)


# Openening PYGAME
pg.init()

width = GSM(0)
height = GSM(1)
reso = (width, height)
# Reso = (x,y) = (1536,864)
screen = pg.display.set_mode(reso)
font = pg.font.SysFont("Arial", 20)

running = True
playernr = 0
while running:

        time.sleep(0.02)
        
        # Background and ground
        draw_background()
        pg.draw.polygon(screen, (119, 118, 125), [(1536,864), (0,864), (0,714), (1536,714), (1536,864)], 0)

        players = len(playersinfo)
   
        for i in range(players):
                draw_tank(i)
                draw_text(i)
                draw_missle_traj(i)
                

        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
                running = False
       
                       
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        running = False
                elif event.type == pg.KEYDOWN:
                        UpdateScreen = True
                        if players < 2:
                               running = False
                               
                        if (event.key == pg.K_LEFT):
                                playersinfo[playernr]["Angle"+str(i)] + 1
                                if playersinfo[playernr]["Angle"+str(i)] > 180:
                                        playersinfo[playernr]["Angle"+str(i)] = 180        
                                UpdateScreen = True
                                
                        elif (event.key == pg.K_RIGHT):
                                playersinfo[playernr]["Angle"+str(i)] - 1
                                if playersinfo[playernr]["Angle"+str(i)] < 0:
                                        playersinfo[playernr]["Angle"+str(i)] = 0
                                UpdateScreen = True
                                
                        elif (event.key == pg.K_UP):
                                playersinfo[i]["Power"+str(i)] = playersinfo[i]["Power"+str(i)] + 1
                                UpdateScreen = True
                                
                        elif (event.key == pg.K_DOWN):
                                playersinfo[i]["Power"+str(i)] = playersinfo[i]["Power"+str(i)] - 1
                                UpdateScreen = True
                                
                        elif (event.key == pg.K_SPACE):
                                draw_background()
                                for i in range(nrplayersleft):
                                        draw_text(i)
                                        draw_tank(i)
                                hit_player_number,x = draw_missle_traj(playernr)
                                        
                        
               
        playernr += 1
        if playernr > nplayers:
                playernr = 0
        pg.display.update()

                        
           
# Closing PYGAME
pg.quit()

