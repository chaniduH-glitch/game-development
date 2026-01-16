import pgzrun 
import random

WIDTH = 600
HEIGHT = 400

bee = Actor("bee") 
bee.pos = 300,0
flower = Actor("flower")
flower.pos = 200,100 
score = 0 
game_over = False
def draw():
    screen.blit("grass_bg",(0,0))
    
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),color = "black",midtop = (300,10)) 
    if game_over:
        screen.fill("red")
        screen.draw.text("Your time is Up your score is "+str(score),color = "black",midtop = (300,10))

def rand_flower():
    flower.x = random.randint(70,530)
    flower.y = random.randint(70,320)

def update():
    global score 
    if keyboard.left:
        bee.x-=10
    elif keyboard.right:
        bee.x+=10
    elif keyboard.up:
        bee.y-=10
    elif keyboard.down:
        bee.y+=10
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score+=2
        rand_flower()

def time_up():
    global game_over 
    game_over = True  

       

clock.schedule(time_up,60.0)
pgzrun.go() 


