# Core Algorithms — Part A: Beginner-Friendly Lecture Notes

## 1. Where we are in the course

This lecture connects earlier mathematical foundations to the quantum algorithms that follow. We have already studied **qubits**, **superposition**, **measurement**, **tensor products**, and **quantum gates**. We now need to combine those tools into actual algorithms. Before doing so, the session finishes the discussion of **eigenvalues and eigenvectors**.

**Everyday picture:** learning vectors and gates is like learning letters and words; algorithms are the complete sentences. We will first revisit the alphabet, then build a small but surprising program.

## 2. Quick review: basis, orthonormal basis, transformations and unitaries

### 2.1 Basis means a coordinate system

A vector is an arrow with a length and direction. A **basis** is a set of reference arrows we use to describe other arrows. In the ordinary 2D plane, the standard basis is

$$
e_1=\begin{pmatrix}1\\\\0\end{pmatrix},\qquad e_2=\begin{pmatrix}0\\\\1\end{pmatrix}.
$$

For example,

$$
v=\begin{pmatrix}3\\\\2\end{pmatrix}=3e_1+2e_2.
$$

This says: move three units along the first reference direction and two along the second. Change the basis and the *coordinates* can change even if the physical arrow does not.

An **orthonormal basis** has mutually perpendicular reference vectors, each of length one. Its special advantage is that the coordinate along a basis vector $b_i$ is simply $\langle b_i,v\rangle$. For complex vectors, the inner product conjugates the first argument: $\langle b_i,v\rangle=b_i^\dagger v$. This is why orthonormal bases make calculations convenient.

### 2.2 Matrices act on vectors

A linear transformation is a rule that respects addition and scaling:

$$
A(u+v)=Au+Av,\qquad A(cv)=cAv.
$$

A matrix is a way to write such a rule. If $A$ is an $m\times n$ matrix and $x$ has $n$ entries, $Ax$ has **$m$ entries**. The transcript says $n$ at one point; that is a dimensional slip, not the general rule.

### 2.3 Why quantum gates must be unitary

**What does “unitary” mean?** Start with the idea, then the equation. In closed quantum circuits, gates are **unitary** so the state stays physically valid and can be run forward and backward in principle.

#### 2.3.1 A gate as a “machine” on one qubit

Picture a single-qubit **quantum gate** $U$ as a box that updates the state **in place** on the qubit wire:

| Stage | What it is |
| --- | --- |
| **Input** | $\lvert\psi\rangle$ — some normalized qubit state |
| **Gate** | $U$ — a unitary operation |
| **Output** | $\lvert\psi'\rangle = U\lvert\psi\rangle$ — a new state on the same qubit |

$U$ **may change** the state, but it must **not destroy or leak** quantum information: amplitudes stay normalized, and the map is reversible (there is an inverse $U^\dagger$).

#### 2.3.2 Everyday analogy: rotate a photograph

Rotate a photo by $90^\circ$: the picture **looks different**, but **nothing is cropped or thrown away**. Rotate by $-90^\circ$ and you recover the original.

A unitary gate is similar:

- It **can** change the quantum state.
- It **must** preserve total probability (all amplitude “weight” stays in the system).
- It **can be undone** by applying the inverse operation $U^\dagger$.

#### 2.3.3 What the mathematics says

A single-qubit gate is a matrix $U$. It is **unitary** when

$$
U^\dagger U = I,
$$

where $U^\dagger$ is the **conjugate transpose** and $I$ is the **identity** (do nothing).

| Symbol | Meaning |
| --- | --- |
| $U$ | The gate as a matrix |
| $U^\dagger$ | Conjugate transpose of $U$ |
| $I$ | Identity matrix |

In words: apply $U$, then $U^\dagger$, and you return to the same state:

$$
U^\dagger U\,|\psi\rangle = |\psi\rangle.
$$

Equivalently, unitary maps **preserve lengths** (normalization):

$$
\|U\psi\| = \|\psi\|,\qquad U^\dagger U = I.
$$

Here $U^\dagger$ conjugates the first factor in inner products, as in §2.1. The columns of $U$ are **orthonormal** — perpendicular and length one — not merely perpendicular.

A normalized computational state satisfies

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle,\qquad |\alpha|^2 + |\beta|^2 = 1.
$$

Those squared magnitudes are measurement probabilities, so they must sum to $1$. A unitary gate cannot turn that into $0.25$ or $4$ total weight.

**Remember this:** valid gates keep total probability at $100\%$; invalid operations are not allowed as reversible quantum gates.

#### 2.3.4 Why this matters for quantum computing

1. **No loss of quantum information** — $Z$-basis probabilities stay normalized. For example,

   $$
   P(0) + P(1) = 1.
   $$

   If $P(0)=0.7$, then $P(1)=0.3$. A unitary gate preserves that total.

2. **Operations are reversible** — every unitary $U$ has inverse $U^\dagger$ on the same Hilbert space, so evolution can be undone in the mathematical model (hardware noise is a separate story).

3. **Interference is preserved** — algorithms combine amplitudes with **+** and **−** signs. Unitary evolution changes phases and mixes branches while keeping overall normalization so interference remains meaningful.

#### 2.3.5 Example: the Pauli-$X$ gate

The **Pauli-$X$** gate is the quantum **NOT**: it swaps basis kets,

$$
|0\rangle \longrightarrow |1\rangle,\qquad |1\rangle \longrightarrow |0\rangle.
$$

Its matrix is

$$
X = \begin{pmatrix}0&1\\\\1&0\end{pmatrix}.
$$

Apply $X$ twice:

$$
X^2 = X X = I.
$$

First $X$ flips $|0\rangle$ to $|1\rangle$; second $X$ flips back to $|0\rangle$. That is unitary “rotate and undo” on a discrete state swap.

## 3. Eigenvectors: directions that a matrix does not turn

### 3.1 Intuition before the equation

Imagine applying a matrix to many arrows. Most arrows may rotate to a different line. A few special arrows only become longer, shorter, reverse, or collapse to zero. These special nonzero arrows are **eigenvectors**.

$$
\boxed{Av=\lambda v,\qquad v\ne0}
$$

- $A$: the square matrix/transformation.
- $v$: a **nonzero eigenvector**.
- $\lambda$: its **eigenvalue**, the scale factor.

If $\lambda=3$, the arrow becomes three times as long; if $\lambda=-1$, it reverses; if $\lambda=0$, it collapses to zero. The zero *vector* is not an eigenvector, although zero can be an eigenvalue.

**Interactive:** drag the slider or pick a matrix to see how a linear map moves the grid. Eigenvector directions stay on their own line (only scale or flip).

<!-- markdownlint-disable MD033 -->
<div class="demo-frame">
<iframe src="../animations/eigenvectors-grid-transform.html" title="Eigenvectors — animated grid transformation" width="100%" height="720" loading="lazy" style="border:1px solid #dce3ef;border-radius:12px;max-width:100%;display:block;"></iframe>
</div>
<!-- markdownlint-enable MD033 -->

### 3.2 First matrix example

$$
A=\begin{pmatrix}2&1\\\\1&2\end{pmatrix}.
$$

Try $v=(1,1)^T$:

$$
Av=\begin{pmatrix}2\cdot1+1\cdot1\\\\1\cdot1+2\cdot1\end{pmatrix}
=\begin{pmatrix}3\\\\3\end{pmatrix}=3\begin{pmatrix}1\\\\1\end{pmatrix}.
$$

So $(1,1)^T$ is an eigenvector with eigenvalue 3. The transcript briefly says $(3,1)$ for the result; the multiplication establishes that the correct result is **$(3,3)$**.

Try $w=(1,0)^T$: $Aw=(2,1)^T$. It is no longer on the original horizontal line, so **not** an eigenvector.

Try $q=(1,-1)^T$:

$$
Aq=(2-1,\,1-2)^T=(1,-1)^T=1q.
$$

So this is an eigenvector with eigenvalue 1. The vector $(2,2)^T$ is also an eigenvector with eigenvalue 3: $A(2,2)^T=(6,6)^T=3(2,2)^T$. Every **nonzero** multiple of an eigenvector works.

**Interactive:** try $(1,1)^T$, $(1,0)^T$, and $(1,-1)^T$ under the same $A$ — watch which arrows stay on their line.

<!-- markdownlint-disable MD033 -->
<div class="demo-frame">
<iframe src="../animations/first-matrix-eigenvectors.html" title="First matrix example — eigenvectors under A = [[2,1],[1,2]]" width="100%" height="920" loading="lazy" style="border:1px solid #dce3ef;border-radius:12px;max-width:100%;display:block;"></iframe>
</div>
<!-- markdownlint-enable MD033 -->

### 3.3 Quantum X gate: swapping coordinates

The next example is the **Pauli-$X$** (quantum NOT) gate — a $2\times2$ flip matrix.

**Interactive:** coordinate swap, reflection across $y=x$, and eigen-directions on the same diagram as §3.3.1–3.3.3 below.

<!-- markdownlint-disable MD033 -->
<div class="demo-frame">
<iframe src="../animations/quantum-x-gate.html" title="Quantum X gate — coordinate swap and reflection" width="100%" height="780" loading="lazy" style="border:1px solid #dce3ef;border-radius:12px;max-width:100%;display:block;"></iframe>
</div>
<!-- markdownlint-enable MD033 -->

#### 3.3.1 How the $X$ gate swaps coordinates

As a matrix,

$$
X=\begin{pmatrix}0&1\\\\1&0\end{pmatrix}.
$$

The superscript $T$ in $(a,b)^T$ means **column vector** (stack $a$ above $b$). Matrix multiply step by step:

