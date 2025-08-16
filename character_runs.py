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
# 사진 왼쪽하단이 좌표임 -> 580 + frame * 144 : 사진 580픽셀부터
# 한 프레임 당 144++
x = 0
frame = 0


gbool1 = True
gbool2 = False
gbool3 = False

def ThreeByFive(): # 뛰기 
    global frame, x
    global gbool1, gbool2

    start_frame = 0
    character.clip_draw( 600 + (start_frame + frame) * 133, 348, 133, 183, x, 130)
    update_canvas()
    frame = (frame + 1) % 4 
    x += 5
    if frame == 0 :
        gbool1 = False
        gbool2 = True

def FourByFive(): # 발 돌리기 
    global frame, x
    global gbool2, gbool1

    start_frame = 0
    character.clip_draw(595+ (start_frame + frame) * 135, 160, 135, 183, x, 130)
    update_canvas()
    frame = (frame + 1) % 4 
    x += 5
    if frame == 0 :
        gbool2 = False
        gbool1 = True

def FiveByFour(): # 소닉 돌기 
    global frame, x
    global gbool3, gbool1

    start_frame = 0
    character.clip_draw( (start_frame + frame) * 135, 0, 135, 129, x, 100)
    update_canvas()
    frame = (frame + 1) % 4
    x += 5
    if(frame == 0):
        gbool3 = False
        gbool1 = True

def FourByFour(): # 원 돌기 
    global frame, x
    character.clip_draw( frame * 138, 174, 138, 129, x, 100)
    update_canvas()
    frame = (frame + 1) % 4
    if(frame == 0 ):
        return
    x += 5

def move_right():
    global gbool1, gbool2, gbool3

    if(gbool1):
        ThreeByFive()
    if(gbool2):
        FourByFive()
    if(gbool3):
        FiveByFour() 



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

#-------------------
# def move_right():
#     global frame, x
#     character.clip_draw( 600 + frame * 133, 348, 133, 183, x, 130)
#     update_canvas()
#     frame = (frame + 1) % 4
#     x += 5 


# def ThreeByFive(): # 뛰기 
#     global frame, x
#     character.clip_draw( 600 + frame * 133, 348, 133, 183, x, 130)
#     update_canvas()
#     frame = (frame + 1) % 4 
#     if(frame == 0 ):
#         return 
#     x += 5

# def FourByFive(): # 발 돌리기 
#     global frame, x
#     character.clip_draw( 595 + frame * 135, 160, 135, 183, x, 130)
#     update_canvas()
#     frame = (frame + 1) % 4 
#     if(frame == 0 ):
#         return 
#     x += 5

# def FiveByFour(): # 소닉 돌기 
#     global frame, x
#     character.clip_draw( frame * 135, 0, 135, 129, x, 100)
#     update_canvas()
#     frame = (frame + 1) % 4
#     if(frame == 0 ):
#         return
#     x += 5

# def FourByFour(): # 원 돌기 
#     global frame, x
#     character.clip_draw( frame * 138, 174, 138, 129, x, 100)
#     update_canvas()
#     frame = (frame + 1) % 4
#     if(frame == 0 ):
#         return
#     x += 5

# def move_right():
#     global frame, x
#     ThreeByFive() 
#     FourByFive()