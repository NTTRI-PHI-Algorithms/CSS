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
alpha_range = np.arange(3.0, 5.0, 0.25)

N_inst = 10

Ps_list_all = []
Ps_avg_list = []
Nsolved_list = []

for alpha in alpha_range:
    
    Ps_list = []
    M = int(N*alpha)
    print("alpha = ", alpha)
    print("solving...")
    for SEED in range(N_inst):
        
        
        

        
        random.seed(SEED)

        #generate problem instance
        C, IDX = inst_uils.randSAT(N,M,K)



        #setup solver
        pt_device = "cpu"

        solver = satcac.SAT(pt_device, N, IDX = IDX, C = C)


        #solver parameters
        solver.T = 2000
        solver.beta = 0.1
        solver.p_init = -1.0
        solver.p_end = 1.0
        solver.dt = 0.05

        #initialize solver to run 10 trajectories
        R = 40
        solver.init(R)

        start_time = time.time()

        



        Ps, E_opt = solver.traj(0)


        print("%i/%i :" % (SEED, N_inst) , Ps)
        Ps_list.append(Ps)
    
    Ps_list_all.append(Ps_list)
    Ps_avg_list.append(np.average(Ps_list))
    Nsolved_list.append(len([Ps for Ps in Ps_list if Ps > 0]))

    
#plot results
alpha_C = 4.266

plt.ylabel("Number solved out of %i" % N_inst)
plt.xlabel(r"$\alpha$")

plt.plot(alpha_range, Nsolved_list)
plt.plot([alpha_C, alpha_C], [0, N_inst], color = "gray", dashes = [3,3])

plt.show()
plt.close()


plt.ylabel("Average Success Rate")
plt.xlabel(r"$\alpha$")

plt.plot(alpha_range, Ps_avg_list)
plt.plot([alpha_C, alpha_C], [0, 1], color = "gray", dashes = [3,3])

plt.show()
plt.close()


#plot results

plt.ylabel("Sucess Rate")
plt.xlabel(r"$\alpha$")


for alpha, Ps_list in zip(alpha_range, Ps_list_all):
    plt.scatter([alpha]*N_inst, Ps_list, color = "blue")

    
plt.plot([alpha_C, alpha_C], [0, 1], color = "gray", dashes = [3,3])

plt.show()
plt.close()

