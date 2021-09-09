import pyautogui
pyautogui.FAILSAFE = True

# (100, 100)으로 이동
pyautogui.moveTo(100, 100)

# 천천히 (150, 150) 만큼 이동
pyautogui.moveRel(150, 150, duration=5)
