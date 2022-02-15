from vpython import *
import math


class d3_visual:
    def __init__(self, a, **kwargs):
        self.a = a
        if len(kwargs) == 1:
            self.b = kwargs["b"]
        elif len(kwargs) == 2:
            self.b = kwargs["b"]
            self.c = kwargs["c"]

    def sphere_3d(self):
        sphere(pos=vector(0, 0, 0), radius=self.a)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь поверхности сферы =' + str(3.1416 * (self.a * 2) ** 2))

    # def cube_3D(self):
    #     box(pos=vector(0, 0, 0), length=self.a, height=self.a, width=self.a)
    #     label(pos=vec(self.a + self.a * 1.1, 0, 0),
    #           text='Площадь куба =' + str(6 * (self.a * 2)) +
    #                '\n Объем =' + str(self.a ** 3) +
    #                '\n Периметр =' + str(self.a * 12))

    # def parallelepiped_3D(self):
    #     box(pos=vector(0, 0, 0), length=self.a, height=self.b, width=self.c)
    #     p = 2 * (self.a * self.b + self.a * self.c + self.c * self.b)
    #     label(pos=vec(self.a + self.a * 1.1, 0, 0),
    #           text='Площадь Параллелепипеда =' + str(self.a * 4 + self.b * 4 + self.c * 4) +
    #                '\n Объем  =' + str(self.a * self.b * self.c) +
    #                '\n Периметр =' + str(p))

    def pyramid_3D(self):
        pyramid(pos=vector(0, 0, 0), length=self.a, height=self.b, width=self.c)
        s = self.a * self.c
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь основания Пирамиды =' + str(s) +
                   '\n Объем Пирамиды =' + str(s / 3 * self.b))

    def cylinder_3D(self):
        cylinder(pos=vector(0, 0, 0), length=self.a, radius=self.b)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь Цилиндра =' + str(2 * 3.1416 * self.b * (self.a + self.b)) +
                   '\n Объем  =' + str(3.1416 * self.b ** 2 * self.a) +
                   '\n Поверхность цилиндра =' + str(2 * 3.1416 * self.b * self.a))

    def cone_3D(self):
        cone(pos=vector(0, 0, 0), length=self.a, radius=self.b)
        l = sqrt(self.a ** 2 + self.b ** 2)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь Конуса =' + str(3.1416 * self.b * (l + self.b)) +
                   '\n Объем  =' + str(3.1416 / 3 * self.b ** 2 * self.a))

    def get_tr3D(self):
        x1, y1 = map(int, self.a.split('.'))
        x2, y2 = map(int, self.b.split('.'))
        x3, y3 = map(int, self.c.split('.'))
        # рисуем
        a = vertex(pos=vec(x1, y1, 0))
        b = vertex(pos=vec(x2, y2, 0))
        c = vertex(pos=vec(x3, y3, 0))
        triangle(v0=a, v1=b, v2=c)
        # применяем формулу Герона
        ab = abs(sqrt((x2 - x1) * 2 + (y2 - y1) * 2))
        ac = abs(sqrt((x3 - x1) * 2 + (y3 - y1) * 2))
        bc = abs(sqrt((x3 - x2) * 2 + (y3 - y2) * 2))
        p=bc+ac+ab
        pp=p/2
        s=sqrt(pp*(pp-ab)*(pp-ac)*(pp-bc))
        label(pos=vec(x1-5, y1-5, 0), text= 'Площядь треугольника = '+ str(s) + '\n Периметр треугольника ='+ str(p/2))

# реализация наследования
class cubes_3d:
    def __init__(self, length, height, width):
        self.a = length
        self.b = height
        self.c = width
        self.parallelepiped_3D()

    def parallelepiped_3D(self):
        box(pos=vector(0, 0, 0), length=self.a, height=self.b, width=self.c)

class child_cubes_3d(cubes_3d):
    def parallelepiped_3D(self):
        def who_are_you(a, b, c):
            if a == b == c:
                return 'Куб'
            else:
                return "Параллелепипед"

        p = 2 * (self.a * self.b + self.a * self.c + self.c * self.b)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь ' + who_are_you(self.a, self.b, self.c) + 'а =' + str(
                  self.a * 4 + self.b * 4 + self.c * 4) +
                   '\n Объем  =' + str(self.a * self.b * self.c) +
                   '\n Периметр =' + str(p))
        cubes_3d.parallelepiped_3D(self)
