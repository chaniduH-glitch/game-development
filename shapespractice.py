import random
import pgzrun 

WIDTH = 500
HEIGHT = 400
def draw():

    screen.fill("black")
    w = 250
    h = 200 
    for i in range(15):
        
        a = Rect((250,200),(w,h))
        a.center = (WIDTH/2,HEIGHT/2)
        screen.draw.rect(a,"red")


        w-= 10 
        h+= 5
pgzrun.go() 
