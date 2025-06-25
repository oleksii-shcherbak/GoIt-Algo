import pulp

# Create the problem variable to maximize
prob = pulp.LpProblem("Beverage Production", pulp.LpMaximize)

# Define the decision variables
# x1 = number of units of Lemonade to produce
# x2 = number of units of Fruit Juice to produce
x1 = pulp.LpVariable("Lemonade", 0, None, pulp.LpInteger)
x2 = pulp.LpVariable("Fruit_Juice", 0, None, pulp.LpInteger)

# Objective function: Maximize total production
prob += x1 + x2, "Total Products"

# Constraints
# Water constraint
prob += (2 * x1) + (1 * x2) <= 100, "Water_Constraint"
# Sugar constraint
prob += (1 * x1) <= 50, "Sugar_Constraint"
# Lemon Juice constraint
prob += (1 * x1) <= 30, "Lemon_Juice_Constraint"
# Fruit Puree constraint
prob += (2 * x2) <= 40, "Fruit_Puree_Constraint"

# Solve the problem
prob.solve()

# Print the results
print("Production Optimization Results:")
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Lemonade to produce: {x1.varValue} units")
print(f"Fruit Juice to produce: {x2.varValue} units")

print("\nResource Usage:")
print(f"Water used: {2 * x1.varValue + 1 * x2.varValue} units (Max 100)")
print(f"Sugar used: {1 * x1.varValue} units (Max 50)")
print(f"Lemon Juice used: {1 * x1.varValue} units (Max 30)")
print(f"Fruit Puree used: {2 * x2.varValue} units (Max 40)")
