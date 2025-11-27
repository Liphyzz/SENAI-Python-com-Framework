import pyautogui as py

py.press('win')
py.write("chrome")

py.sleep(3)

py.press('Enter')

py.sleep(3)

py.write("SENAI Americana")
py.press('Enter')

py.sleep(3)

print(py.position())

py.click(x=258, y=459, button = 'left')

py.sleep(3)

py.click(x=1419, y=777, button = 'left')

py.sleep(3)

py.click(x=209, y=498, button = 'left')

py.sleep(3)

py.write("Python")

py.sleep(3)

py.press('Enter')