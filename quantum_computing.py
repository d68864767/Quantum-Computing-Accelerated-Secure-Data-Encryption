```python
# Import necessary libraries
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
from qiskit.providers.aer import QasmSimulator
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor

# Load IBM Q account
IBMQ.load_account()

# Define a function to create a quantum circuit
def create_quantum_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits)
    return qc

# Define a function to add quantum gates
def add_quantum_gates(qc, gate_type, qubit):
    if gate_type == 'h':
        qc.h(qubit)
    elif gate_type == 'x':
        qc.x(qubit)
    elif gate_type == 'y':
        qc.y(qubit)
    elif gate_type == 'z':
        qc.z(qubit)
    return qc

# Define a function to simulate the quantum circuit
def simulate_quantum_circuit(qc):
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    return counts

# Define a function to run the quantum circuit on real quantum computer
def run_quantum_circuit(qc):
    provider = IBMQ.get_provider('ibm-q')
    qcomp = provider.get_backend('ibmq_16_melbourne')
    job = execute(qc, backend=qcomp)
    job_monitor(job)
    result = job.result()
    return result.get_counts(qc)
```
