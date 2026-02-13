import pgzrun

WIDTH = 600
HEIGHT = 500

mbox = Rect(0,0,590,50)
qbox = Rect(0,0,420,100)
tbox = Rect(0,0,100,100)
sbox = Rect(0,0,100,250)
abox1 = Rect(0,0,185,100)
abox2 = Rect(0,0,185,100)
abox3 = Rect(0,0,185,100)
abox4 = Rect(0,0,185,100)
abox = [abox1,abox2,abox3,abox4]

mbox.move_ip(0,0)
qbox.move_ip(30,70)
tbox.move_ip(470,70)
sbox.move_ip(470,200)
abox1.move_ip(30,200)
abox2.move_ip(250,200)
abox3.move_ip(30,350)
abox4.move_ip(250,350)


def draw():
    screen.clear()
    screen.fill("blue")
    screen.draw.filled_rect(mbox,"blue")
    screen.draw.filled_rect(qbox,"red")
    screen.draw.filled_rect(tbox,"yellow")
    screen.draw.filled_rect(sbox,"green")
    
    for i in abox:
        screen.draw.filled_rect(i,"orange")

pgzrun.go() 
        
