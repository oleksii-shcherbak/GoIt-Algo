import random
import matplotlib.pyplot as plt
import pandas as pd


def monte_carlo_dice_simulation(num_rolls: int) -> dict:
    """
    Simulates rolling two dice 'num_rolls' times and calculates
    the empirical probability of each possible sum (2 to 12).
    """
    sum_counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1

    probabilities = {
        total: count / num_rolls for total, count in sum_counts.items()
    }
    return probabilities


def analytical_probabilities() -> dict:
    """
    Returns the exact analytical probabilities for the sum of two dice.
    """
    return {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }


def plot_comparison(mc1k: dict, mc10k: dict, mc100k: dict, analytic: dict):
    """
    Plots bar charts comparing Monte Carlo results with different roll counts
    to analytical probabilities.
    """
    sums = list(range(2, 13))
    width = 0.2
    x = list(range(len(sums)))

    plt.figure(figsize=(10, 6))
    plt.bar(
        [i - 1.5 * width for i in x],
        [mc1k[s] for s in sums],
        width=width,
        label="MC 1k",
        color="#D62728",  # Red
    )
    plt.bar(
        [i - 0.5 * width for i in x],
        [mc10k[s] for s in sums],
        width=width,
        label="MC 10k",
        color="#FF7F0E",  # Orange
    )
    plt.bar(
        [i + 0.5 * width for i in x],
        [mc100k[s] for s in sums],
        width=width,
        label="MC 100k",
        color="#FFD700",  # Yellow
    )
    plt.bar(
        [i + 1.5 * width for i in x],
        [analytic[s] for s in sums],
        width=width,
        label="Analytical",
        color="#7F7F7F",  # Gray
    )

    plt.xticks(x, sums)
    plt.xlabel("Sum of Dice")
    plt.ylabel("Probability")
    plt.title("Monte Carlo vs Analytical Dice Sum Probabilities")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def display_combined_dataframe(
    mc1k: dict, mc10k: dict, mc100k: dict, analytic: dict
):
    """
    Builds and prints a single DataFrame comparing all Monte Carlo results
    with analytical probabilities.
    """
    df = pd.DataFrame({
        "Sum": list(range(2, 13)),
        "MC 1k": [mc1k.get(i, 0) for i in range(2, 13)],
        "MC 10k": [mc10k.get(i, 0) for i in range(2, 13)],
        "MC 100k": [mc100k.get(i, 0) for i in range(2, 13)],
        "Analytical": [analytic.get(i, 0) for i in range(2, 13)],
    })

    print("\nCombined Probability Table")
    print(df.to_string(index=False, float_format="%.5f"))


def main():
    """
    Main workflow:
    - Runs Monte Carlo simulations for 1k, 10k, and 100k rolls
    - Calculates analytical probabilities
    - Displays comparison DataFrame
    - Plots results
    """
    mc1k = monte_carlo_dice_simulation(1_000)
    mc10k = monte_carlo_dice_simulation(10_000)
    mc100k = monte_carlo_dice_simulation(100_000)
    analytic = analytical_probabilities()

    display_combined_dataframe(mc1k, mc10k, mc100k, analytic)
    plot_comparison(mc1k, mc10k, mc100k, analytic)


if __name__ == "__main__":
    main()
