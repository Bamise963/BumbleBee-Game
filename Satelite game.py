import pgzrun, random

WIDTH=600
HEIGHT=800

station=[]


for i in range(8):
    satellite=Actor("satellite (1)")
    satellite.x=(random.randint(0,550))
    satellite.y=(random.randint(0,750))
    station.append(satellite)


def draw():
    screen.blit("space background",(0,0))
    number=1
    for i in station:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+10))
        i.draw()
        number=number+1

pgzrun.go()