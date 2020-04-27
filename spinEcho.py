import LT.box as B
import numpy as np
import pandas as pd

df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\NMR\\T22.csv')


spinEcho = df['Voltage(V)']
tao = df['tao(s)']

y = np.log(spinEcho)

# dy = np.sqrt(((1/spinEcho)*0.02)**2)
dy = df['dy']



B.plot_exp(tao,y,0.03)

B.pl.title('FID VS Tao: Linear ')
B.pl.xlabel('Tao(s)')
B.pl.ylabel('FID (v)')
fit1 = B.linefit(tao,y)
B.plot_line(fit1.xpl,fit1.ypl)
# fit1 = B.polyfit(tao,spinEcho)
# B.plot_line(fit1.xpl, fit1.ypl)

B.pl.show()

slope = fit1.par[1]

T2 = -1/slope

m0 = np.exp(1.4000572874265063)
print(T2)

print(m0)
print (1/1.4720613294391014)
