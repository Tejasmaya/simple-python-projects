import pyautogui as pg
import time

print('Program will run in 5 seconds:...')
time.sleep(5)

for i in range(50):
    pg.write("")
    time.sleep(0.001)

    pg.press('Enter')
