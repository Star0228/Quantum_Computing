from numpy import pi
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.circuit.library import QFT
from qiskit import QuantumRegister, ClassicalRegister

n_qubits = 4
qr = QuantumRegister(4)
cr = ClassicalRegister(3)
qc = QuantumCircuit(qr, cr)

## change the value of theta to test the algorithm
theta = pi / 4 
# theta = 2 * pi / 3 ## Q2.23

## initialize the state
qc.initialize([3/5,4/5], 3) 
# qc.x(3) 
for i in range(0, qc.num_qubits-1, 1):
    qc.h(i)
for i in range(0, qc.num_qubits-1, 1):
    for j in range(0, 2**i, 1):
        qc.cp(theta, i, 3)

qc = qc.compose(QFT(3, inverse=True), [0, 1, 2])

## measure qubits 0, 1, 2 to classical bits 0, 1, 2
qc.measure([0, 1, 2], [0, 1, 2])
print(qc)
backend = BasicSimulator()
tqc = transpile(qc, backend)
result = backend.run(tqc).result()
counts = result.get_counts()
print(counts)