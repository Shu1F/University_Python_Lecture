import random


def simulate_secretary_problem(n, trials):
    """
    Simulate the secretary problem using Monte Carlo method.

    Parameters:
    - n: int, number of candidates
    - trials: int, number of simulation trials

    Returns:
    - k_best: int, optimal value of k
    - probabilities: dict, success probabilities for each k
    """
    success_counts = [0] * n  # Success count for each k

    for _ in range(trials):
        # Generate random rankings for candidates
        candidates = list(range(1, n + 1))
        random.shuffle(candidates)

        for k in range(1, n + 1):
            # First k-1 candidates are ignored
            best_so_far = max(candidates[: k - 1]) if k > 1 else float("-inf")
            chosen = None

            # Select the first candidate better than the best_so_far
            for i in range(k - 1, n):
                if candidates[i] > best_so_far:
                    chosen = candidates[i]
                    break

            # Check if the chosen candidate is the best overall
            if chosen == max(candidates):
                success_counts[k - 1] += 1

    # Calculate success probabilities
    probabilities = {k: success_counts[k - 1] / trials for k in range(1, n + 1)}

    # Find the k with the highest probability
    k_best = max(probabilities, key=probabilities.get)

    return k_best, probabilities


# Parameters
n = 30  # Number of candidates
trials = 10000  # Number of simulation trials

# Run the simulation
k_best, probabilities = simulate_secretary_problem(n, trials)

# Display the results
print(f"Optimal k for n={n}: {k_best}")
print("Success probabilities for each k:")
for k, prob in probabilities.items():
    print(f"k={k}: {prob:.4f}")
