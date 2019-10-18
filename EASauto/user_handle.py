import pyautogui

def user_handle(orgX,orgY):
    pyautogui.PAUSE = 1.0
    pyautogui.moveTo(orgX,orgY,duration=1)
    print(orgX)
    pyautogui.PAUSE = 1.0
    pyautogui.click()
    #pyautogui.click(x=1656.0,y=573.0,button='left')
    pyautogui.PAUSE=1.0
    pyautogui.moveTo(10, 30, duration = 0.25)
    pyautogui.PAUSE = 1.0