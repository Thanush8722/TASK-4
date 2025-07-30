from pulp import *

print("Running optimization model...")  # Just to check if the file runs

# Step 1: Define the problem (Maximization)
model = LpProblem("Maximize_Profit", LpMaximize)

# Step 2: Define decision variables
chairs = LpVariable("Chairs", lowBound=0, cat='Integer')
tables = LpVariable("Tables", lowBound=0, cat='Integer')

# Step 3: Define the objective function
model += 50 * chairs + 60 * tables, "Total_Profit"

# Step 4: Add constraints
model += 2 * chairs + 3 * tables <= 100, "Wood_Constraint"
model += 3 * chairs + 2 * tables <= 120, "Labor_Constraint"

# Step 5: Solve the problem
model.solve()

# Step 6: Display the results
print("Status:", LpStatus[model.status])
print("Chairs to produce:", chairs.varValue)
print("Tables to produce:", tables.varValue)
print("Maximum Profit: ₹", value(model.objective))