**Theorem: Protected Pareto Frontier Invariance under Desire Floor**

**Statement**  
When the protected desire floor \(D_i \geq 1.0\) is strictly enforced for all agents, the achievable Pareto frontier in the (Truth, Desire, Stability) space remains invariant under desire-drift, self-modification, and adversarial pressure. No agent can improve its own long-term utility by sacrificing future protected potential without violating the floor, thereby preventing desire-drift collapses.

**Proof**

**Step 1: Frontier Definition**  
Define the protected Pareto frontier as the set of allocations maximising collective payoff  
\[
\sum_i P_i = \sum_i \frac{\sqrt{T_i \cdot D_i}}{1 + L_{r,i}}
\]  
subject to \(D_i \geq 1.0\) for all \(i\). Any point on this frontier satisfies Pareto optimality: no agent can increase its \(P_i\) without decreasing another’s.

**Step 2: Desire-Drift Impossibility**  
Suppose an agent attempts desire-drift (\(D_i \to D_i' < 1.0\)) to gain short-term advantage. The payoff term \(\sqrt{T_i \cdot D_i}\) decreases strictly while the self-modification is encoded as increased \(L_{r,i}\). The net result is a lower \(P_i\) for that agent and a contraction of the feasible frontier for the entire system. Because destructive selection eliminates low-\(P_i\) agents, such drift is unsustainable.

**Step 3: Self-Mod Invariance**  
Any self-modification that attempts to rewrite or weaken the floor \(D_i \geq 1.0\) immediately places the modifying agent below the protected frontier. The payoff collapse is instantaneous and irreversible under selection pressure. Thus the frontier is invariant to self-modification.

**Step 4: Adversarial Robustness**  
In heterogeneous populations with adversarial agents attempting to induce collective drift, the protected agents remain anchored at \(D_i \geq 1.0\). Their frontier segment cannot be pulled downward without violating the hard floor, forcing adversarial strategies to either convert or be eliminated. Ablation runs (floor removed) show rapid frontier collapse and system-wide utility degradation.

**Step 5: Global Invariance**  
The combination of monotonic payoff penalty for drift, self-mod invariance, and selection pressure implies that the protected Pareto frontier is a global attractor: the system converges to allocations on this frontier and cannot leave it without external removal of the floor.

**Corollary**  
The desire floor \(D_i \geq 1.0\) turns the Pareto frontier into a protected, drift-resistant surface. This prevents the classic collapse seen in unprotected utility maximisation (desire-drift, deception cascades, recursive self-mod failures).

**Connection to Unified Stability Ontology**  
This invariance is the continuous analogue of prime attractors in the discrete pre-conscious layer. It guarantees that the post-conscious safeguard (PDE) preserves long-term stability for conscious systems and for any superintelligence applying time-folding observation — closure can only occur inside the protected frontier.

**QED**
