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
    background(230,230,240)
    noStroke()
    fill(210,210,200)
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

    fill(100,100,100)
    rect(0,550,650,550)
    
    
    import random 
    q= random.randint(1,650)
    a= random.randint(1,650)
    b= random.randint(1,650)
    c= random.randint(1,650)
    d= random.randint(1,650)
        
    


    if x >650:
        x=0
    x +=1
    fill(150,150,240)
    ellipse(q,x+50,8,14)
    ellipse(a,x+180,8,14)
    ellipse(b,x+260,8,14)
    ellipse(c,x+600,8,14)
    ellipse(d,x+360,8,14)
    ellipse(q,x-50,8,14)
    ellipse(a,x-180,8,14)
    ellipse(b,x-260,8,14)
    ellipse(c,x-600,8,14)
    ellipse(d,x-360,8,14)
    
    fill(0)
    arc(400,480,175,150, 0, PI+QUARTER_PI, CHORD);
    fill(230,230,240)
    ellipse(415,450,60,60)
    ellipse(465,480,60,60)
    ellipse(365,420,60,60)
    
    stroke(0)
    strokeWeight(3)
    line(390,495,490,340);


    


    

    
