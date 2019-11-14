# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:50:28 2019

@author: quent
"""

import keyboard  # using module keyboard

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break