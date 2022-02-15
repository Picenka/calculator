from tkinter import *
from open_img import *
from square import *
from d3_visualization import *


class create_widgets:
    def __init__(self, window_xd, name_page, name_label):
        self.window_xd = window_xd
        self.name_page = name_page
        self.name_label = name_label
        self.__create_widgets()

    def __create_widgets(self):
        self.notebook = ttk.Notebook(self.window_xd)
        self.notebook.grid(row=4, sticky="NSWE", columnspan=2)
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        page1 = ttk.Frame(self.notebook)
        self.notebook.add(page1, text=self.name_page)
        label = Label(page1, text=self.name_label)
        label.grid(column=0, row=1, **opts)
        self.edit = Entry(page1)
        self.edit.grid(column=0, row=2, **opts)
        self.dict_fig={'Площядь и Периметр Круга': self.p_circle_2D,
                        'Площядь и Периметр Треугольника':self.p_striangle_2D,
                        'Площядь и Периметр Квадрата': self.p_square_2D,
                        'Площядь и Периметр Прямоугольной Трапеции': self.p_trapezium_2D,
                        'Площядь и Периметр Прямоугольника': self.p_rectangle_2D,
                        'Площядь и Периметр Ромба(равностроннего)': self.p_rhombus_2D,
                        'Площядь Сферы': self.sphere_3D,
                        'Площадь, Объем и Периметр Куба': self.cube_3D,
                        'Площадь, Объем и Периметр Параллелепипеда': self.parallelepiped_3D,
                        'Площадь, Объем и Периметр Пирамиды': self.pyramid_3D,
                        'Площадь, Объем и Периметр Цилиндра': self.cylinder_3D,
                        'Площадь, Объем и Периметр Конуса': self.cone_3D,
                        }
        for key, value in self.dict_fig.items():
            if self.name_page==key:
                mybutton = Button(page1, text="Расчет", command=value)
                mybutton.grid(column=0, row=3, **opts)

    def p_circle_2D(self):
        a = int(self.edit.get())
        circle_init = square(a)
        circle_init.circle_2D()

    def p_striangle_2D(self):
        a, b, c = self.edit.get().split()
        striangle_init=d3_visual(a, b=b, c=c)
        striangle_init.get_tr3D()

    def p_square_2D(self):
        a = int(self.edit.get())
        square_init = square(a)
        square_init.get_t()

    def p_trapezium_2D(self):
        a, b, c = map(int, self.edit.get().split())
        trapezium_init = square(a, b=b, c=c)
        trapezium_init.trapezium()

    def p_rectangle_2D(self):
        a, b = map(int, self.edit.get().split())
        rectangle_init = square(a, b=b)
        rectangle_init.rectangle()

    def p_rhombus_2D(self):
        a = int(self.edit.get())
        rectangle_init = square(a)
        rectangle_init.rhomb()

         # 3d
    def sphere_3D(self):
        a = int(self.edit.get())
        square_init = d3_visual(a)
        square_init.sphere_3d()

    def cube_3D(self):
        a = int(self.edit.get())
        child_cubes_3d(a, a, a)

    def parallelepiped_3D(self):
        a, b, c = map(int, self.edit.get().split())
        child_cubes_3d(a, b, c)

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