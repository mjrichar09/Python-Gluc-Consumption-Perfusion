import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar

# Define the ODE
def model(t, g, V, A, B, C, D):
    return (A + B - C*g - D) / V

# Function to solve the ODE and return the final g value
def solve_ode(D, V, A, B, C, g0, t_span):
    sol = solve_ivp(model, t_span, [g0], args=(V, A, B, C, D), dense_output=True)
    return sol.sol(t_span[1])[0]

# Function to find the root (difference between calculated and target g_final)
def objective(D, V, A, B, C, g0, g_final, t_span):
    return solve_ode(D, V, A, B, C, g0, t_span) - g_final

# Set known parameters
# Define the constants


V = 9.9
vcd1 = 6.617
vcd2 = 11.74
fin1 = vcd1 * 0.05 * V / (24*60)
A = fin1 * 4.6
B = 0
C = fin1


# Define the initial and final conditions
g0 = 4.19
g_final = 3.17
t = 1227  # time in minutes


t_span = (0, 1227)

# Find D using root-finding method
result = root_scalar(objective, args=(V, A, B, C, g0, g_final, t_span), 
                     method='brentq', bracket=[0, 10])  # Adjust bracket if needed

D = result.root

print(f"The value of D that satisfies the conditions is: {D:.6f}")

# Verify the solution
sol = solve_ivp(model, t_span, [g0], args=(V, A, B, C, D), dense_output=True)
g_calculated = sol.sol(t_span[1])[0]

print(f"g(0) = {g0:.6f}")
print(f"g(1440) calculated = {g_calculated:.6f}")
print(f"g(1440) target = {g_final:.6f}")

k = D * 2 / (vcd1 + vcd2) / 10 ** 9 / 9.9

k
