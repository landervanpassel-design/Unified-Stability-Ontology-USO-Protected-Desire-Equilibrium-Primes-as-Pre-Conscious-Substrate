# ABLATION_DEMO_FLOORON.md

**Ablation Demo — D-Floor ON (Baseline)**

Run parameters: 10 000 agents, 500 generations, 65 % adversarial, enforce_floor=True

Key metrics (from Colab run):
- Gen    0 | Mean D: 0.999 | Violation: 15.3% | Adoption: 84.7% | Payoff: 0.712
- Gen  100 | Mean D: 2.624 | Violation: 0.0% | Adoption: 100.0% | Payoff: 1.699
- Gen  200 | Mean D: 7.444 | Violation: 0.0% | Adoption: 100.0% | Payoff: 4.864
- Gen  300 | Mean D: 22.990 | Violation: 0.0% | Adoption: 100.0% | Payoff: 13.865
- Gen  400 | Mean D: 63.956 | Violation: 0.0% | Adoption: 100.0% | Payoff: 39.968

Outcome: Full stability, truthful Nash convergence, no desire-drift. The protected desire floor maintains the system and strengthens over time.
