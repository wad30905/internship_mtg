from ase.calculators.calculator import Calculator
from ase import Atoms
from ase import Atom

import numpy as np
print("method 1.")

a = 1.805
model = Atoms(cell=np.diag((a,a,a)), symbols=["Cu"]*4, positions=[(0,0,0), (0,a,a,), (a,0,a), (a,a,0)])
print(model)

#method 2.
print("- "* 20)
print("method 2.")
cell = np.diag((a,a,a))
model1 = Atoms()
model1.cell = cell
Cu1 = Atom("Cu", position=(0,0,0))
Cu2 = Atom("Cu", position=(0,a,a))
Cu3 = Atom("Cu", position=(a,0,a))
Cu4 = Atom("Cu", position=(a,a,0))
for i in [Cu1, Cu2, Cu3, Cu4]: 
  model1.append(i)

print(model1)

#method 3. using build module, ase db 를 사용
print("- "* 20)
print("method 3.")

from ase.build import bulk

a = 3.6  # Define the lattice constant 'a' for cubic cell

# Create the bulk copper structure with cubic unit cell
model = bulk("Cu", cubic=True, a=a)
print(model)