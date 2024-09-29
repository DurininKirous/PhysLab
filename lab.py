import matplotlib.pyplot as plt
import numpy as np

voltage_values = np.array([0.06, 0.13, 0.32, 0.72, 0.9, 1.18, 1.64, 1.97, 2.38, 3.05])
t = np.array([100, 200, 300, 400, 450, 500, 550, 600, 650, 700])

T = t + 273.15

power_values = voltage_values * 1e-3

sigma_values = power_values / (7.854 * T**4)

table_data = []
for i in range(len(power_values)):
    table_data.append([f'{t[i]:.0f}', f'{T[i]:.2f}', f'{power_values[i]:.6f}', f'{voltage_values[i]:.2f}', f'{sigma_values[i]:.2e}'])

fig1, ax1 = plt.subplots(figsize=(8, 6))
fig2, ax2 = plt.subplots(figsize=(8, 6))

ax1.bar(power_values, voltage_values, width=0.00067)
ax1.set_xlabel('Power (W)')
ax1.set_ylabel('Voltage (V)')
ax1.set_title('Dependence of Voltage on Power for a Thermocouple')
ax1.grid(True)

ax2.axis('off')
ax2.table(cellText=table_data, loc='center', colLabels=['t (°C)', 'T (K)', 'Power (W)', 'Voltage (V)', 'Sigma (W/m^2K^4)'],
          fontsize=24, cellLoc='center', bbox=[0, 0, 1, 1])

plt.figure(fig1.number)
plt.tight_layout()
plt.show()

plt.figure(fig2.number)
plt.tight_layout()
plt.show()
