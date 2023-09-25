from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('miniSonic.png')
# 'miniSonic.png' : 1159 x 979 
# 'penguin.png' : 2048 x 2048
# 'sonic.png' : 850 x 1504 
#     clip_draw( left,     bottom, width, height, x, y)
# chr.clip_draw( frame * 100, 0,    100,   100,   x, 90)
#                왼쪽부터, 사진y축, 픽셀 가로,세로, 그릴좌표
#  frame = (frame + 1) % 8 
# 사진 왼쪽하단이 좌표임 -> 580 + frame * 144 : 사진 580픽셀부터 한 프레임 당 144++
x = 0
frame = 0

def move_right():
    global frame, x
    character.clip_draw( 585 + frame * 137, 348, 137, 183, x, 90)
    update_canvas()
    frame = (frame + 1) % 4
    x += 5 



while( x < 800 ):
    clear_canvas()
    grass.draw(400,30)

    move_right()

    delay(0.05)
    get_events()


close_canvas()


# def move_right():
#     global frame, x
#     character.clip_draw(frame * 100, 0, 100, 100, x, 90)
#     update_canvas()
#     frame = (frame + 1)%8
#     x -= 5
#     pass