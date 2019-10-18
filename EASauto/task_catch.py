import win32ui,win32con,pythoncom,win32gui
import win32api
import pyautogui
import findx

def login():
    win32api.ShellExecute(0, 'open', 'D:\\EAS\eas\\client\\bin\\client.bat', '', '', 1)
    #win32api.ShellExecute(0, 'open', 'F:\\Documents\\Desktop\\qq\\11.txt', '', '', 1)
    tab = findx.matchImg('D:/myproject/EAS_auto/EASauto/chinese/login.png',
                         'D:/myproject/EAS_auto/EASauto/chinese/task_catch_simpletaget.png', 0.9)
    print(tab)

    pyautogui.FAILSAFE = True
    pyautogui.moveTo(300, 300, duration=0.25)
    pyautogui.PAUSE = 3.0
    pyautogui.moveTo(300, 200, duration=0.25)
    pyautogui.size()
    # (1366, 768)
    width, height = pyautogui.size()
    print(width, height)
    pyautogui.moveTo(tab['result'][0],tab['result'][1]+40, duration=0.25)
    pyautogui.click()
    pyautogui.typewrite('lshbiao')
    pyautogui.PAUSE = 0.3
    pyautogui.press('shift')
    pyautogui.PAUSE = 0.3
    pyautogui.press('tab')
    pyautogui.PAUSE = 1.0
    pyautogui.typewrite('p@ssw0rd1')
    pyautogui.PAUSE = 0.3
    pyautogui.press('enter')
    pyautogui.PAUSE = 1.5
    pyautogui.moveTo(300, 500, duration=0.25)
    pyautogui.PAUSE = 1.5
    pyautogui.press('enter')
    pyautogui.PAUSE = 1.5
    pyautogui.moveTo(300, 600, duration=0.25)
    pyautogui.PAUSE = 1.5