$$
X\begin{pmatrix}a\\\\b\end{pmatrix}
=
\begin{pmatrix}0&1\\\\1&0\end{pmatrix}
\begin{pmatrix}a\\\\b\end{pmatrix}
=
\begin{pmatrix}0a+1b\\\\1a+0b\end{pmatrix}
=
\begin{pmatrix}b\\\\a\end{pmatrix}.
$$

Each **row** is one output entry: the top row outputs $b$, the bottom row outputs $a$. So $(3,1)^T$ becomes $(1,3)^T$.

#### 3.3.2 Why swapping is a reflection across $y=x$

Start at the tip $(3,1)$: 3 right, 1 up. After $X$, the tip is $(1,3)$: 1 right, 3 up.

The midpoint of $(3,1)$ and $(1,3)$ is $(2,2)$, on the line $y=x$. The segment between the tips meets that line at a **right angle**, so the two tips are **mirror images** across $y=x$. The tail stays at the origin (also on $y=x$), so the whole arrow **reflects** across $y=x$.

#### 3.3.3 Why $(1,1)^T$ and $(1,-1)^T$ are eigenvectors

A nonzero $v$ is an **eigenvector** when $Xv=\lambda v$: one number $\lambda$ scales **both** coordinates at once.

| Input $v$ | Output $Xv$ | Arrow picture | $\lambda$ |
| --- | --- | --- | --- |
| $(1,1)^T$ | $(1,1)^T=1\cdot(1,1)^T$ | On the mirror line $y=x$; unchanged | $+1$ |
| $(1,-1)^T$ | $(-1,1)^T=-1\cdot(1,-1)^T$ | On $y=-x$, **perpendicular** to the mirror; **reverses** along that line | $-1$ |

An eigenvector may **flip direction** ($\lambda=-1$) and still lie on the same line through the origin. That is not a failure of the definition — the tip moves to the opposite side of the origin **along the same ray**.

Check:

$$
X(1,1)^T=(1,1)^T,\qquad
X(1,-1)^T=(-1,1)^T=-(1,-1)^T.
$$

#### 3.3.4 Why it is called the quantum flip gate

In the **computational basis**, $\lvert0\rangle$ is the column $\begin{pmatrix}1\\\\0\end{pmatrix}$ and $\lvert1\rangle$ is $\begin{pmatrix}0\\\\1\end{pmatrix}$. The same swap gives

$$
X\lvert0\rangle
= X\begin{pmatrix}1\\\\0\end{pmatrix}
= \begin{pmatrix}0\\\\1\end{pmatrix}
= \lvert1\rangle,
\qquad
X\lvert1\rangle
= X\begin{pmatrix}0\\\\1\end{pmatrix}
= \begin{pmatrix}1\\\\0\end{pmatrix}
= \lvert0\rangle.
$$

The normalized states $\lvert+\rangle=\frac{1}{\sqrt2}(1,1)^T$ and $\lvert-\rangle=\frac{1}{\sqrt2}(1,-1)^T$ are still eigenvectors of $X$ with eigenvalues $+1$ and $-1$ (scaling $(1,1)^T$ and $(1,-1)^T$ does not change the eigenvalues).

### 3.4 Identity and the Hadamard exercise

**Identity $I$.** The identity matrix **copies** each coordinate to the same place. For every nonzero column $v$,

$$
Iv = v = 1\cdot v.
$$

So **every nonzero vector** is an eigenvector of $I$ with eigenvalue $\lambda=1$. That is expected: $I$ is the “do nothing” map — no direction is singled out, so **every** direction is an eigen-direction with the same eigenvalue.

**Hadamard $H$ — not every matrix is that generous.** The lecture suggests testing $(1,1)^T$ with the Hadamard matrix

$$
H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\\\1&-1\end{pmatrix}.
$$

Apply $H$ to $(1,1)^T$:

$$
H\begin{pmatrix}1\\\\1\end{pmatrix}
=
\frac{1}{\sqrt2}
\begin{pmatrix}1&1\\\\1&-1\end{pmatrix}
\begin{pmatrix}1\\\\1\end{pmatrix}
=
\begin{pmatrix}\sqrt2\\\\0\end{pmatrix}.
$$

The input lies on $y=x$. The output is $(\sqrt2,0)^T$ — along the **$x$-axis** only. For an eigenvector we need a single $\lambda$ with

$$
H\begin{pmatrix}1\\\\1\end{pmatrix}
\stackrel{?}{=}
\lambda\begin{pmatrix}1\\\\1\end{pmatrix}
=
\begin{pmatrix}\lambda\\\\\lambda\end{pmatrix}.
$$

But $\sqrt2\neq\lambda$ and $0\neq\lambda$ at the same time, so **no** $\lambda$ works. **$(1,1)^T$ is not an eigenvector of $H$.**

**How to read that:** $H$ **mixes** $x$ and $y$ components (it is not a simple swap or scale). Any eigenvector of $H$ would have to be a direction that $H$ only **stretches** or **flips**, not one that it **redirects** to a different line. You can find $H$’s true eigenvectors by solving $\det(H-\lambda I)=0$; they are not $(1,1)^T$ or $(1,-1)^T$.

**Exercise:** repeat the same test for $H(1,-1)^T$, or compute eigenvalues of $H$ and compare with $X$.

### 3.5 Why there are infinitely many eigenvectors

If $Av=\lambda v$, then for any nonzero scalar $c$,

$$
A(cv)=cAv=c\lambda v=\lambda(cv).
$$

Similarly, if $Av=\lambda v$ and $Aw=\lambda w$,

$$
A(v+w)=Av+Aw=\lambda(v+w).
$$

The set $\{v:Av=\lambda v\}$, **including zero**, is a vector subspace called an **eigenspace**. A sum that happens to be zero is in the eigenspace but is not itself an eigenvector. A basis describes this whole subspace without listing infinitely many vectors. Choosing length-one eigenvectors helps normalize the description, but does not always leave only two possibilities: in a higher-dimensional eigenspace there can still be infinitely many unit vectors.

## 4. Given a matrix $A$, how do we discover these special vectors and their corresponding eigenvalues?

### 4.1 What are we trying to find?

In the previous section, we learned about **eigenvectors** and **eigenvalues**.

Remember that when a matrix transforms a vector, normally the vector changes its direction and length.

However, some special vectors behave differently:

- Their direction stays along the same line.
- Their length may increase or decrease.
- They may even reverse direction.

These special vectors are called **eigenvectors**.

The number that tells us how the eigenvector is scaled is called its **eigenvalue**, represented by $\lambda$ (lambda).

Mathematically, this relationship is written as

$$
Av=\lambda v,
$$

where

- $A$ = the matrix representing the transformation,
- $v$ = an eigenvector (the special vector),
- $\lambda$ = an eigenvalue (the scaling factor).

**The question we want to answer is:** given a matrix $A$, how can we discover its eigenvalues and eigenvectors?

We cannot simply guess them. We need a systematic mathematical method.

That is what this section teaches us.

---

### 4.2 First understand a simpler problem: $Bx=0$

Before finding eigenvalues, the lecture introduces a simpler mathematical problem.

Consider

$$
Bx=0,
$$

where $B$ is a matrix and $x$ is an unknown vector.

Suppose

$$
B=\begin{pmatrix}a&b\\\\c&d\end{pmatrix},
\qquad
x=\begin{pmatrix}x_1\\\\x_2\end{pmatrix}.
$$

Multiplying $B$ by $x$ gives

$$
\begin{pmatrix}a&b\\\\c&d\end{pmatrix}
\begin{pmatrix}x_1\\\\x_2\end{pmatrix}
=
\begin{pmatrix}0\\\\0\end{pmatrix},
$$

which produces two equations:

$$
ax_1+bx_2=0,
$$

$$
cx_1+dx_2=0.
$$

**What are we looking for?** Values of $x_1$ and $x_2$ that satisfy both equations.

There is always one obvious solution:

$$
x=\begin{pmatrix}0\\\\0\end{pmatrix}.
$$

This is called the **trivial solution**.

But we are interested in something more useful: can we find a solution where at least one coordinate is nonzero? For example,

$$
x=\begin{pmatrix}1\\\\-1\end{pmatrix}
$$

is a **nontrivial solution**.

**Why is this important?** We will soon convert our eigenvector equation into exactly this type of problem.

But first, we need to understand when a nontrivial solution exists.

---

### 4.3 When does $Bx=0$ have a nonzero solution?

Use the two equations

$$
ax_1+bx_2=0,
$$

$$
cx_1+dx_2=0.
$$

Multiply the first equation by $d$:

$$
adx_1+bdx_2=0.
$$

Multiply the second equation by $b$:

$$
bcx_1+bdx_2=0.
$$

Subtract the second equation from the first:

$$
(ad-bc)x_1=0.
$$

For a nonzero solution, we need the matrix to be **singular**.

A matrix is called singular when its determinant is zero.

For a $2\times2$ matrix,

$$
B=\begin{pmatrix}a&b\\\\c&d\end{pmatrix},
$$

the determinant is

$$
\det(B)=ad-bc.
$$

Therefore, the condition for a nonzero solution is

$$
\boxed{ad-bc=0}
$$

or simply

$$
\boxed{\det(B)=0}.
$$

**What does this mean intuitively?** Think of a matrix as a machine that transforms vectors.

Usually, a nonsingular matrix cannot turn a nonzero vector into a zero vector.

But a singular matrix can.

For example,

$$
B=\begin{pmatrix}1&1\\\\1&1\end{pmatrix},
$$

with

$$
\det(B)=(1\times1)-(1\times1)=0.
$$

Now try

$$
x=\begin{pmatrix}1\\\\-1\end{pmatrix}.
$$

