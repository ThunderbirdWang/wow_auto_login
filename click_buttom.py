import pyautogui
from PIL import ImageGrab
import time,os
from locate import get_coordinate
import psutil

flag=True #结束进程标记
paths=['run_game.png','system.png','enter_wow.png']
while 1:
    img=ImageGrab.grab()
    center=get_coordinate(paths[0],img)
    if center and flag==False:
        pyautogui.mouseDown(center[0],center[1],button='left')
        pyautogui.mouseUp(button='left')
        flag=True
        time.sleep(2)
    center=get_coordinate(paths[1],img)
    if center and flag==True:
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if p.name() == 'WowClassic.exe':
                cmd = 'taskkill /F /IM WowClassic.exe'
                os.system(cmd)
                flag=False
                time.sleep(2)
    center=get_coordinate(paths[2],img)
    if center: 
        pyautogui.mouseDown(center[0],center[1],button='left')
        pyautogui.mouseUp(button='left')
        time.sleep(2)



    # for i in range(0,len(paths)):
    #     center=get_coordinate(paths[i],img)
    #     if center:
    #         if i==0 and flag==False:
    #             pyautogui.mouseDown(center[0],center[1],button='left')
    #             pyautogui.mouseUp(button='left')
    #             flag=True
    #             time.sleep(2)
    #         elif i==1 and flag==True:
    #             pids = psutil.pids()
    #             for pid in pids:
    #                 p = psutil.Process(pid)
    #                 if p.name() == 'WowClassic.exe':
    #                     cmd = 'taskkill /F /IM WowClassic.exe'
    #                     os.system(cmd)
    #                     flag=False
    #                     time.sleep(2)
    #         else: 
    #             pyautogui.mouseDown(center[0],center[1],button='left')
    #             pyautogui.mouseUp(button='left')
    #             time.sleep(2)