#pip install Pillow
#pip install opencv-python
#conda install -c anaconda tk

from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy as np
import tkinter.filedialog as tkFileDialog


class test:
    def __init__(self, image):
        self.root = Tk()
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.panel = Label(image=image)
        self.panel.image = image
        self.panel.pack()
        self.frame = Frame(self.root, width=100, height=100)
        self.panel.bind("<Key>", self.key)
        self.panel.bind("<Button-1>", self.callback)
        #self.frame.pack()
    def callback(self, event):
        self.panel.focus_set()
        print('mouse', event.x, event.y)
    def key(self, event):
        self.panel.focus_set()
        print('keyboard', repr(event.char), event.char)
    def do_loop(self):
        self.root.mainloop()



board = np.zeros((512, 512, 3), dtype=np.uint8)
board = cv2.rectangle(board, (100,100), (400, 400), 255, 3)

test(board).do_loop()