Then

$$
Bx=
\begin{pmatrix}1&1\\\\1&1\end{pmatrix}
\begin{pmatrix}1\\\\-1\end{pmatrix}
=
\begin{pmatrix}0\\\\0\end{pmatrix}.
$$

We found a nonzero vector that becomes zero after multiplication — because the matrix is singular.

**Remember:**

$$
Bx=0,\quad x\neq0
$$

has a nonzero solution **if and only if** $\det(B)=0$.

For a square matrix of any size, this same rule applies.

---

### 4.4 The important connection: turning the eigenvector equation into $Bx=0$

We want eigenvectors and eigenvalues. We know

$$
Av=\lambda v.
$$

The goal is to rewrite this into the simpler form $Bx=0$, because we already know how to solve that problem.

**Step 1 — start with the eigenvector equation**

$$
Av=\lambda v.
$$

Move everything to the left:

$$
Av-\lambda v=0.
$$

**Step 2 — introduce the identity matrix**

Remember that $Iv=v$. For example,

$$
\begin{pmatrix}1&0\\\\0&1\end{pmatrix}
\begin{pmatrix}3\\\\5\end{pmatrix}
=
\begin{pmatrix}3\\\\5\end{pmatrix}.
$$

So we can write

$$
Av-\lambda Iv=0.
$$

**Step 3 — factor out $v$**

$$
\boxed{(A-\lambda I)v=0}.
$$

This has exactly the same structure as $Bx=0$:

| Simpler equation | Eigenvector equation |
| --- | --- |
| $B$ | $A-\lambda I$ |
| $x$ | $v$ |
| $0$ | $0$ |

**Step 4 — apply what we learned about determinants**

We want an eigenvector, and an eigenvector cannot be the zero vector: $v\neq0$.

From §4.3, a nonzero solution exists only when the matrix is singular. Our matrix is $A-\lambda I$, so

$$
\boxed{\det(A-\lambda I)=0}.
$$

This is the **characteristic equation**.

**Main discovery of this section:** instead of guessing eigenvectors directly, first use the determinant to find the eigenvalues.

---

### 4.5 Let's calculate eigenvalues and eigenvectors using an example

Consider

$$
A=\begin{pmatrix}2&0\\\\0&3\end{pmatrix}.
$$

**Step 1 — write the characteristic equation**

$$
\det(A-\lambda I)=0.
$$

**Step 2 — subtract $\lambda I$ from $A$**

$$
A-\lambda I=
\begin{pmatrix}2-\lambda&0\\\\0&3-\lambda\end{pmatrix}.
$$

**Step 3 — calculate the determinant**

For a $2\times2$ matrix, $\det(B)=ad-bc$, so

$$
(2-\lambda)(3-\lambda)-0=0.
$$

Expand:

$$
\lambda^2-5\lambda+6=0.
$$

Factor:

$$
(\lambda-2)(\lambda-3)=0.
$$

So

$$
\boxed{\lambda=2\quad\text{or}\quad\lambda=3}.
$$

**Step 4 — find the eigenvectors**

For each eigenvalue, substitute it into $(A-\lambda I)v=0$.

**Eigenvector for $\lambda=2$**

$$
A-2I=
\begin{pmatrix}0&0\\\\0&1\end{pmatrix}.
$$

Let $v=\begin{pmatrix}v_1\\\\v_2\end{pmatrix}$. Then

$$
\begin{pmatrix}0&0\\\\0&1\end{pmatrix}
\begin{pmatrix}v_1\\\\v_2\end{pmatrix}
=
\begin{pmatrix}0\\\\0\end{pmatrix},
$$

which gives $v_2=0$. We can choose $v_1=1$, so

$$
\boxed{v=\begin{pmatrix}1\\\\0\end{pmatrix}}.
$$

**Eigenvector for $\lambda=3$**

$$
A-3I=
\begin{pmatrix}-1&0\\\\0&0\end{pmatrix},
$$

so $-v_1=0$ and we can choose $v_2=1$:

$$
\boxed{v=\begin{pmatrix}0\\\\1\end{pmatrix}}.
$$

| Eigenvalue | Corresponding eigenvector |
| --- | --- |
| $\lambda=2$ | $\begin{pmatrix}1\\\\0\end{pmatrix}$ |
| $\lambda=3$ | $\begin{pmatrix}0\\\\1\end{pmatrix}$ |

Verify:

$$
A\begin{pmatrix}1\\\\0\end{pmatrix}
=
\begin{pmatrix}2\\\\0\end{pmatrix}
=
2\begin{pmatrix}1\\\\0\end{pmatrix},
\qquad
A\begin{pmatrix}0\\\\1\end{pmatrix}
=
\begin{pmatrix}0\\\\3\end{pmatrix}
=
3\begin{pmatrix}0\\\\1\end{pmatrix}.
$$

---

### 4.6 The Y gate: eigenvalues and eigenvectors

So far we used ordinary real numbers. Quantum computing also uses complex numbers. This subsection works through the **Pauli-$Y$ gate** from start to finish.

#### 4.6.1 First, what are we trying to find?

We have a quantum gate called the **Y gate**:

$$
Y=\begin{pmatrix}0&-i\\\\i&0\end{pmatrix}.
$$

It takes an input quantum state and transforms it into another quantum state.

We want to find two things:

1. **Eigenvalues** — how does the gate affect its special states?
2. **Eigenvectors** — which special states behave this way?

Remember the eigenvector equation:

$$
Yv=\lambda v.
$$

In plain language: when we apply the Y gate to an eigenvector, the result is the same vector multiplied by a number called the eigenvalue.

For example, $Yv=2v$ scales the vector by $2$, and $Yv=-v$ scales it by $-1$ (direction reversed along the same line).

Our job is to discover these special values and vectors.

#### 4.6.2 Before proceeding, understand the imaginary number $i$

You might wonder what $i$ means. We already know

$$
i^2=-1,
$$

so $i\times i=-1$ and therefore $(-i)^2=1$ (equivalently $-i^2=1$ when read as $-(i^2)$).

Useful products:

| Calculation | Answer |
| --- | --- |
| $i\times i$ | $-1$ |
| $(-i)\times i$ | $+1$ |
| $i\times(-i)$ | $+1$ |
| $(-i)\times(-i)$ | $-1$ |

**Why do we need $i$?** Quantum states use complex amplitudes, so gates can contain imaginary entries. For this example, you only need the algebra above — not a full physical interpretation of $i$ yet.

#### 4.6.3 Finding the eigenvalues

We know $Yv=\lambda v$. From §4.4 this becomes $(Y-\lambda I)v=0$. For a nonzero eigenvector, the matrix must be singular:

$$
\boxed{\det(Y-\lambda I)=0}.
$$

That is our starting point.

**Step 1 — write $Y$ and $\lambda I$**

$$
Y=\begin{pmatrix}0&-i\\\\i&0\end{pmatrix},
\qquad
I=\begin{pmatrix}1&0\\\\0&1\end{pmatrix},
\qquad
\lambda I=
\begin{pmatrix}\lambda&0\\\\0&\lambda\end{pmatrix}.
$$

**Step 2 — subtract $\lambda I$ from $Y$**

Subtract entry by entry:

$$
Y-\lambda I
=
\begin{pmatrix}0&-i\\\\i&0\end{pmatrix}
-
\begin{pmatrix}\lambda&0\\\\0&\lambda\end{pmatrix}
=
\begin{pmatrix}-\lambda&-i\\\\i&-\lambda\end{pmatrix}.
$$

**Step 3 — calculate the determinant**

For $B=\begin{pmatrix}a&b\\\\c&d\end{pmatrix}$, $\det(B)=ad-bc$. Here $a=-\lambda$, $b=-i$, $c=i$, $d=-\lambda$, so

$$
\det(Y-\lambda I)=(-\lambda)(-\lambda)-(-i)(i).
$$

Compute each factor:

$$
(-\lambda)(-\lambda)=\lambda^2,
\qquad
(-i)(i)=-i^2=1.
$$

So

$$
\det(Y-\lambda I)=\lambda^2-1.
$$

Set the determinant to zero:

$$
\lambda^2-1=0
\quad\Rightarrow\quad
(\lambda-1)(\lambda+1)=0.
$$

**Result:** the Y gate has two eigenvalues:

$$
\boxed{\lambda=+1}
\qquad\text{and}\qquad
\boxed{\lambda=-1}.
$$

Next we find the eigenvectors that go with each eigenvalue.

#### 4.6.4 Finding the eigenvector for $\lambda=+1$

Substitute $\lambda=+1$ into $Yv=\lambda v$:

$$
Yv=v.
$$

We are looking for a vector that is **unchanged** when the Y gate is applied.

**Step 1 — matrix equation**

Let $v=\begin{pmatrix}v_1\\\\v_2\end{pmatrix}$. Then

$$
\begin{pmatrix}0&-i\\\\i&0\end{pmatrix}
\begin{pmatrix}v_1\\\\v_2\end{pmatrix}
=
\begin{pmatrix}v_1\\\\v_2\end{pmatrix}.
$$

**Step 2 — multiply**

First row: $0\cdot v_1+(-i)v_2=-iv_2$. Second row: $iv_1+0\cdot v_2=iv_1$. So

$$
\begin{pmatrix}-iv_2\\\\iv_1\end{pmatrix}
=
\begin{pmatrix}v_1\\\\v_2\end{pmatrix},
$$

which gives

$$
-iv_2=v_1 \qquad (1),
\qquad
iv_1=v_2 \qquad (2).
$$

**Step 3 — solve**

From (2), choose $v_1=1$ (any nonzero scale of an eigenvector is still an eigenvector). Then $v_2=i$:

