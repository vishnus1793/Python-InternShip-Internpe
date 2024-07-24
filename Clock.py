import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)


# Create the main window
root = tk.Tk()
root.title("Clock with Background Image")



# Load the background image
bg_image_path = "background.jpg"  
bg_image = Image.open(bg_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)



# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=bg_photo.width(), height=bg_photo.height())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")


# Load the font
bold_font = font.Font(family="One Piece", size=60, weight="bold")


# Create a label to display the clock with a matching background
clock_label = tk.Label(root, font=bold_font, fg="Red", bg=canvas.cget("background"), bd=0)

# Adjust the label position: move it down by 150 pixels (adjust as needed)
y_offset = 150
canvas.create_window(bg_photo.width()//2, bg_photo.height()//2 + y_offset, window=clock_label)

# Update the time for the first time
update_time()


# Start the Tkinter event loop
root.mainloop()
