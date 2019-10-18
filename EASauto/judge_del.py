import PrintScreen
import findx
import pyautogui

def judge_del():

    count=1

    pyautogui.click(1200,177)

    PrintScreen.printScreen(str(count))
    com_judge = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/" + str(count) + ".png",
                               "D:/myproject/EAS_auto/EASauto/company/C050011.png", 0.1)
    print("com_judge",com_judge)
    while (com_judge['confidence'] < 0.999):
        count=count+1
        pyautogui.press('pagedown')
        PrintScreen.printScreen(str(count))
        # 组织页面是否到结尾
        com_end = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/" + str(count) + ".png",
                                 "D:/myproject/EAS_auto/EASauto/pic/" + str(count-1) + ".png", 0.01)
        print("com_end:",com_end)
        if (com_end['confidence']>0.999):
            close_1 = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/" + (str(count)) + ".png",
                                     "D:/myproject/EAS_auto/EASauto/chinese/close_next.png", 0.9)
            # 关闭组织页面
            close_1x = close_1['result'][0]
            close_1y = close_1['result'][1]
            print(close_1x,close_1y)
            pyautogui.moveTo(close_1x,close_1y,0.25)
            pyautogui.click()
            break
        # 判断在该页是否存在组织
        com_judge = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/" + str(count) + ".png",
                                   "D:/myproject/EAS_auto/EASauto/company/C050011.png", 0.01)
        print(com_judge)
        return 'do not exist com'
    else:
        pyautogui.click(com_judge['result'][0], com_judge['result'][1])
        del_judge = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/"+str(count)+".png",
                                   'D:/myproject/EAS_auto/EASauto/chinese/del_button.png', 0.9)
        judgex = del_judge['result'][0]
        judgey = del_judge['result'][1]
        print(del_judge)
        pyautogui.moveTo(judgex, judgey, 0.25)
        pyautogui.PAUSE=1.0
        pyautogui.click()
        #截图判断是否亦权限
        PrintScreen.printScreen(str(count+0.1))
        try:
            com_judge_1 = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/" + (str(count+0.1)) + ".png",
                                       "D:/myproject/EAS_auto/EASauto/chinese/com_judge_1.png", 0.1)
            print(com_judge_1,"dsadasd")
            #有权限则取消删除
            if (com_judge_1['confidence']>0.98):
                com_del = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/"+(str(count+0.1))+".png",
                                             "D:/myproject/EAS_auto/EASauto/chinese/cancel.png", 0.9)
                delx = com_del['result'][0]
                dely = com_del['result'][1]
                pyautogui.moveTo(delx, dely, 0.25)
                pyautogui.PAUSE=1.0
                pyautogui.click()
                return 'have permission'
            else:
                close_1 = findx.matchImg("D:/myproject/EAS_auto/EASauto/pic/" + (str(count)) + ".png",
                                             "D:/myproject/EAS_auto/EASauto/chinese/close_next.png", 0.9)
                #关闭组织页面
                print(close_1)
                close_1x=close_1['result'][0]
                close_1y=close_1['result'][1]
                pyautogui.moveTo(close_1x, close_1y, 0.25)
                pyautogui.click()
                print("删除成功！！！")
                return 'success'

            print(com_judge['confidence'])
        except(TypeError):
            pass
            print("抛出异常，有一个步骤没匹配到")

    print()

#judge_del()
#information=judge_del()
#print(information)