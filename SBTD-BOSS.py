import time
import pyautogui as auto


auto.click(3353, 832)
while True:
    for x in range(10):
        #click next
        auto.click(3353, 833)
        time.sleep(1)
        # cicks play
        auto.click(2834, 825)
        time.sleep(15)

    answer = input("continue?").lower
    if answer == "y":
            continue
    else:
            break