import pyautogui
pyautogui.FAILSAFE = True

# shift + 오른쪽 커서 3회
pyautogui.keyDown("shift")
pyautogui.typewrite(["right"] * 3, interval=1)
pyautogui.keyUp("shift")

# ctrl + c
pyautogui.hotkey("ctrl", "c")
