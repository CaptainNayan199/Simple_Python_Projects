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
        x = 400 / 2 + 0.7 * 400 / 2 * math.cos(angle)
        y = 400 / 2 + 0.7 * 400 / 2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y - 10, text=str(i + 12), font=("Helvetica", 12))
        else:
            canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))

    # Minute lines

    for i in range(60):
        angle = i * math.pi / 30 - math.pi / 2
        x1 = 400 / 2 + 0.8 * 400 / 2 * math.cos(angle)
        y1 = 400 / 2 + 0.8 * 400 / 2 * math.sin(angle)
        x2 = 400 / 2 + 0.9 * 400 / 2 * math.cos(angle)
        y2 = 400 / 2 + 0.9 * 400 / 2 * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)

    # Hour hand drawing

    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    hour_x = 400 / 2 + 0.5 * 400 / 2 * math.cos(hour_angle)
    hour_y = 400 / 2 + 0.5 * 400 / 2 * math.sin(hour_angle)
    canvas.create_line(400 / 2, 400 / 2, hour_x, hour_y, fill="black", width=6)

    # Minute hand drawing

    minute_angle = (minute + second / 60) * math.pi / 30 - math.pi / 2
    minute_x = 400 / 2 + 0.7 * 400 / 2 * math.cos(minute_angle)
    minute_y = 400 / 2 + 0.7 * 400 / 2 * math.sin(minute_angle)
    canvas.create_line(400 / 2, 400 / 2, minute_x, minute_y, fill="black", width=4)

    # Draw second hand

    second_angle = second * math.pi / 30 - math.pi / 2
    second_x = 400 / 2 + 0.6 * 400 / 2 * math.cos(second_angle)
    second_y = 400 / 2 + 0.6 * 400 / 2 * math.sin(second_angle)
    canvas.create_line(400 / 2, 400 / 2, second_x, second_y, fill="black", width=1)



# canvas.after(1000, clock_logic)

clock_logic()
root.mainloop()