import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import UnitaryGate
from qiskit.providers.basic_provider import BasicSimulator


def grover(n,times):
    qc = QuantumCircuit(n,n)
    qc.h(range(n))
        
    for _ in range(times):
        qc.append(G(n),range(n))
        
    qc.measure(range(0,n), range(n))
    return qc

def G(n):
    qc = QuantumCircuit(n)
    qc.append(oracle(),range(n))
    qc.h(range(n))
    
    qc.append(rotate(n),range(n))
    
    qc.h(range(n))
    return qc

def rotate(n):
    matrix = np.zeros((2 ** n, 2 ** n), dtype=int)
    for i in range(2**n):
        matrix[i][i] = -1
    matrix[0][0] = 1
    return UnitaryGate(matrix)

def oracle():
    # Q2.2
    qc = QuantumCircuit(4)
    qc.cz(0, 3)
    return qc

# def oracle():
#     # Q2.4
#     qc = QuantumCircuit(4)
#     qc.ccz(0,1,2)
#     return qc

N = 4
times = 1
qc = grover(N,oracle,times)
print(qc.draw())
print("iteration:",times)

backend = BasicSimulator()
tqc = transpile(qc, backend)
result = backend.run(tqc).result()
counts = result.get_counts()
print("counts:", counts)