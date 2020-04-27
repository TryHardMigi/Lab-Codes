import LT.box as B
import numpy as np
import pandas as pd
import LT_Fit.parameters as P
import LT_Fit.gen_fit as G

df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\NMR\\T1A7.18B3.54.csv')

DIF = df['Voltage(V)']
tao = df['tao(s)']

y = np.log(0.5*(1-(DIF/4.055432285469148)))





B.plot_exp(tao,y,0.02)
B.pl.title('Spin Echo VS Tau Linear')
B.pl.ylabel('Spin Echo (v)')
B.pl.xlabel('Tau(s)')
fit1 = B.linefit(tao,y)
B.plot_line(fit1.xpl,fit1.ypl)

slope = fit1.par[1]

T1 = -1/slope
print(T1)
print (1/0.26248527624448215)



# M0 = P.Parameter(4.055432285469148, 'M0')
# T1 = P.Parameter(0.04900121822053086, 'T1')
# c1=  P.Parameter (0,'c1')

# fit1 = B.polyfit(tao, DIF, 0.02)
# B.plot_line(fit1.xpl, fit1.ypl, color='green')
# def myfun(x):
#     value = M0()*(1-2*np.exp(-(x/T1())))+c1()
#     return (value)
# # fit2 = G.genfit(myfun, [ M0, T1,c1], x = tao, y = y,
# #                 y_err = 0.02)
# # B.plot_line(fit2.xpl, fit2.ypl, color='blue')
# B.pl.figtext(0.6, 0.5, "T1 = 0.049 ")

B.pl.show()









