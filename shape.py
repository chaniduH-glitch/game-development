import pgzrun 
import random

WIDTH = 500
HEIGHT = 400
def draw():
    screen.fill("black")
    w = 250
    h = 200
    for i in range(15):
       a = Rect((250,200),(w,h))
       r = random.randint(0,255)
       g = random.randint(0,255)
       b = random.randint(0,255)

       a.center = (WIDTH/2,HEIGHT/2)
       screen.draw.rect(a,(r,g,b))
       w-= 10 
       h+= 5
pgzrun.go() 
