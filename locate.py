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
    if min_val < fz:
        top_left=min_loc
        center=(top_left[0]+int(w/2),top_left[1]+int(h/2))
        return center
    else:
        return False
        
if __name__ == "__main__":
    path='run_game.png'
    while 1:
        img=ImageGrab.grab()
        center=get_coordinate(path,img)
        if center:
            print(center)
            break