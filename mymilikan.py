import numpy as np
import pandas as pd
import LT.box as B
import decimal 

# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\1.1.csv')
# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\1.2.csv')
# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\2.3.csv')
# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\2.4.csv')
# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\3.5.csv')
# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\3.6.csv')
# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\4.7.csv')
# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\4.8.csv')

# df = pd.read_csv('C:\\Users\\iw2ba\\Desktop\\Senior Physics\\Milikan\\test.csv')

# p = 1.03454e5 # barometric pressure of dry air [Pa]
# do = 8.8000e2 #density of oil [kg/m^3]
# g = 9.79 #acceleration of gravity [m/s^2]
# eta = 1.8400e-5 #viscosity of air at ~23 deg Celsius this changes per file
# b = 8.20e-3 #constant [Pa*m]
# d = .0078 #plate sepaaration [m]
# E = 500/d #Eletric field [V/m]
# n_con = (9*eta)/(2*g*do)
# bover2p = b/(2*p)

# df = df.round({'falltime': 10, 'ristime':10})

# falltime = df['falltime']
# risetime  = df['risetime']

# v_fall = 0.0005/falltime #fall velocity in m/s
# v_rise = 0.0005/risetime #rise velocity in m/s




# v_combined = (v_fall+v_rise)/v_fall

# a = np.sqrt((bover2p**2)+(v_fall*n_con))-(bover2p)

# N = np.sqrt(((bover2p)**2)+(n_con*v_fall))


# Q = (4/3)*np.pi*do*g*((N-bover2p)**3)*(v_combined/E)



# Qne = np.average(Q)



# print(Qne)

# print('Q1 = 2.52e-19')
# print('Q2 = 17.54e-19')
# print('Q3 = 9.95e-19')
# print('Q4 = 11.80e-19')
# print('Q5 = 12.42e-19')
# print('Q6 = 4.82e-19')
# print('Q7 =10.14e-19')
# print('Q8 = 2.57e-19')

Q1 = 1.764
Q2 = 12.278
Q3 = 6.97
Q4 = 8.26
Q5 = 8.69
Q6 = 3.374
Q7 = 7.10
Q8 = 1.80

print('q = 1.764e-19 C')
print('Percent error  =10.11%')
data = {'Qs':[1.764,12.278,6.97,8.26,8.69,3.374,7.10,1.80]}
df1 = pd.DataFrame(data)

q_int = df1['Qs']/Q1


df1['Q_int'] = round(q_int)

df1.dropna(inplace = True)
df1.reset_index(inplace = True, drop = True)


B.plot_exp(df1['Q_int'],df1['Qs'],.3)
B.pl.title('Method of Smallest Value')
B.pl.ylabel('Drop Charge (e^-19 Coulombs)')
B.pl.xlabel('# of Electrons lost')

fit2 = B.linefit(df1['Q_int'],df1['Qs'],)

B.plot_line(fit2.xpl, fit2.ypl)

B.pl.show()















    