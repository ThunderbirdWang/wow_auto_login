from cv2 import cv2
from PIL import ImageGrab
import numpy as np


def get_coordinate(path,img):
    fz=0.1
    template=cv2.imread(path)
    h,w,t=template.shape
    img=np.array(img)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    res=cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print(min_val, max_val, min_loc, max_loc)
    # if min_val >fz :
    #     print("没有匹配")
    # else:
    print(min_val)
    if min_val < fz:
        top_left=min_loc
        center=(top_left[0]+int(w/2),top_left[1]+int(h/2))
        return center
        
if __name__ == "__main__":
    path='run_game.png'
    while 1:
        img=ImageGrab.grab()
        center=get_coordinate(path,img)
        if center:
            print(center)
            break

# # img=cv2.imread('battlenet.png')
# # print(img.shape)
# template=cv2.imread('system.png')
# template2=cv2.imread('run_game.png')
# # print(template.shape)
# h,w,t=template.shape
# h2,w2,t2=template2.shape

# while 1:
#     img=ImageGrab.grab()
#     img=np.array(img)
#     img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     res=cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
#     res2=cv2.matchTemplate(img,template2,cv2.TM_SQDIFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
#     # print(min_val, max_val, min_loc, max_loc)
#     if min_val >fz and min_val2>fz:
#         print("没有匹配")
#     else:
#         if min_val <fz:
#             top_left=min_loc
#             center=(top_left[0]+int(w/2),top_left[1]+int(h/2))
#         if min_val2<fz:
#             top_left=min_loc2
#             center=(top_left[0]+int(w2/2),top_left[1]+int(h2/2))
#         pyautogui.mouseDown(center[0],center[1],button='left')
#         pyautogui.mouseUp(button='left')
#         time.sleep(2)