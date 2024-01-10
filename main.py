
import time
import pyperclip
import pyautogui as pg
import tkinter as tk
from PIL import Image, ImageTk


def image_to_tkimage():
    img_path="Color-Palette.png"
    image = Image.open(img_path)
    return ImageTk.PhotoImage(image)


def copy_rgb(rgb):
    pyperclip.copy(str(rgb))
    print("You copied:","RGB: "+str(rgb))
    
    
def get_rgb_click(event):
    x,y=pg.position()
    rgb=pg.pixel(x,y)
    copy_rgb(rgb)
    
    
    

window = tk.Tk()
colors_image=image_to_tkimage()
colors_label=tk.Label(window,image=colors_image)
colors_label.pack()


window.bind("<Button-1>",get_rgb_click)
window.mainloop()



