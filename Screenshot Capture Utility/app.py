import pyautogui

def take_screenshot(filename="screenshot.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")

take_screenshot()
