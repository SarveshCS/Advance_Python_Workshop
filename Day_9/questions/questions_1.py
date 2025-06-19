import matplotlib.pyplot as plt
import numpy as np

u = float(input("What is the initial velocity (u) in m/s? "))
a = float(input("What is the acceleration (a) in m/s²? "))
t_max = float(input("How many seconds should we plot? "))

time_points = np.linspace(0, t_max, 100)

velocity = []
for time in time_points:
    v = u + a * time
    velocity.append(v)

displacement_method1 = []
for time in time_points:
    s = u * time + 0.5 * a * time**2
    displacement_method1.append(s)

displacement_method2 = []
for i, time in enumerate(time_points):
    v = velocity[i]
    if a != 0:
        s = (v**2 - u**2) / (2 * a)
    else:
        s = 0
    displacement_method2.append(s)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(time_points, velocity, 'blue', linewidth=2, label=f'v = {u} + {a}t')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(time_points, displacement_method1, 'red', linewidth=2, label=f's = {u}t + 0.5×{a}t²')
plt.xlabel('Time (seconds)')
plt.ylabel('Displacement (meters)')
plt.title('Displacement vs Time (Method 1)')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(time_points, displacement_method2, 'green', linewidth=2, label=f's = (v²-u²)/(2×{a})')
plt.xlabel('Time (seconds)')
plt.ylabel('Displacement (meters)')
plt.title('Displacement vs Time (Method 2)')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

middle_time = t_max / 2
velocity_at_middle = u + a * middle_time
displacement_method1_sample = u * middle_time + 0.5 * a * middle_time**2

print(f"At t = {middle_time:.1f}s:")
print(f"Velocity = {velocity_at_middle:.2f} m/s")
print(f"Displacement (Method 1) = {displacement_method1_sample:.2f} m")

if a != 0:
    displacement_method2_sample = (velocity_at_middle**2 - u**2) / (2 * a)
    print(f"Displacement (Method 2) = {displacement_method2_sample:.2f} m")
