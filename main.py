"""
Main entry point for executing quantum simulation logic.
"""
from qiskit.quantum_info import Statevector
from src.quantum_ops import get_evolution_circuit, evolve_state, get_circuit_operator
from src.visualization import get_state_representation, generate_measurement_plot

def run_simulation():
    # 1. Initialize State
    ket0 = Statevector([1, 0])
    
    # 2. Setup Circuit
    circuit = get_evolution_circuit()
    
    # 3. Operations
    final_state = evolve_state(ket0, circuit)
    circuit_op = get_circuit_operator(circuit)
    
    # 4. Outputs
    print("--- Final State Representation ---")
    print(get_state_representation(final_state))
    
    print("\n--- Circuit Operator Representation ---")
    print(get_state_representation(circuit_op))
    
    print("\n--- Measurement Histogram ---")
    generate_measurement_plot(final_state)

if __name__ == "__main__":
    run_simulation()