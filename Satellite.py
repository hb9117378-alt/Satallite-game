import pgzrun
from random import randint
from time  import time

WIDTH=800
HEIGHT=800

satellites=[]
Lines=[]
next_satellite=0
Start=0
End=0
Total=0
Number_of_satellites=10

def create_satellite():
    global start_time
    for i in range(Number_of_satellites):
        S=Actor("Satellite")
        S.pos=randint(40 ,WIDTH -40),randint(40 ,HEIGHT -40)
        Satellites.append(S)
    start_time=time()

def draw():
    global total_time 
    screen.blit("Nebula-Galaxy",(0,0))
    num=1
    for sat in Satellites:
        screen.draw.text(str(num),sat.pos[0],sat.pos[1]+20)
        sat.draw()
        num=num+1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    
    if next_satellite<Number_of_satellites:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,2)),(15,10),fontsize=20)
    else:
        screen.draw.text(str(round(total_time,2)),(15,10),fontsize=20)


def on_mouse_down(pos):
    global next_satellite,Lines

    if next_satellite < Number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                Lines.append(satellites[next_satellite-1].pos,satellites[next_satellite].pos)
            next_satellite = next_satellite+1
        else:
            Lines=[]
            next_satellite=0

create_satellite()

pgzrun.go

