#importing packages
import pyautogui
import time
from random import randint
import tkinter as neha


def screenshot():
    name = (randint(10, 900) * 1000)
    name = 'E:/PythonProjects/screenshot image/{}.png'.format(name)
    time.sleep(0)
    img = pyautogui.screenshot(name)
    img.show()


# screenshot()

root = neha.Tk()
root.title("Hello Beautiful People! Please Take Screenshot")
root.geometry("600x400")
frame = neha.Frame(root)
frame.pack()
button = neha.Button(
    frame,
    text="Take SS",
    command=screenshot
)

button.pack(side=neha.LEFT)

close = neha.Button(
    frame,
    text='Quit',
    command=quit
)
close.pack(side=neha.RIGHT)

root.mainloop()


# screenshot taking applicatio using in python
