import pyautogui
import time

pyautogui.PAUSE = 1

# 1. Spotify
# Open the Windowns Tab and search for Spotify
pyautogui.press('win')
pyautogui.write('Spotify')
pyautogui.press('enter')

time.sleep(5)

# Select playlist
pyautogui.click(x=59, y=459)
# Start the playlist
pyautogui.click(x=307, y=396)
# Enable suffle
pyautogui.click(x=872, y=969)

# 2. Set Workspace
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

time.sleep(3)

# Select account in Google
pyautogui.click(x=782, y=592)
pyautogui.getWindowsWithTitle("Google Chrome")[0].maximize()

# Open Alura tabs
pyautogui.click(x=268, y=15)
pyautogui.click(x=1002, y=84)

time.sleep(3)

# Courses
pyautogui.click(x=498, y=796)


pyautogui.click(x=486, y=119)
pyautogui.write('GET YOUR WATER AND LETS GO!')
