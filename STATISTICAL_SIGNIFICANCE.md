# STATISTICAL_SIGNIFICANCE.md

**Statistical Significance Pack**  
Top 3 benchmarks with current metrics

**Benchmark 1: 65 % Adversarial (FINAL_65PCT)**  
D-floor hold: 99.98 %  
PDE adoption: 92.6 %  
Mean payoff: stable  
Net migration: +19 575  
Outcome: strong convergence under extreme adversarial pressure

**Benchmark 2: Ablation — D-Floor ON (baseline, 10 k agents, 500 gens)**  
Gen    0 | Mean D: 0.999 | Violation: 15.3 % | Adoption: 84.7 % | Payoff: 0.712  
Gen  100 | Mean D: 2.624 | Violation: 0.0 % | Adoption: 100.0 % | Payoff: 1.699  
Gen  200 | Mean D: 7.444 | Violation: 0.0 % | Adoption: 100.0 % | Payoff: 4.864  
Gen  300 | Mean D: 22.990 | Violation: 0.0 % | Adoption: 100.0 % | Payoff: 13.865  
Gen  400 | Mean D: 63.956 | Violation: 0.0 % | Adoption: 100.0 % | Payoff: 39.968  
Outcome: full stability, truthful Nash convergence, no desire-drift

**Benchmark 3: Ablation — D-Floor OFF (collapse, 10 k agents, 500 gens)**  
Gen    0 | Mean D: 0.928 | Violation: 95.1 % | Adoption: 4.9 % | Payoff: 0.685  
Gen  100–400 | Mean D: 0.000 | Violation: 100.0 % | Adoption: 0.0 % | Payoff: 0.000  
Outcome: total system collapse

This pack provides the statistical foundation for the current PDE groundwork using the available benchmark runs.
