# RANDOM_SEED_STANDARDIZATION.md

**Random-Seed Standardization Across All New Sims**  
np.random.seed(42) + logging for full reproducibility

**Standard Rule for Every New Simulation Script**

Add the following block at the very start of every new .py file (right after imports):

```python
import numpy as np

# === RANDOM SEED STANDARDIZATION ===
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
print(f"[REPRODUCIBILITY] Random seed fixed to {RANDOM_SEED} for this run")
