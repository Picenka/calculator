import numpy as np
import matplotlib.pyplot as plt
import math
from open_img import *

class triangle:
    def __init__(self,a):
        self.a = a
        self.b = a
        self.c = a

    def calc_angles(self,a, b, c):
        # работает только если стороны близкие по размерам
        a_arccos = (b ** 2 + c ** 2 - a ** 2) / (2. * b * c)
        if a_arccos >= -1 and a_arccos <= 1:
            alpha = np.arccos(a_arccos)
        else:
            alpha = np.arccos(a_arccos % 1)
        b_arccos = (-b ** 2 + c ** 2 + a ** 2) / (2. * a * c)
        if b_arccos >= -1 and b_arccos <= 1:
            beta = np.arccos(b_arccos)
        else:
            beta = np.arccos(b_arccos % 1)
        gamma = np.pi - alpha - beta

        return alpha, beta, gamma

    def calc_point(self,alpha, beta, c):
        x = (c * np.tan(beta)) / (np.tan(alpha) + np.tan(beta))
        y = x * np.tan(alpha)
        return (x, y)

    def get_triangle(self,a, b, c):
        z = np.array([a, b, c])
        while z[-1] != z.max():
            z = z[[2, 0, 1]]
        alpha, beta, _ = self.calc_angles(*z)
        x, y = self.calc_point(alpha, beta, z[-1])
        return [(0, 0), (z[-1], 0), (x, y)]


    def get_t(self):
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        dreieck = plt.Polygon(self.get_triangle(self.a, self.a, self.a))
        ax.add_patch(dreieck)
        ax.relim()
        ax.autoscale_view()
        area_triangle=(self.a**2*math.sqrt(3))/4

        self.text_area_circle="Площядь треугольника  = "+str(area_triangle)+" Периметр треугольника ="+str(self.a*3)

        self.path = 'test.png'
        plt.savefig(self.path)
        open_img.open_img(self,self.path,self.text_area_circle)