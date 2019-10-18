import task_catch
import user_handle
import pyautogui
import findx
import judge_del
import insert_DB


org=findx.matchImg('D:/myproject/EAS_auto/EASauto/chinese/pic.png','D:/myproject/EAS_auto/EASauto/chinese/taget.png',0.9)

orgX=org['result'][0]

orgY=org['result'][1]

usernum=1
while (usernum<2500):
    user_handle.user_handle(orgX,orgY)
    information=judge_del.judge_del()
    insert_DB.insert_log_1(usernum,result=information)
    if (information=='success'):
        pyautogui.moveTo(orgX,orgY-50)
        pyautogui.press('down')
        print("sssss")
    else:
        break
    usernum=usernum+1

else:
    print("finsh!!!")