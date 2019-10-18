import task_catch
import user_handle
import pyautogui
import findx
import judge_del
import insert_DB

task_catch.login()

org=findx.matchImg('D:/myproject/EAS_auto/EASauto/chinese/pic.png','D:/myproject/EAS_auto/EASauto/chinese/taget.png',0.9)

orgX=org['result'][0]

orgY=org['result'][1]

print(orgX)

pyautogui.PAUSE = 1.0

pyautogui.moveTo()

#print(findx.matchImg('D:/myproject/EAS_auto/EASauto/chinese/pic.png','D:/myproject/EAS_auto/EASauto/chinese/taget.png',0.9))

# TODO(stan):find the compyne taget

#taget=findx.matchImg('D:/myproject/EAS_auto/EASauto/pic/test.png','open.jpg',0.5)

#print(taget)
pyautogui.moveTo(1600, 30, duration=0.25)

pyautogui.PAUSE = 3.0
pyautogui.click(x=1600, y=30, button='left')
# 移动到选择框
pyautogui.PAUSE = 0.3
pyautogui.typewrite('SPT0101')
pyautogui.PAUSE = 3.0
pyautogui.press('shift')
pyautogui.moveTo(1600, 30, duration=0.25)
pyautogui.PAUSE = 3.0
pyautogui.press('enter')


imformation='1'
usernum=1

while (usernum<2500):
    user_handle.user_handle(orgX,orgY)
    information=judge_del.judge_del()
    insert_DB.insert_log_1(usernum,result=information)
    if (information=='success'):
        pyautogui.press('down')
    else:
        break
    usernum=usernum+1

else:
    print("finsh!!!")