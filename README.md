# CSS
Coherent SAT solver

Author: Sam Reifenstein

# Installation

## local install (windows)

1) create a python environment (e.g. CSS)
2) clone the python repository found at https://github.com/NTTRI-PHI-Algorithms/CSS
3) install via "pip install ." at the root of the repository
4) see notebook "SAT Solver.ipynb", or run "python ./CSS/random3-SAT.py",
"python ./CSS/phaseTransition.py"


# Description

## Introduction

The Coherent SAT Solver, or CSS, is a computational method designed to resolve Boolean satisfiability issues[1]. It employs a technique known as Chaotic Amplitude Control (CAC) to achieve this.

## Model

A boolean satisfiability problem can be given in conjunctive normal form (CNF). 
The coherent SAT solver is designed to find a vatiable assignment which satisifes of the problem, or, if it is unsatisfiable, find an assignment which satisifes the maximuum number of clauses (MAX-SAT). The SAT problem is specified by a sparse matrix $C_{ij}$ as follows:

$$C_{ij} =\{
\begin{array}{ll}
      1 &  i\text{th variable is included un-negated in }j\text{th clause} \\
      -1 & i\text{th variable is included negated in }j\text{th clause} \\
      0 & i\text{th variable is not included in }j\text{th clause} \\
\end{array} 
. $$


Then we also define the set $I_j$ for each clause as $I_j = \{ i \mid C_{ij} \neq 0 \}$
The boolean variables are represented by sof spins $x_i \in \mathbb{R}$ where $x_i > 0$ represents True and $x_i < 0$ represents False. Then we define the following quantaties:
$$K_j = \prod_{i \in I_j} \frac{1 - C_{ij}x_i}{2} \quad K_{ij} = \frac{-C_{ij}}{2}\prod_{k \in I_j, k \neq i} \frac{1 - C_{kj}x_k}{2} $$
Then, the coherent SAT solver equations can be written as:

$$\frac{dx_i}{dt} = (p-1)x_i - x_i^3 - e_i \sum_j K_{ij}$$
$$\frac{de_i}{dt} = \beta e_i (1 - x_i^2)$$

## Parameters

| Parameter | Interpretation |
| --------------- | --------------- |
| $T$          | Number of time steps         |
| $p$         | linear gain          |
| $\beta$         | Rate of change of auxiliary variables          |
| $\Delta t$         | Time step size          |


## Benchmark

A typical problem class used to benchmark SAT solver is random 3-SAT. A random 3-SAT problem is parameterised by number of variables (N), and number of clasues (M) as well as the clause to vairbale ratio $\alpha = M/N$. A problem is created by randomly generating M caluses with 3 vvariables each. Each variable is chosen randomly from the N possibilities (variables are not repeated in a clause) and the negation is chosen radnomly. It is known that in the limit that $N$ is large these random problems will be satisifiable with high probability if and only if $\alpha < \alpha_C$. This critical value of alpha is calculated to be around $\alpha_C \approx 4.26$.

## References

[1] Reifenstein, Sam, et al. "Coherent SAT solvers: a tutorial." Advances in Optics and Photonics 15.2 (2023): 385-441.