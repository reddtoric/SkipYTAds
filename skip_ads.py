# Version: 1.1

from python_imagesearch.imagesearch import imagesearch
import pyautogui
import ctypes
from pynput import keyboard
import time
from threading import Thread
import os
import argparse
from point import Point


# === User Settings ===
# Verbosity: Show 'a' = show all, 't' = show toggle only, 'q' = hide all
VERBOSE = 't'

# Interval in seconds
interval = 6

# Accuracy (min:0, max: 1)
accuracy = 0.6

# Override screen_min if top-left not (0,0). Default = None
# Set to None to not override
override_screen_min = None
#override_screen_min = Point(-2560, -1080)
# === End of Settings ===


# ---


# Relative directory path of where all the images to search/match against
rel_dir_path = "images"

# Offset to click on the center
button_offset = Point(50, 20)

# Absolute file path of script
script_dir = os.path.dirname(__file__)

# List of image file paths in directory
images = [os.path.join(script_dir, rel_dir_path, img) for img in os.listdir(rel_dir_path)]

# Verbosity and interval override with cli arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose',
                    choices=['a', 't', 'q'],
                    default='t',
                    help="Set verbosity. Show (a)ll outputs, show (t)oggle \
                          only outputs, or (q)uiet output.")
parser.add_argument('-i', '--interval',
                    metavar='float>=1',
                    type=float,
                    help="Set interval in seconds.")

# Override verbose
args = parser.parse_args()
VERBOSE = args.verbose

# Save mode msg for later
mode = ""
if VERBOSE == 'a':
    mode = "show all output"
elif args.verbose == 't':
    mode = "show toggle only"
else:
    mode = "quiet"

# Override interval
if args.interval is not None:
    interval = args.interval if args.interval >= 1 else 1

# Is_SearchLoop_enabled
is_enabled = True

# Top-Left of display corner
screen_min = override_screen_min or Point()

# Ref: Stick Corner Workaround
# First half of my workaround for center sticky corner in 2x2 monitor setup
#screen_center = Point()
#(screen_center.x, screen_center.y) = pyautogui.size()
#screen_center.x = int(screen_center.x/2)
#screen_center.y = int(screen_center.y/2)

# Where user had cursor originally
original_cursor_pos = Point()


# On key press
def on_press(key):
    if key == keyboard.Key.pause:
        global is_enabled

        if VERBOSE == 'a' or VERBOSE == 't':
            print("|| Paused" if is_enabled else "|> Resume")

        is_enabled = not is_enabled

        # Restart search
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
    if VERBOSE == 'a':
        print("Searching")

    for i in range(0,len(images)):
        # Search 'skip ads' image
        pos = imagesearch(images[i], 0.6)

        if pos[0] != -1:
            x = pos[0] + screen_min.x
            y = pos[1] + screen_min.y

            if VERBOSE == 'a':
                print("Ad position: ", x, y)

            # Save current mouse position
            (original_cursor_pos.x, original_cursor_pos.y) = pyautogui.position()

            # Second half of workaround for center sticky corners
            #if y < 0:
            #    ctypes.windll.user32.SetCursorPos(screen_center.x, -1 * screen_center.x)
            #else:
            #    ctypes.windll.user32.SetCursorPos(screen_center.x, screen_center.y)

            # Mouse left click on center of button
            pyautogui.click(x + button_offset.x, y + button_offset.y)

            if VERBOSE == 'a' or VERBOSE == 't':
                print("Ad skipped")

            # Move mouse back
            ctypes.windll.user32.SetCursorPos(original_cursor_pos.x,
                                              original_cursor_pos.y)

            # Break for loop if first version is already found and clicked
            break


# Def the search loop thread
class SearchLoop(Thread):
    def run(self):
        global is_enabled
        while is_enabled:
            search()

            if VERBOSE == 'a':
                print(f"Waiting {str(interval)}s")

            # Wait x sec before searching again
            time.sleep(interval)


# Main
print(f"Running skip_ads.py at {str(interval)}s intervals in {mode} mode.")
KeyboardListener().start()
SearchLoop().start()
