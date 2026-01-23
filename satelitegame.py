import pgzrun
import random

WIDTH = 600
HEIGHT = 400
satelites = []
lines = []
next_satelite = 0
numberofsatelites = 10

def create_satelite():
    for i in range(numberofsatelites):

        
        satelite = Actor("satelite")
        satelite.pos = random.randint(40,560),random.randint(40,360)
        satelites.append(satelite)




def draw():

    number = 1
    screen.blit("space",(0,0)) 
    for i in satelites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+15))
        i.draw()
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")

def on_mouse_down(pos):
    global next_satelite,lines
    if next_satelite < numberofsatelites:
        if satelites[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((satelites[next_satelite-1].pos,satelites[next_satelite].pos))
            next_satelite+=1
        else:
            lines = []
            next_satelite = 0
            
    

create_satelite()
pgzrun.go()

