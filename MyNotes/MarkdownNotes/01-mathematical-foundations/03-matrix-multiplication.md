# Matrix multiplication

[Home](../README.md) · [Roadmap](../00-learning-roadmap.md) · [Glossary](../glossary.md)

**Previous:** [Vector notation and bra-ket](02-vector-notation-and-bra-ket.md) · **Next:** [Complex numbers and unitary matrices](04-complex-numbers-and-unitary-matrices.md)

---

A **matrix** is a grid of numbers. In quantum computing, a matrix is the usual way to write an *operation*: “take this state-vector in, send that state-vector out.”

Multiplying a matrix by a vector is a recipe. Each output number is made by walking along one row of the matrix, pairing it with the vector, multiplying pairs, and adding.

## 2-by-2 matrix times a 2-vector

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
=
\begin{bmatrix} ax + by \\ cx + dy \end{bmatrix}
$$

The top output uses the top row: \(a\) with \(x\), and \(b\) with \(y\). The bottom output uses the bottom row: \(c\) with \(x\), and \(d\) with \(y\).

## 3-by-3 matrix times a 3-vector

Same idea, one extra piece in each row:

$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
=
\begin{bmatrix}
ax + by + cz \\
dx + ey + fz \\
gx + hy + iz
\end{bmatrix}
$$

## Two 2-by-2 matrices

When you multiply two matrices, each *column* of the second matrix is treated like a vector. You multiply the first matrix by that column, and that becomes one column of the answer.

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} w & x \\ y & z \end{bmatrix}
=
\begin{bmatrix}
aw + by & ax + bz \\
cw + dy & cx + dz
\end{bmatrix}
$$

Sizes must fit: the number of columns on the left must equal the number of rows on the right.

## The identity matrix: “do nothing”

The **identity** matrix has \(1\)s on the main diagonal (top-left to bottom-right) and \(0\)s everywhere else. Multiplying by it leaves a vector unchanged. It is the matrix version of multiplying a number by \(1\).

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} a \\ b \\ c \end{bmatrix}
=
\begin{bmatrix} a \\ b \\ c \end{bmatrix}
$$

## A permutation matrix: “shuffle, do not erase”

A **permutation** matrix has a single \(1\) in each row and each column, and \(0\)s elsewhere. It only rearranges the entries of a vector. That kind of shuffle can be undone, so it is reversible.

This example takes the vector with a \(1\) in the second slot and moves that \(1\) to the third slot:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}
$$

Check: the input vector is “pick the second column of the matrix.” That second column is \(\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}\), which is the output.

Identity and permutation matrices are the linear-algebra picture of “I can always get the input back from the output.” The next notes connect that idea to complex numbers and to quantum gates.

---

**Previous:** [Vector notation and bra-ket](02-vector-notation-and-bra-ket.md) · **Next:** [Complex numbers and unitary matrices](04-complex-numbers-and-unitary-matrices.md)
