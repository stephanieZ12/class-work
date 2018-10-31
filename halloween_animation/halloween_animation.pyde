def setup():
    size(650,650)
    global sat_img
    sat_img=loadImage("ghost_PNG12.png");
    
transparency = 0
def draw():
    background(0) 
    fill(40,40,40)
    noStroke()
    triangle(325,310,100,650,550,650)
    stroke(200,40,40)
    strokeWeight(15)
    fill(240,50,50)
    rect(225,100,200,350)
    strokeWeight(8)
    fill(240,60,60)
    rect(255,120,50,80)
    rect(345,120,50,80)
    rect(255,230,50,80)
    rect(345,230,50,80)
    rect(255,340,50,80)
    rect(345,340,50,80)
    fill(255,215,0)
    strokeWeight(4)
    stroke(270,160,10)
    ellipse(407,280,12,12)
    
    textSize(30)
    fill(200,200,200,transparency)
    text("knock...",500,200)
    
    fill(200,200,200,transparency-100)
    text("knock",450,300)
    
    fill(0,0,0,transparency-200)
    rect(0,0,650,650)
    


def mousePressed(): 
    global transparency
    if transparency == 0:
        transparency = 100
    elif transparency == 100:
        transparency = 200
    elif transparency ==200:
        transparency = 500
        image(sat_img,150,100,400,400)
    else:
        transparency = 0

        

    
