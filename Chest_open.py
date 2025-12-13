import pyautogui as auto
import time

def all(x,y,e,r=514):
    auto.click(x,y)
    time.sleep(0.2)
    auto.click(e,r)
    time.sleep(2.5)
    for i in range(5):
        time.sleep(0.3)
        auto.click(2841,372)
    time.sleep(4.3)
    auto.click(2841,372)



#init
A = int(input("how many times: "))
row = int(input("what row: "))
auto.click(2800,500)
auto.moveTo(2800,500)

#process
if row == 1:
    for x in range(A):
        all(2369,381,2696)
elif row == 2:
    for x in range(A):
        all(2575,362,2880)
elif row == 3:
    for x in range(A):
        all(2757,362,3080)
elif row == 4:
    for x in range(A):
        all(3143,342,3467)

