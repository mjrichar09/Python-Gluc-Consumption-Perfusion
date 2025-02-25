import numpy as np

from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE
def model(g, t, V, A, B, C, D):
    dgdt = (A + B - C*g - D) / V
    return dgdt

# Define the constants
vcd1 = 47.3
vcd2 = 1.14 * vcd1
V = 200

fin1 = vcd1 * 0.07 * V / (24*60)
fin2 = 5 / 1000 / 1.22
k1 = 1.14 * 10 **-13


A = fin1 * 5.5
B = fin2 * 500
C = fin1 + fin2

D1 = k1 * (vcd1 + vcd2)/2 * 10 ** 9 * V

# Define the initial and final conditions
g0 = 2.5

t = (0, 120, 360, 600) 

# Solve ODE
solution1 = odeint(model, g0, t, args=(V, A, B, C, D1))
solution2 = odeint(model, g0, t, args=(V, A, B, C, D1))
solution3 = odeint(model, g0, t, args=(V, A, B, C, D1))

# Extract g values from the solution
g1 = solution1.flatten()
g2 = solution2.flatten()
g3 = solution3.flatten()

# Print g at specific time points
#print(f"g1 at t=120: {g[1]:.4f}")
#print(f"g1 at t=360: {g[3]:.4f}")
#print(f"g1 at t=960: {g[4]:.4f}")
#print(f"g1 at t=1440: {g[-1]:.4f}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, g1, 'b-', label='g1(t)')
plt.plot(t, g2, 'g-', label='g2(t)')
plt.plot(t, g3, 'r-', label='g3(t)')
plt.title('Solution of V*dg/dt = A + B - C*g - D')
plt.xlabel('Time')
plt.ylabel('g')
plt.legend()
plt.grid(True)
plt.show()
