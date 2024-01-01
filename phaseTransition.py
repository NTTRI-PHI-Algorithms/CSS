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