$$
\boxed{v=\begin{pmatrix}1\\\\i\end{pmatrix}}.
$$

**Step 4 — verify**

$$
Y\begin{pmatrix}1\\\\i\end{pmatrix}
=
\begin{pmatrix}
0(1)+(-i)(i)\\\\
i(1)+0(i)
\end{pmatrix}
=
\begin{pmatrix}1\\\\i\end{pmatrix}.
$$

**Verified:** eigenvalue $+1$ with eigenvector $\begin{pmatrix}1\\\\i\end{pmatrix}$.

#### 4.6.5 Finding the eigenvector for $\lambda=-1$

Substitute $\lambda=-1$:

$$
Yv=-v.
$$

The vector should become its **negative** under $Y$.

**Step 1 — equation**

$$
\begin{pmatrix}0&-i\\\\i&0\end{pmatrix}
\begin{pmatrix}v_1\\\\v_2\end{pmatrix}
=
-\begin{pmatrix}v_1\\\\v_2\end{pmatrix}.
$$

**Step 2 — multiply**

$$
\begin{pmatrix}-iv_2\\\\iv_1\end{pmatrix}
=
\begin{pmatrix}-v_1\\\\-v_2\end{pmatrix},
$$

so $-iv_2=-v_1$ and $iv_1=-v_2$. From $iv_1=-v_2$, take $v_1=1$, then $v_2=-i$:

$$
\boxed{v=\begin{pmatrix}1\\\\-i\end{pmatrix}}.
$$

**Step 3 — verify**

$$
Y\begin{pmatrix}1\\\\-i\end{pmatrix}
=
\begin{pmatrix}(-i)(-i)\\\\i\end{pmatrix}
=
\begin{pmatrix}-1\\\\i\end{pmatrix},
$$

and

$$
-\begin{pmatrix}1\\\\-i\end{pmatrix}
=
\begin{pmatrix}-1\\\\i\end{pmatrix}.
$$

**Verified:** eigenvalue $-1$ with eigenvector $\begin{pmatrix}1\\\\-i\end{pmatrix}$.

#### 4.6.6 Why divide by $\sqrt{2}$?

The lecture often writes normalized eigenvectors as

$$
\frac{1}{\sqrt{2}}\begin{pmatrix}1\\\\i\end{pmatrix}
$$

instead of $\begin{pmatrix}1\\\\i\end{pmatrix}$.

In quantum computing, states are **normalized**: for $v=\begin{pmatrix}a\\\\b\end{pmatrix}$,

$$
|a|^2+|b|^2=1.
$$

For $\begin{pmatrix}1\\\\i\end{pmatrix}$, $|1|^2+|i|^2=1+1=2$. Divide both components by $\sqrt{2}$:

$$
\boxed{
v_+=\frac{1}{\sqrt{2}}
\begin{pmatrix}1\\\\i\end{pmatrix}
}.
$$

Then $\frac{1}{2}+\frac{1}{2}=1$. The same scaling applies to the $\lambda=-1$ eigenvector:

$$
\boxed{
v_-=\frac{1}{\sqrt{2}}
\begin{pmatrix}1\\\\-i\end{pmatrix}
}.
$$

#### 4.6.7 Final results: what did we discover?

| Eigenvalue | Normalized eigenvector | Effect of applying $Y$ |
| --- | --- | --- |
| $\lambda=+1$ | $v_+=\dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\\\i\end{pmatrix}$ | Leaves this state unchanged |
| $\lambda=-1$ | $v_-=\dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\\\-i\end{pmatrix}$ | Maps the state to its negative |

The recipe is the same as in §4.5: characteristic equation from $\det(Y-\lambda I)=0$, then $(Y-\lambda I)v=0$ for each $\lambda$. Only the arithmetic involves complex numbers.

**Check your understanding:** short quiz on the Y gate eigenvalues, eigenvectors, and $i$ arithmetic.

<!-- markdownlint-disable MD033 -->
<div class="demo-frame">
<iframe src="../animations/y-gate-quiz.html" title="Y gate — test your understanding" width="100%" height="720" loading="lazy" style="border:1px solid #dce3ef;border-radius:12px;max-width:100%;display:block;"></iframe>
</div>
<!-- markdownlint-enable MD033 -->

---

### 4.7 Rotation example: why do we need complex eigenvectors?

#### 4.7.1 First, what is the problem we are trying to solve?

Remember what an eigenvector means. For a transformation matrix $A$,

$$
Av=\lambda v.
$$

An eigenvector is a special vector whose direction stays along the **same line** through the origin after the transformation:

- The original arrow points in one direction.
- The transformed arrow stays on that line.
- Its length may change.
- It may reverse direction along the line.

**Question for this section:** what if the transformation is a **rotation**? Can we find eigenvectors for rotation?

We investigate that next — first with a concrete $90^\circ$ example, then with complex numbers.

#### 4.7.2 Imagine an arrow pointing to the right

Take a real arrow

$$
v=\begin{pmatrix}1\\\\0\end{pmatrix}
$$

(horizontal position $1$, vertical position $0$).

Rotate it **$90^\circ$ counterclockwise**. It points upward:

$$
\begin{pmatrix}1\\\\0\end{pmatrix}
\longrightarrow
\begin{pmatrix}0\\\\1\end{pmatrix}.
$$

The original arrow pointed right; the new arrow points up. They are **not** on the same line.

So this vector is **not** an eigenvector of a $90^\circ$ rotation.

#### 4.7.3 How does the rotation matrix do this?

A rotation by angle $\theta$ is represented by

$$
R_\theta=
\begin{pmatrix}
\cos\theta&-\sin\theta\\\\
\sin\theta&\cos\theta
\end{pmatrix}.
$$

For $90^\circ$: $\cos90^\circ=0$, $\sin90^\circ=1$, so

$$
R_{90^\circ}=
\begin{pmatrix}0&-1\\\\1&0\end{pmatrix}.
$$

Multiply by our arrow:

$$
R_{90^\circ}
\begin{pmatrix}1\\\\0\end{pmatrix}
=
\begin{pmatrix}
0(1)+(-1)(0)\\\\
1(1)+0(0)
\end{pmatrix}
=
\begin{pmatrix}0\\\\1\end{pmatrix}.
$$

**Could some other real arrow stay on its original line after a $90^\circ$ rotation?**

No. Every nonzero arrow in the plane turns by $90^\circ$ and ends up **perpendicular** to where it started.

So a $90^\circ$ rotation has **no nonzero real eigenvector**.

That is where we extend the story to **complex** vectors.

#### 4.7.4 What if we allow complex numbers?

So far we used real column vectors such as $\begin{pmatrix}1\\\\0\end{pmatrix}$.

In quantum computing, amplitudes can be complex, e.g.

$$
v=\begin{pmatrix}1\\\\i\end{pmatrix},
\qquad i^2=-1.
$$

Even though $90^\circ$ rotation has no real eigenvector, it **does** have complex eigenpairs. We find them with the same determinant recipe as in §4.4–§4.6.

#### 4.7.5 Find the eigenvalues of $R_{90^\circ}$

We already have

$$
R_{90^\circ}=
\begin{pmatrix}0&-1\\\\1&0\end{pmatrix}.
$$

Require

$$
\det(R_{90^\circ}-\lambda I)=0.
$$

Subtract $\lambda I$:

$$
R_{90^\circ}-\lambda I=
\begin{pmatrix}-\lambda&-1\\\\1&-\lambda\end{pmatrix}.
$$

Determinant:

$$
(-\lambda)(-\lambda)-(-1)(1)=\lambda^2+1=0,
$$

so $\lambda^2=-1$. Since $i^2=-1$,

$$
\boxed{\lambda=+i\quad\text{or}\quad\lambda=-i}.
$$

We could not get **real** eigenvalues here; allowing complex numbers gives two solutions.

#### 4.7.6 Find the eigenvectors

**Case A: $\lambda=+i$**

Start from $Rv=\lambda v$ with $R=R_{90^\circ}$:

$$
Rv=iv.
$$

Let $v=\begin{pmatrix}v_1\\\\v_2\end{pmatrix}$. Then

$$
\begin{pmatrix}0&-1\\\\1&0\end{pmatrix}
\begin{pmatrix}v_1\\\\v_2\end{pmatrix}
=
i\begin{pmatrix}v_1\\\\v_2\end{pmatrix},
$$

so

$$
\begin{pmatrix}-v_2\\\\v_1\end{pmatrix}
=
\begin{pmatrix}iv_1\\\\iv_2\end{pmatrix},
$$

giving $-v_2=iv_1$ and $v_1=iv_2$. Choose $v_1=1$: then $v_2=-i$,

$$
\boxed{v=\begin{pmatrix}1\\\\-i\end{pmatrix}}.
$$

**Verify:**

$$
R_{90^\circ}\begin{pmatrix}1\\\\-i\end{pmatrix}
=
\begin{pmatrix}i\\\\1\end{pmatrix},
\qquad
i\begin{pmatrix}1\\\\-i\end{pmatrix}
=
\begin{pmatrix}i\\\\-i^2\end{pmatrix}
=
\begin{pmatrix}i\\\\1\end{pmatrix}.
$$

So $R_{90^\circ}\begin{pmatrix}1\\\\-i\end{pmatrix}=i\begin{pmatrix}1\\\\-i\end{pmatrix}$.

**Case B: $\lambda=-i$**

Now $Rv=-iv$. The same multiplication gives $-v_2=-iv_1$. With $v_1=1$, $v_2=i$:

$$
\boxed{v=\begin{pmatrix}1\\\\i\end{pmatrix}}.
$$

**Check:**

