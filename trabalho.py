from sympy import *
from plotly.graph_objs import *
import plotly.graph_objs as go
import numpy as np
import plotly

class Hidro():

    def __init__(self, xi, yi):
        self.xi = xi
        self.yi = yi
        self.funcao = None
        self.matriz = []

    def gera_matriz(self):
        self.matriz.append(self.yi)
        for i in range(1,len(self.xi)):
            l=[]
            for j in range(len(self.xi)-i):
                l.append(((self.matriz[i-1][j+1])-self.matriz[i-1][j])/(self.xi[j+1]-self.xi[j]))
            self.matriz.append(l)
        #return self.matriz

    def newton(self):
        x=symbols('x')
        self.funcao = self.matriz[0][0]
        n=len(self.xi)
        t=1
        for i in range(1,n):
            t*=x-self.xi[i-1]
            self.funcao+=self.matriz[i][0]*t
        #return self.funcao

    def graf(self):
        self.gera_matriz()
        self.newton()
        x = symbols('x')
        x_valor = np.arange(self.xi[0], self.xi[len(self.xi)-1]+1, 0.1)
        y_valor = []

        for i in x_valor:
            y_valor.append(self.funcao.subs(x, i))
        print(x_valor)
        print(y_valor)

        linha = [go.Scatter(x=x_valor, y=y_valor, name='batimetria')]
        #data = Data([linha])
        layout = go.Layout(title='Perfil da Secção', xaxis=dict(title='distancia[m]'),
        yaxis = dict(title='altura[m]', autorange='reversed'))
        fig = go.Figure(data=linha, layout=layout)
        plotly.offline.plot(fig)
