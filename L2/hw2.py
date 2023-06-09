import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
ENCUT_x = np.arange(300, 800, 100)
ENCUT_y = np.array([-14.85898711,-14.86286578,-14.85715426,-14.85837076,-14.85717297])/4

KPOINTS_x = np.arange(4, 20, 2)
KPOINTS_y = np.array([-14.65809773, -14.86286578, -14.91365284, -14.91418746,  -14.90976925, -14.90816546, -14.90897402, -14.90758802]) /4
print(KPOINTS_y)
# plot
plt.subplot(1,2,1)
plt.title("ENCUT convergence test")
plt.xlabel("ENCUT")
plt.ylabel("entropy")
plt.xlim(300, 700)
plt.xticks(np.arange(300, 800, 100))
plt.ylim(-3.8, -3.6)
plt.yticks(np.arange(-3.8, -3.6, 0.02))
plt.plot(ENCUT_x, ENCUT_y, marker='o')

plt.subplot(1,2,2)
plt.title("KPOINTS convergence test")
plt.xlabel("KPOINTS")
plt.ylabel("entropy")
plt.xlim(4, 18)
plt.xticks(np.arange(4, 20, 2))
plt.ylim(-3.8, -3.6)
plt.yticks(np.arange(-3.8, -3.6, 0.02))
plt.plot(KPOINTS_x, KPOINTS_y, marker='o')
plt.show()
plt.savefig("convergence_test.png")