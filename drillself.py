from pico2d import *
import os
os.chdir('C:\\Drill\Drill02')
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x = 0
y = 90
isRecCicle = False
isCircle = False
# 800, 600
# 42, 92 중앙 21,46
def moveRec():
    global x
    global y
    global isRecCicle
    global isCircle
    
    if((x >= 0 and x < 758) and (y <= 90 and y > 0)):
        if x > 399 and isRecCicle == True:
            isCircle = True
            return False
        x += 2
    elif (( x >= 758) and (y <= 600 - 46 )): # 전체 599 - 캐릭피봇y + 땅위치
        y += 2
    elif ((x >= 2 ) and (y > 600 - 46 )):
        x -= 2
    elif ((x < 21 ) and (y > 90)):
        y -= 2
        isRecCicle = True

import math

seta_pi = math.pi * 3/2 # 2분의 3pi가 초기값 


def moveCircle():
    global x
    global y
    global seta_pi
    global isCircle
    global isRecCicle
    circle_x = 400
    circle_y = 300
    
    x =  circle_x + 200*math.cos(seta_pi)
    y =  circle_y + 200*math.sin(seta_pi)
    seta_pi = seta_pi + 0.01

    if(seta_pi > 2*math.pi + math.pi * 3/2):
        seta_pi = math.pi * 3/2
        x = 400
        y = 90
        isCircle = False
        isRecCicle = False


while( x < 800 ):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)

    if(moveRec()):
        pass
    if (isRecCicle == True and isCircle == True):
        moveCircle()

    delay(0.001)

close_canvas()


# def drawRec():
#     global x
#     global y
    
#     if x >= 790 and y < 550:
#         y = y + 2
#     elif x < 790:
#         x = x + 2

#     if y >= 550:
#         x = x - 4
#         if x < 80:
#             y = y-4
#     elif y > 90 and x < 80:
#         y = y -4


# import random
# random.randint(1,5) # 1~5
# for 변수 in 리스트(또는 튜플):

# for n in [1,3,5,6]:
# for i in range(1,100+1) # 1~100
# for x,y,r in [(200,200,50),(-200,-200,30),(100,100,50)]

# def add(a,b):
#     sum = a+b
#     return sum

# grass.py 열기해서 import 실시 -> 얘도 파이선 폴더라


# 800x600
# 볼 23x23 
# 애니메이션 802x402
# 캐릭터 42x92
# grass 802x62
# run animation 802x102