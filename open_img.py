from tkinter import *
from PIL import Image

class open_img:
    def open_img(self,road,text):
        im = Image.open(road)
        (width, height) = im.size
        root = Tk()
        canvas = Canvas(root,width=width, height=height)
        canvas.pack(fill=BOTH, expand=YES)
        img = PhotoImage(master = canvas,file=road)
        canvas.create_image(0,0, anchor=NW, image=img)
        canvas.pack(fill=BOTH, expand=YES)
        label = Label(root, text=text)
        label.pack()
        mainloop()