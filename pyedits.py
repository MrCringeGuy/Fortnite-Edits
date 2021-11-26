import time
import pynput
import keyboard

from pynput.keyboard import *

keyboard = Controller()

if key.is_pressed('pause'):
    keyboard.press('e')
    time.sleep(0.001)
    keyboard.press('r')
    keyboard.release('e')
    time.sleep(0.001)
    keyboard.release('r')
