import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import LT.box as B

df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Magnetic Moment\\magtorque=gravtorque.csv')
#? units of I is in amperes
#?units of r are in cm
#sigma is the symbol used to represent uncertainty so I place it in front of every variable that requires it. 
#I have grabbed my 'current' values and their uncertainties from the data file. 

#i know that mu-cross-Bfield=r-cross-mg where m is the mass of our slider, and r is the radius of the slider from the center.

m = 1.5
sigma_m = 0.05
m = m/1000
sigma_m = sigma_m/1000
#units in kg

#define gravity
g = 9.8
#units of gravity in m/s**2
mu_naught  = 4*np.pi*10**-7
# units in (kg*m)/((s**2)*(A**2))


R = (23.5+17.9)/2
sigma_R = (0.05**2)/2
R = R/100
sigma_R = sigma_R/100
# units of R in mn

N = 195

Bfield  = ((mu_naught*N*df['I'])/(R))*((4/5)**(3/2))
# Bfield = Bfield*10**6
#units in kg/As^2
Torque = df['r']*m*g
Torque = Torque/100

#error propagation 
sigma_Torque = np.sqrt(((m*g*df['sigmar'])**2)+((df['r']*g*sigma_m)**2))

# print(sigma_Torque)



B.plot_exp(Bfield,Torque,0.00004)

B.pl.title("Torque Vs Magentic Field")
B.pl.ylabel("Torque   [(kgm^2)/(s^2)]")
B.pl.xlabel("Magnetic field *10^-6  [kg/(s^2)(A)]")

fit2 = B.linefit(Bfield,Torque)
B.plot_line(fit2.xpl, fit2.ypl)
B.pl.show()












