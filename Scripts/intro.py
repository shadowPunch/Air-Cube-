import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import subprocess

root = tk.Tk()
root.geometry("1920x1080")
root.title("Air Cube")

gifImage = "bg.gif"
openImage = Image.open(gifImage)
frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(openImage)]
count = 0
showAnimation = None

def animation(count):
    global showAnimation
    newImage = frames[count]

    gif_Label.configure(image=newImage)
    count += 1
    if count == len(frames):
        count = 0
    
    showAnimation = root.after(50, lambda: animation(count))

gif_Label = tk.Label(root, image="")
gif_Label.place(y=100,width=1540, height=1000)
gif_Label.pack()

def run_external_script():
    subprocess.run(["python", "main.py"])


button = tk.PhotoImage(file="cube_button.png")


button_frame = tk.Frame(root, highlightbackground="#8d667b", highlightthickness=0, bd=0)
button_start = tk.Button(button_frame, image=button, borderwidth=0,highlightthickness=0,command=run_external_script,width=275,height=50)
button_start.pack()
button_frame.place(x=620, y=760)

animation(count)
root.mainloop()
