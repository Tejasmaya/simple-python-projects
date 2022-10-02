import pywhatkit
import pyautogui as pg
# # pywhatkit.sendwhatmsg(phone_num,message,time_hour,time_min,wait_time,print_wait_time,tab_close)
# pywhatkit.sendwhatmsg('+919178726330', 'Tejasmaya', 19, 4, 20, True, False)

# for instant messaging
pywhatkit.sendwhatmsg_instantly('+919178726330', 'Message Tejasmaya')
pg.press('Enter')
