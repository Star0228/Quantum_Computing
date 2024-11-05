from qubit_simulator import QubitSimulator
import matplotlib.pyplot as plt


def plot_histogram(result):
    labels, counts = zip(*result.items())
    total_counts = sum(counts)
    frequencies = [float(count) / total_counts for count in counts]
    
    bar = plt.bar(labels, frequencies)
    plt.xlabel('Measurement outcome')
    plt.ylabel('Frequency')
    plt.title('GHZ State Measurement Results')
    plt.bar_label(bar, label_type='edge')
    plt.show()

circ = QubitSimulator(5)

circ.h(0)  
for i in range(4):
    circ.cx(i, i + 1)  
print(circ.__str__())

result = circ.run(shots=1000)  

plot_histogram(result)


