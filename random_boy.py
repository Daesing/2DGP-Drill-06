from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

hand_x, hand_y = 0, 0


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

    hand.draw(hand_x,hand_y)

    delay(1)



while running:
    clear_canvas()
    #TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    print_hand()

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()




