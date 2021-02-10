# manga-scroller
Simple script that scrolls for you when reading manga.

## Context
Just wanted to make a quick script that could scroll manga webpages for me. It's not perfect, and certainly doesn't cover all the edge cases, but it works. Don't download this expecting it to be bugfree or anything though.

## What does it do?
You first show the script where the "Next Chapter" button is so that it knows where to find it. Then set a scrolling speed and delay and let it do its work. Just make sure that the terminal you open the script in is on the same monitor as the webpage you are viewing manga in. To stop the program, simply left click your mouse.

## How to Run
Clone the repository, activate the Python environment in `env` and run `python scroller.py`. This uses the PyAutoGui and PyWin32 libraries, so this only works on Windows.
