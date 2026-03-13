import pgzrun
import random

WIDTH = 800
HEIGHT = 800

ship = Actor("galaga")
bullets = []
enemies = []

for i in range(5):
    for j in range(5):

        enemies.append(Actor("bug"))
        enemies[-1].x = 100+50*i
        enemies[-1].y = 80+50*j

ship.pos = (WIDTH//2,HEIGHT-60)
speed = 6
direction = 1

score = 0
ship.dead = False
ship.countdown = 90
def display_Score():
    screen.draw.text("SCORE ="+str(score),(500,30))


def game_over():
    screen.draw.text("GAME OVER",(250,30))

def on_key_down(key):
    if ship.dead == False:

        if key == keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y-50
def update():

    
    global score,direction
    move_down = False 
    if ship.dead == False:

        if keyboard.a:
            ship.x-= speed 
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.d:
            ship.x+= speed
            if ship.x >= WIDTH:
                ship.x = WIDTH
    for i in bullets:
        if i.y <= 0:
            bullets.remove(i)
        else:
            i.y-=10 
    if len(enemies) == 0:
        game_over()

        
    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x<80):
        move_down = True
        direction = direction*-1 


    for j in enemies:
        j.x+=5*direction
        if move_down == True:
            
            j.y+=50
        if j.y>HEIGHT:
            enemies.remove(j)

        
        for i in bullets:
            if j.colliderect(i):
                sounds.eep.play()
                score+=100
                bullets.remove(i)
                enemies.remove(j)
                if len(enemies)==0:
                    game_over()
        if j.colliderect(ship):
            ship.dead = True
    if ship.dead:
        ship.countdown-=1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90
def draw(): 
    screen.clear()
    screen.fill("darkblue")
    for i in bullets:
        i.draw()
    for j in enemies:
        j.draw()
    if ship.dead == False:
        ship.draw()
    display_Score()
    if len(enemies) == 0:
        game_over()

pgzrun.go()

                





        






