import pgzrun,random
WIDTH=600
HEIGHT=800
TITLE="BumbleBee"


message="Collect The Flowers"
Bee=Actor("bee.png")
flower = Actor("flower.png")
def draw():
    screen.fill("teal")
    Bee.draw()
    flower.draw()
    screen.draw.text(message,(0,750))

def flowerrandom():
    flower.x=random.randint(0,600)
    flower.y=random.randint(0,800)

def update():
    global message
    if keyboard.left:
        Bee.x=Bee.x-5
    elif keyboard.right:
        Bee.x=Bee.x+5
    elif keyboard.up:
        Bee.y=Bee.y-5
    elif keyboard.down:
        Bee.y=Bee.y+5
    if Bee.colliderect(flower):
        flowerrandom()
        message="Yippie!" 

flowerrandom()
pgzrun.go()