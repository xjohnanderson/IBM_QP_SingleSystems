 
# Handles quantum state evolution and circuit operations.
 
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator

def get_evolution_circuit():
    """Defines the quantum circuit sequence."""
    circuit = QuantumCircuit(1)
    circuit.h(0)
    circuit.t(0)
    circuit.h(0)
    circuit.s(0)
    circuit.y(0)
    return circuit

def evolve_state(initial_state, circuit):
    """Evolves a statevector through a given circuit."""
    return initial_state.evolve(circuit)

def get_circuit_operator(circuit):
    """Extracts the unitary operator from a circuit."""
    return Operator.from_circuit(circuit)