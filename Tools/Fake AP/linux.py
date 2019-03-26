# AUTHOR: o-o
# DATE: 2/27/2019
# DESCRIPTION: Executes Linux Commands.

from pynput.keyboard import Key, Controller
import time

# GLOBAL VARIABLES.

TIME = 3

# Creates a new tab.
# Precondition: None.
# Postcondition: Creates a new tab.

def tab():

    # Keyboard (Object)

    keyboard = Controller()

    # SHIFT + CTRL + T

    keyboard.press(Key.shift_l) 
    keyboard.press(Key.ctrl_l) 
    keyboard.press("t") 
    keyboard.release(Key.shift_l) 
    keyboard.release(Key.ctrl_l) 
    keyboard.release("t") 
    time.sleep(TIME)

# Executes a Command.
# Precondition: A String.
# Postcondition: Executes a Command.

def command(command):

    # Keyboard (Object)

    keyboard = Controller()

    # COMMAND

    keyboard.type(command)
    time.sleep(TIME)

    # ENTER

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(TIME)

# Closes the Current Tab.
# Precondition: None.
# Postcondition: Closes the Current Tab.

def end():

    # Keyboard (Object)

    keyboard = Controller()

    # CTRL + C

    keyboard.press(Key.ctrl_l)
    keyboard.press("c")
    keyboard.release(Key.ctrl_l)
    keyboard.release("c")
    time.sleep(TIME)

    # SHIFT + CTRL + W

    keyboard.press(Key.shift_l)
    keyboard.press(Key.ctrl_l)
    keyboard.press("w")
    keyboard.release(Key.shift_l)
    keyboard.release(Key.ctrl_l)
    keyboard.release("w")
    time.sleep(TIME)
