from ase.build import bulk

cu_bct = bulk("Cu", crystalstructure="bct", a=1.8, c=3.6)

from ase.io.vasp import write_vasp

write_vasp("POSCAR", cu_bct, direct=True)