$$
R_{90^\circ}\begin{pmatrix}1\\\\i\end{pmatrix}
=
\begin{pmatrix}-i\\\\1\end{pmatrix},
\qquad
-i\begin{pmatrix}1\\\\i\end{pmatrix}
=
\begin{pmatrix}-i\\\\-i^2\end{pmatrix}
=
\begin{pmatrix}-i\\\\1\end{pmatrix}.
$$

#### 4.7.7 How can a complex eigenvector “stay in the same direction”?

If you picture rotation on paper, every real arrow turns — so “same direction” sounds impossible.

A complex eigenvector is not just an arrow in the **real** $xy$-plane. The eigenvector condition is

$$
Rv=\lambda v:
$$

the output must be a **scalar multiple** of the input, and that scalar $\lambda$ may be **complex**.

For $v=\begin{pmatrix}1\\\\-i\end{pmatrix}$,

$$
R_{90^\circ}v=\begin{pmatrix}i\\\\1\end{pmatrix}=i\begin{pmatrix}1\\\\-i\end{pmatrix}.
$$

The two columns look different as real pictures, but they differ only by the factor $i$. That is exactly the definition of an eigenvector in $\mathbb{C}^2$.

We are not claiming an ordinary real arrow stays fixed on the page; we are claiming a **complex** linear relationship $Rv=\lambda v$.

#### 4.7.8 What does $e^{i\theta}$ mean?

**Euler's formula** (no derivation needed here):

$$
e^{i\theta}=\cos\theta+i\sin\theta.
$$

For $\theta=90^\circ$, $\cos90^\circ=0$, $\sin90^\circ=1$, so

$$
e^{i90^\circ}=i,
\qquad
e^{-i90^\circ}=-i.
$$

Our $90^\circ$ eigenvalues are $+i$ and $-i$ — the same numbers written in exponential form would be $e^{i\pi/2}$ and $e^{-i\pi/2}$.

For a **general** rotation $R_\theta$, the characteristic equation gives

$$
\det(R_\theta-\lambda I)=\lambda^2-2\lambda\cos\theta+1=0,
$$

$$
\boxed{\lambda=\cos\theta\pm i\sin\theta=e^{\pm i\theta}}.
$$

Eigenpairs for this convention (including $90^\circ$):

| Eigenvalue | Eigenvector (example) |
| --- | --- |
| $e^{i\theta}$ | $\begin{pmatrix}1\\\\-i\end{pmatrix}$ |
| $e^{-i\theta}$ | $\begin{pmatrix}1\\\\i\end{pmatrix}$ |

#### 4.7.9 What is the lesson?

**Real vectors in the plane**

- A $90^\circ$ rotation changes the direction of every nonzero **real** vector.
- There is no nonzero **real** eigenvector.

**Complex vectors**

$$
R_{90^\circ}\begin{pmatrix}1\\\\-i\end{pmatrix}=i\begin{pmatrix}1\\\\-i\end{pmatrix},
\qquad
R_{90^\circ}\begin{pmatrix}1\\\\i\end{pmatrix}=-i\begin{pmatrix}1\\\\i\end{pmatrix}.
$$

Two complex eigenpairs exist.

**Takeaways**

1. Not every real matrix has a **real** eigenvector.
2. Working over the complex numbers can produce eigenvalues and eigenvectors that do not exist using real numbers alone.
3. Quantum states use complex amplitudes, so this extension is standard — not optional decoration.

**Fact:** every $n\times n$ matrix with $n\ge1$ has at least one **complex** eigenvalue (and a corresponding nonzero complex eigenvector), counting multiplicities in the usual algebraic sense.

---

### 4.8 Eigenvalues of unitary matrices always have magnitude one

Quantum gates are **unitary** matrices: they preserve vector length, $\|Uv\|=\|v\|$.

Suppose $Uv=\lambda v$, where $v$ is an eigenvector and $\lambda$ its eigenvalue.

Because $U$ preserves length,

$$
\|Uv\|=\|v\|,
$$

but $Uv=\lambda v$, so

$$
\|\lambda v\|=\|v\|.
$$

Multiplying by $\lambda$ scales length by $|\lambda|$, hence

$$
|\lambda|\|v\|=\|v\|.
$$

Since $v\neq0$,

$$
\boxed{|\lambda|=1}.
$$

For real numbers, $| \lambda |=1$ means $\lambda=\pm1$ only.

For complex numbers, $|\lambda|^2=1$ is **not** the same as $\lambda^2=1$: $i$, $-i$, and $e^{i\theta}$ also lie on the unit circle.

**Key takeaway:** eigenvectors are special directions; eigenvalues describe scaling or phase along them. A unitary matrix cannot stretch or shrink eigenvector length — only rotate phase. That is why unitary quantum gates preserve normalized states.

---

### 4.9 Final summary: what have we learned?

**The process**

1. Start with $Av=\lambda v$.
2. Rearrange to $(A-\lambda I)v=0$.
3. Need $v\neq0$, so the matrix must be singular: $\det(A-\lambda I)=0$.
4. Solve for the eigenvalues $\lambda$.
5. For each $\lambda$, solve $(A-\lambda I)v=0$ for the eigenvectors $v$.

**Important concepts**

| Concept | Meaning |
| --- | --- |
| Eigenvector | A vector whose direction stays along the same line after transformation |
| Eigenvalue | The scaling factor $\lambda$ associated with that eigenvector |
| Singular matrix | A square matrix whose determinant is zero |
| Characteristic equation | $\det(A-\lambda I)=0$ |
| Complex eigenvalue | An eigenvalue that may involve $i$ |
| Unitary matrix | A matrix that preserves vector length |
| Unit magnitude | An eigenvalue with $\lvert\lambda\rvert=1$ |

**Big picture:** we started with $Bx=0$ and learned that a nonzero solution exists only when $\det(B)=0$. The eigenvector equation $Av=\lambda v$ becomes $(A-\lambda I)v=0$, so determinants discover eigenvalues first; then each eigenvalue gives its eigenvectors. That is the foundation for understanding how quantum gates transform quantum states.

---

## 5. Moving to quantum algorithms

The lecture now begins the central part of the course. The coming algorithms exploit behavior unavailable in the same form to ordinary classical queries. It previews **Deutsch**, **Deutsch–Jozsa**, and **Simon**, but this session works through Deutsch and only introduces the Deutsch–Jozsa problem. It also contrasts a small two-versus-one query improvement for Deutsch with a much larger classical-versus-quantum query separation for Deutsch–Jozsa.

**Extra explanation:** a *query* means one use of a provided black-box function. Query count is not the same thing as the total number of physical gates or total running time.

## 6. Review: many qubits, tensor products, gates and measurement

### 6.1 Why $n$ qubits need $2^n$ basis states

This review assumes you are seeing the multi-qubit picture for the first time.

**Main idea:** every time we add **one more qubit**, the number of possible **basis states** **doubles**. Below: what those states are, why $2^n$, and how the formulas describe amplitudes — without claiming one measurement reads them all.

#### 6.1.1 One qubit: two basis states

A classical bit is only $0$ or $1$.

A qubit has two basic states:

- $\lvert0\rangle$
- $\lvert1\rangle$

These are **basis states** — building blocks for richer quantum states.

| One qubit | |
| --- | --- |
| First basis state | $\lvert0\rangle$ |
| Second basis state | $\lvert1\rangle$ |
| **Total** | **2** basis states |

#### 6.1.2 Two qubits: four combinations

Each qubit is $0$ or $1$. List all pairs:

| First qubit | Second qubit | Combined state |
| --- | --- | --- |
| 0 | 0 | $\lvert00\rangle$ |
| 0 | 1 | $\lvert01\rangle$ |
| 1 | 0 | $\lvert10\rangle$ |
| 1 | 1 | $\lvert11\rangle$ |

Two choices for qubit 1, two for qubit 2:

$$
2\times 2=4.
$$

**Total = 4** basis states: $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$.

#### 6.1.3 Three qubits: double again

Take each two-qubit string and append $0$ or $1$:

| Previous | +0 | +1 |
| --- | --- | --- |
| 00 | 000 | 001 |
| 01 | 010 | 011 |
| 10 | 100 | 101 |
| 11 | 110 | 111 |

So

$$
2\times 2\times 2=8
$$

— eight basis strings from $\lvert000\rangle$ through $\lvert111\rangle$.

#### 6.1.4 General rule for $n$ qubits

| Number of qubits | Number of basis states |
| --- | --- |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| $n$ | $2^n$ |

Each extra qubit **doubles** the count. The general formula is

$$
\boxed{\text{Number of basis states}=2^n}.
$$

**Notation trap:** $2^n$ means “2 to the power $n$,” not $2n$ (twice $n$). Examples: $2^2=4$ for two qubits; $2^3=8$ for three; $2^{10}=1024$ for ten.

#### 6.1.5 The quantum state formula

An arbitrary $n$-qubit pure state is written

$$
\boxed{|\psi\rangle=\sum_{x\in\{0,1\}^n}\alpha_x|x\rangle}.
$$

**Meaning:** $|\psi\rangle$ can be a **superposition** of every $n$-bit basis string $\lvert x\rangle$, each with its own **amplitude** $\alpha_x$ (real or complex).

**Two-qubit example.** Basis states $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$:

$$
\begin{aligned}
|\psi\rangle={}&
\alpha_{00}|00\rangle\\
&+\alpha_{01}|01\rangle\\
&+\alpha_{10}|10\rangle\\
&+\alpha_{11}|11\rangle.
\end{aligned}
$$

| Basis state | Amplitude |
| --- | --- |
| $\lvert00\rangle$ | $\alpha_{00}$ |
| $\lvert01\rangle$ | $\alpha_{01}$ |
| $\lvert10\rangle$ | $\alpha_{10}$ |
| $\lvert11\rangle$ | $\alpha_{11}$ |

