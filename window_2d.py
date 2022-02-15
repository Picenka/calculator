from tkinter import Tk, ttk
import matplotlib.pyplot as plt
from open_img import *
from tab_c import *
from square import *


class MainWindow_2d:

    def __init__(self, Window_2d):

        self.Window_2d = Toplevel(Window_2d)
        self.Window_2d.title("Геометрический калькулятор 2d")
        self.lbl = Label(self.Window_2d, text="Выберите с какими изображениями будите работать", font=50)
        self.lbl.grid(column=0, row=0, columnspan=2, pady=10)
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.dict_2d = {'circle_2D': [self.create_widgets_circle_2D, 0, 1, 'круг'],
                        'square_2D': [self.create_widgets_square_2D, 0, 2, 'квадрат'],
                        'rectangle_2D': [self.create_widgets_rectangle_2D, 0, 3, 'прямоугольник'],
                        'triangle_2D': [self.create_widgets_triangle_2D, 1, 1, 'триугольник'],
                        'trapezium_2D': [self.create_widgets_trapezium_2D, 1, 2, 'трапеция'],
                        'rhombus_2D': [self.create_widgets_rhombus_2D, 1, 3, 'ромб'],
                        }
        for key, value in self.dict_2d.items():
            self.key = Button(self.Window_2d, text=value[3], **opts1, command=value[0])
            self.key.grid(column=value[1], row=value[2], **opts)

    def create_widgets_circle_2D(self):
        create_widgets(self.Window_2d, "Площядь и Периметр Круга", "Введите радиус")

    def create_widgets_square_2D(self):
        create_widgets(self.Window_2d, "Площядь и Периметр Квадрата","Введите сторону")

    def create_widgets_triangle_2D(self):
        create_widgets(self.Window_2d, "Площядь и Периметр Треугольника",
                                      "Введите координаты (x1.y1 x2.y2 x3.y3)")

    def create_widgets_trapezium_2D(self):
        create_widgets(self.Window_2d, "Площядь и Периметр Прямоугольной Трапеции",
                                     "Введите три стороны(через пробел)")

    def create_widgets_rectangle_2D(self):
        create_widgets(self.Window_2d, "Площядь и Периметр Прямоугольника",
                                          "Введите две стороны(через пробел)")

    def create_widgets_rhombus_2D(self):
        create_widgets(self.Window_2d, "Площядь и Периметр Ромба(равностроннего)",
                                          "Введите сторону")







