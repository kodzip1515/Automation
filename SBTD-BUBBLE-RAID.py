import time
import pyautogui as auto

auto.click(2646,473)#inital click

for x in range(10): #change to how many times you want to replay
    #7x speed
    auto.click(3063,61)
    auto.click(2902,798) #presses start

    auto.press("5") #selects starter
    auto.moveTo(2646,474)
    time.sleep(8)
    auto.click(2646,474) #places starter

    auto.press("4") #selects starter
    auto.moveTo(3102,434)
    time.sleep(7)
    auto.click(3102,434) #places starter

    #auto.press("4") #selects Dorudon
    #auto.moveTo(3442,369)
    #time.sleep(12)
    #auto.click(3442,369) #places Dorudon
    time.sleep(277) #waits for game to end

        #click replay
    auto.click(2646,473)
    time.sleep(0.5)
    auto.click(3340,840)
    time.sleep(0.5)
