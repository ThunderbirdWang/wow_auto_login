import pyautogui
from PIL import ImageGrab
import time,os
from locate import get_coordinate

flag=True #结束进程标记
paths=['run_game.png','system.png','enter_wow.png']
while 1:
    img=ImageGrab.grab()
    for i in range(0,len(paths)):
        center=get_coordinate(paths[i],img)
        if center:
            if i==0 and flag==False:
                pyautogui.mouseDown(center[0],center[1],button='left')
                pyautogui.mouseUp(button='left')
                flag=True
                time.sleep(2)
            elif i==1 and flag==True:
                cmd = 'taskkill /F /IM WowClassic.exe'
                os.system(cmd)
                flag=False
                time.sleep(2)
            else: 
                pyautogui.mouseDown(center[0],center[1],button='left')
                pyautogui.mouseUp(button='left')
                time.sleep(2)