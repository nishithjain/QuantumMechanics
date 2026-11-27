# CNOT gate

[Home](../README.md) · [Roadmap](../00-learning-roadmap.md) · [Glossary](../glossary.md)

**Previous:** [Representing multiple qubits](02-representing-multiple-qubits.md)

---

**CNOT** means *controlled NOT*. It looks at two bits:

- the first bit is the **control**
- the second bit is the **target**

Rule in plain language:

- if the control is \(0\), leave the target alone
- if the control is \(1\), flip the target

The control itself never changes.

| Input | Output |
|---|---|
| \(|00\rangle\) | \(|00\rangle\) |
| \(|01\rangle\) | \(|01\rangle\) |
| \(|10\rangle\) | \(|11\rangle\) |
| \(|11\rangle\) | \(|10\rangle\) |

That is a permutation of the four two-bit states, so it is reversible. Doing CNOT twice returns you to the start, so this particular gate *is* its own inverse.

## The matrix

$$
C
=
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

The top-left \(2\times 2\) block is “do nothing” on \(|00\rangle\) and \(|01\rangle\). The bottom-right block swaps \(|10\rangle\) and \(|11\rangle\).

## Four calculations

### Control \(1\), target \(0\) \(\rightarrow\) flip to \(1\)

$$
C|10\rangle
=
C\left(
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
\right)
=
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
|11\rangle
$$

### Control \(1\), target \(1\) \(\rightarrow\) flip to \(0\)

$$
C|11\rangle
=
C\left(
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\right)
=
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
|10\rangle
$$

### Control \(0\), target \(0\) \(\rightarrow\) no change

$$
C|00\rangle
=
C\left(
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
\right)
=
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}
=
|00\rangle
$$

### Control \(0\), target \(1\) \(\rightarrow\) no change

$$
C|01\rangle
=
C\left(
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
\otimes
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\right)
=
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}
=
|01\rangle
$$

## Building larger logic

Ordinary computers can be built from **NAND** gates. NAND is *not* reversible: it throws information away.

CNOT is a basic two-bit *reversible* gate, and you use it as a brick for larger reversible circuits. It is **not** a drop-in replacement for NAND. You cannot make every classical function from CNOT alone. The reversible gate that can play the role NAND plays classically is the **Toffoli** gate (a controlled-controlled-NOT on three bits). That is a topic for a later note.

---

**Previous:** [Representing multiple qubits](02-representing-multiple-qubits.md)
