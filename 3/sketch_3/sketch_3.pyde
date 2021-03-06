def setup(): 
    size(400, 400) 
    textSize(100)   
    strokeWeight(3)
    global b
    b=False
    
def draw():  

    clear()
    background(255, 153, 153)
    global b

    text("R", width/2-50, height/2)
    c = get(mouseX, mouseY)
    print(hex(c))
    print(keyPressed)
    
    if (c == -1):
        text("R", width/2-50, height/2)
        fill(255, 102, 153)
    text("R", width/2-50, height/2)
    fill(255, 255, 255)
    text("B", width/2+50, height/2)
    
    if keyPressed and (c == -1):
        if keyCode == 39:
            fill(255, 255, 255)
            text("R", width/2-50, height/2)
            fill(213, 93, 173)
            text("B", width/2+50, height/2)

    if keyPressed:
        if key == "b" or key == "B":
            text("B", width/2+50, height/2)
            fill(213, 93, 173)
            b=True
    
        if keyCode == 37 and b:
            fill(255, 102, 153)
            text("R", width/2-50, height/2)
            fill(255, 255, 255)
    else:
        b=False
   
    text("B", width/2+50, height/2)
    fill(255, 255, 255)
    
    if keyPressed:
        if key == "r" or key == "R":
            fill(255, 102, 153)
                                                                                                                
    x = createShape()  
    x.beginShape()  
    x.fill(255, 230, 230)  
    x.stroke(218, 179, 255) 
    x.beginShape(); 
    x.vertex(20, 30) 
    x.vertex(70, 40) 
    x.vertex(50, 60) 
    x.vertex(120, 80) 
    x.vertex(80, 80) 
    x.vertex(50, 120) 
    x.endShape(CLOSE)  

    shape(x, 70, 140)

#drobny mankament, że klawisz w lewo podświetlał R nawet gdy nie było wybrane B. Przeanalizuj rozwiązanie.
# 2pkt
    
