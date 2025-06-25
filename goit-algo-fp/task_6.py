def greedy_algorithm(amount, items):
    """
    Selects food items using a greedy algorithm that maximizes the
    calories-to-cost ratio without exceeding the given budget.

    Parameters:
        amount (int): The budget available.
        items (dict): Dictionary of items with their cost and calories.

    Returns:
        tuple: Total cost, total calories, and a list of selected items.
    """
    # Convert items to list of tuples and compute calories-to-cost ratio
    item_list = [
        (name, item['cost'], item['calories'], item['calories'] / item['cost'])
        for name, item in items.items()
    ]
    # Sort by highest calories-to-cost ratio
    item_list.sort(key=lambda x: x[3], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, cost, calories, _ in item_list:
        if total_cost + cost <= amount:
            total_cost += cost
            total_calories += calories
            selected_items.append({'name': name, 'cost': cost, 'calories': calories})

    return total_cost, total_calories, selected_items


def dynamic_programming(amount, items):
    """
    Solves the calorie maximization problem using dynamic programming.

    Parameters:
        amount (int): The budget available.
        items (dict): Dictionary of items with their cost and calories.

    Returns:
        tuple: Total cost (used), total calories, and list of selected items.
    """
    item_list = [(name, item['cost'], item['calories']) for name, item in items.items()]

    # dp[i] = max calories achievable with budget i
    dp = [0] * (amount + 1)
    # selection[i] stores the list of items chosen for budget i
    selection = [[] for _ in range(amount + 1)]

    for name, cost, calories in item_list:
        for budget in range(amount, cost - 1, -1):
            new_calories = dp[budget - cost] + calories
            if new_calories > dp[budget]:
                dp[budget] = new_calories
                selection[budget] = selection[budget - cost] + [{'name': name, 'cost': cost, 'calories': calories}]

    max_calories = max(dp)
    best_budget = dp.index(max_calories)
    selected_items = selection[best_budget]

    return best_budget, max_calories, selected_items


def main():
    """
    Main function to run the greedy and dynamic programming approaches.
    Prints the results of both algorithms.
    """
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # Define the budget amount
    amount = 70

    print("\nGreedy Algorithm")
    total_cost, total_calories, selection_greedy = greedy_algorithm(amount, items)
    print(f"Total cost: {total_cost}, Total calories: {total_calories}")
    print("Selected items:")
    for item in selection_greedy:
        print(f" - {item['name']} (cost: {item['cost']}, calories: {item['calories']})")

    print("\nDynamic Programming")
    total_cost, total_calories, selection_dp = dynamic_programming(amount, items)
    print(f"Total cost: {total_cost}, Total calories: {total_calories}")
    print("Selected items:")
    for item in selection_dp:
        print(f" - {item['name']} (cost: {item['cost']}, calories: {item['calories']})")


if __name__ == "__main__":
    main()
