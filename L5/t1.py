from ase.build import bulk

si8 = bulk("Si", cubic=True)
print(si8)

from ase.io.vasp import write_vasp
write_vasp("si8.vasp", si8, direct=True, vasp5=True, )