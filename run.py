from trabalho import *

x=[0.2 * h for h in range(35)]
y=[0,0.7,0.7,0.82,0.87,
0.9,0.92,0.96,1.01,1.03,
1.06,1.08,1.11,1.11,1.12,1.13,
1.12,1.12,1.08,1.08,1.08,
1.07,1.07,1.07,1.06,1.05,
1.04,1.02,1.01,1,1,
0.8,0.6,0.47,0]

teste = Hidro(x,y)
teste.area_setor()
