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

    def cube_3D(self):
        box(pos=vector(0, 0, 0), length=self.a, height=self.a, width=self.a)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь куба =' + str(6 * (self.a * 2)) +
                   '\n Объем =' + str(self.a ** 3) +
                   '\n Периметр =' + str(self.a * 12))

    def parallelepiped_3D(self):
        box(pos=vector(0, 0, 0), length=self.a, height=self.b, width=self.c)
        p=2* (self.a * self.b + self.a * self.c + self.c * self.b)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь Параллелепипеда =' + str(self.a * 4 + self.b * 4 + self.c * 4) +
                   '\n Объем  =' + str(self.a * self.b * self.c) +
                   '\n Периметр =' + str(p))

    def pyramid_3D(self):
        pyramid(pos=vector(0, 0, 0), length=self.a, height=self.b, width=self.c)
        print(self.a, self.b, self.c)
        s=self.a * self.c
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь основания Пирамиды =' + str(s) +
                   '\n Объем Пирамиды =' + str(s/3*self.b) )

    def cylinder_3D(self):
        cylinder(pos=vector(0, 0, 0), length=self.a, radius =self.b)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь Цилиндра =' + str(2*3.1416*self.b*(self.a+self.b)) +
                   '\n Объем  =' + str(3.1416*self.b**2*self.a) +
                   '\n Поверхность цилиндра =' + str(2*3.1416*self.b*self.a))

    def cone_3D(self):
        cone(pos=vector(0, 0, 0), length=self.a, radius =self.b)
        l=sqrt(self.a**2+self.b**2)
        label(pos=vec(self.a + self.a * 1.1, 0, 0),
              text='Площадь Конуса =' + str(3.1416*self.b*(l+self.b)) +
                   '\n Объем  =' + str(3.1416/3*self.b**2*self.a) )
