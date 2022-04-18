import time
import pyautogui
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop


pyautogui.FAILSAFE = False
TIMELAPSE = 1

def main() :
 while True:
    pos = imagesearch("./prijmout.png")
    pos = imagesearch("./cz.png")
    if pos[0] != -1: 
     pyautogui.moveTo(pos[0], pos[1])
     pyautogui.click(clicks=2)
     print("position : ", pos[0], pos[1])
     print("hra byla přijata")
    
