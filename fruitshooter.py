import pgzrun
import random

WIDTH = 600
HEIGHT = 400 

ship = Actor("galaga")
bullets = []
enemies = []
object  = Actor(random.choice(["fruit","bomb"]))

ship.pos = (WIDTH//2,HEIGHT-60)
speed = 10
object.x = random.randint(70,WIDTH-70)
object.y = -100
enemies.append(object)
score = 0

def display_Score():
    screen.draw.text("SCORE ="+str(score),(500,30))
    
def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-50
def update():
    global score
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
    for j in enemies:
        j.y+=5 
        if j.y > HEIGHT:
            j.y = -100
            j.x = random.randint(50,WIDTH-50)
        for i in bullets:
            if j.colliderect(i):
                sounds.eep.play()
                if j.image == "bomb":
                    score -=50 
                else:
                    score+=100
                    
                score+=100
                
                bullets.remove(i)
                enemies.remove(j)
                new = Actor(random.choice(["fruit","bomb"])) 
                new.x = random.randint(70,WIDTH-70)
                new.y = -100
                enemies.append(new)
def draw():
    screen.clear()
    screen.fill("darkblue")
    for i in bullets:
        i.draw()
    for j in enemies:
        j.draw()
    ship.draw()
    display_Score()

pgzrun.go()

                





        






