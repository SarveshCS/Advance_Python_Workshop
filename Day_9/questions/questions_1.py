"""
Take the initial velocity and accelerations, and plot the following relations
v = u + at
s = u*t + (1/2 * (a*t) ** 2)
s = (v**2 - u**2)/(2*a)
"""

import matplotlib.pyplot as plt
import numpy as np


u = float(input("Enter initial velocity (u) in m/s: "))
a = float(input("Enter acceleration (a) in m/s²: "))
t_max = float(input("Enter maximum time for plotting (seconds): "))

t = np.linspace(0, t_max, 100)

v = u + a * t
s1 = u * t + 0.5 * a * t**2
s2 = np.where(a != 0, (v**2 - u**2) / (2 * a), 0)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(t, v, 'b-', linewidth=2, label=f'v = {u} + {a}t')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time\nv = u + at')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(t, s1, 'r-', linewidth=2, label=f's = {u}t + 0.5×{a}t²')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Displacement vs Time\ns = ut + ½at²')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(t, s2, 'g-', linewidth=2, label=f's = (v²-u²)/(2×{a})')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Displacement vs Time\ns = (v²-u²)/(2a)')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

print(f"\nSample calculations at t = {t_max/2:.1f}s:")
print(f"Velocity: v = {u} + {a}×{t_max/2:.1f} = {u + a*(t_max/2):.2f} m/s")
print(f"Displacement (method 1): s = {u}×{t_max/2:.1f} + 0.5×{a}×{t_max/2:.1f}² = {u*(t_max/2) + 0.5*a*(t_max/2)**2:.2f} m")
if a != 0:
    v_at_half = u + a*(t_max/2)
    s_method2 = (v_at_half**2 - u**2) / (2*a)
    print(f"Displacement (method 2): s = ({v_at_half:.2f}²-{u}²)/(2×{a}) = {s_method2:.2f} m")
