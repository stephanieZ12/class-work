#my screen froze and i was unable to save my
# progress so i had to start over
def setup():
    size(650,650)
    noStroke()

x = 0
y = 0
def draw():
    global x
    if x >950:
         x=0
    x += 2
    global y
    if y >650:
        y=0
    y +=1
    background(180,225,300)
    
    fill(300,300,300)
    ellipse(x-200,100,50,50)
    ellipse(x-225,90,60,60)
    ellipse(x-250,110,30,30)
    
    ellipse(x,200,70,70)
    ellipse(x+50,220,100,100)
    ellipse(x+100,205,115,115)
    ellipse(x+150,230,60,60)
    
    ellipse(y,150,50,50)
    ellipse(y+25,130,60,60)
    ellipse(y+50,140,30,30)


    rect(0,550,650,550)

    

    
