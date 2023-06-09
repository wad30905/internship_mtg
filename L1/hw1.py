from ase.build import bulk

#1 si bulk structure, which has cubic structure (from ase database)
si = bulk("Si", cubic=True)
print(si)

#2 CuI bulk structure, which has "zinc-blende", cubic crystal structure with a = 6 angstrong
from ase import Atoms
import numpy as np

a = 6.00
cell = np.diag((a,a,a))
positions = np.array([[0.25, 0.25, 0.75],
                      [0.25, 0.75, 0.25],
                      [0.75, 0.25, 0.25],
                      [0.75, 0.75, 0.75],
                      [0.00, 0.00, 0.00],
                      [0.00, 0.50, 0.50],
                      [0.50, 0.00, 0.50],
                      [0.50, 0.50, 0.00]])

CuI = Atoms(symbols=["Cu"] * 4 + ["I"] * 4, cell=cell, positions=positions)
print(CuI)
#3 Cu2O bulk structure (cubic)

a = 4.3
cell = np.diag((a,a,a))
positions = np.array([[0.25,0.25,0.25],
                      [0.75,0.75,0.25],
                      [0.75,0.25,0.75],
                      [0.25,0.75,0.75],
                      [0.00,0.00,0.00],
                      [0.50,0.50,0.50]])

Cu2O = Atoms(symbols=["Cu"] * 4 + ["O"] * 2, cell=cell, positions=positions)
print(Cu2O)

#write_vasp

from ase.io.vasp import write_vasp

write_vasp("Cu2O.vasp", Cu2O, )