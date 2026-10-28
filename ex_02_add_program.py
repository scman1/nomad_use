# Assignment 2.2: Program typing and composition

# Assignment 2.2

# Create a Program(name='VASP', version='5.0.0'), attach it to Simulation.program,
# then assign an integer to version and inspect the stored result.

from nomad_simulations.schema_packages.general import Program, Simulation

simulation = Simulation()
program = Program(name='VASP', version='5.0.0')
simulation.program = program

assert simulation.program.name == 'VASP'
assert simulation.program.version == '5.0.0'

# Compatible scalar inputs are auto-converted to string when possible.
program.version = 5
assert program.version == '5'
