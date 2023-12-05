# CSS
Coherent SAT solver - Curator: Sam Reifenstein

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
