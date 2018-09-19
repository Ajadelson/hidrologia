from sympy import *
from plotly.graph_objs import *
import plotly.graph_objs as go
import numpy as np
import plotly

class Hidro():

    def __init__(self, xi, yi):
        self.xi = xi
        self.yi = yi
        self.quantidade = len(yi)
        self.area = []

    def area_setor(self):
        for i in range(self.quantidade - 1):
            if i == 0:
                self.area.append((self.yi[i+1]*0.2)/2)
            elif i == (self.quantidade - 2):
                self.area.append(self.yi[i]*0.1)
            else:
                self.area.append((self.yi[i]+self.yi[i+1])*0.1)
        print (self.area)
        print(len(self.area))

    def graf(self):

        linha = [go.Scatter(x=self.xi, y=self.yi, name='batimetria',
                line=dict(shape='spline', width=4))]

        layout = go.Layout(title='Perfil da Secção', xaxis=dict(title='distancia[m]'),
        yaxis = dict(title='altura[m]', autorange='reversed'))
        fig = go.Figure(data=linha, layout=layout)
        plotly.offline.plot(fig)
