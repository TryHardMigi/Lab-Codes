import scipy.stats as stats
import LT.box as B
import LT_Fit.parameters as param
import LT_Fit.gen_fit as gen
import math 
import random
import numpy as np




# By simply running the function without changing anything the output will give you results in this order
# 2d volume, uncertainty
# 3d volume, uncertainty
# 1d volume, uncertainty
# 4d volume, uncertainty
# 5d volume, uncertainty
#Histogram fit results



def approx_pi():
    i = 1
    counter = 0
    stop_iter = 0

    while True:
        x = random.random()
        y = random.random()
        if ((x**2) + (y**2)) < 1:
            counter +=1
        if np.absolute((counter/i)*4 - np.pi) < 0.0001:
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*4,np.absolute((counter/i)*4 - np.pi))
            break
        elif stop_iter > 10000:
            print('Hit max iterations!')
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*4,np.absolute((counter/i)*4 - np.pi))
            break
        
        i+=1
        stop_iter+=1

approx_pi()


def threeD():
    i = 1
    counter = 0
    stop_iter = 0

    while True:
        x = random.random()
        y = random.random()
        z = random.random()
        if ((x**2) + (y**2) + (z**2)) < 1:
            counter +=1
        if np.absolute((counter/i)*8 - 4.1887902047863905) < 0.0001:# the 4.1887902047863905 is the analytic solution 
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*8,np.absolute((counter/i)*8 - 4.1887902047863905))
            break
        elif stop_iter > 10000:
            print('Hit max iterations!')
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*8,np.absolute((counter/i)*8 - 4.1887902047863905))
            break
        
        i+=1
        stop_iter+=1

threeD()

def oneD():
    i = 1
    counter = 0
    stop_iter = 0

    while True:
        x = random.random()
        if ((x**2)) < 1:
            counter +=1
        if np.absolute((counter/i)*2 - 2) < 0.0001: #2 is the analytic solution
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*2,np.absolute((counter/i)*2 - 2))
            break
        elif stop_iter > 10000:
            print('Hit max iterations!')
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*2,np.absolute((counter/i)*2 - 2))
            break
        
        i+=1
        stop_iter+=1

oneD()

def fourD():
    i = 1
    counter = 0
    stop_iter = 0

    while True:
        x = random.random()
        y = random.random()
        z = random.random()
        a = random.random()
        if ((x**2) + (y**2) + (z**2) + (a**2)) < 1:
            counter +=1
        if np.absolute((counter/i)*16 - 4.9348) < 0.0001:# the 4.9348 is the analytic solution 
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*16,np.absolute((counter/i)*16 - 4.9348))
            break
        elif stop_iter > 10000:
            print('Hit max iterations!')
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*16,np.absolute((counter/i)*16 - 4.9348))
            break
        
        i+=1
        stop_iter+=1

fourD()

def fiveD():
     i = 1
     counter = 0
     stop_iter = 0
     
     while True:
        x = random.random()
        y = random.random()
        z = random.random()
        a = random.random()
        b = random.random()
        if ((x**2) + (y**2) + (z**2) + (a**2) +(b**2)) < 1:
            counter +=1
        if np.absolute((counter/i)*32 - 5.26379) < 0.0001:# the 5.26379 is the analytic solution 
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*32,np.absolute((counter/i)*32 - 5.26379))
            break
        elif stop_iter > 10000:
            print('Hit max iterations!')
            # print(f'Iterations:{i} | Counter: {counter} | Approx: {i/counter}')
            print((counter/i)*32,np.absolute((counter/i)*32 - 5.26379))
            break
        
        i+=1
        stop_iter+=1

fiveD()

xbin = []
box = []
num = 10000
for ii in range(num):
    
 x1 = random.random()
 y1 = random.random()
 z1 = np.sqrt(-2 * np.log(x1)) * np.cos(2 * np.pi * y1)
 
 box.append(z1)
 xbin.append(x1)
 
mean = np.average(xbin)

SD = np.std(xbin)

graph = B.histo (box, range = (-4,4), bins = 50)
graphx = graph.bin_center
graphy = graph.bin_content

miu = param.Parameter(mean,'mu')
sigma = param.Parameter(SD,'sigma')
height = param.Parameter(700.,'height')
factor = len(box) * (8./40.)

def gauss(x):
    
 gaussgraph = stats.norm.pdf((x-miu()) / sigma()) * factor
 
 return gaussgraph

fit = gen.genfit(gauss, [height, miu, sigma], x = graphx, y = graphy)

B.plot_line(fit.xpl, fit.ypl, color = 'yellow', linewidth = 2)


graph.plot()
graph.fit()
B.pl.show()




#ignore below _____________________________________________________________________________________________________________________________


# def generateData(length):
#     x,y = [],[]
#     for _ in range(length):
#         x.append(random.random())
#         y.append(random.random())

      
#     randomData = {
#         'x':x,
#         'y':y
#     }

#     df = pd.DataFrame(randomData)
#     return df

# def mc_simulation(num,ct):

#     df = generateData(num)
    
#     df['x2'] = (df['x']**2) + (df['y']**2)

#     counter = df[df['x2']<1]['x2'].count()

#     if np.absolute((num/counter)-np.pi) < 0.01:
#         print(num,counter)
#     elif ct > 10000:
#         print('Too many iterations')
#         print(num,counter)
#     else:
#         print(num/counter)
#         mc_simulation(num + 1000,ct+1)
    

# mc_simulation(100,0)
#!____________________________________________________________________________________________