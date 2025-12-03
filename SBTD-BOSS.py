import time
import pyautogui as auto

#how many times to loop
answer = int(input("How many times: "))
auto.click(3353, 832)
while True:
    for x in range(answer):
        #click next
        auto.click(3353, 833)
        time.sleep(1)
        # cicks play
        auto.click(2834, 825)
        time.sleep(21.2)
    
    ask = input("go again y/n: ")
    if ask == "y":
        answer = int(input("how many times: "))

    else:
        break