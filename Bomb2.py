import pyautogui , threading

message = input("message : ")
repeats = input("repeats : ")

def fast():
    for i in range(int(repeats)):
        pyautogui.typewrite(message)
        pyautogui.press('enter')


for i in range(int(repeats)):
    thread = threading.Thread(target=fast)
    thread.start()
