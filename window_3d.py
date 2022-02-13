from tkinter import *

from open_img import *
from tab_c import *

class MainWindow_3d:

    def __init__(self, Window_3d):

        self.Window_3d = Toplevel(Window_3d)
        self.Window_3d.title((self.Window_3d.title() + " 3d"))

        self.lbl = Label(self.Window_3d, text="Выберите с какими изображениями будите работать", font=50)
        self.lbl.grid(column=0, row=0, columnspan=2, pady=10)
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        opts1= {'pady': 10, 'padx':10, 'font':50}
        #Сфера
        self.sphere_3D = Button(self.Window_3d, text="sphere_3D", **opts1,
                                command=self.create_widgets_sphere_3D)
        self.sphere_3D.grid(column=0, row=1, **opts)
        #Куб
        self.cube_3D = Button(self.Window_3d, text="cube_3D", **opts1,
                              command=self.create_widgets_cube_3D)
        self.cube_3D.grid(column=0, row=2, **opts)
        #Паралелеппед
        self.parallelepiped_3D = Button(self.Window_3d, text="parallelepiped_3D!", **opts1,
                                        command=self.create_widgets_parallelepiped_3D)
        self.parallelepiped_3D.grid(column=0, row=3, **opts)
        #
        self.pyramid_3D = Button(self.Window_3d, text="pyramid_3D", **opts1,
                                 command=self.create_widgets_pyramid_3D)
        self.pyramid_3D.grid(column=1, row=1, **opts)
        # Трапеция
        self.cylinder_3D = Button(self.Window_3d, text="cylinder_3D", **opts1,
                                  command=self.create_widgets_cylinder_3D)
        self.cylinder_3D.grid(column=1, row=2, **opts)
        # Ромб
        self.cone_3D = Button(self.Window_3d, text="cone_3D", **opts1,
                              command=self.create_widgets_cone_3D)
        self.cone_3D.grid(column=1, row=3, **opts)

    def create_widgets_sphere_3D(self):
        t=create_widgets(self.Window_3d,"Площядь Сферы","Введите радиус")
        t.create_widgets()
    def create_widgets_cube_3D(self):
        t = create_widgets(self.Window_3d, "Площадь, Объем и Периметр Куба",
                                      "Введите сторону")
        t.create_widgets()
    def create_widgets_parallelepiped_3D(self):
        t= create_widgets(self.Window_3d, "Площадь, Объем и Периметр Параллелепипеда",
                         "Введите три стороны(через пробел)")
        t.create_widgets()

    def create_widgets_pyramid_3D(self):
        t = create_widgets(self.Window_3d, "Площадь, Объем и Периметр Пирамиды",
                           "Введите высоту, длину, ширину(через пробел)")
        t.create_widgets()


    def create_widgets_cylinder_3D(self):
        t = create_widgets(self.Window_3d, "Площадь, Объем и Периметр Цилиндра",
                                      "Введите высоту и радиус(через пробел)")
        t.create_widgets()

    def create_widgets_cone_3D(self):
        t = create_widgets(self.Window_3d, "Площадь, Объем и Периметр Конуса",
                                      "Введите высоту и радиус(через пробел)")
        t.create_widgets()
