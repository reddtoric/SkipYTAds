from python_imagesearch.imagesearch import imagesearch
import pyautogui
import ctypes
from pynput import keyboard
import time
from threading import Thread
import os


# === User Settings ===
# Verbosity
VERBOSE = False
VERBOSE_PAUSE = True

# Interval in seconds
interval = 6

# Center of button (top left corner = 0,0
offset_x = 50
offset_y = 20

# Relative path and file name of skip ads image
rel_file_path = "skip ads.png"

# Accuracy (min:0, max: 1)
accuracy = 0.6
# === End of Settings ===


# ---


# Absolute dir the script is in
script_dir = os.path.dirname(__file__)

# Absolute file path
abs_file_path = os.path.join(script_dir, rel_file_path)

# Where user had cursor
current_cursor_pos_x = 0
current_cursor_pos_y = 0

# Is_SearchLoop_enabled
is_enabled = True


# On key press
def on_press(key):
    if key == keyboard.Key.pause:
        global is_enabled

        if VERBOSE or VERBOSE_PAUSE:
            print("|| PAUSED" if is_enabled else "|> resume")

        is_enabled = not is_enabled

        # Start thread again
        SearchLoop().start()


# Ignore on release
def on_release(key):
    pass


# Def the keyboard listener thread
class KeyboardListener(Thread):
    def run(self):
        with keyboard.Listener(on_press=on_press,
                               on_release=on_release) as listener:
            listener.join()


# Search and click skip ad button
def search():
    # Search 'skip ads' image
    pos = imagesearch(abs_file_path, accuracy)

    if VERBOSE:
        print("searching image")

    if pos[0] != -1:
        # My 2x2 monitor offset (my ranges: -2560 - 2556, -1080 - 1079)
        x = pos[0] - 2560
        y = pos[1] - 1080

        if VERBOSE:
            print("position : ", x, y)

        # Save current mouse position
        (current_cursor_pos_x, current_cursor_pos_y) = pyautogui.position()

        # Workaround for sticky corners
        if y < 0:
            ctypes.windll.user32.SetCursorPos(1280, -540)
        else:
            ctypes.windll.user32.SetCursorPos(1280, 540)

        # Move cursor to center of button
        # ctypes.windll.user32.SetCursorPos(x + offset_x, y + offset_y)

        # Mouse left click
        pyautogui.click(x + offset_x, y + offset_y)
        if VERBOSE:
            print("ad skipped")

        # Move mouse back
        ctypes.windll.user32.SetCursorPos(current_cursor_pos_x,
                                          current_cursor_pos_y)


# Def search loop thread
class SearchLoop(Thread):
    def run(self):
        global is_enabled
        while is_enabled:
            search()

            if VERBOSE:
                print("waiting " + str(interval) + " seconds")

            # Wait 5 sec before searching again
            time.sleep(interval)


# Main
print("Running skip_ads.py at " + str(interval) + "s intervals")
KeyboardListener().start()
SearchLoop().start()
