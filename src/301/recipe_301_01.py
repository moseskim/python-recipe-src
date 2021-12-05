import pyautogui
pyautogui.FAILSAFE = True

# abc를 입력한 후 enter 키를 입력
pyautogui.typewrite(["a", "b", "c", "return"], interval=1)
