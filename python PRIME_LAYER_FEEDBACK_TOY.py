# PRIME_LAYER_FEEDBACK_TOY.py

**Toy Prime-Layer Feedback Simulation**  
Destructive sieving + simple observation pressure on gap statistics  
Ontology bridge (pre-conscious primes + observer feedback)

```python
import numpy as np

# === RANDOM SEED STANDARDIZATION ===
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
print(f"[REPRODUCIBILITY] Random seed fixed to {RANDOM_SEED} for this run\n")

def prime_layer_toy(n=100000, observation_steps=8):
    print("=== Toy Prime-Layer Feedback Simulation ===")
    print(f"Generating primes up to {n} (destructive sieving phase)\n")
    
    # Step 1: Destructive sieving (classic sieve of Eratosthenes)
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0:2] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*i::i] = False
    primes = np.nonzero(is_prime)[0]
    
    print(f"Initial primes found: {len(primes)}")
    
    # Step 2: Compute initial gaps (distributional layer)
    gaps = np.diff(primes)
    print(f"Initial gap statistics: mean={gaps.mean():.2f}, max={gaps.max()}")
    
    # Step 3: Apply observation pressure (destructive feedback on gaps)
    current_gaps = gaps.copy()
    for step in range(observation_steps):
        threshold = np.percentile(current_gaps, 92)
        current_gaps = current_gaps[current_gaps < threshold]
        print(f"Step {step+1:2d} (observation pressure) → gaps remaining: {len(current_gaps)} | mean={current_gaps.mean():.2f}")
    
    print("\nSimulation complete.")
    print("Primes themselves are unchanged and observer-independent.")
    print("Only the gap distribution (statistical attractor) was re-ordered by observation pressure.")
    print("This mirrors partial RH approaches touching different slices of the same universal prime layer.")

if __name__ == "__main__":
    prime_layer_toy()
