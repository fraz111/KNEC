import numpy as np
from math import pi
from matplotlib import pyplot as plt

with open("sfho_m140120_m0_ber.dat") as original_file:
    quantity_info = original_file.readline()
    data = original_file.readlines()

Mass = np.zeros(len(data))
Entropy = np.zeros(len(data))
Rho = np.zeros(len(data))
Temperature = np.zeros(len(data))
Ye = np.zeros(len(data))
Velocity = np.zeros(len(data))

Radius = np.zeros(len(data))



for i in range(len(data)):
    line = data[i].split()
    Mass[len(data)-1-i] = float(line[0])
    Entropy[len(data)-1-i] = float(line[1])
    Rho[len(data)-1-i] = float(line[2])
    Temperature[len(data)-1-i] = float(line[3])
    Ye[len(data)-1-i] = float(line[4])
    Velocity[len(data)-1-i] = float(line[5])

r_inner = 2.95e7 

Radius[0] = r_inner

for i in range(1,len(data)):
    
    dmass = Mass[i]-Mass[i-1]
    r_center = (Radius[i-1]**3 + dmass/2/(4*pi/3*Rho[i-1]))**(1/3)
    Radius[i] = (r_center**3 + dmass/2/(4*pi/3*Rho[i]))**(1/3)

with open("modified_sfho_m140120_m0_ber.dat",'w') as outfile:
    outfile.write(str(len(Mass))+'\n')
    for i in range(len(Mass)):
        s0=str(i+1).rjust(6," ")
        s1="     %.9e" %Mass[i]
        s2="     %.9e" %Radius[i] 
        s3="     %.9e" %Temperature[i]
        s4="     %.9e" %Rho[i]
        s5="     %.9e" %Velocity[i]
        s6="     %.9e" %Ye[i]
        s7="     %.9e" %Entropy[i]        
        outfile.write(s0+s1+s2+s3+s4+s5+s6+s7+'\n')
    










