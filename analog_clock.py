import tkinter as tk
import time
import math

root = tk.Tk()
root.title("Simple analog Clock from Python")
canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
canvas.pack()


def clock_logic():
    