from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 750
frame = 0

def move_left():
    global frame, x
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1)%8
    x += 5 

def move_right():
    global frame, x
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1)%8
    x -= 5
    pass

while( x < 800 ):
    clear_canvas()
    grass.draw(400,30)

    move_right()

    delay(0.05)
    get_events()


close_canvas()

