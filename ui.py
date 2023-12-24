```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from quantum_computing import QuantumComputing
from qkd import QuantumKeyDistribution
from post_quantum_encryption import PostQuantumEncryption
from parallel_processing import ParallelProcessing
from quantum_resistant_cryptography import QuantumResistantCryptography
from key_management import KeyManagement

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quantum Computing Accelerated Secure Data Encryption")

        # Initialize all the classes
        self.qc = QuantumComputing()
        self.qkd = QuantumKeyDistribution()
        self.pqe = PostQuantumEncryption()
        self.pp = ParallelProcessing()
        self.qrc = QuantumResistantCryptography()
        self.km = KeyManagement()

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Create labels, entries, and buttons
        self.input_label = tk.Label(self.window, text="Input:")
        self.input_entry = tk.Entry(self.window)
        self.encrypt_button = tk.Button(self.window, text="Encrypt", command=self.encrypt_data)
        self.decrypt_button = tk.Button(self.window, text="Decrypt", command=self.decrypt_data)
        self.output_label = tk.Label(self.window, text="Output:")
        self.output_entry = tk.Entry(self.window)

        # Grid layout
        self.input_label.grid(row=0, column=0)
        self.input_entry.grid(row=0, column=1)
        self.encrypt_button.grid(row=1, column=0)
        self.decrypt_button.grid(row=1, column=1)
        self.output_label.grid(row=2, column=0)
        self.output_entry.grid(row=2, column=1)

    def encrypt_data(self):
        # Get the input data
        data = self.input_entry.get()

        # Quantum Computing Integration
        self.qc.integrate()

        # Quantum Key Distribution
        self.qkd.distribute()

        # Post-Quantum Encryption Algorithms
        encrypted_data = self.pqe.encrypt(data)

        # High-Performance Parallel Processing
        self.pp.process()

        # Quantum-resistant Cryptography
        self.qrc.protect()

        # Key Management and Storage
        self.km.manage()

        # Display the encrypted data
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, encrypted_data)

    def decrypt_data(self):
        # Get the encrypted data
        encrypted_data = self.output_entry.get()

        # Decrypt the data
        decrypted_data = self.pqe.decrypt(encrypted_data)

        # Display the decrypted data
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, decrypted_data)

    def interact(self):
        # Start the main loop
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.interact()
```