Equal superposition example:

$$
|\psi\rangle=
\frac{1}{2}|00\rangle+
\frac{1}{2}|01\rangle+
\frac{1}{2}|10\rangle+
\frac{1}{2}|11\rangle.
$$

All four amplitudes are equal. That is allowed only if probabilities still sum to 1 (next subsection).

#### 6.1.6 Normalization

Amplitudes must satisfy

$$
\boxed{\sum_x|\alpha_x|^2=1}.
$$

$|\alpha_x|^2$ is the **probability** of measuring basis label $x$.

For the equal example, each amplitude is $1/2$:

| Basis state | Amplitude | Probability |
| --- | --- | --- |
| $\lvert00\rangle$ | $1/2$ | $1/4$ (25%) |
| $\lvert01\rangle$ | $1/2$ | $1/4$ (25%) |
| $\lvert10\rangle$ | $1/2$ | $1/4$ (25%) |
| $\lvert11\rangle$ | $1/2$ | $1/4$ (25%) |

$$
\frac{1}{4}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}=1.
$$

Total probability must always be 100% for a valid state.

#### 6.1.7 One measurement does not reveal all amplitudes

Take the same two-qubit state:

$$
|\psi\rangle=
\frac12|00\rangle+
\frac12|01\rangle+
\frac12|10\rangle+
\frac12|11\rangle.
$$

**Before measurement:** four amplitudes are specified mathematically.

**After one measurement** in the computational basis you get **one** outcome — $\lvert00\rangle$, $\lvert01\rangle$, $\lvert10\rangle$, or $\lvert11\rangle$ — each with probability 25%. You do **not** see all four labels at once, and you do not “read out” the other amplitudes directly from that single shot.

That is why quantum algorithms apply **gates** to reshape amplitudes **before** measuring, so useful outcomes are more likely.

#### 6.1.8 Summary

1. **One qubit:** basis states $\lvert0\rangle,\lvert1\rangle$ (2 states).
2. **More qubits:** each added qubit **doubles** the basis count.
3. **State:** sum over all $\lvert x\rangle$ with amplitudes $\alpha_x$.
4. **Measurement:** one classical outcome per run, not a dump of all $2^n$ amplitudes.

Key formulas:

$$
\boxed{\text{Number of basis states}=2^n},
\qquad
\boxed{|\psi\rangle=\sum_{x\in\{0,1\}^n}\alpha_x|x\rangle},
\qquad
\boxed{\sum_x|\alpha_x|^2=1}.
$$

Ten qubits means $2^{10}=1024$ amplitudes in the **description** of $|\psi\rangle$ — not 1024 answers from **one** measurement. Keeping that distinction straight is central to quantum computing.

### 6.2 Separate gates on separate qubits

$$
(A\otimes B)(|u\rangle\otimes|v\rangle)=A|u\rangle\otimes B|v\rangle.
$$

The tensor-product symbol $\otimes$ means “combine systems or operators”; it is **not** ordinary addition. It says apply $A$ to the first qubit and $B$ to the second.

### 6.3 Hadamard, X and CNOT

$$
H|0\rangle=|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},\qquad H|1\rangle=|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
$$

Applying Hadamard twice returns the original state: $H^2=I$. The X gate flips $0\leftrightarrow1$. In bit notation, $X|b\rangle=|b\oplus1\rangle$, where $\oplus$ is **XOR** (addition modulo 2).

CNOT uses a **control** bit $a$ and **target** bit $b$:

$$
\mathrm{CNOT}|a,b\rangle=|a,b\oplus a\rangle.
$$

| Control $a$ | Target before $b$ | Target after $b\oplus a$ |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

CNOT **can** create entanglement, for example when its control is in superposition, but not for every input.

### 6.4 Measurement

If $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, measuring in the computational basis yields **one** result: $0$ with probability $|\alpha|^2$, or $1$ with probability $|\beta|^2$. We do not read out both amplitudes from a single measurement.

![Hadamard basis states](../images/concept-03.png)

## 7. Bit-string dot product and parity

The lecture is building a tool: **pick certain bits** from a binary string and ask whether the number of selected **1**s is **even** or **odd**.

That idea is called the **bit-string dot product (mod 2)**. It shows up constantly in the algorithms ahead.

### 7.1 Imagine three light bulbs

Suppose three bulbs; each is **ON** ($1$) or **OFF** ($0$).

Current state $x=111$:

| Bulb | State ($x$) |
| --- | --- |
| Bulb 1 | 1 (ON) |
| Bulb 2 | 1 (ON) |
| Bulb 3 | 1 (ON) |

Now a second string — a **selection mask**:

$$
s=101.
$$

- **1** in the mask → **select** that bulb.
- **0** in the mask → **ignore** that bulb.

### 7.2 What the mask does (example $s=101$, $x=111$)

| Position | Mask $s$ | Action | Bulb $x$ |
| --- | --- | --- | --- |
| 1 | 1 | **Select** | 1 |
| 2 | 0 | **Ignore** | 1 |
| 3 | 1 | **Select** | 1 |

We selected bulbs 1 and 3. Bulb 2 is ignored.

Among **selected** positions, the ON bits are $1$ and $1$. Count them:

$$
1+1=2.
$$

The lecture cares about **even vs odd**:

- even count → parity **0**
- odd count → parity **1**

Since $2$ is even,

$$
2\bmod 2=0.
$$

So for this pair,

$$
\boxed{s\cdot x=101\cdot111=0}.
$$

That boxed value is the whole definition in action.

### 7.3 Why multiply the bits?

For equal-length strings $s=s_1\dots s_n$ and $x=x_1\dots x_n$,

$$
\boxed{s\cdot x=(s_1x_1+s_2x_2+\cdots+s_nx_n)\bmod 2}.
$$

Multiplication is how the mask **selects**: $s_ix_i=0$ whenever $s_i=0$, so that position contributes nothing.

| Mask $s_i$ | Bulb $x_i$ | Product $s_ix_i$ | Meaning |
| --- | --- | --- | --- |
| 1 | 1 | $1$ | Selected and ON |
| 1 | 0 | $0$ | Selected but OFF |
| 0 | 1 | $0$ | Ignored |
| 0 | 0 | $0$ | Ignored |

**Other checks:** $s=111$, $x=111$ gives $(1+1+1)\bmod 2=1$ (odd). Communication systems use the same “count 1s mod 2” idea for simple parity.

### 7.4 Try it step by step (default example)

Walk through the logic you would get from toggling bits:

**Step 1 — choose mask $s$** (tap each bit to flip $0\leftrightarrow 1$). Start with $s=101$.

**Step 2 — choose input $x$**. Start with $x=111$.

**Step 3 — read the outcome**

| Quantity | Value |
| --- | --- |
| Mask $s$ | $101$ |
| Input $x$ | $111$ |
| Selected products $s_ix_i$ | $1,0,1$ → selected ON count from positions 1 and 3 → two 1s |
| Number of selected 1s | $2$ |
| **Parity** | **0 — EVEN** ($2\bmod 2=0$) |

Change $s$ or $x$ and repeat: only positions with $s_i=1$ matter; parity is the sum of those $x_i$ taken mod 2.

### 7.5 Two identities used later

**Identity 1 — parity distributes over XOR**

$$
s\cdot(x\oplus y)=(s\cdot x)\oplus(s\cdot y).
$$

Here $\oplus$ is **XOR** ($0\oplus0=0$, $0\oplus1=1$, $1\oplus0=1$, $1\oplus1=0$).

You can either XOR $x$ and $y$ first and then take masked parity, or take masked parity of each and XOR the two answers. **Same result** — handy for rearranging algorithm steps.

**Identity 2 — XOR as a product of signs**

$$
(-1)^{a\oplus b}=(-1)^a(-1)^b,
\qquad a,b\in\{0,1\}.
$$

| $a$ | $b$ | $a\oplus b$ | $(-1)^{a\oplus b}$ | $(-1)^a(-1)^b$ |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | $+1$ | $+1$ |
| 0 | 1 | 1 | $-1$ | $-1$ |
| 1 | 0 | 1 | $-1$ | $-1$ |
| 1 | 1 | 0 | $+1$ | $+1$ |

Quantum formulas often use $(-1)^{s\cdot x}$:

- parity $0$ → $(-1)^0=+1$
- parity $1$ → $(-1)^1=-1$

**Why identity 2 helps:** if both bits are 1, XOR is 0 so the left side is $+1$, and $(-1)(-1)=+1$ on the right. If exactly one bit is 1, both sides are $-1$. For exponents of $-1$, adding or removing an **even** integer to the exponent does not change the sign.

### 7.6 Why this matters for quantum algorithms

This is not “just” even/odd counting. Many algorithms need to:

1. Take a binary input $x$.
2. Select positions using a mask $s$.
3. Compute parity of the selected 1s ($s\cdot x$).
4. Turn that bit into a **phase** $\pm1$ via $(-1)^{s\cdot x}$.

**Remember in one sentence:** the bit-string dot product **selects** bits with the mask, **counts** how many selected bits are 1, and reports whether that count is **even (0)** or **odd (1)**. Once that picture is clear, the notation is much less scary.

**Check yourself:** $s=1011$, $x=1101$. Selected positions are 1, 3, and 4 with values $(1,0,1)$, so the sum of selected 1s is $2$ and **parity is 0**.

---

## 8. A reversible black-box function $U_f$

### 8.1 What is a black box?

Imagine a machine with an input slot and an output display. You know that entering $x$ gives $f(x)$, but you do not know or need to inspect the machine's internal implementation. In algorithm analysis we assume we can **query** this function.

