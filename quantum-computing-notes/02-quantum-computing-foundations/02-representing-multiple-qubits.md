# Representing multiple qubits

[Home](../README.md) · [Roadmap](../00-learning-roadmap.md) · [Glossary](../glossary.md)

**Previous:** [Combining X and H](07-combining-x-and-h.md) · **Next:** [CNOT gate](03-cnot-gate.md)

---

One bit is a column of \(2\) numbers. Two bits together are not “two separate columns you keep in your pocket.” They are combined with the **tensor product** into one column of \(4\) numbers. Three bits become a column of \(8\) numbers. For \(n\) bits (or \(n\) qubits) the product state is a vector of size \(2^n\).

We still use

$$
|0\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix},
\qquad
|1\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

A string such as \(10\) means “first bit is \(1\), second bit is \(0\).” In ket notation that is \(|10\rangle\), which means \(|1\rangle \otimes |0\rangle\).

## Two bits

$$
|00\rangle
=
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}
$$

$$
|01\rangle
=
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
\otimes
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}
$$

$$
|10\rangle
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}
$$

$$
|11\rangle
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}
$$

Each of these is a **product state**: you can factor the big column back into the two small ones.

Notice the pattern. The single \(1\) sits in a different row for each bit-string. If you read the bit-string as a binary number, that number tells you *which row* (counting from zero):

| Ket | Binary as a number | Row of the \(1\) (starting at row 0) |
|---|---|---|
| \(|00\rangle\) | \(0\) | first row |
| \(|01\rangle\) | \(1\) | second row |
| \(|10\rangle\) | \(2\) | third row |
| \(|11\rangle\) | \(3\) | fourth row |

## Three bits

The decimal number \(4\) is binary \(100\), so \(|4\rangle\) means \(|100\rangle\):

$$
|4\rangle
=
|100\rangle
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}
$$

The \(1\) is in row number \(4\) (the fifth row if you count from one). Same rule as above.

These notes started with classical bits. A register of qubits uses the same stacking. The extra quantum ingredient is that the entries may be complex amplitudes, not only a single \(1\).

## Two qubits in superposition

The same tensor-product rule works when each qubit is already a mix. If

$$
\begin{bmatrix} a \\ b \end{bmatrix}
\otimes
\begin{bmatrix} c \\ d \end{bmatrix}
=
\begin{bmatrix} ac \\ ad \\ bc \\ bd \end{bmatrix}
$$

then \(a,b,c,d\) may be complex, and the four amplitudes must still satisfy

$$
|ac|^2 + |ad|^2 + |bc|^2 + |bd|^2 = 1
$$

Example: two copies of the fair-coin state

$$
\begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}
\otimes
\begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}
=
\begin{bmatrix} 1/2 \\ 1/2 \\ 1/2 \\ 1/2 \end{bmatrix}
$$

Check:

$$
4 \times \left|\frac{1}{2}\right|^2 = 4 \times \frac{1}{4} = 1
$$

(Your screenshot wrote the four squares as “\(\lvert\lvert 1/4\rvert\rvert\)” added together. After squaring, each term *is* \(1/4\), and four of them add to \(1\).)

This product state has a \(1/4\) chance of collapsing to each of \(|00\rangle\), \(|01\rangle\), \(|10\rangle\), and \(|11\rangle\).

The next note applies a two-bit reversible gate, CNOT, to these four-row vectors.

---

**Previous:** [Combining X and H](07-combining-x-and-h.md) · **Next:** [CNOT gate](03-cnot-gate.md)
