import pyautogui as auto

# coordinates from xdtool
x, y = 3499, 862

# take screenshot and get pixel color
color = auto.screenshot().getpixel((x, y))
print(color)  # prints (R, G, B)
