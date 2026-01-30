import pgzrun 
import random

WIDTH = 600
HEIGHT = 400

spaceship = Actor("spaceship") 
spaceship.pos = 300,0
star = Actor("star")
star.pos = 200,100 
score = 0 
game_over = False
def draw():
    screen.blit("space",(0,0))

    spaceship.draw()
    star.draw()
    screen.draw.text("score:"+str(score),color = "white",midtop = (300,10))
    if game_over:
        screen.fill("red")
        screen.draw.text("your time is up your score is "+str(score),color="white",midyop = (300,10))
def rand_star():
    star.x = random.randint(70,530)
    star.y = random.randint(70,320)
def update():
    global score 
    if keyboard.left:
        spaceship.x-=10
    elif keyboard.right:
        spaceship.x+=10
    elif keyboard.up:
        spaceship.y-=10
    elif keyboard.down:
        spaceship.y+=10
    star_collected = spaceship.colliderect(star)
    if star_collected:
        score+=2
        rand_star()
def time_up():
    global game_over 
    game_over = True 

clock.schedule(time_up,60.0)
pgzrun.go()
    
        


                         

    




    
   