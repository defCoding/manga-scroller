import pyautogui
import win32api, win32con
from time import sleep
import os


def clear_term():
    """
    Clears the terminal.
    """
    os.system('cls' if os.name =='nt' else 'clear')

def get_next_click_pos():
    """
    Gets the x, y coordinates of the next left-click.

    Returns:
    (int, int) - the x and y coordinates.
    """
    while win32api.GetKeyState(0x01) > -127:
        sleep(0.001)

    print("GOT")
    pos = win32api.GetCursorPos()

    while win32api.GetKeyState(0x01) <= -127:
        sleep(0.001)
    
    return pos

def click(coords):
    """
    Raises a mouse left-click action at the provided coordinates.

    Params:
    coords (Tuple(int, int)): The x, y coordinates of the click as a tuple.
    """
    x, y = coords
    win32api.SetCursorPos(coords)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def scroll(interval):
    """
    Raises a mouse scroll event with the specified scroll amount.

    Params:
    interval (int): How much to scroll.
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, interval, 0)

if __name__ == '__main__':
    clear_term()
    print('Welcome to the Manga Autoscroller. To begin, please go to your desired manga chapter.')
    print('Once you are there, we will need to determine where the "Next Chapter" button is at the end of a chapter.')
    input('Press Enter when you are ready...')
    clear_term()
    print('Click as close as you can to the top left corner of the "Next Chapter" button as you can without pressing it.')
    tlx, tly = get_next_click_pos()
    clear_term()
    print('Click as close as you can to the bottom right corner of the "Next Chapter" button as you can without pressing it.')
    brx, bry = get_next_click_pos()
    clear_term()

    region = (tlx, tly, brx - tlx, bry - tly)
    next_button = pyautogui.screenshot(region=region)
    print('Image saved.')

    # Set and bound scrolling speed.
    scroll_speed = int(input('Choose a scroll speed from 1 to 50 (10 is usually good):\n'))
    scroll_speed = min(50, max(0, scroll_speed))

    # Set time delay before next page.
    delay = int(input('Choose a time delay in seconds for how long the bot should wait before moving to the next page:\n'))
    delay = max(0, delay)

    clear_term()
    input("Everything is ready. You can stop this program at any time by left-clicking your mouse.\nWhen you wish for scrolling to start, press Enter in this terminal...")
    sleep(3)

    while win32api.GetKeyState(0x01) > -127:
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, tlx, tly, -scroll_speed, 0)
        pos = pyautogui.locateOnScreen(next_button, confidence=0.9, region=(region[0], region[1] - 100, region[2] + 100, region[3] + 100))
        if pos:
            sleep(delay)
            click((pos[0] + pos[2] // 2, pos[1] + pos[3] // 2))
            sleep(1)
            win32api.SetCursorPos((pos[0] + 300, pos[1]))
            sleep(1)