import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
from open_img import *
class square:
    def __init__(self,a,**kwargs):
        self.a = a
        if len(kwargs)==1:
            self.b = kwargs["b"]
        elif len(kwargs)==2:
            self.b = kwargs["b"]
            self.c = kwargs["c"]

    def get_t(self):
        a=self.a
        plt.xlim(-1 , a * 1.5)
        plt.ylim(-1 , a * 1.5)
        plt.gca().set_aspect('equal')
        ax = plt.gca()
        ax.add_patch(patches.Rectangle((0, 0),  a,  a))
        ax.autoscale_view()
        self.text_area_circle="Площядь квадрата  = "+str(a*a)+" Периметр квадрата ="+str(4*a)
        self.path = 'test.png'
        plt.savefig(self.path)
        open_img.open_img(self,self.path,self.text_area_circle)

    def trapezium(self):
        plt.fill_between([0, self.a], [self.b, self.c])
        plt.xlim([-1, self.b*2]);
        plt.ylim([-1, self.c*2]);
        plt.gca().set_aspect('equal')
        hd= abs(self.b - self.c)
        cd= math.sqrt(self.b*2+hd*2)
        if self.b > self.c:
            s=(self.a+self.b)/2*self.c
        elif self.b < self.c:
            s = (self.a + self.c) / 2 * self.b
        else:
            s=self.a * self.c
        self.text_area_circle = "Площядь трапеции  = " + str(s) +\
                                "Периметр трапеции =" + str(self.a +self.b + self.c + cd)
        self.path = 'test.png'
        plt.savefig(self.path)
        open_img.open_img(self, self.path, self.text_area_circle)

    def rectangle(self):
        a=self.a
        b=self.b
        plt.xlim(-1 , a * 1.5)
        plt.ylim(-1 , a * 1.5)
        plt.gca().set_aspect('equal')
        ax = plt.gca()
        ax.add_patch(patches.Rectangle((0, 0),  a,  b))
        ax.autoscale_view()
        self.text_area_circle="Площядь прямоугольника  = "+str(a*b)+" Периметр прямоугольника ="+str(2*(b*a))
        self.path = 'test.png'
        plt.savefig(self.path)
        open_img.open_img(self,self.path,self.text_area_circle)

    def rhomb(self):
        a=self.a
        plt.xlim(-1 , a * 2)
        plt.ylim(-1 , a * 2)
        plt.gca().set_aspect('equal')
        ax = plt.gca()
        ax.add_patch(patches.Rectangle((a, 0),  a,  a,angle=45))
        ax.autoscale_view()
        self.text_area_circle="Площядь ромба  = "+str(a*a)+" Периметр ромба ="+str(4*a)
        self.path = 'test.png'
        plt.savefig(self.path)
        open_img.open_img(self,self.path,self.text_area_circle)