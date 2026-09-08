# Tensor products

[Home](../README.md) · [Roadmap](../00-learning-roadmap.md) · [Glossary](../glossary.md)

**Previous:** [Complex numbers and unitary matrices](04-complex-numbers-and-unitary-matrices.md) · **Next:** [Classical bits and reversibility](../02-quantum-computing-foundations/01-classical-bits-and-reversibility.md)

---

A **tensor product** (symbol \(\otimes\)) is a rule for gluing two small vectors into one bigger vector. If each small system has \(2\) numbers, two systems together have \(2 \times 2 = 4\) numbers. Three systems have \(2^3 = 8\) numbers. In general, \(n\) two-level systems make a vector of size \(2^n\).

Everyday picture: one light switch has two positions. Two switches have four combined positions: off-off, off-on, on-off, on-on. The tensor product is how we write that “combined list” as one column.

## Two vectors

Take each number of the first vector, and multiply the *entire* second vector by it. Then stack those pieces.

$$
\begin{bmatrix} x_0 \\ x_1 \end{bmatrix}
\otimes
\begin{bmatrix} y_0 \\ y_1 \end{bmatrix}
=
\begin{bmatrix}
x_0 \begin{bmatrix} y_0 \\ y_1 \end{bmatrix} \\
x_1 \begin{bmatrix} y_0 \\ y_1 \end{bmatrix}
\end{bmatrix}
=
\begin{bmatrix}
x_0 y_0 \\
x_0 y_1 \\
x_1 y_0 \\
x_1 y_1
\end{bmatrix}
$$

Numbers:

$$
\begin{bmatrix} 1 \\ 2 \end{bmatrix}
\otimes
\begin{bmatrix} 3 \\ 4 \end{bmatrix}
=
\begin{bmatrix} 1\cdot 3 \\ 1\cdot 4 \\ 2\cdot 3 \\ 2\cdot 4 \end{bmatrix}
=
\begin{bmatrix} 3 \\ 4 \\ 6 \\ 8 \end{bmatrix}
$$

## Three vectors

Do the same thing again: tensor the first pair, then tensor with the third vector. The eight entries are every product \(x_i y_j z_k\) in a fixed order:

$$
\begin{bmatrix} x_0 \\ x_1 \end{bmatrix}
\otimes
\begin{bmatrix} y_0 \\ y_1 \end{bmatrix}
\otimes
\begin{bmatrix} z_0 \\ z_1 \end{bmatrix}
=
\begin{bmatrix}
x_0 y_0 z_0 \\
x_0 y_0 z_1 \\
x_0 y_1 z_0 \\
x_0 y_1 z_1 \\
x_1 y_0 z_0 \\
x_1 y_0 z_1 \\
x_1 y_1 z_0 \\
x_1 y_1 z_1
\end{bmatrix}
$$

Numbers (this one is \(|1\rangle \otimes |1\rangle \otimes |0\rangle\)):

$$
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
\otimes
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}
$$

Only the product \(x_1 y_1 z_0 = 1 \cdot 1 \cdot 1\) is nonzero, and that product sits in the seventh slot.

## Product states

When a big vector is built this way from smaller ones, we call it a **product state**. You can factor it back into the pieces you started with.

Not every big vector can be factored. Those “un-factorable” states are how **entanglement** will appear later. For the classical-bit notes that follow, every state we write *is* a product state.

---

**Previous:** [Complex numbers and unitary matrices](04-complex-numbers-and-unitary-matrices.md) · **Next:** [Classical bits and reversibility](../02-quantum-computing-foundations/01-classical-bits-and-reversibility.md)
