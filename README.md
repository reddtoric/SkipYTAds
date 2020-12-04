# SkipYTAds

Hate YouTube ads but don't want to use an ad blocker? You don't mind those ads because some are good or introduces you to new things but you don't want those extra long annoying ones? Well, here's a python script just for that!

This script automatically searches for the skip button every 6 seconds (adjustable) and if there is a skippable ad, it'll skip it for you. And if you're in the middle of watching a skippable ad but interested in continuing, just press the pause button (before it does it's thing) and it'll pause the script. Then returns your cursor back to where it was (but does not refocus your original window; a feature to be added).

**!Important:** The skip button has to be visible! It cannot be hidden behind another window.


## Prerequisites
*To do. Python 3?

## Running the script
In a cli, traverse into the directory and run `$ py ./skip_ads.py` or double click script to run.

## Pausing/Unpausing script
Press the keyboard `pause` button to toggle between pausing and resuming the script.

## Verbosity Modes
Adjustable in file/overridable with cli arguments.  
'a' = Show all outputs  
't' = Show toggle (pause/unpause) outputs (Default)  
'q' = Quiet  
Show all example: `$ py .\skip_ad.py -v a`

## Interval
Default interval is 6 seconds but is adjustable in file/overridable with cli arguments. Accepts float number greater than or equal to 1.
`$ py .\skip_ad.py -i 1`

## Running multiple monitors?
Use the opt_verify_corner_pos script to find out the position value of your top-left corner.  
I have a 2x2 setup where my bottom-right monitor is the main display. So, my top-left corner are negative values. My monitors are 2560x1080 so I have to override the screen min values like so `override_screen_min = Point(-2560, -1080)` in user settings section.

If you're like me with a 2x2 setup, uncomment all code sections under "Ref: Stick Corner Workaround".

Mismatched monitor sizes can cause problems.

You on your own if problems arise.

## Other settings
`rel_file_path` path of the image to match with.
`accuracy` accuracy of the image match. Default is 0.6. min: 0, max: 1

## Features to implement (if I feel like it)
- Set focus back to original window to minimize interruption
- More robust solution
- GUI notification for pause/resume
- Run in background
- Auto start up app

## Libraries used
- [python-imagesearch](https://github.com/drov0/python-imagesearch)
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [pynput](https://pypi.org/project/pynput/)
- ctypes
- time
- os
- threading
- argparse

---

### Dev note
This script may be clunky and not robust but it works to my specs. I wanted something that clicks the button for me when I'm doing stuff and have a video playing. 

It doesn't work while in a game that centers your cursor and not allowing it outside of the window which I'm okay with. 

I don't use ad blockers because I actually like to see some of the ads. But other ads like an ad of a tutorial on a brand of smart lights that is several minutes long is extremely displeasing. I DON'T OWN ANY. Why is an **ad** showing me how to use smart lights!? Just assuming that it's popular or everyone owns them.
