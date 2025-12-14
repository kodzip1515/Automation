import time
import pyautogui as auto

def color_match(actual, target, tol=1):
    # Returns True if each RGB component is within the tolerance
    return all(abs(a - t) <= tol for a, t in zip(actual, target))

def alls(x, y, unit, t, unit2, x2, y2, t2):
    for i in range(A):
        time.sleep(1)
        auto.click(3364, 858)  # replay
        time.sleep(0.8)
        auto.click(2902, 798)  # play
        time.sleep(5)
        # unit 1
        auto.press(unit)
        auto.moveTo(x, y)
        time.sleep(t)
        auto.click(x, y)
        time.sleep(1)
        # unit 2
        auto.press(unit2)
        auto.moveTo(x2, y2)
        time.sleep(t2)
        auto.click(x2, y2)

        # wait until the pixel changes TO the target color (with tolerance)
        r, b = 3499, 862
        target_color = (222, 174, 31)

        while True:
            current_color = auto.pixel(r, b)
            if color_match(current_color, target_color, tol=1):
                auto.click(r, b)  # click once when it becomes close enough
                break
            time.sleep(0.1)

A = int(input("how many times: "))
auto.click(2646, 473)  # initial click
auto.moveTo(3000, 500)
auto.click(3063, 61)  # 7x speed

alls(2979, 470, "6", 6, "3", 2742, 485, 6)
