# emt calculator
from ase.calculators.calculator import Calculator
from ase import Atoms
from ase.build import bulk

a = 3.6  # Define the lattice constant 'a' for cubic cell

# Create the bulk copper structure with cubic unit cell
model = bulk("Cu", cubic=True, a=a)
print(model)
