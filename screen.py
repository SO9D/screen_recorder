import pyautogui

from datetime import datetime

import time

counter = 0

step = 60


while True:
    
    time.sleep(step)
    
    counter = counter + step

    zrzut = pyautogui.screenshot()
    
    timestamp = str(datetime.now())
    
    timestamp = timestamp.replace(":", "_")
    timestamp = timestamp.replace(".", "_")
    timestamp = timestamp.replace("-", "_")
    
    timestamp = timestamp + ' counter = ' + str(counter) + '.png'
    
    zrzut.save(timestamp)
    
    print(timestamp + ' Press Ctrl+C to interrupt :)')

