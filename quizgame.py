import pgzrun

WIDTH = 600
HEIGHT = 500


index = 0
count = 0 
questions = []
game_over = False 
score  = 0
timeleft = 10
question_File = "C:\\Users\\chami\\OneDrive\\Desktop\\game developement__\\questions.txt"
message = ""


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
    global message
    screen.clear()
    screen.fill("blue")
    screen.draw.filled_rect(mbox,"blue")
    screen.draw.filled_rect(qbox,"red")
    screen.draw.filled_rect(tbox,"yellow")
    screen.draw.filled_rect(sbox,"green")
    
    for i in abox:
        screen.draw.filled_rect(i,"orange")
    message =  "Quiz Game "+f"Q:{index}of{count}"
    screen.draw.textbox(message,mbox,color = "white") 
    screen.draw.textbox(str(timeleft),tbox,color="black")
    screen.draw.textbox("Skip",sbox,color="white")
    screen.draw.textbox(question[0].strip(),qbox,color="black")
    i = 1
    for j in abox:
        screen.draw.textbox(question[i].strip(),j,color="black")
        i +=1 
def update():
    move_message()
def move_message():
    mbox.x = mbox.x-2
    if mbox.right<0:
        mbox.left = WIDTH
def read_question():
    global count,questions
    file=open(question_File,"r")
    for i in file:
        questions.append(i)
        count+=1
    file.close()

def read_next_question():
    global index 
    index +=1
    return questions.pop(0).split(",")
def on_mouse_down(pos):
    i =1
    for j in abox:
        if j.collidepoint(pos):
            if i is int(question[5]):
                correct_answer()
            else:
                gameover()
        i+=1
    if sbox .collidepoint(pos):
        skip_question()

def correct_answer():
    global score,question,questions,timeleft
    score+=1
    if questions:
        question = read_next_question()
        timeleft = 10
    else:
        gameover()
def gameover():
    global question,timeleft,game_over
    m = f"GAME OVER! YOU GOT {score}questions correct"
    question = [m,"-","-","-","-",5]
    timeleft = 0 
    game_over=True
    







       



        
read_question()
question = read_next_question()
pgzrun.go() 

