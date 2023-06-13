import numpy as np
import matplotlib.pyplot as plt


volumes = np.array([19.2, 19.9, 20.5, 21.2, 21.9, 22.5, 23.2, 23.9, 24.7, 25.41, 26.17, 26.93, 27.72, 28.52, 29.33])
print(len(volumes))
energies = np.array([
  -6.8, 
  -7.01, 
  -7.15,
  -7.28,
  -7.36,
  -7.41,
  -7.45,
  -7.46,
  -7.45,
  -7.43,
  -7.4,
  -7.32,
  -7.26,
  -7.19,
  -7.11
])

print(len(energies))

volumes /= 2
energies /=2

from ase.eos import EquationOfState as EOS

eos = EOS(volumes, energies, "birchmurnaghan")
eos.fit()
eos.plot()
plt.show()