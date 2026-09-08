# Learning roadmap

Follow this order. Each note builds on the one before it. Skip ahead only if you already know that topic well.

Start with [README](README.md) if you want the full table of contents. Use the [glossary](glossary.md) whenever a word is new.

## Recommended order

1. [Why quantum computing?](00-why-quantum-computing.md)  
   Why shrinking chips has limits, and which problems quantum ideas are aimed at.

2. [Scalars and vectors](01-mathematical-foundations/01-scalars-and-vectors.md)  
   What a number is versus a list of numbers, and why quantum states are written as vectors.

3. [Vector notation and bra-ket](01-mathematical-foundations/02-vector-notation-and-bra-ket.md)  
   How physicists write vectors with `|ψ⟩` and `⟨ψ|`, inner products, and outer products.

4. [Matrix multiplication](01-mathematical-foundations/03-matrix-multiplication.md)  
   How a grid of numbers can change a vector. This is the language of quantum gates.

5. [Complex numbers and unitary matrices](01-mathematical-foundations/04-complex-numbers-and-unitary-matrices.md)  
   Why quantum amplitudes use complex numbers, and what it means for a gate to be “unitary.”

6. [Tensor products](01-mathematical-foundations/05-tensor-products.md)  
   How to combine two small systems into one larger system.

7. [Classical bits and reversibility](02-quantum-computing-foundations/01-classical-bits-and-reversibility.md)  
   Ordinary 0 and 1, and why quantum computers prefer operations you can undo.

8. [The qubit](02-quantum-computing-foundations/04-the-qubit.md)  
   Superposition, normalization, and what measurement does.

9. [Pauli-X gate](02-quantum-computing-foundations/05-pauli-x-gate.md)  
   Quantum NOT: swap the two amplitudes.

10. [Hadamard gate](02-quantum-computing-foundations/06-hadamard-gate.md)  
    The usual way to create (and undo) equal superposition.

11. [Combining X and H](02-quantum-computing-foundations/07-combining-x-and-h.md)  
    Chain gates, read a circuit left to right, and see reversibility.

12. [Representing multiple qubits](02-quantum-computing-foundations/02-representing-multiple-qubits.md)  
    Two or more qubits as one vector, including a two-qubit superposition.

13. [CNOT gate](02-quantum-computing-foundations/03-cnot-gate.md)  
    A two-qubit gate that flips one bit depending on another.

## How to use these notes

- Read one file at a time. Do not rush the math notes; later quantum notes assume them.
- Keep the [glossary](glossary.md) open while you read.
- Diagrams live in [assets/images](assets/images/).
