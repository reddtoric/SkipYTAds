import pyautogui
from pynput import keyboard

size = pyautogui.size()
print("Your monitor size: ", size[0], size[1])

print("Press spacebar to print current cursor position.")


# On key press
def on_press(key):
    if key == keyboard.Key.space:
        pos = pyautogui.position()
        print("Cursor position: ", pos[0], pos[1])


# Ignore on release
def on_release(key):
    pass


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
