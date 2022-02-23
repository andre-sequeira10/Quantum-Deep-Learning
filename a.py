import pennylane as qml 

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def qc(wire=0):
    #qml.Hadamard(wires=0)

    return qml.var(qml.PauliZ(0))


print(qc())