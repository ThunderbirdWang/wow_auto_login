import pyautogui
from PIL import ImageGrab
import time,os,win32gui,win32con
from locate import get_coordinate

flag=True #结束进程标记
paths=['run_game.png','animation.png','enter_wow.png','setting.png']
while 1:
    hwnd = win32gui.FindWindow(None, '魔兽世界') 
    hwnd_battle=win32gui.FindWindow(None, '暴雪战网')
    aw=win32gui.GetForegroundWindow()

    if hwnd:
        # if aw!=hwnd:
        #     try:
        #         win32gui.SetForegroundWindow(hwnd)
        #     except Exception as e:
        #         print(e)
        #     time.sleep(2)
        img=ImageGrab.grab()
        if get_coordinate(paths[1],img):
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            time.sleep(2)
            if hwnd_battle:
                if not win32gui.FindWindow(None, '魔兽世界'):
                    aw=win32gui.GetForegroundWindow()
                    if aw!=hwnd_battle:
                        try:
                            win32gui.SetForegroundWindow(hwnd_battle)
                            time.sleep(2)
                        except Exception as e:
                            print(e)
                    pyautogui.press('enter')
                    time.sleep(15)
                    hwnd = win32gui.FindWindow(None, '魔兽世界')
                    if hwnd:
                        aw=win32gui.GetForegroundWindow()
                        if aw!=hwnd:
                            try:
                                win32gui.SetForegroundWindow(hwnd)
                                time.sleep(2)
                            except Exception as e:
                                print(e)
                        img=ImageGrab.grab()
                        center=get_coordinate(paths[2],img)
                        if center:
                            pyautogui.mouseDown(center[0],center[1],button='left')
                            pyautogui.mouseUp(button='left')
                            time.sleep(20)
            else:
                print('请运行战网')
    else:
        if hwnd_battle:
            aw=win32gui.GetForegroundWindow()
            if aw!=hwnd_battle:
                try:
                    win32gui.SetForegroundWindow(hwnd_battle)
                    time.sleep(2)
                except Exception as e:
                    print(e)
            pyautogui.press('enter')
            time.sleep(15)
            hwnd = win32gui.FindWindow(None, '魔兽世界')
            if hwnd:
                aw=win32gui.GetForegroundWindow()
                if aw!=hwnd:
                    try:
                        win32gui.SetForegroundWindow(hwnd)
                        time.sleep(2)
                    except Exception as e:
                        print(e)
                img=ImageGrab.grab()
                center=get_coordinate(paths[2],img)
                if center:
                    pyautogui.mouseDown(center[0],center[1],button='left')
                    pyautogui.mouseUp(button='left')
                    time.sleep(20)
    time.sleep(5)

# hwnd = win32gui.FindWindow(None, '魔兽世界')
# if hwnd:
#     win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
# while 1:
#     img=ImageGrab.grab()
#     if get_coordinate(paths[1],img):
#         cmd = 'taskkill /F /IM WowClassic.exe'
#         os.system(cmd)
#         time.sleep(2)
#         while 1:
#             center=get_coordinate(paths[0],img)
#             if center:
#                 pyautogui.mouseDown(center[0],center[1],button='left')
#                 pyautogui.mouseUp(button='left')
#                 time.sleep(10) 
#                 while 1:
#                     center=get_coordinate(paths[2],img)
#                     if center:
#                         pyautogui.mouseDown(center[0],center[1],button='left')
#                         pyautogui.mouseUp(button='left')
#                         break
#                 break
#             else:
#                 print('战网不要被遮挡或最小化')
#     else:
#         time.sleep(1)
        

    # center=get_coordinate(paths[0],img)
    # if center and flag==False:
    #     pyautogui.mouseDown(center[0],center[1],button='left')
    #     pyautogui.mouseUp(button='left')
    #     flag=True
    #     time.sleep(2)
    # center=get_coordinate(paths[1],img)
    # if center and flag==True:
    #     pids = psutil.pids()
    #     for pid in pids:
    #         p = psutil.Process(pid)
    #         if p.name() == 'WowClassic.exe':
    #             cmd = 'taskkill /F /IM WowClassic.exe'
    #             os.system(cmd)
    #             flag=False
    #             time.sleep(2)
    # center=get_coordinate(paths[2],img)
    # if center: 
    #     pyautogui.mouseDown(center[0],center[1],button='left')
    #     pyautogui.mouseUp(button='left')
    #     time.sleep(2)



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