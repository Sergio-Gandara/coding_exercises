#
## This file is for experimenting with the pynput module
#from pynput.keyboard import Key, Controller
#
#keyboard = Controller()
#
## Press and release space

# keyboard.press(Key.space)
# keyboard.release(Key.space)

#
## Type a lower case A; this will work even if no key on the
## physical keyboard is labelled 'A'
#keyboard.press('a')
#keyboard.release('a')
#
## Type two upper case As
#keyboard.press('A')
#keyboard.release('A')
#with keyboard.pressed(Key.shift):
#    keyboard.press('a')
#    keyboard.release('a')
#
# keyboard.type('Hello World')
## Type 'Hello World' using the shortcut type method

from pynput import keyboard

print("code")
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# This is a keyboard listener in the form of a thread