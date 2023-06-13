from ase.build import bulk

Si = bulk("Si")


from ase.io.vasp import write_vasp
write_vasp("Si.vasp", Si, direct=True, vasp5=True)