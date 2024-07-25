###Using MSS to take the screenshot

import pyautogui

def take_screenshot(imagename:str):
    image = pyautogui.screenshot()
    imagename = imagename + ".png"
    image.save(imagename)

take_screenshot("sc")