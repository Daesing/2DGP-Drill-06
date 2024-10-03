from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

CHAR_W,CHAR_H = 100, 100

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

hand_x, hand_y = random.randint(100,1200), random.randint(100,1000)
boy_x, boy_y = 100, 100
origin_x,origin_y =100, 100


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
#hide_cursor()

def print_hand():
    global hand_x,hand_y
    hand_x = random.randint(100,1200)
    hand_y = random.randint(100,1000)


i=0
direction = 0

def move_boy():
    global boy_x, boy_y, i, direction, origin_x, origin_y

    t = 1 - (i - 100) ** 2 / 10000 #출발과 도착에 속도 조절
    boy_x = (1 - t) * origin_x + t * hand_x
    boy_y = (1 - t) * origin_y + t * hand_y
    i += 1

    if i>100:
        i=0
        print_hand()
        origin_x = boy_x
        origin_y = boy_y


    if boy_x - hand_x > 0:
        direction = 1
    elif boy_x - hand_x < 0:
        direction = 2
    pass

def print_boy():
    if direction == 1:
        character.clip_draw(frame * CHAR_W, 0, CHAR_W, CHAR_H, boy_x, boy_y)
    elif direction == 2:
        character.clip_draw(frame * CHAR_W, 100, CHAR_W, CHAR_H, boy_x, boy_y)
    delay(0.02)


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(hand_x,hand_y)
    move_boy()
    print_boy()

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()




