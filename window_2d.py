from tkinter import *
from tkinter import Tk, ttk
from PIL import ImageTk, Image
import tkinter as tk
import matplotlib.pyplot as plt


from open_img import *
from tab_c import *
from square import *


class MainWindow_2d:

    def __init__(self, Window_2d):

        self.Window_2d = Toplevel(Window_2d)
        self.Window_2d.title((self.Window_2d.title() + " 2d"))

        self.lbl = Label(self.Window_2d, text="Выберите с какими изображениями будите работать", font=50)
        self.lbl.grid(column=0, row=0, columnspan=2, pady=10)
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        # круг
        self.circle_2D = Button(self.Window_2d, text="circle_2D", pady=10, padx=10, font=50,
                                command=self.create_widgets_circle_2D )
        self.circle_2D.grid(column=0, row=1, **opts)
        # Квадрат
        self.square_2D = Button(self.Window_2d, text="square_2D", pady=10, padx=10, font=50,
                                command=self.create_widgets_square_2D)
        self.square_2D.grid(column=0, row=2, **opts)
        # Прямоугольник
        self.rectangle_2D = Button(self.Window_2d, text="rectangle_2D!", pady=10, padx=10, font=50,
                                command=self.create_widgets_rectangle_2D)
        self.rectangle_2D.grid(column=0, row=3, **opts)
        # Треугольник
        self.triangle_2D = Button(self.Window_2d, text="triangle_2D", pady=10, padx=10, font=50,
                                command=self.create_widgets_triangle_2D)
        self.triangle_2D.grid(column=1, row=1, **opts)
        # Трапеция
        self.trapezium_2D = Button(self.Window_2d, text="trapezium_2D", pady=10, padx=10, font=50,
                                command=self.create_widgets_trapezium_2D)
        self.trapezium_2D.grid(column=1, row=2, **opts)
        # Ромб
        self.rhombus_2D = Button(self.Window_2d, text="rhombus_2D", pady=10, padx=10, font=50,
                                command=self.create_widgets_rhombus_2D)
        self.rhombus_2D.grid(column=1, row=3, **opts)

    def create_widgets_circle_2D(self):
        t = create_widgets(self.Window_2d, "Площядь и Периметр Круга", "Введите радиус")
        t.create_widgets()

    def create_widgets_square_2D(self):
        t = create_widgets(self.Window_2d, "Площядь и Периметр Квадрата","Введите сторону")
        t.create_widgets()

    def create_widgets_triangle_2D(self):
        t = create_widgets(self.Window_2d, "Площядь и Периметр Равностороннего Треугольника",
                                      "Введите сторону")
        t.create_widgets()

    def create_widgets_trapezium_2D(self):
        t = create_widgets(self.Window_2d, "Площядь и Периметр Прямоугольной Трапеции",
                                     "Введите три стороны(через пробел)")
        t.create_widgets()

    def create_widgets_rectangle_2D(self):
        t = create_widgets(self.Window_2d, "Площядь и Периметр Прямоугольника",
                                          "Введите две стороны(через пробел)")
        t.create_widgets()

    def create_widgets_rhombus_2D(self):
        t = create_widgets(self.Window_2d, "Площядь и Периметр Ромба(равностроннего)",
                                          "Введите сторону")
        t.create_widgets()







    # def create_widgets(self):
    #     self.notebook = ttk.Notebook(self.Window_2d)
    #     self.notebook.grid(row=4, sticky="NSWE", columnspan=2)
    #     opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
    #
    #     page1 = ttk.Frame(self.notebook)
    #     self.notebook.add(page1, text='Площядь')
    #     label=Label(page1, text='Введите радиус')
    #     label.grid(column=0,row=1,**opts)
    #     self.edit=Entry(page1)
    #     self.edit.grid(column=0,row=2,**opts)
    #     mybutton = Button(page1, text="Расчет",command=self.p)
    #     mybutton.grid(column=0,row=3,**opts)
    #     # периметр
    #     page2 = ttk.Frame(self.notebook)
    #     self.notebook.add(page2, text='Периметр')
    #     mybutton = Button(page2, text="Расчет")
    #     mybutton.grid(row=1,column=1,**opts)
    #     edit=Entry(page2)
    #     edit.grid(row=2,column=1)
