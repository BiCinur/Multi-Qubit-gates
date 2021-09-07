mport numpy as np
from pyquil import Program, get_qc
from pyquil.api import WavefunctionSimulator
from pyquil.gates import*
wavefunction_simulator = WavefunctionSimulator()
qc = get_qc('9q-generic-qvm')


# Multiple qubits also produce the expected scaling of the state.
p = Program(I(0), I(1))
wavefunction = wavefunction_simulator.wavefunction(p)
print("The quantum state is of dimension:", len(wavefunction.amplitudes))

p = Program(I(0), I(1), I(2), I(3))
wavefunction = wavefunction_simulator.wavefunction(p)
print("The quantum state is of dimension:", len(wavefunction.amplitudes))

p = Program()
for x in range(10):
    p += I(x)
wavefunction = wavefunction_simulator.wavefunction(p)
print("The quantum state is of dimension:", len(wavefunction.amplitudes))



p = Program(I(0), I(1))
results = qc.run_and_measure(p, trials=10)

print(results)




p = Program()
# Declare two bits of classical memory
classical_memory = p.declare('ro', 'BIT', 2)

p.inst(H(0))
p.inst(X(1))

# Measure out on qubit 0 and record the results in the 0th index of classical_memory
p.inst(MEASURE(0, classical_memory[0]))
# Measure out on qubit 1 and record the results in the 1st index of classical_memory
p.inst(MEASURE(1, classical_memory[1]))

# Print out the Quil code for this Program
print(p)

# Measure the qubits specified by classical_register (qubits 0 and 1) a number of times
p.wrap_in_numshots_loop(shots=10)
# Compile and run the Program
results = qc.run(qc.compile(p))

print(results)




p = Program(CNOT(0, 1))
wavefunction = wavefunction_simulator.wavefunction(p)
print("CNOT|00> = ", wavefunction)
print("With outcome probabilities\n", wavefunction.get_outcome_probs(), "\n")

p = Program(X(0), CNOT(0, 1))
wavefunction = wavefunction_simulator.wavefunction(p)
print("CNOT|01> = ", wavefunction)
print("With outcome probabilities\n", wavefunction.get_outcome_probs(), "\n")

p = Program(X(1), CNOT(0, 1))
wavefunction = wavefunction_simulator.wavefunction(p)
print("CNOT|10> = ", wavefunction)
print("With outcome probabilities\n", wavefunction.get_outcome_probs(), "\n")

p = Program(X(0), X(1), CNOT(0, 1))
wavefunction = wavefunction_simulator.wavefunction(p)
print("CNOT|11> = ", wavefunction)
print("With outcome probabilities\n", wavefunction.get_outcome_probs(), "\n")



















