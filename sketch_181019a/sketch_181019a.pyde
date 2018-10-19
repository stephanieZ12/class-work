#my screen froze and i was unable to save my
# progress so i had to start over
def setup():
    size(650,650)
    noStroke()

x = 0

def draw():
    global x
    if x >=650:
         x=0
    x += 2
        
    background(180,250,300)
    ellipse(x,90,100,100)
    
