import pulp

# Create a linear programming problem
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Define decision variables
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Define objective function: maximize total production
model += lemonade + fruit_juice, "Total_Production"

# Add resource constraints
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solve the problem
model.solve()

# Print the results
print("Status:", pulp.LpStatus[model.status])
print("Lemonade Production:", pulp.value(lemonade))
print("Fruit Juice Production:", pulp.value(fruit_juice))
print("Total Production:", pulp.value(model.objective))