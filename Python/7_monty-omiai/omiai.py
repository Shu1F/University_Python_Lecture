import numpy as np
import matplotlib.pyplot as plt


def secretary_problem_simulation(n, simulations=10000):
    best_k = 1
    max_success_rate = 0

    for k in range(1, n + 1):
        success_count = 0

        for _ in range(simulations):
            candidates = np.random.permutation(n)
            best_seen = -1

            for i in range(k - 1):
                best_seen = max(best_seen, candidates[i])

            for i in range(k - 1, n):
                if candidates[i] > best_seen:
                    if candidates[i] == n - 1:
                        success_count += 1
                    break

        success_rate = success_count / simulations

        if success_rate > max_success_rate:
            max_success_rate = success_rate
            best_k = k

    return best_k, max_success_rate


def find_optimal_k_for_range(n_max, simulations=10000):
    optimal_ks = []
    success_probs = []

    for n in range(1, n_max + 1):
        k, success_rate = secretary_problem_simulation(n, simulations)
        optimal_ks.append(k)
        success_probs.append(success_rate)

    return optimal_ks, success_probs


n_max = 30
simulations = 10000
optimal_ks, success_probs = find_optimal_k_for_range(n_max, simulations)

for n in range(1, n_max + 1):
    print(
        f"n = {n}, Optimal k = {optimal_ks[n-1]}, Success Probability = {success_probs[n-1]:.4f}"
    )

plt.figure(figsize=(10, 6))
plt.plot(range(1, n_max + 1), optimal_ks, marker="o", label="Optimal k")
plt.title("Optimal k vs. Number of Candidates (n)")
plt.xlabel("Number of Candidates (n)")
plt.ylabel("Optimal k")
plt.xticks(range(1, n_max + 1))
plt.grid()
plt.legend()
plt.show()
