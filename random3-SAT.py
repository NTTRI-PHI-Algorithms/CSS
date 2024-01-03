## CSS
# Coherent SAT solver
# Author: Sam Reifenstein

##BSD 3-Clause License

#Copyright (c) 2023, NTT Research Inc., PHI labs, algorithms

#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

#1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

#2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

#3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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




