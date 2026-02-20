import pgzrun 
import random

WIDTH = 400
HEIGHT = 400 

centrex = WIDTH/2
centrey = HEIGHT/2 
center = (centrex,centrey)
lvls = 5 
start_speed = 10 
Items = ["fish1","fish2","fish3","fish4"]
game_over = False
game_completed = False 
current_lvl = 1 
items = []
animations = []

def draw():
    global items,current_lvl,game_over,game_completed 
    screen.clear()
    screen.blit("ocean",(0,0))
    if game_over:
        display_message("GAME OVER!")
    elif game_completed:
        display_message("YOU WON!")
    else:
        for i in items:
            i.draw()
def update():
    global items 
    if len(items)== 0:
        items = make_items(current_lvl)
def make_items(extraitems):
    itemstocreate = optiontocreate(extraitems)
    new_items = createitems(itemstocreate)
    layout_items(new_items)
    animateitems(new_items)
    return new_items
def optiontocreate(extraitems):
    itemstocreate= ["plasticbag"]
    for i in range(0,extraitems):
        randomoption= random.choice(Items)
        itemstocreate.append(randomoption)
    return itemstocreate
def createitems(itemstocreate):
    newitems=[]
    for i in itemstocreate:
        item = Actor(i)
        newitems.append(item)
    return newitems
def layout_items(itemstolayout):
    gaps = len(itemstolayout)+1
    gapsize = WIDTH/gaps
    random.shuffle(itemstolayout)
    for i , j in enumerate(itemstolayout):
        newx = (i+1)*gapsize
        j.x = newx 

def animateitems(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration = start_speed-current_lvl
        i.anchor = ("center","bottom")
        animation = animate(i,duration= duration,on_finished=handlegameover,y=HEIGHT)
        animations.append(animation)
def handlegameover():
    global game_over
    game_over = True 
def display_message(t):
    screen.draw.text(t,fontsize=50,center=center,color = "white")

def on_mouse_down(pos):
    global items,current_lvl
    for i in items:
        if i.collidepoint(pos):
            if "plasticbag"in i.image:

                handlegamecomplete()
            else:
                handlegameover()
def handlegamecomplete():
    global current_lvl,items,animations,game_completed
    stopanimations(animations)
    if current_lvl == lvls:
        game_completed= True 
    else:
        current_lvl+= 1 
        items= []
        animations = []

def stopanimations(animationstostop):
    for i in animationstostop:
        if i.running:
            i.stop()







    
pgzrun.go()


