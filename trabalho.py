from sympy import *
from calcvelocidade import *
from plotly.graph_objs import *
import plotly.graph_objs as go
import numpy as np
import plotly

class Hidro():

    def __init__(self, xi, yi,v20,v60,v80):
        self.xi = xi
        self.yi = yi
        self.quantidade = len(yi)
        self.area = []
        self.n20 = v20
        self.n60 = v60
        self.n80 = v80
        self.v20 = []
        self.v60 = []
        self.v80 = []
        self.vmedia = []
        self.vsetor = []

    def area_setor(self):
        for i in range(self.quantidade - 1):
            if i == 0:
                self.area.append((self.yi[i+1]*0.2)/2)
            elif i == (self.quantidade - 2):
                self.area.append(self.yi[i]*0.1)
            else:
                self.area.append((self.yi[i]+self.yi[i+1])*0.1)

    def velocidades(self):
        for i in range(len(self.n20)):
            v1 = vel(self.n20[i])
            self.v20.append(v1)
            v2 = vel(self.n60[i])
            self.v60.append(v2)
            v3 = vel(self.n80[i])
            self.v80.append(v3)

            media = (v1 + 2*v2 + v3) / 4
            self.vmedia.append(media)

        for i in range(len(self.vmedia)+1):
            if i == 0:
                self.vsetor.append(self.vmedia[i]/2)
            elif i == (len(self.vmedia)):
                self.vsetor.append(self.vmedia[i-1]/2)
            else:
                self.vsetor.append((self.vmedia[i]+self.vmedia[i-1])/2)
        


    def graf(self):

        linha = [go.Scatter(x=self.xi, y=self.yi, name='batimetria',
                line=dict(shape='spline', width=4))]

        layout = go.Layout(title='Perfil da Secção', xaxis=dict(title='distancia[m]'),
        yaxis = dict(title='altura[m]', autorange='reversed'))
        fig = go.Figure(data=linha, layout=layout)
        plotly.offline.plot(fig)
