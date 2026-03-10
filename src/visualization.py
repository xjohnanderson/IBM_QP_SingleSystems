"""
Handles state representation and plotting utilities.
"""
import sys
from qiskit.visualization import plot_histogram

def get_state_representation(state):
    """Returns ASCII representation for terminal, LaTeX for Jupyter."""
    if 'ipykernel' in sys.modules:
        return state.draw("latex")
    return state.draw("text")

def generate_measurement_plot(state, shots=4000, filename="histogram.png"):
    """Saves histogram to disk for terminal inspection."""
    statistics = state.sample_counts(shots)
    print(f"Measurement Counts: {statistics}")
    
    # Generate and save plot
    fig = plot_histogram(statistics)
    fig.savefig(filename)
    print(f"Histogram visualization saved to {filename}")