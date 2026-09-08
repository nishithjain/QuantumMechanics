# Classical bits and reversibility

[Home](../README.md) · [Roadmap](../00-learning-roadmap.md) · [Glossary](../glossary.md)

**Previous:** [Tensor products](../01-mathematical-foundations/05-tensor-products.md) · **Next:** [The qubit](04-the-qubit.md)

---

A **classical bit** (cbit) is an ordinary computer bit: it is either \(0\) or \(1\). We will write those two values as the same two kets you already met:

$$
|0\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix},
\qquad
|1\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

An **operation** is a matrix that takes one of these columns in and produces a column out.

## What “reversible” means

An operation is **reversible** if, given the operation and the output, you can uniquely recover the input.

In matrix language: if \(A x = B\), and you know \(A\) and \(B\), there is only one \(x\). That happens when \(A\) has an inverse.

- Operations that only **permute** (shuffle) values are reversible.
- Operations that **erase** or **overwrite** are not reversible. Two different inputs get smashed into the same output, so you cannot tell which input it was.

Quantum computers use only reversible operations. In linear algebra they are the **unitary** matrices from the previous notes. The inverse of a quantum gate \(U\) is \(U^\dagger\). That inverse is *not* always the same matrix as \(U\) itself.

## Four operations on one cbit

### Identity — reversible

Do nothing: \(f(x) = x\).

- \(0 \rightarrow 0\)
- \(1 \rightarrow 1\)

$$
\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$

$$
\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

### Negation (NOT) — reversible

Flip the bit: \(f(x) = \neg x\).

- \(0 \rightarrow 1\)
- \(1 \rightarrow 0\)

$$
\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

$$
\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$

If you see a \(1\) come out, you know a \(0\) went in, and vice versa. This matrix is also its own inverse: apply NOT twice and you are back.

### Set-0 — not reversible

Force the answer to \(0\), no matter what came in: \(f(x) = 0\).

- \(0 \rightarrow 0\)
- \(1 \rightarrow 0\)

$$
\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$

$$
\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$

Both inputs become \(|0\rangle\). The original bit has been erased. You cannot undo it.

### Set-1 — not reversible

Force the answer to \(1\): \(f(x) = 1\).

- \(0 \rightarrow 1\)
- \(1 \rightarrow 1\)

$$
\begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

$$
\begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

Again, two inputs, one output. Overwrite, not a shuffle.

## What we will keep

From here on we only care about reversible operations, because those are the ones quantum computers are allowed to use.

---

**Previous:** [Tensor products](../01-mathematical-foundations/05-tensor-products.md) · **Next:** [The qubit](04-the-qubit.md)
