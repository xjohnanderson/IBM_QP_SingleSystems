# Quantum State Evolution Simulation

A modularized project designed to simulate quantum circuit evolution using Qiskit, the open-source quantum computing software development framework maintained by IBM. This implementation focuses on clean separation of concerns between quantum logic, visualization, and execution.

## Features
* **Circuit Modeling**: Encapsulates quantum gate sequences into reusable components.
* **State Evolution**: Provides clear logic for evolving `Statevector` objects through quantum operators.
* **Visualization**: Streamlined utilities for LaTeX rendering and measurement statistics.

## Project Structure
```text
quantum_project/
├── main.py             # Entry point
├── requirements.txt    # Dependency list
└── src/                # Core logic
    ├── __init__.py
    ├── quantum_ops.py  # Gate and evolution logic
    └── visualization.py # Display utilities
