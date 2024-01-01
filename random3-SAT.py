import numpy as np
import time
import SAT_CAC as satcac
import InstanceUtils as inst_uils



import torch
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import scipy.sparse

#instance parameters
N = 50

K = 3
alpha = 3.8

M = int(N*alpha)

print("N", N)
print("M", M)
print("K", K)

print("generating problem...")

SEED = 0
random.seed(SEED)

#generate problem instance
C, IDX = inst_uils.randSAT(N,M,K)



#setup solver
pt_device = "cpu"

solver = satcac.SAT(pt_device, N, IDX = IDX, C = C)


#solver parameters
solver.T = 5000
solver.beta = 0.1
solver.p_init = -1.0
solver.p_end = 1.0
solver.dt = 0.05

#initialize solver to run 10 trajectories
R = 100
solver.init(R)

start_time = time.time()

#solve
print("solving...")



Ps, E_opt, traj_info = solver.traj(0, R_rec = 1)

print("Sucess Rate", Ps)
print("Best Energies Found", E_opt)

print(time.time() - start_time, "s")

print("Plots of first trajectory:")
plt.plot(traj_info["T"], traj_info["E"])
plt.xlabel("Time Step")
plt.ylabel("SAT Energy (Number of uunsatififed clauses)")

plt.show()
plt.close()


for i in range(N):
    plt.plot(traj_info["T"], traj_info["x"][:,i])
    
plt.xlabel("Time Step")
plt.ylabel("x variable")


plt.show()
plt.close()

for i in range(N):
    plt.plot(traj_info["T"], traj_info["e"][:,i])
    
plt.xlabel("Time Step")
plt.ylabel("e variable")

plt.show()
plt.close()




