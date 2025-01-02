import random
import matplotlib.pyplot as plt


def simulate_monty_hall(max_trials, step):
    """
    Simulate the Monty Hall problem using Monte Carlo method.

    Parameters:
    - max_trials: int, maximum number of trials
    - step: int, step size for the number of trials

    Displays:
    - A plot of winning ratios for "change" and "no-change" strategies.
    """
    nc_win_ratios = []  # No-change winning ratios
    c_win_ratios = []  # Change winning ratios
    num_trials = range(10, max_trials + 1, step)  # Trial ranges

    for trials in num_trials:
        nc_wins = 0
        c_wins = 0

        for _ in range(trials):
            if no_change_strategy() == "win":
                nc_wins += 1
            if change_strategy() == "win":
                c_wins += 1

        nc_win_ratios.append(nc_wins / trials)
        c_win_ratios.append(c_wins / trials)

    # Plot results
    plt.figure()
    plt.plot(num_trials, c_win_ratios, "b", label="Change")
    plt.plot(num_trials, nc_win_ratios, "r", label="No-Change")
    plt.title("Winning Ratio")
    plt.xlabel("Number of Trials")
    plt.ylabel("Winning Ratio")
    plt.ylim(0.0, 1.0)
    plt.legend(loc="best")
    plt.show()


def no_change_strategy():
    """Simulate the no-change strategy in the Monty Hall problem."""
    car_position = random.choice(["A", "B", "C"])
    player_choice = random.choice(["A", "B", "C"])

    if player_choice == car_position:
        return "win"
    else:
        return "lose"


def change_strategy():
    """Simulate the change strategy in the Monty Hall problem."""
    car_position = random.choice(["A", "B", "C"])
    player_choice = random.choice(["A", "B", "C"])

    # Monty opens a goat door
    remaining_doors = [
        door
        for door in ["A", "B", "C"]
        if door != player_choice and door != car_position
    ]
    monty_choice = random.choice(remaining_doors)

    # Player changes their choice
    player_second_choice = [
        door
        for door in ["A", "B", "C"]
        if door != player_choice and door != monty_choice
    ][0]

    if player_second_choice == car_position:
        return "win"
    else:
        return "lose"


# Parameters
max_trials = 1000  # Maximum number of trials
step = 50  # Step size for trials

# Run the simulation
simulate_monty_hall(max_trials, step)
