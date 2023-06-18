import tkinter as tk
import time
import math

root = tk.Tk()
root.title("Simple analog Clock from Python")
canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
canvas.pack()


def clock_logic():
    canvas.delete("All")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    # Clock logic

    canvas.create_oval(2, 2, 400, 400, outline="gold", width=2)
    
    # Hours numbers
    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
