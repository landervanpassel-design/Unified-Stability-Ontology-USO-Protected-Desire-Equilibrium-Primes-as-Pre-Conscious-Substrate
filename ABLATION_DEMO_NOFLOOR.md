# ABLATION_DEMO_NOFLOOR.md

**Ablation Demo — D-Floor OFF (Collapse)**

Run parameters: 10 000 agents, 500 generations, 65 % adversarial, enforce_floor=False

Key metrics (from Colab run):
- Gen    0 | Mean D: 0.928 | Violation: 95.1% | Adoption: 4.9% | Payoff: 0.685
- Gen  100 | Mean D: 0.000 | Violation: 100.0% | Adoption: 0.0% | Payoff: 0.000
- Gen  200 | Mean D: 0.000 | Violation: 100.0% | Adoption: 0.0% | Payoff: 0.000
- Gen  300 | Mean D: 0.000 | Violation: 100.0% | Adoption: 0.0% | Payoff: 0.000
- Gen  400 | Mean D: 0.000 | Violation: 100.0% | Adoption: 0.0% | Payoff: 0.000

Outcome: Immediate and total collapse. Without the D ≥ 1.0 hard floor, desire-drift destroys the system within the first 100 generations.

This proves the floor is necessary for stability under destructive selection.
