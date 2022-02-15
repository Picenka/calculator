from tkinter import *
from open_img import *
from tab_c import *


class MainWindow_3d:
    def __init__(self, Window_3d):
        self.Window_3d = Window_3d
        self.dict_3d = {'sphere_3D': [self.create_widgets_sphere_3D, 0, 1, 'сфера'],
                        'cube_3D': [self.create_widgets_cube_3D, 0, 2, 'куб'],
                        'parallelepiped_3D': [self.create_widgets_parallelepiped_3D, 0, 3, 'паралелепипед'],
                        'pyramid_3D': [self.create_widgets_pyramid_3D, 1, 1,'пирамида'],
                        'cylinder_3D': [self.create_widgets_cylinder_3D, 1, 2,'цилиндр'],
                        'cone_3D': [self.create_widgets_cone_3D, 1, 3,'конус'],
                        }
        self.__new_win()

    def __new_win(self):
        self.Window_3d = Tk()
        self.Window_3d.title("Геометрический калькулятор 3d")
        self.lbl = Label(self.Window_3d, text="Выберите с какими изображениями будите работать", font=50)
        self.lbl.grid(column=0, row=0, columnspan=2, pady=10)
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        opts1 = {'pady': 10, 'padx': 10, 'font': 50}

        for key, value in self.dict_3d.items():
            self.key = Button(self.Window_3d, text=value[3], **opts1, command=value[0])
            self.key.grid(column=value[1], row=value[2], **opts)

    def create_widgets_sphere_3D(self):
        create_widgets(self.Window_3d, "Площядь Сферы", "Введите радиус")

    def create_widgets_cube_3D(self):
        create_widgets(self.Window_3d, "Площадь, Объем и Периметр Куба","Введите сторону")

    def create_widgets_parallelepiped_3D(self):
        create_widgets(self.Window_3d, "Площадь, Объем и Периметр Параллелепипеда",
                           "Введите три стороны(через пробел)")
    def create_widgets_pyramid_3D(self):
        create_widgets(self.Window_3d, "Площадь, Объем и Периметр Пирамиды",
                           "Введите высоту, длину, ширину(через пробел)")

    def create_widgets_cylinder_3D(self):
        create_widgets(self.Window_3d, "Площадь, Объем и Периметр Цилиндра",
                           "Введите высоту и радиус(через пробел)")

    def create_widgets_cone_3D(self):
        create_widgets(self.Window_3d, "Площадь, Объем и Периметр Конуса",
                           "Введите высоту и радиус(через пробел)")

