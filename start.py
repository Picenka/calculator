from tkinter import *
from window_2d import MainWindow_2d
from window_3d import MainWindow_3d

def open_2d():
    MainWindow_2d(window)
def open_3d():
    MainWindow_3d(window)

window = Tk()
window.title("Геометрический калькулятор")
lbl = Label(window, text="Выберите с какими изображениями будите работать", font=50)
lbl.grid(column=0, row=0, columnspan=2, pady=10)
btn_2D = Button(window, text="2D!", command=open_2d, pady=10, padx=10, font=50)
btn_2D.grid(column=0, row=1)
btn_3D = Button(window, text="3D!", command=open_3d, pady=10, padx=10, font=50)
btn_3D.grid(column=1, row=1)
window.mainloop()