A quantum operation cannot generally erase the input and replace it with $f(x)$ because it must be reversible. Instead, the lecturer uses

$$
\boxed{U_f|x\rangle|y\rangle=|x\rangle|y\oplus f(x)\rangle}.
$$

Here $x$ can contain $n$ bits, $y$ is **one** bit, and $f(x)$ is **one** bit. The first register is unchanged; the second is XORed with the function result. This defines the oracle's action on basis states and extends linearly to superpositions.

### 8.2 Example: $f(x)=s\cdot x$ with $s=101$

Let $x=x_1x_2x_3$. Since $s=101$,

$$
f(x)=x_1\oplus x_3.
$$

We want the target to become $y\oplus x_1\oplus x_3$. Use **two CNOTs**: one controlled by $x_1$, then one controlled by $x_3$. We do nothing with $x_2$.

![Two CNOTs implement a parity oracle](../images/concept-02.png)

Example input $x=110$, $y=0$: first CNOT toggles $y:0\to1$; third-bit control is 0, so the second CNOT does nothing. Output is $|110\rangle|1\rangle$, since $f(110)=1$.

**Interactive:** [Oracle circuit step-by-step](../animations/animation-02.html).

### 8.3 Four one-bit function examples

| Function $f(x)$ | Required change to target | Simple circuit |
|---|---|---|
| Always 0 | $y\to y$ | Identity / no gate |
| Always 1 | $y\to y\oplus1$ | X on target |
| $f(x)=x$ | $y\to y\oplus x$ | CNOT |
| $f(x)=1\oplus x$ | $y\to y\oplus x\oplus1$ | CNOT then X on target |

In response to a question, the lecture revisits the last example: **CNOT** adds the input bit to the target modulo 2, and **X** adds the extra 1 by flipping the target.

### 8.4 Why the oracle can be reversed

Apply it twice:

$$
|x,y\rangle\xrightarrow{U_f}|x,y\oplus f(x)\rangle\xrightarrow{U_f}|x,y\oplus f(x)\oplus f(x)\rangle=|x,y\rangle.
$$

A bit XORed with itself is zero: $b\oplus b=0$. Therefore $\boxed{U_f^2=I}$, so the oracle is its own inverse. As a permutation of computational-basis states, it is unitary.

## 9. Phase kickback: turning function values into signs

This is the lecturer's next central idea. So far the function changed the **target bit**. Now we want $f(x)$ to change the **sign of the amplitude of $|x\rangle$**.

### 9.1 Prepare the minus state

$$
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
$$

Apply the oracle to $|x\rangle|-\rangle$. Expand the second register first:

$$
U_f(|x\rangle|-\rangle)=\frac1{\sqrt2}\big(U_f|x,0\rangle-U_f|x,1\rangle\big).
$$

Now use the definition of $U_f$:

$$
=\frac1{\sqrt2}\left(|x,f(x)\rangle-|x,1\oplus f(x)\rangle\right).
$$

There are only two cases:

- If $f(x)=0$: output is $|x\rangle(|0\rangle-|1\rangle)/\sqrt2=|x\rangle|-\rangle$.
- If $f(x)=1$: output is $|x\rangle(|1\rangle-|0\rangle)/\sqrt2=-|x\rangle|-\rangle$.

Both cases fit one equation:

$$
\boxed{U_f(|x\rangle|-\rangle)=(-1)^{f(x)}|x\rangle|-\rangle}.
$$

The minus-state register ends up **unchanged**; the input register gains a sign determined by $f(x)$. This is called **phase kickback**.

### 9.2 Why a sign can matter

A minus sign multiplying an entire isolated quantum state is an unobservable **global phase**. But if the input is a superposition,

$$
\sum_x\alpha_x|x\rangle\quad\longrightarrow\quad\sum_x(-1)^{f(x)}\alpha_x|x\rangle,
$$

then *different components* can receive different signs. These **relative phases** can affect later interference and measurements. That is the algorithmic advantage. It is not that a single sign is directly measurable.

**Interactive:** [Phase kickback and relative sign explorer](../animations/animation-03.html).

### 9.3 The eigenvector connection

The lecture notes that $X|-\rangle=-|-\rangle$: the minus state is an eigenvector of the X gate with eigenvalue $-1$. In the oracle, $f(x)=1$ means “apply X to the target,” so the eigenvalue $-1$ is kicked back as a phase. Later, more general controlled unitaries can kick back other eigenvalue phases. That deeper theory is explicitly postponed.

## 10. Compact Hadamard notation for one bit

The lecture now introduces a formula that will recur in the algorithms.

$$
H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},\qquad H|1\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
$$

Both can be written as

$$
\boxed{H|b\rangle=\frac1{\sqrt2}\sum_{z\in\{0,1\}}(-1)^{bz}|z\rangle}.
$$

Read the notation slowly: $b$ is the input bit; $z$ is the output-basis label, taking values 0 and 1; $\sum$ means “add both terms”; $(-1)^{bz}$ determines the sign.

| Input $b$ | Output term $z$ | $bz$ | Sign $(-1)^{bz}$ |
|---|---|---|---|
| 0 | 0 | 0 | + |
| 0 | 1 | 0 | + |
| 1 | 0 | 0 | + |
| 1 | 1 | 1 | − |

Only the $b=z=1$ combination produces a minus sign. The transcript has a couple of spoken slips (“both terms zero”); the table and equations above show the intended rule.

## 11. Hadamard on two, three, then $n$ qubits

### 11.1 Two qubits: expand the tensor product

$$
H^{\otimes2}|x_1x_2\rangle=(H|x_1\rangle)\otimes(H|x_2\rangle).
$$

Using the one-bit rule:

$$
=\frac12\left(|00\rangle+(-1)^{x_2}|01\rangle+(-1)^{x_1}|10\rangle+(-1)^{x_1+x_2}|11\rangle\right).
$$

The 1/2 comes from $(1/\sqrt2)(1/\sqrt2)$. There are four terms because each of two qubits has two choices. The sign for $|01\rangle$ checks $x_2$, for $|10\rangle$ checks $x_1$, and for $|11\rangle$ checks the parity of both.

### 11.2 Three qubits: predict signs without multiplying everything

For output label $z=101$, the sign depends on $x_1\oplus x_3$. For $z=011$, it depends on $x_2\oplus x_3$. This is exactly the bit-string dot product introduced earlier:

$$
x\cdot z=(x_1z_1+x_2z_2+x_3z_3)\bmod2.
$$

There are eight output terms and the common factor is $1/\sqrt8$.

### 11.3 The general Hadamard identity

$$
\boxed{H^{\otimes n}|x\rangle=\frac1{\sqrt{2^n}}\sum_{z\in\{0,1\}^n}(-1)^{x\cdot z}|z\rangle}.
$$

**Decode every part:** $H^{\otimes n}$ means apply H independently to each of $n$ qubits; $x$ is the input bit string; $z$ runs through all $2^n$ output strings; $x\cdot z$ computes selected-bit parity; the sign is + for even parity and − for odd; every basis state has amplitude magnitude $1/\sqrt{2^n}$.

**Why the formula works:** multiply the $n$ individual expansions $H|x_j\rangle=2^{-1/2}\sum_{z_j}(-1)^{x_jz_j}|z_j\rangle$. The $n$ normalization factors multiply to $2^{-n/2}$. The signs multiply to $(-1)^{\sum_jx_jz_j}$, which is the same as $(-1)^{x\cdot z}$. The tensor products of the $|z_j\rangle$ form $|z\rangle$.

The lecturer says this can later be understood as a change between orthonormal bases and connected to the Fourier transform; those interpretations are deferred.

### 11.4 Worked example: $H^{\otimes2}|10\rangle$

Take $x=10$ and enumerate output strings:

| $z$ | $x\cdot z$ | Sign |
|---|---|---|
| 00 | 0 | + |
| 01 | 0 | + |
| 10 | 1 | − |
| 11 | 1 | − |

Therefore

$$
\boxed{H^{\otimes2}|10\rangle=\tfrac12(|00\rangle+|01\rangle-|10\rangle-|11\rangle)}.
$$

Cross-check: $H|1\rangle\otimes H|0\rangle=|-\rangle\otimes|+\rangle$, which expands to the same answer.

### 11.5 Worked example: $H^{\otimes3}|110\rangle$

Here $x\cdot z=z_1\oplus z_2$. The third input bit is zero, so $z_3$ does not affect the sign.

| $z$ | Parity $z_1\oplus z_2$ | Sign |
|---|---|---|
| 000 | 0 | + |
| 001 | 0 | + |
| 010 | 1 | − |
| 011 | 1 | − |
| 100 | 1 | − |
| 101 | 1 | − |
| 110 | 0 | + |
| 111 | 0 | + |

$$
H^{\otimes3}|110\rangle=\frac1{\sqrt8}(|000\rangle+|001\rangle-|010\rangle-|011\rangle-|100\rangle-|101\rangle+|110\rangle+|111\rangle).
$$

**Interactive:** [Hadamard sign explorer for 1–3 qubits](../animations/animation-04.html). Change the input bits and inspect each output's parity and sign.

## 12. A useful parity-sum identity

The lecture next considers the sum

$$
S(a)=\sum_{x\in\{0,1\}^n}(-1)^{a\cdot x}.
$$

The mask $a$ is **fixed**, while $x$ runs through **all** $2^n$ bit strings. There are two cases:

$$
\boxed{S(a)=\begin{cases}2^n,&a=00\cdots0,\\\\0,&a\ne00\cdots0.\end{cases}}
$$

### 12.1 Why the zero mask gives $2^n$

