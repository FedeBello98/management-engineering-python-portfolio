import pulp


def optimize_production():
  # Initialize the optimization problem to maximize profit
  prob = pulp.LpProblem(
      "Production_Planning_Optimization", pulp.LpMaximize
  )

  # Decision variables: how many units to produce of Product A and Product B
  x1 = pulp.LpVariable("Product_A", lowBound=0, cat="Continuous")
  x2 = pulp.LpVariable("Product_B", lowBound=0, cat="Continuous")

  # Objective Function: Maximize total profit (e.g., €40 for A, €30 for B)
  prob += 40 * x1 + 30 * x2, "Total_Profit"

  # Resource constraints (e.g., machine hours available per department)
  # Constraint 1: Machine 1 hours (e.g., max 100 hours available)
  prob += 2 * x1 + 1 * x2 <= 100, "Machine_1_Constraint"

  # Constraint 2: Machine 2 hours (e.g., max 80 hours available)
  prob += 1 * x1 + 2 * x2 <= 80, "Machine_2_Constraint"

  # Solve the optimization model
  prob.solve()

  print(f"Optimization Status: {pulp.LpStatus[prob.status]}")
  print(f"Optimal quantity for Product A: {x1.varValue:.2f} units")
  print(f"Optimal quantity for Product B: {x2.varValue:.2f} units")
  print(f"Maximum Total Profit: €{pulp.value(prob.objective):.2f}")


if __name__ == "__main__":
  optimize_production()
