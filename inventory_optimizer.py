import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def calculate_eoq(demand_annual, order_cost, holding_cost_per_unit):
  """Calculate the Economic Order Quantity (EOQ)."""
  eoq = np.sqrt((2 * demand_annual * order_cost) / holding_cost_per_unit)
  return round(eoq, 2)


def simulate_inventory(
    days=90, daily_demand_mean=20, daily_demand_std=5, reorder_point=100
):
  """Simulate daily warehouse inventory levels and stock replenishments."""
  np.random.seed(42)  # Set seed for reproducible results
  days_list = list(range(1, days + 1))
  demand = np.random.normal(
      daily_demand_mean, daily_demand_std, days
  ).astype(int)
  demand = np.clip(demand, 5, 40)  # Avoid negative demand values

  inventory = 200
  inventory_levels = []
  orders_placed = []

  for d in demand:
    inventory -= d
    is_order = 0
    # If inventory drops below the reorder point, place a replenishment order
    if inventory <= reorder_point:
      inventory += 150  # Replenishment batch size
      is_order = 1

    inventory_levels.append(max(0, inventory))
    orders_placed.append(is_order)

  df = pd.DataFrame({
      "Day": days_list,
      "Demand": demand,
      "Inventory_Level": inventory_levels,
      "Order_Placed": orders_placed,
  })
  return df


if __name__ == "__main__":
  # Test parameters
  D = 5000  # Annual demand
  S = 50  # Ordering cost per order
  H = 2  # Annual holding cost per unit

  optimal_eoq = calculate_eoq(D, S, H)
  print(f"Optimal Economic Order Quantity (EOQ): {optimal_eoq} units")

  # Run simulation
  simulation_df = simulate_inventory()
  print("\nLast 5 rows of the inventory simulation:")
  print(simulation_df.tail())
