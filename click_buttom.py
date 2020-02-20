import pyautogui
from PIL import ImageGrab
import time,os,win32gui,win32con
from locate import get_coordinate

paths=['run_game.png','animation.png','enter_wow.png','setting.png']
while 1:
    hwnd = win32gui.FindWindow(None, '魔兽世界') 
    hwnd_battle=win32gui.FindWindow(None, '暴雪战网')
    aw=win32gui.GetForegroundWindow()

    if hwnd:
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