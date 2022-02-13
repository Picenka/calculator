from tkinter import *
from matplotlib.patches import Circle

from open_img import *
from triangle import *
from square import *
from d3_visualization import *


class create_widgets:
    def __init__(self, window_xd, name_page, name_label):
        self.window_xd = window_xd
        self.name_page = name_page
        self.name_label = name_label

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.window_xd)
        self.notebook.grid(row=4, sticky="NSWE", columnspan=2)
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        page1 = ttk.Frame(self.notebook)
        self.notebook.add(page1, text=self.name_page)
        label = Label(page1, text=self.name_label)
        label.grid(column=0, row=1, **opts)
        self.edit = Entry(page1)
        self.edit.grid(column=0, row=2, **opts)
        # 2d
        # 2d# 2d
        # 2d# 2d# 2d
        if self.name_page == "Площядь и Периметр Круга":
            mybutton = Button(page1, text="Расчет", command=self.p_circle_2D)
        elif self.name_page == "Площядь и Периметр Равностороннего Треугольника":
            mybutton = Button(page1, text="Расчет", command=self.p_striangle_2D)
        elif self.name_page == "Площядь и Периметр Квадрата":
            mybutton = Button(page1, text="Расчет", command=self.p_square_2D)
        elif self.name_page == "Площядь и Периметр Прямоугольной Трапеции":
            mybutton = Button(page1, text="Расчет", command=self.p_trapezium_2D)
        elif self.name_page == "Площядь и Периметр Прямоугольника":
            mybutton = Button(page1, text="Расчет", command=self.p_rectangle_2D)
        elif self.name_page == "Площядь и Периметр Ромба(равностроннего)":
            mybutton = Button(page1, text="Расчет", command=self.p_rhombus_2D)
        # 3d
        # 3d # 3d
        # 3d # 3d # 3d
        if self.name_page == "Площядь Сферы":
            mybutton = Button(page1, text="Расчет", command=self.sphere_3D)
        elif self.name_page == "Площадь, Объем и Периметр Куба":
            mybutton = Button(page1, text="Расчет", command=self.cube_3D)

        elif self.name_page == "Площадь, Объем и Периметр Параллелепипеда":
            mybutton = Button(page1, text="Расчет", command=self.parallelepiped_3D)

        elif self.name_page == "Площадь, Объем и Периметр Пирамиды":
            mybutton = Button(page1, text="Расчет", command=self.pyramid_3D)

        elif self.name_page == "Площадь, Объем и Периметр Цилиндра":
            mybutton = Button(page1, text="Расчет", command=self.cylinder_3D)
        elif self.name_page == "Площадь, Объем и Периметр Конуса":
            mybutton = Button(page1, text="Расчет", command=self.cone_3D)
        mybutton.grid(column=0, row=3, **opts)



    def p_circle_2D(self):
        r = int(self.edit.get())
        plt.xlim(-r * 2, r * 2)
        plt.ylim(-r * 2, r * 2)
        plt.gca().set_aspect('equal')
        ax = plt.gca()
        circle = Circle((0, 0), r)
        area_circle = 3.14 * r ** 2
        circumference = 2 * 3.14 * r
        self.text_area_circle = "Площядь круга = " + str(area_circle) + " Длина окружности =" + str(circumference)
        ax.add_patch(circle)
        self.path = 'test.png'
        plt.savefig(self.path)
        open_img.open_img(self, self.path, self.text_area_circle)

    def p_striangle_2D(self):
        a = int(self.edit.get())
        striangle_init=square(a)
        striangle_init.get_tr()

    def p_square_2D(self):
        a = int(self.edit.get())
        square_init = square(a)
        square_init.get_t()

    def p_trapezium_2D(self):
        a, b, c = map(int, self.edit.get().split())
        square_init = square(a, b=b, c=c)
        square_init.trapezium()

    def p_rectangle_2D(self):
        a, b = map(int, self.edit.get().split())
        square_init = square(a, b=b)
        square_init.rectangle()

    def p_rhombus_2D(self):
        a = int(self.edit.get())
        square_init = square(a)
        square_init.rhomb()
        # 1
        # 1
        # 3d
        # 1
        # 1

    def sphere_3D(self):
        a = int(self.edit.get())
        square_init = d3_visual(a)
        square_init.sphere_3d()

    def cube_3D(self):
        a = int(self.edit.get())
        cube_3D_init = d3_visual(a)
        cube_3D_init.cube_3D()

    def parallelepiped_3D(self):
        a, b, c = map(int, self.edit.get().split())
        parallelepiped_init = d3_visual(a, b=b, c=c)
        parallelepiped_init.parallelepiped_3D()

    def pyramid_3D(self):
        a, b, c = map(int, self.edit.get().split())
        pyramid_init = d3_visual(a, b=b, c=c)
        pyramid_init.pyramid_3D()

    def cylinder_3D(self):
        a, b = map(int, self.edit.get().split())
        pyramid_init = d3_visual(a, b=b)
        pyramid_init.cylinder_3D()

    def cone_3D(self):
        a, b = map(int, self.edit.get().split())
        pyramid_init = d3_visual(a, b=b)
        pyramid_init.cone_3D()