If $a=0\cdots0$, then $a\cdot x=0$ for every $x$. Each term is $(-1)^0=+1$. Add $2^n$ ones and get $2^n$.

### 12.2 Why every nonzero mask gives zero

Take $a=10$ for two bits. The strings $x=00,01,10,11$ give signs $+,+,-,-$, whose sum is zero. For $a=11$, signs are $+,-,-,+$, also zero.

**General argument:** if any bit of $a$, say $a_j$, equals 1, pair each input $x$ with the input obtained by flipping $x_j$. Their parities differ by one, so one contributes +1 and the other −1. Every pair cancels. Thus exactly half the strings give even parity and half odd parity, **provided $a\ne0$**.

This identity is a mathematical version of **destructive interference**: equal numbers of + and − amplitudes cancel when added. The lecturer revisits it after a student asks why the sum is zero, emphasizing that the mask selects positions and the balance applies over all possible inputs, not necessarily to any arbitrary small sample.

**Check your understanding:** with $n=4$, $a=0000$, the sum is 16; with $a=0010$, it is 0.

## 13. Deutsch's problem: one query instead of two

### 13.1 State the problem first

We are given a black-box function $f:\{0,1\}\to\{0,1\}$. There are four possible functions:

| $f(0)$ | $f(1)$ | Type | XOR $f(0)\oplus f(1)$ |
|---|---|---|---|
| 0 | 0 | Constant | 0 |
| 1 | 1 | Constant | 0 |
| 0 | 1 | Different outputs / balanced | 1 |
| 1 | 0 | Different outputs / balanced | 1 |

We only want to know **whether the outputs match**, not their individual values. A deterministic classical algorithm must check both $f(0)$ and $f(1)$: **two queries** in the worst case. Deutsch's quantum circuit uses **one query to $U_f$**.

### 13.2 The circuit in lecture order

Start with two qubits $|0\rangle|1\rangle$. Apply H to both; call $U_f$ once; apply H to the **first** qubit only; measure the first qubit.

![Deutsch circuit sequence](../images/concept-04.png)

### 13.3 Step 1: prepare superposition and the minus state

$$
(H\otimes H)|0,1\rangle=|+\rangle|-\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes\frac{|0\rangle-|1\rangle}{\sqrt2}.
$$

The first qubit contains both basis components. The second is prepared in $|-\rangle$ specifically to enable phase kickback.

### 13.4 Step 2: query the oracle once

Use the phase-kickback identity separately on the $|0\rangle$ and $|1\rangle$ terms:

$$
U_f(|+\rangle|-\rangle)=\frac{(-1)^{f(0)}|0\rangle+(-1)^{f(1)}|1\rangle}{\sqrt2}\otimes|-\rangle.
$$

If $f(0)=f(1)$, both signs match: the first register is $|+\rangle$, possibly multiplied by a global minus. If they differ, the signs oppose: it is $|-\rangle$, possibly multiplied by a global minus. The second register remains $|-\rangle$.

### 13.5 Step 3: convert the sign difference into a measurable bit

Because $H|+\rangle=|0\rangle$ and $H|-\rangle=|1\rangle$, applying H to the first qubit yields:

$$
\boxed{\text{Measure }0\iff f(0)=f(1),\qquad\text{Measure }1\iff f(0)\ne f(1).}
$$

Equivalently, the measured bit is $f(0)\oplus f(1)$. For this promised problem, the outcome is **certain**, not merely more likely.

**Interactive:** [Run Deutsch's algorithm for all four functions](../animations/animation-05.html).

### 13.6 Why it works: interference, not reading both values

For any $a_0|0\rangle+a_1|1\rangle$,

$$
H(a_0|0\rangle+a_1|1\rangle)=\frac{(a_0+a_1)|0\rangle+(a_0-a_1)|1\rangle}{\sqrt2}.
$$

In Deutsch's algorithm, $a_0=(-1)^{f(0)}/\sqrt2$ and $a_1=(-1)^{f(1)}/\sqrt2$. If their signs match, $a_0-a_1=0$, so the $|1\rangle$ amplitude cancels. If their signs differ, $a_0+a_1=0$, so the $|0\rangle$ amplitude cancels.

**Important misconception:** quantum interference cancels **amplitudes**, which may be negative or complex. Classical probabilities themselves are nonnegative and cannot cancel this way. The algorithm does **not** reveal both $f(0)$ and $f(1)$; it reveals the property we asked for.

**Key takeaway:** superposition lets the oracle attach different phases to components; the final Hadamard makes those relative phases interfere into a definite answer.

## 14. Deutsch–Jozsa: the next problem, introduced before the break

This session ends by motivating the next algorithm. This is the **problem statement and classical query argument only**. The quantum circuit and proof are left for the next session.

### 14.1 A function of $n$ bits

Now $f:\{0,1\}^n\to\{0,1\}$. There are $2^n$ possible inputs. We are **promised** that $f$ belongs to one of two categories:

- **Constant:** every input returns the same output (all 0 or all 1).
- **Balanced:** exactly half the inputs return 0 and half return 1.

We need only identify which category applies. The promise matters: functions with, for example, 30 zeros and 2 ones when $n=5$ are excluded.

### 14.2 Why the deterministic classical worst case needs many queries

Suppose we have already queried $2^{n-1}$ different inputs and every output was 0. It might be a constant-zero function, **or** a balanced function whose zero outputs happen to be precisely the inputs checked so far. We cannot yet decide. One more query resolves the worst-case ambiguity: if it is 1, the function is balanced; if it is 0, a balanced function is no longer possible.

$$
\boxed{\text{Worst-case deterministic classical queries}=2^{n-1}+1.}
$$

The lecturer initially says $2^{n-1}$ informally, then clarifies the exact **plus one** using an example.

### 14.3 Five-bit example

If $n=5$, there are $2^5=32$ inputs. Under the promise, the outputs are either all identical or split into **16 zeros and 16 ones**. After 16 identical outputs, both cases are still possible. On the **17th** distinct query, we can finally decide in the worst case. The upcoming Deutsch–Jozsa quantum algorithm will use **one oracle query**, but its implementation and proof are **not covered in this transcript**.

### 14.4 How this connects back to Deutsch

When $n=1$, “balanced” means one zero and one one. That is precisely Deutsch's problem. Deutsch–Jozsa is presented as a natural extension before the break.

## 15. End-of-lecture review

| Concept | What you should now be able to explain |
|---|---|
| Eigenvectors | Why $Av=\lambda v$ means a special nonzero direction |
| Determinant test | Why $\det(A-\lambda I)=0$ finds eigenvalues |
| Unitary matrices | Why their eigenvalues have $\lvert\lambda\rvert=1$ |
| Bit parity | How $s\cdot x$ selects bits and checks even/odd parity |
| Oracle $U_f$ | Why it uses $y\oplus f(x)$ and is reversible |
| Phase kickback | Why $\lvert-\rangle$ turns $f(x)$ into $(-1)^{f(x)}$ |
| Hadamard identity | Why output signs depend on $x\cdot z$ |
| Parity sum | Why nonzero masks produce cancellation |
| Deutsch | Why one oracle call distinguishes constant vs balanced for one-bit inputs |
| Deutsch–Jozsa | What its promise is and why classical worst case is $2^{n-1}+1$ |

### Short practice questions (with answers)

1. **Is $v=0$ an eigenvector?** No, by definition an eigenvector must be nonzero.
2. **What does $\lambda=-1$ mean?** The vector reverses direction without changing length.
3. **For $s=101$, which bits matter?** First and third.
4. **What does $U_f$ do to $|x,0\rangle$?** It gives $|x,f(x)\rangle$.
5. **What does $U_f$ do twice?** Returns the original input.
6. **What is the amplitude sign for $x=10,z=11$ in the Hadamard formula?** Minus, since $x\cdot z=1$.
7. **Why is $|-\rangle$ useful?** It is an X eigenstate with eigenvalue −1, allowing phase kickback.
8. **What does Deutsch output for $f(0)=1,f(1)=0$?** Measurement 1.
9. **For $n=5$, how many deterministic classical oracle queries can be needed for Deutsch–Jozsa?** 17.

## 16. Transcript verification and editorial notes

These are **identified transcription slips or statements requiring qualification**, not silent alterations:

- A general $m\times n$ matrix maps an $n$-vector to an **$m$-vector**, not necessarily an $n$-vector.
- For $A=\bigl(\begin{smallmatrix}2&1\\\\1&2\end{smallmatrix}\bigr)$, $A(1,1)^T=(3,3)^T$, not $(3,1)^T$.
- The eigenvector is $v$; $\lambda$ is the eigenvalue. The transcript occasionally interchanges the words.
- A set of **all eigenvectors plus zero** is a subspace; zero itself is not an eigenvector.
- For a unitary eigenvalue the correct condition is $|\lambda|^2=1$, not $\lambda^2=1$ in general.
- Every square matrix has a **complex** eigenvalue; a real matrix need not have a **real** eigenvalue.
- The parity-balance identity has the explicit exception $a=0$.
- The Deutsch measurement yields 0 for **equal** function values and 1 for **different** values; some spoken sentences near the end reverse or truncate that distinction.
- The exact deterministic classical worst-case Deutsch–Jozsa bound is $2^{n-1}+1$, not merely $2^{n-1}$.
- Names such as “Doish Joshua” and “phase feedback” in the speech recognition have been rendered as **Deutsch–Jozsa** and **phase kickback** where the context is clear.

**Source boundary:** no slides were supplied with this request. Diagram choices, clarifying examples, and any corrections are based on the transcript plus explicitly marked mathematical explanation; unclear slide-only details have not been invented.
