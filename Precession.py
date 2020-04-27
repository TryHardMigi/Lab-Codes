import numpy as np
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt
import LT.box as B


#first we're going to make a plot of frequency over time.

df1 = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Magnetic Moment\\Data3.2.csv')



# B.plot_exp (df1['Time(s)'],df1['Frequency(Hz)'],0.25)


# B.pl.title("Freq over Time")
# B.pl.ylabel("Frequency (strobe counts)")
# B.pl.xlabel("Time (s)")

# fit1 = B.linefit(df1['Time(s)'], df1['Frequency(Hz)'])
# B.plot_line(fit1.xpl, fit1.ypl)
# B.pl.show()


mu_naught  = 4*np.pi*10**-7
# units in (kg*m)/((s**2)*(A**2))
R = (23.5+17.9)/2
sigma_R = (0.05**2)/2
R = R/100
sigma_R = sigma_R/100
# units of R in m

N = 195

Bfield  = ((mu_naught*N*df1['Current(A)'])/(R))*((4/5)**(3/2))




df2 = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Magnetic Moment\\DataFinal.csv')


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



precesion_period = df2['Time(s)']/df2['Period(cycle)']
omega = (2*np.pi)/precesion_period
ang_vel = 2*np.pi*df2['Strobe']

L = moment_I*ang_vel

BoverL = 0.002541/L

#error propagation

sigma_T = df2['sigmat(s)']

sigma_omega = ((-2*np.pi)/(precesion_period**2))*np.sqrt(sigma_T)



sigma_strobe = 0.05

sigma_B = np.sqrt((((mu_naught/(2*np.pi*R))*df1['Sigmai(A)'])**2)+(((-mu_naught*3.00)/(2*np.pi*((R)**2))*sigma_R)**2))

sigma_ang_vel = np.sqrt(sigma_strobe)

sigma_Imoment = (2/5)*np.sqrt(((((rBall)**2)*sigma_mBall)**2)+((2*(rBall*mBall*sigma_rBall))**2))

sigma_L = np.sqrt(((ang_vel*sigma_Imoment)**2)+((moment_I*sigma_ang_vel)**2))

sigma_mu = np.sqrt((((1/BoverL)*sigma_omega)**2)+(((-omega*L/((0.002541)**2))*sigma_B)**2)+(((omega/0.002541)*sigma_L)**2))

errorbar = sigma_omega


B.plot_exp (BoverL,omega,0.008)

B.pl.title("Precesional Frequency over B/L")
B.pl.ylabel("Frequency (HZ)")
B.pl.xlabel("B/L")

fit2 = B.linefit(BoverL,omega)
B.plot_line(fit2.xpl, fit2.ypl)
B.pl.show()




