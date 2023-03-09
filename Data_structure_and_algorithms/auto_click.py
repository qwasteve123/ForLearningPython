import time
import threading

from pynput.mouse import Controller, Button
from pynput.keyboard import Listener,KeyCode

TOGGLE_KEY = KeyCode(char = 'g')

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left)
            time.sleep(0.0001)
        else:
            time.sleep(0.0001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listenser:
    listenser.join()