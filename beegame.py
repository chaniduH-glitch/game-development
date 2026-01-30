import pgzrun
import random

WIDTH = 600
HEIGHT = 400
flowers = []
lines = []
next_flowers = 0
numberofflowers = 10

def create_flowers():
    for i in range(numberofflowers):

        
        flower = Actor("flower")
        flower.pos = random.randint(40,560),random.randint(40,360)
        flowers.append(flower)




def draw():

    number = 1
    screen.blit("grass_bg",(0,0)) 
    for i in flowers:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+35),color = "black")

        i.draw()
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")

def on_mouse_down(pos):
    global next_flowers,lines
    if next_flowers < numberofflowers:
        if flowers[next_flowers].collidepoint(pos):
            if next_flowers:
                lines.append((flowers[next_flowers-1].pos,flowers[next_flowers].pos))
            next_flowers+=1
        else:
            lines = []
            next_flowers = 0 



            
    

create_flowers()
pgzrun.go()

