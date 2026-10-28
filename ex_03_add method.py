# Assignment 2.3: DFT under Simulation.model_method

# Assignment 2.3

# Instantiate a DFT method and append it to Simulation.model_method. Use DFT.xc
# (XCFunctional) to represent XC identity in the current schema.

from nomad_simulations.schema_packages.general import Simulation
from nomad_simulations.schema_packages.model_method import DFT, XCFunctional

simulation = Simulation()
dft = DFT(name='DFT', type='KS', xc=XCFunctional(functional_key='PBE'))
simulation.model_method.append(dft)

assert isinstance(simulation.model_method[0], DFT)
assert simulation.model_method[0].xc.functional_key == 'PBE'
