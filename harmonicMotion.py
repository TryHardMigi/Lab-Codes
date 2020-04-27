import numpy as np
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt
import LT.box as B

df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Magnetic Moment\\harmonic1.csv')

N = 195

mu_naught  = 4*np.pi*10**-7
# units in (kg*m)/((s**2)*(A**2))

T = (df['Time(s)'])/3

Tsquared = T**2

R = (23.5+17.9)/2
sigma_R = (0.05**2)/2
R = R/100
sigma_R = sigma_R/100
# units of R in m

rBall = 5.15/2
rBall = rBall/100
sigma_rBall = 0.05
sigma_rBall = sigma_rBall/100
# units in m

mBall = 142.01
mBall = mBall/1000
sigma_mBall = 0.05
sigma_mBall = sigma_mBall/1000
# units in kg

moment_I = (2*mBall*(rBall**2))/5

Bfield = ((mu_naught*N*df['Current(A)'])/(R))*((4/5)**(3/2))

IoverB = moment_I/Bfield


axis_X = 4*(np.pi**2)*IoverB

print(Bfield)

B.plot_exp(Tsquared,axis_X,0.15)

B.pl.title("Harmonic Motion")
B.pl.ylabel("4pi*I/B  (T^-1)")
B.pl.xlabel("period squared (s^2)")
fit2 = B.linefit(Tsquared,axis_X,)

B.plot_line(fit2.xpl, fit2.ypl)
B.pl.show()

# plt.plot([list(axis_X)],[list(Tsquared)],'ro')
# plt.ylabel('period squared (s^2)')
# plt.xlabel('4pi*I/B  (T^-1)')
# plt.show()
