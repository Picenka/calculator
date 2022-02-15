from tkinter import *
from PIL import Image


class open_img:
    def __init__(self, road, text):
        self.text = text
        self.road = road
        self.__open_img()

    def __open_img(self):
        im = Image.open(self.road)
        (width, height) = im.size
        root = Tk()
        canvas = Canvas(root, width=width, height=height)
        canvas.pack(fill=BOTH, expand=YES)
        img = PhotoImage(master=canvas, file=self.road)
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.pack(fill=BOTH, expand=YES)
        label = Label(root, text=self.text)
        label.pack()
        mainloop()
