import pyautogui as auto
auto.PAUSE = 0
import time

def color_match(actual, target, tol=1):
    return all(abs(actual - target) <=tol for actual, target in zip(actual,target))

x,y = 318, 478
target = (78, 41, 35)

while True:
    color = auto.pixel(x,y)
    if color_match(color, target,):
        auto.click(x,y)