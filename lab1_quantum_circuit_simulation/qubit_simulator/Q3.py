import random
import time
from qubit_simulator import QubitSimulator
import matplotlib.pyplot as plt
import time


def apply_circuit(circuit, n):
    circuit.h(n - 1)
    for qubit in range(n - 1):
        circuit.cu(qubit, qubit + 1, random.random() * 3.14, random.random() * 3.14, random.random() * 3.14)

# n_qubits = 5 # change this value (<=16)
n_qubits_list = list(range(2, 16))
times = []
for n_qubits in n_qubits_list:
    simulator = QubitSimulator(n_qubits)
    t = time.time()
    apply_circuit(simulator, n_qubits)
    simulator.run(shots=1000)
    elapsed_time = time.time() - t
    times.append(elapsed_time)
    print(f"n_qubits: {n_qubits}, time: {elapsed_time}")
    del simulator
    time.sleep(5)  

plt.plot(n_qubits_list, times, marker='o')

plt.title('Times when Qubits Increase')
plt.xlabel('qubits number (n)')
plt.ylabel('time (s)')

plt.show()