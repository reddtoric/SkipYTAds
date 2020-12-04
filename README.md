# SkipYTAds

Hate YouTube ads but don't want to use an ad blocker? You don't mind those ads because some are good or introduces you to new things but you don't want those extra long annoying ones? Well, here's a python script just for that!

This script automatically searches for the skip button every 6 seconds (adjustable) and if there is a skippable ad, it'll skip it for you. And if you're in the middle of watching a skippable ad but interested in continuing, just press the pause button (before it does it's thing) and it'll pause the script.

**!Important:** The skip button has to be visible! It cannot be behind another window.


## Running the script
In a cli within the directory you downloaded the repo, run `py ./skip_ads.py`

## Pausing/Unpausing script
Press the `pause` button to toggle between pausing and resuming the script.

## Verbosity Modes
2 variables defined in the script that allows you to choose whether the script is verbose or not.  
`VERBOSE = True` will display all messages.  
`VERBOSE_PAUSE = True` will display when you toggle pause/resume.  

## Interval
Default `interval` is 6 seconds but is adjustable.

## Other settings
`Offset_x, _y` where you want the cursor to click on, in the event it's for something else.  
`rel_file_path` path of the image to match on desktop  
`accuracy` accuracy of the image match. Default is 0.6. min: 0, max: 1

## Features to implement (if I feel like it)
- Set focus back to original window to minimize interruption
- More robust solution
- GUI notification for pause/resume
- Run in background
- Auto start up app

---

### Dev note
This script may be clunky and not robust but it works to my specs. I wanted something that clicks the button for me when I'm doing stuff and have a video playing. 

It doesn't work while in a game that centers your cursor and not allowing it outside of the window which I'm okay with. 

I don't use ad blockers because I actually like to see some of the ads. But other ads like an ad of a tutorial on a brand of smart lights that is several minutes long is extremely displeasing. I DON'T OWN ANY. Why is an **ad** showing me how to use smart lights!? Just assuming that it's popular or everyone owns them.
