import pgzrun 
import random 
WIDTH = 600
HEIGHT = 600
alien = Actor("alien")
msg = ""
def draw():
    screen.fill("black")
    alien.draw()  
    screen.draw.text(msg,center=(400,10))
    

def update():
    if keyboard.left:
        alien.x-=10
    elif keyboard.right:
        alien.x+=10
    elif keyboard.up:
        alien.y-=10 
    elif keyboard.down:
        alien.y+=10
def rand_alien():
    alien.x = random.randint(50,550)
    alien.y= random.randint(80,520)
def on_mouse_down(pos):
    global msg 
    if alien.collidepoint(pos):
        msg = "Good Shot!"

        
        rand_alien() 
    else:
        msg = "You Missed!"
        
        



pgzrun.go() 





