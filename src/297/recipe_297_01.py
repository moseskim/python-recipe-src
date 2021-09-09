import pyautogui

# 마우스 포인터 위치
mouse_pos = pyautogui.position()
print(mouse_pos.x, mouse_pos.y)

# 화면 크기
disp_size = pyautogui.size()
print(disp_size.height, disp_size.width)
