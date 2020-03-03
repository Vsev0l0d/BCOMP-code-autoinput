from time import sleep
import pyautogui

INPUT_FILE_NAME = 'code.txt'
INTERVAL = 0.1
SLEEP_TIME = 5

file = open(INPUT_FILE_NAME, "r")

lastAddress = "000"

start_point = '0'

print("you have " + str(SLEEP_TIME) + " secs")
sleep(SLEEP_TIME)
print("START")
pyautogui.typewrite("0", INTERVAL)
for line in file.readlines():
    data = line.split()
    if len(data) == 3:
        start_point = data[0]
        data[1] = data[2]
    adress = data[0]
    code = data[1]
    if int(adress, 16) == int(lastAddress, 16) + 1:
        pyautogui.typewrite(code, INTERVAL)
        pyautogui.press('f5', interval=INTERVAL)
    else:
        pyautogui.typewrite(adress, INTERVAL)
        pyautogui.press('f4', interval=INTERVAL)
        pyautogui.typewrite(code, INTERVAL)
        pyautogui.press('f5', interval=INTERVAL)
    lastAddress = adress

pyautogui.typewrite(start_point, INTERVAL)
pyautogui.press('f4', interval=INTERVAL)

print("finished")
