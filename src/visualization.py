# Handles state representation and plotting utilities.
from qiskit.visualization import array_to_latex, plot_histogram

def display_state_latex(state):
    """Renders statevector or operator in LaTeX."""
    return state.draw("latex")

def generate_measurement_plot(state, shots=4000):
    """Generates a histogram plot for state sampling."""
    statistics = state.sample_counts(shots)
    return plot_histogram(statistics)