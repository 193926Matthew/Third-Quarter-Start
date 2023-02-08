creature = Actor('sad')
creature.pos = 250, 150

WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((70,50,200))
    creature.draw()

def update():
    creature.left = creature.left + 2
    if creature.left > WIDTH:
        creature.right = 0

def on_mouse_down(pos):
    if creature.collidepoint(pos):
        print("Foolish")
        sounds.boom.play()
        creature.image = 'happy'
    else:
        print("...")
        creature.image = 'sad'
