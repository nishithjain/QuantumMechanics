# Glossary

[Home](README.md) · [Roadmap](00-learning-roadmap.md)

| Term | Plain-language meaning |
|---|---|
| **Scalar** | A single number, with no direction. Speed is a scalar. |
| **Vector** | A quantity with size and direction. Velocity is a vector. Written as a column of numbers. |
| **Ket** \(\|v\rangle\) | Dirac name for a column vector. Also stands for a quantum state. |
| **Bra** \(\langle v\|\) | Dirac name for the matching row vector (conjugate transpose of the ket). |
| **Inner product** \(\langle b\|a\rangle\) | A single number: how much two states overlap. |
| **Outer product** \(\|a\rangle\langle b\|\) | A matrix built from a ket and a bra. |
| **Amplitude** | A (possibly complex) entry of a state vector. Probability is the squared length \(\lvert\alpha\rvert^2\). |
| **Normalization** | Amplitudes satisfy \(\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1\) so probabilities add to \(100\%\). |
| **Superposition** | A state that is a combination of basis states, not a single classical \(0\) or \(1\). |
| **Measurement** | Looking in a basis; the state collapses to one outcome with probability given by \(\lvert\text{amplitude}\rvert^2\). |
| **Global phase** | An overall factor such as \(-1\) in front of a whole vector. It does not change \(0/1\) measurement probabilities. |
| **Pauli-X / bit flip** | Quantum NOT. Matrix \(\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\). |
| **Hadamard gate** \(H\) | Creates or undoes equal superposition. Its own inverse. |
| **Moore's law** | Historical trend: transistor counts on chips roughly doubled about every two years. |
| **Shor's algorithm** | Quantum factoring algorithm (1994). Threatens RSA if large machines exist. |
| **Grover's algorithm** | Quantum unstructured search in about \(\sqrt{n}\) steps (1996). |
| **Matrix** | A grid of numbers that represents an operation on a vector. |
| **Identity matrix** \(I\) | The “do nothing” operation. Ones on the diagonal, zeros elsewhere. |
| **Permutation matrix** | A matrix that only shuffles entries. Reversible. |
| **Complex number** | A number with a real part and an imaginary part; \(i^2 = -1\). |
| **Conjugate** | Flip the sign of the imaginary part. |
| **Transpose** \(U^T\) | Turn rows into columns. |
| **Conjugate transpose** \(U^\dagger\) or \(U^H\) | Transpose, then conjugate. Also called the adjoint. |
| **Hermitian matrix** | A matrix that equals its own conjugate transpose: \(A^\dagger = A\). |
| **Unitary matrix** | A square matrix with \(U^\dagger U = I\). Reversible and length-preserving. Every quantum gate is unitary. |
| **Tensor product** \(\otimes\) | A rule for combining two vectors into one larger vector. |
| **Product state** | A combined state that can be factored back into single-system states. |
| **cbit** | Classical bit: strictly \(0\) or \(1\). |
| **Qubit** | Quantum bit: a state vector, often written as a mix of \(\|0\rangle\) and \(\|1\rangle\). |
| **Reversible operation** | From the output and the rule, you can uniquely recover the input. |
| **CNOT** | Controlled-NOT: flip the target bit only if the control bit is \(1\). |
| **Toffoli gate** | Three-bit controlled-controlled-NOT. The usual reversible stand-in for NAND. |
