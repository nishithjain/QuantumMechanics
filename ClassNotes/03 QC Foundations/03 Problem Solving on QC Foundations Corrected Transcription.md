# Problem Solving on Quantum Computing Foundations — Corrected Lecture Transcription

**Lecture:** Linear Algebra for Quantum Computing — Linear Maps, Eigenvalues, Tensor Products  
**Professor:** Amit Kumar, Department of Computer Science and Engineering, IIT Delhi  
**Lecture date on slides:** 25 October 2026  
**Sources:** `03 Problem Solving on QC Foundations.txt` and `03 Problem Solving on QC Foundations Slides.pdf`

> **Editorial scope.** This is an edited **transcription**, not a new set of study notes. Repeated fillers, broken sentences, and obvious automatic-transcription errors have been cleaned up; the teaching sequence, main examples, mathematical reasoning, and questions have been retained. Equations and technical names have been restored where the spoken context establishes them. Student questions are sometimes **paraphrased** because the original transcription primarily captures the professor repeating or answering them. Mathematical corrections are noted separately when necessary, rather than silently treating a slip as a statement made accurately in the lecture.
>
> **Slide coverage limitation.** The attached PDF has 26 PDF pages but ends with the material numbered **12/49** in its slide footer, on *Matrix Entries as Inner Products*. The remainder of the transcript—including compositions, projectors, adjoints, Hermitian matrices, invertibility, and unitarity—is preserved from the **transcription only**. Those passages have not been checked against missing slides. We have not invented any material from slides 13–49.
>
> **Notation:** $|0\rangle,|1\rangle$ are *kets* (qubit basis states); $\langle u,v\rangle=u^\dagger v$ denotes the complex inner product; $A^\dagger$ means conjugate transpose; $\alpha,\beta$ are generally **complex**, so probabilities are $|\alpha|^2$ and $|\beta|^2$, not ordinary $\alpha^2,\beta^2$.

---

## 1. Opening questions: Where is the quantum advantage?

**Student question (paraphrased):** In a classical setting with two bits, there can be four possible outcomes. After one query, perhaps the possible outcomes are reduced to two. In the quantum case, if we make one query and then measure, don't we again get two possible outcomes? Where is the quantum advantage?

**Professor:** That is a very good question. You're right that when you measure one qubit, you see an outcome for that qubit. We will come to the distinction gradually. One of the important ideas is **entanglement**.

So far, you may have seen a situation where you measure one qubit and get to know its state, but you do not automatically know the state of another. However, you can create **entangled** two-qubit states in which the measurement outcomes are correlated. For example, there are states for which, if both qubits are measured in the same specified basis, the results will agree: if one result is 0, the other is 0, and if one result is 1, the other is 1.

Imagine two people each taking one of two coins, travelling far apart, and observing correlated outcomes. That gives a rough intuition for the correlation we are discussing. We will define entanglement formally later. Making many qubits interact coherently and become entangled in a controlled fashion is one reason quantum computers are difficult to build. Creating entanglement between two qubits is one thing; managing large numbers of qubits is much harder.

**Editorial clarification:** Correlated classical coins are only an analogy; ordinary correlation alone does **not** establish quantum entanglement. Entanglement does not enable instantaneous communication. Also, a quantum speedup is not explained solely by the fact that two entangled measurements are correlated; the algorithms and interference effects matter as well.

## 2. Questions about bases and changing coordinates

**Student question (paraphrased):** To check whether vectors form a basis, do we need to check that they are orthogonal? You previously mentioned that not all bases are orthogonal.

**Professor:** That is correct. Not every basis is orthogonal. In quantum computing, however, we will usually work with **orthonormal bases**. They are convenient because coordinates can be calculated by taking inner products.

**Student question (paraphrased):** I want to understand the idea of a basis intuitively. What is the point of changing the basis?

**Professor:** The intuition is that an object can look complicated in one coordinate system and much simpler in another. Think about an image. If you record all its pixel values and brightness information directly, the representation can be complicated. In engineering, changing to another basis can sometimes simplify that representation.

Or a vector might have coordinates such as $(2,3,4)$ in one basis and $(1,0,0)$ in another. We have not changed the underlying vector; we have changed how we describe it. **Changing the axes changes the coordinates.** When you choose the right basis, a calculation or measurement can become simpler and more meaningful.

The standard basis and the Hadamard basis are two examples, but they are certainly not the only possible bases. You need not memorize names without understanding. I encourage you to work through the exercises because that is how these ideas become familiar.

**Class logistics:** The professor initially could not share the screen; after sharing was enabled, he began the main lecture.

**Professor:** Today I will go slowly and revisit a few concepts from the previous lecture, then connect them. Feel free to ask questions in the chat or speak up.

**Short exchange on complex numbers:** A question is raised about De Moivre's theorem and powers or roots of a complex number. The discussion refers to writing a complex number in polar or exponential form and then working with powers or roots.

**Mathematical notation restored:** Euler's formula is $e^{i\theta}=\cos\theta+i\sin\theta$. De Moivre's theorem states $(\cos\theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta)$ for integer $n$. The original speech conflates the names briefly; the exact problem posed by the student is not fully recoverable from the transcript.

---

## 3. Recap: Vectors, complex inner products, and orthonormal bases

**Slides:** *Recap: What We Already Have* (PDF page 2, slide 2/49).

**Professor:** Let us recap. We talked about vectors. We will mainly use **column vectors**. A vector in $\mathbb{C}^n$ is a list of $n$ complex numbers:

$$
\mathbf v=\begin{pmatrix}v_1\\v_2\\\vdots\\v_n\end{pmatrix},\qquad v_j\in\mathbb C.
$$

We also defined the inner product of two complex vectors. You take the **complex conjugate of the first vector** and multiply corresponding entries:

$$
\langle\mathbf u,\mathbf v\rangle
=\mathbf u^\dagger\mathbf v
=\sum_{j=1}^{n}\overline{u_j}\,v_j.
$$

Why take the complex conjugate? In particular, we want the inner product of a vector with itself to give the **square of its length**:

$$
\langle\mathbf v,\mathbf v\rangle
=\sum_j|v_j|^2=\|\mathbf v\|^2.
$$

The dagger symbol $\dagger$ means **transpose and complex conjugate**. A column vector becomes a row vector, with the entries conjugated.

Next, we discussed an **orthonormal basis**. Think of basis vectors as axes. *Ortho-* means they are mutually perpendicular, and *normal* means that every basis vector has length 1. For example, in three-dimensional real space:

$$
\mathbf e_1=(1,0,0)^T,\qquad
\mathbf e_2=(0,1,0)^T,\qquad
\mathbf e_3=(0,0,1)^T.
$$

But we do not have to use these particular axes. We can rotate the axes and choose a different orthonormal basis. If I give you a vector $\mathbf p$, you can project it onto each basis direction to obtain its coordinates.

If $\{\mathbf e_1,\mathbf e_2\}$ is an orthonormal basis, then

$$
\mathbf p=\alpha_1\mathbf e_1+\alpha_2\mathbf e_2,
\qquad
\alpha_j=\langle\mathbf e_j,\mathbf p\rangle.
$$

This is what makes orthonormal bases so useful: **the coordinate along a basis vector is found by taking an inner product with that basis vector.**

### 3.1 Standard basis and Hadamard basis

**Professor:** In two dimensions, the **standard basis** is

$$
\mathbf e_1=\begin{pmatrix}1\\0\end{pmatrix},\qquad
\mathbf e_2=\begin{pmatrix}0\\1\end{pmatrix}.
$$

Both vectors have length 1, and they are perpendicular. Now suppose I choose two axes at 45 degrees to the original coordinate directions. These new basis vectors are called the **Hadamard basis**:

$$
\mathbf h_+=\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},
\qquad
\mathbf h_-=\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

They are still orthonormal. In this real two-dimensional picture, the new axes are diagonal directions; remember that the full quantum-computing setting is $\mathbb C^2$. A pair of complex numbers generally needs four real coordinates to write out, so a simple two-dimensional sketch is only an aid to intuition.

Suppose a point has standard-basis coordinates $(4,5)$. We can also write the same point as

$$
\mathbf p=4\mathbf e_1+5\mathbf e_2
=\alpha_+\mathbf h_++\alpha_-\mathbf h_-.
$$

How do we obtain $\alpha_+$ and $\alpha_-$? We take inner products:

$$
\alpha_+=\langle\mathbf h_+,\mathbf p\rangle
=\frac{4+5}{\sqrt2}=\frac9{\sqrt2},
$$

$$
\alpha_-=\langle\mathbf h_-,\mathbf p\rangle
=\frac{4-5}{\sqrt2}=-\frac1{\sqrt2}.
$$

Therefore, in the Hadamard basis, the coordinates of the same point are

$$
\left(\frac9{\sqrt2},-\frac1{\sqrt2}\right).
$$

Nothing happened to the point itself. **Only its coordinates changed**, because we changed the basis.

The inner-product rule relies on orthonormality. For a general non-orthonormal basis, these simple inner products do not directly give the expansion coefficients.

**Student question (paraphrased):** Where does this idea appear in quantum computing?

**Professor:** In quantum computing, we write the two standard basis vectors as $|0\rangle$ and $|1\rangle$. When we **measure** a qubit, the choice of orthonormal basis matters. The measurement tells us which of the basis outcomes occurred, and the post-measurement state depends on that outcome. We will return to this in a moment.

---

## 4. A single qubit is a unit vector in $\mathbb C^2$

**Slides:** *A Single Qubit Is a Vector in $\mathbb C^2$* (PDF pages 3–4, slide 3/49).

**Professor:** In a classical bit, there are two possible values, 0 or 1. For a qubit, the corresponding **basis states** are

$$
|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},\qquad
|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}.
$$

We are just changing the notation: $\mathbf e_1$ becomes $|0\rangle$, and $\mathbf e_2$ becomes $|1\rangle$. A general qubit is a vector in $\mathbb C^2$:

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle
=\begin{pmatrix}\alpha\\\beta\end{pmatrix},
\qquad\alpha,\beta\in\mathbb C.
$$

The condition is that the length of this vector must be **1**:

$$
|\alpha|^2+|\beta|^2=1.
$$

**Student question (paraphrased):** What does the state $|0\rangle$ mean here?

**Professor:** Its coordinates are $(1,0)$. In other words,

$$
|0\rangle=1\cdot|0\rangle+0\cdot|1\rangle.
$$

The notation $|\psi\rangle$ is a **ket**: it denotes a quantum state vector. You will see this notation throughout quantum computing. For now, just become comfortable reading it.

Can you have $|0\rangle+|1\rangle$ as a qubit state exactly as written? No, because its squared length is $2$, not $1$. But you *can* have

$$
|\psi\rangle=\frac1{\sqrt2}|0\rangle
+\frac1{\sqrt2}|1\rangle.
$$

That is a normalized state. We say that the qubit is in a **superposition** of $|0\rangle$ and $|1\rangle$. Here, *superposition* means a linear combination of the two basis states; the coefficients $\alpha$ and $\beta$ are called **amplitudes**.

### 4.1 Probabilities appear when we measure

**Professor:** If we measure a qubit in the computational basis $\{|0\rangle,|1\rangle\}$, the outcome is either 0 or 1. The probabilities are

$$
P(0)=|\alpha|^2,\qquad P(1)=|\beta|^2.
$$

This is why we require $|\alpha|^2+|\beta|^2=1$: the probabilities of all possible outcomes must sum to 1.

For our equal-superposition example,

$$
|\psi\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad P(0)=\frac12,\quad P(1)=\frac12.
$$

But this is **not** saying that before measurement the qubit was secretly in $|0\rangle$ half the time and $|1\rangle$ half the time. It has the superposition state $|\psi\rangle$. When we measure in this basis, we see one of the two outcomes with the probabilities above. After the measurement, the qubit is in the basis state corresponding to the result.

**Student question (paraphrased):** What happens with two qubits?

**Professor:** Two qubits are a little more complex; we will come to them later. I want to build up the foundation first, especially linear maps and matrices.

### 4.2 Measurement in another orthonormal basis

**Professor:** What exactly does it mean to *measure*? In this setting, you specify an **orthonormal basis**, say $\{\mathbf b_1,\mathbf b_2\}$. Write the state as

$$
|\psi\rangle=\alpha_1|b_1\rangle+\alpha_2|b_2\rangle.
$$

If we measure in this basis, the two possible outcomes are labelled by $|b_1\rangle$ and $|b_2\rangle$, with probabilities

$$
P(b_1)=|\alpha_1|^2,\qquad P(b_2)=|\alpha_2|^2.
$$

So, if you measure in the Hadamard basis $\{|+\rangle,|-\rangle\}$, your possible outcomes are $|+\rangle$ or $|-\rangle$, and the probabilities depend on the **coordinates in that basis**.

This is why the choice of orthonormal basis matters in quantum computing. In the computational basis, we obtain 0 or 1. In the Hadamard basis, the outcomes have different labels and may have different probabilities for the very same input state.

**Student question (paraphrased):** Where does the rule $|\alpha_1|^2$ come from?

**Professor:** That is a basic rule, or postulate, of quantum mechanics: the measurement probability is the squared magnitude of the amplitude in the chosen orthonormal basis. We are using that rule as a starting point.

**Student question (paraphrased):** If we measure $|\psi\rangle$ and get $|b_1\rangle$, can we recover the original $|\psi\rangle$?

**Professor:** No. A measurement with a particular outcome does not, in general, let us reconstruct the original unknown superposition. Some information about the original state has been lost.

---

## 5. Linear maps: changing a vector without measuring it

**Slides:** *Today's Plan* and *Linear Maps* (PDF pages 5–12; slides 4–5/49, including handwritten examples).

**Professor:** So far we have talked about a qubit state and what happens when we measure it. But in a quantum computation, we will often want to **change the state** of a qubit **without measuring it**.

For intuition, think of a point in the plane. You might rotate it by 90 degrees, reflect it about an axis, or otherwise transform its coordinates. The language that lets us discuss such operations is that of **linear maps**, also called **linear transformations**.

A map $T$ takes a vector in one vector space and produces a vector in another:

$$
T:V\longrightarrow W.
$$

For example, we can imagine a copy of $\mathbb R^2$ on the left and a copy of $\mathbb R^2$ on the right. A point $\mathbf p$ on the left is sent to some point $T(\mathbf p)$ on the right. A different point $\mathbf q$ is sent to $T(\mathbf q)$. In a rotation example, the new point is just the rotated version of the old one.

What makes the map **linear**? It must respect two operations: vector addition and scalar multiplication.

### 5.1 Linearity respects addition

**Professor:** If $\mathbf u$ and $\mathbf v$ are vectors, then

$$
\boxed{T(\mathbf u+\mathbf v)=T(\mathbf u)+T(\mathbf v).}
$$

What does this mean? You have two options. First, add $\mathbf u$ and $\mathbf v$ and then apply $T$. Or apply $T$ to each vector separately and then add the results. **Both methods give the same final vector.**

If you draw the vectors as arrows, the parallelogram rule gives $\mathbf u+\mathbf v$. After a linear transformation, the transformed parallelogram still obeys the same addition rule.

### 5.2 Linearity respects scaling

**Professor:** The other rule is

$$
\boxed{T(\alpha\mathbf v)=\alpha T(\mathbf v).}
$$

If a point $\mathbf p$ goes to $T(\mathbf p)$, where does $2\mathbf p$ go? It goes to $2T(\mathbf p)$. You can scale first and then transform, or transform first and then scale. The answer is the same.

We can combine the two rules into one equation:

$$
\boxed{T(\alpha\mathbf u+\beta\mathbf v)
=\alpha T(\mathbf u)+\beta T(\mathbf v).}
$$

For complex vector spaces such as $\mathbb C^2$, this must work for **complex scalars** $\alpha,\beta\in\mathbb C$, not just real numbers.

### 5.3 Examples and non-examples

**Professor:** Let us look at examples. A rotation about the origin is linear. A reflection about a line through the origin is linear. Scaling all coordinates, perhaps by a factor of two, is also a linear map. We will see that many more transformations can be represented in this way.

Here is an example that is **not** linear. Suppose every point is shifted one unit to the right:

$$
T(x,y)=(x+1,y).
$$

Then $T(4,0)=(5,0)$ and $T(8,0)=(9,0)$. But $(8,0)=2(4,0)$. If $T$ were linear, we would need

$$
T(8,0)=2T(4,0)=(10,0),
$$

which does not happen. So this translation is not linear.

There is an even easier test: any linear map must send the **zero vector** to the zero vector:

$$
T(\mathbf 0)=\mathbf 0.
$$

Why? Because $T(2\mathbf 0)=2T(\mathbf 0)$, but $2\mathbf 0=\mathbf 0$. Hence $T(\mathbf0)=2T(\mathbf0)$, which forces $T(\mathbf0)=\mathbf0$. A nonzero translation moves the origin and therefore fails this test.

**Other examples on the supplied slides:** The map $\mathbf v\mapsto\|\mathbf v\|$ is not linear. Also, complex conjugation $\mathbf v\mapsto\overline{\mathbf v}$ is **not complex-linear**, because

$$
T(i\mathbf v)=-i\,T(\mathbf v)\ne i\,T(\mathbf v)
$$

for general $\mathbf v$. (As a map on the corresponding real vector space, conjugation *is* real-linear; the lecture is working over complex scalars.)

**Professor:** A linear map takes the grid in the plane to another evenly structured grid. Straight lines remain straight or can collapse to a point. They do not become wavy curves just because you apply a linear map. Rotations, reflections, shears, scalings, and projections are examples we will work with.

**Editorial clarification:** A linear transformation need not be invertible. Therefore the statement “lines go to lines” is only literally true for lines whose direction is not collapsed to zero. A projection may send a whole line to a single point.

### 5.4 Can a linear map change the number of dimensions?

**Student question (paraphrased):** Can a linear map take vectors from a higher-dimensional space into a lower-dimensional space?

**Professor:** Yes. The input and output spaces need not have the same dimension. For example,

$$
T:\mathbb R^2\longrightarrow\mathbb R,
\qquad T(x,y)=x
$$

takes a pair of real coordinates and returns the first coordinate. That is a linear map. We will consider maps between different dimensions, although the usual one-qubit gates act from $\mathbb C^2$ back to $\mathbb C^2$.

---

## 6. A linear map is determined by what it does to the basis vectors

**Slides:** *What a Linear Map Does to the Plane* and *From Linear Map to Matrix* (PDF pages 13–15 and 19–21; slides 6 and 10/49).

**Professor:** Here is a very important observation. Suppose you know the two standard basis vectors $\mathbf e_1$ and $\mathbf e_2$ and you have a linear transformation $T$. Once you know **where the two basis vectors go**, you know where **every** vector goes.

Why? Any vector in the plane can be written as a linear combination of those two basis vectors:

$$
\begin{pmatrix}x\\y\end{pmatrix}
=x\begin{pmatrix}1\\0\end{pmatrix}
+y\begin{pmatrix}0\\1\end{pmatrix}
=x\mathbf e_1+y\mathbf e_2.
$$

By linearity,

$$
T\begin{pmatrix}x\\y\end{pmatrix}
=xT(\mathbf e_1)+yT(\mathbf e_2).
$$

This means the entire transformation is fixed by the images of $\mathbf e_1$ and $\mathbf e_2$.

### 6.1 Worked example with two basis vectors

**Professor:** Suppose I tell you that

$$
T\begin{pmatrix}1\\0\end{pmatrix}
=\begin{pmatrix}4\\5\end{pmatrix},
\qquad
T\begin{pmatrix}0\\1\end{pmatrix}
=\begin{pmatrix}1\\-3\end{pmatrix}.
$$

Now I ask: where does $(4,5)$ go under this map? We can write

$$
\begin{pmatrix}4\\5\end{pmatrix}
=4\begin{pmatrix}1\\0\end{pmatrix}
+5\begin{pmatrix}0\\1\end{pmatrix}.
$$

Therefore,

$$
\begin{aligned}
T\begin{pmatrix}4\\5\end{pmatrix}
&=4T\begin{pmatrix}1\\0\end{pmatrix}
+5T\begin{pmatrix}0\\1\end{pmatrix}\\
&=4\begin{pmatrix}4\\5\end{pmatrix}
+5\begin{pmatrix}1\\-3\end{pmatrix}\\
&=\begin{pmatrix}21\\5\end{pmatrix}.
\end{aligned}
$$

For a general vector,

$$
T\begin{pmatrix}x\\y\end{pmatrix}
=x\begin{pmatrix}4\\5\end{pmatrix}
+y\begin{pmatrix}1\\-3\end{pmatrix}.
$$

Now look at this in matrix form:

$$
\boxed{
T\begin{pmatrix}x\\y\end{pmatrix}
=\underbrace{\begin{pmatrix}4&1\\5&-3\end{pmatrix}}_{M}
\begin{pmatrix}x\\y\end{pmatrix}.
}
$$

The **first column** is where $\mathbf e_1$ goes. The **second column** is where $\mathbf e_2$ goes. This is the important interpretation of a matrix as a linear transformation.

**Professor:** In quantum computing, suppose I tell you what a gate does to $|0\rangle$ and what it does to $|1\rangle$. Then I have already told you what it does to *any* superposition:

$$
T\bigl(\alpha|0\rangle+\beta|1\rangle\bigr)
=\alpha T|0\rangle+\beta T|1\rangle.
$$

So we do not need to specify what happens to every possible qubit individually. We only need to specify what happens to the basis states.

### 6.2 General rule for $n$ dimensions

**Professor:** For a basis $\{\mathbf e_1,\ldots,\mathbf e_n\}$, write

$$
\mathbf v=\sum_{j=1}^n v_j\mathbf e_j.
$$

Then

$$
T(\mathbf v)=\sum_{j=1}^n v_jT(\mathbf e_j).
$$

The matrix representing $T$ has these images as columns:

$$
[T]=\begin{pmatrix}
\vline&\vline&&\vline\\
T(\mathbf e_1)&T(\mathbf e_2)&\cdots&T(\mathbf e_n)\\
\vline&\vline&&\vline
\end{pmatrix},
\qquad T(\mathbf v)=[T]\mathbf v.
$$

**The rule to remember: Column $j$ of the matrix is the image of basis vector $\mathbf e_j$.** This is how we obtain gate matrices from their action on basis states.

**Second matrix example from the spoken lecture:** If

$$
M=\begin{pmatrix}3&1\\1&i\end{pmatrix},
$$

then $M\mathbf e_1=(3,1)^T$ and $M\mathbf e_2=(1,i)^T$. The first and second columns tell you the destinations of the two basis vectors. You then multiply $M$ by the column of coordinates of any other vector to find its image.

**Student question (paraphrased):** Does the converse hold? Does every matrix give a linear transformation?

**Professor:** Yes. Multiplication by a fixed matrix is a linear transformation, and once bases have been chosen, every linear transformation between finite-dimensional vector spaces can be represented by a matrix of the appropriate size.

---

## 7. Visual gallery: What different matrices do

**Slides:** *A Gallery of Linear Maps (1), (2), and (3)* (PDF pages 16–18; slides 7–9/49).

**Professor:** Now look at the pictures. A grey letter F is transformed into an orange image. The pictures give you the geometry; the matrices give you the algebra. Always read a matrix by asking what it does to $\mathbf e_1$ and $\mathbf e_2$.

### 7.1 Scaling

For example,

$$
S=\begin{pmatrix}2&0\\0&\tfrac12\end{pmatrix}.
$$

We have $S\mathbf e_1=(2,0)^T$ and $S\mathbf e_2=(0,\frac12)^T$. So the $x$ direction is stretched by a factor of two, while the $y$ direction is compressed by a factor of one-half. The image becomes wider and shorter.

### 7.2 Rotation by 90 degrees

For a 90-degree counterclockwise rotation, the slide shows

$$
R_{90^\circ}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$

The first basis vector $(1,0)$ goes to $(0,1)$; the second $(0,1)$ goes to $(-1,0)$. Those are exactly the images of the two axes after a quarter-turn counterclockwise.

### 7.3 Shear

For example,

$$
S_{\mathrm{shear}}=\begin{pmatrix}1&\tfrac12\\0&1\end{pmatrix}.
$$

Here $(1,0)$ stays where it is, but $(0,1)$ goes to $(\frac12,1)$. The shape is slanted sideways. This operation is linear, but it does not generally preserve perpendicularity.

### 7.4 Reflections

Reflection in the $x$-axis is represented by

$$
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

This leaves the first coordinate alone and negates the second:

$$
Z\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}x\\-y\end{pmatrix}.
$$

Reflection in the line $y=x$ is represented by

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

It interchanges the coordinates:

$$
X\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}y\\x\end{pmatrix}.
$$

### 7.5 Projection

Projection onto the $x$-axis is represented by

$$
P_x=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

Then

$$
P_x\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}x\\0\end{pmatrix}.
$$

The $y$ coordinate is removed. Many different input vectors have the same projection, so this transformation is **not invertible**.

### 7.6 Hadamard, a 45-degree rotation, and minus the identity

**Professor:** The Hadamard matrix is

$$
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

It sends the first basis vector to $\mathbf h_+$ and the second to $\mathbf h_-$. Both output vectors have length 1 and are perpendicular.

**Slide-based correction to the geometric analogy:** The lecture's spoken description briefly equates $H$ with a rotation by 45 degrees, but the **provided slide 9/49 explicitly distinguishes them**:

$$
\underbrace{\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}}_{\text{Hadamard: reflection about a line at }22.5^\circ}
\quad\ne\quad
\underbrace{\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}}_{\text{counterclockwise rotation by }45^\circ}.
$$

The Hadamard **basis directions** lie at 45 degrees to the original axes, but the **Hadamard transformation** is geometrically a reflection in this real-plane illustration, not a 45-degree rotation. This distinction also explains why $H^2=I$.

Finally,

$$
-I=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}
$$

acts in the real plane as a 180-degree rotation, not as a reflection in a single line.

**Professor:** These are examples to help you interpret what a matrix does. You do not have to memorize all the pictures. We are going to use the algebraic way of thinking more and more, especially when complex numbers and multiple qubits are involved.

---

## 8. The important one-qubit gates: $X$, $Z$, and $H$

**Slides:** *Important Examples* (PDF pages 22–23; slide 11/49).

**Professor:** In quantum computing, we often call these operators **gates**. A gate acts on an input state and produces another state. The circuit picture is a line or wire with a box labelled by the gate.

### 8.1 The bit-flip gate $X$

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

The first basis vector goes to the second, and the second goes to the first:

$$
X|0\rangle=|1\rangle,\qquad X|1\rangle=|0\rangle.
$$

For a general qubit,

$$
X\bigl(\alpha|0\rangle+\beta|1\rangle\bigr)
=\beta|0\rangle+\alpha|1\rangle.
$$

So $X$ **swaps the two amplitudes**. It is called a bit flip because it interchanges the computational-basis states.

### 8.2 The phase-flip gate $Z$

$$
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

It leaves $|0\rangle$ unchanged and multiplies $|1\rangle$ by $-1$:

$$
Z|0\rangle=|0\rangle,\qquad Z|1\rangle=-|1\rangle.
$$

Thus

$$
Z\bigl(\alpha|0\rangle+\beta|1\rangle\bigr)
=\alpha|0\rangle-\beta|1\rangle.
$$

**Professor:** We call this a **phase flip** because we have changed the phase of the $|1\rangle$ amplitude relative to the $|0\rangle$ amplitude. The length of the state vector is unchanged.

**Editorial clarification:** In the real two-dimensional drawing, $Z$ is a reflection across the $x$-axis. In the actual complex state space, the physically relevant description is a relative phase change; the real-plane picture is limited.

### 8.3 The Hadamard gate $H$

$$
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

It maps the standard basis to the Hadamard basis:

$$
H|0\rangle=|+\rangle
=\frac{|0\rangle+|1\rangle}{\sqrt2},
$$

$$
H|1\rangle=|-\rangle
=\frac{|0\rangle-|1\rangle}{\sqrt2}.
$$

For a general column vector,

$$
H\begin{pmatrix}x\\y\end{pmatrix}
=\frac1{\sqrt2}\begin{pmatrix}x+y\\x-y\end{pmatrix}.
$$

This follows from linearity: $x$ times the first column plus $y$ times the second column. You can find the effect of any gate on any qubit just by matrix multiplication.

### 8.4 Do the transformed basis vectors stay orthonormal?

**Student question (paraphrased):** If we begin with an orthonormal basis and apply a linear transformation, will the transformed basis vectors remain orthonormal?

**Professor:** Not for **every** linear transformation. A shear, for example, can send perpendicular vectors to directions that are no longer perpendicular. Linearity by itself is not sufficient. In quantum computing, we will impose additional restrictions on the transformations allowed as gates. This will lead us to **unitary** matrices.

---

## 9. Applying a sequence of linear transformations

**Slide verification:** The material from this point onwards is **not covered** by the pages included in the supplied slide PDF. It is edited from the transcript.

**Professor:** In many quantum algorithms, you will apply one operation after another. Suppose we begin with a vector $\mathbf v$. First we apply the matrix $A$. The result is $A\mathbf v$. Next we apply $B$, and then $C$:

$$
\mathbf v\ \xrightarrow{A}\ A\mathbf v
\ \xrightarrow{B}\ B(A\mathbf v)
\ \xrightarrow{C}\ C(B(A\mathbf v)).
$$

Matrix multiplication is **associative**:

$$
C(B(A\mathbf v))=(CBA)\mathbf v.
$$

Therefore, the entire sequence can be represented by **one matrix**, namely $CBA$. You multiply the matrices in the order appropriate to their action: the matrix for the gate applied **last** is written on the **left**.

### 9.1 Example: Apply $X$ and then $Z$

**Professor:** Let us begin with a state $\mathbf v$, apply $X$, and then apply $Z$. The final output is

$$
Z(X\mathbf v)=(ZX)\mathbf v.
$$

Here

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Multiplying them gives

$$
\boxed{ZX=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.}
$$

You can check this by following the basis vectors. Starting with $|0\rangle$, $X$ changes it to $|1\rangle$, and then $Z$ changes it to $-|1\rangle$. So the first column of $ZX$ is $(0,-1)^T$. Starting with $|1\rangle$, $X$ changes it to $|0\rangle$, and $Z$ leaves that unchanged. So the second column is $(1,0)^T$.

Now reverse the order. If you apply $Z$ first and $X$ second, you get

$$
\boxed{XZ=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.}
$$

These matrices are different:

$$
ZX\ne XZ.
$$

**Professor:** So the **order** in which you apply operations matters. Matrix multiplication is generally **not commutative**, although it is associative.

**Editorial clarification:** In this particular example, $ZX=-XZ$. Thus, although the matrices differ, their outputs differ only by an overall minus sign when applied to a given state; that overall phase does not alter measurement probabilities. This nuance does not change the algebraic point that matrix multiplication is noncommutative.

---

## 10. Projection maps and bra–ket notation

**Slide context:** The included PDF ends with *Matrix Entries as Inner Products* (PDF pages 24–26; slide 12/49), which supports the inner-product and outer-product notation used here. The detailed spoken discussion of projections continues beyond the provided pages.

**Professor:** Let me give one more example of a linear map: **projection**. Suppose we have an orthonormal basis $\{\mathbf e_1,\mathbf e_2\}$ and write

$$
\mathbf v=\alpha_1\mathbf e_1+\alpha_2\mathbf e_2.
$$

If I project onto the $\mathbf e_1$ direction, I want to keep the first component and remove the second:

$$
P_1(\mathbf v)=\alpha_1\mathbf e_1.
$$

Similarly, projection onto the $\mathbf e_2$ direction would give $\alpha_2\mathbf e_2$.

In the standard basis, projection onto the first axis is

$$
P_1=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

But there is another useful way to write the projection matrix. Let $\mathbf e$ be a unit vector. Form the matrix

$$
\boxed{P=\mathbf e\mathbf e^\dagger.}
$$

When this matrix acts on a vector $\mathbf v$,

$$
P\mathbf v
=\mathbf e(\mathbf e^\dagger\mathbf v)
=\langle\mathbf e,\mathbf v\rangle\mathbf e.
$$

Since $\langle\mathbf e,\mathbf v\rangle$ is the coordinate of $\mathbf v$ along $\mathbf e$, this takes exactly the component along that direction.

Let us verify it for $\mathbf e=(1,0)^T$:

$$
\mathbf e\mathbf e^\dagger
=\begin{pmatrix}1\\0\end{pmatrix}
\begin{pmatrix}1&0\end{pmatrix}
=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

This is the same projection matrix as before.

### 10.1 Kets, bras, inner products and outer products

**Professor:** In quantum notation, a column vector is written as a **ket**, $|u\rangle$. Its conjugate transpose is written as a **bra**, $\langle u|$. So

$$
|u\rangle=\begin{pmatrix}u_1\\u_2\end{pmatrix},
\qquad
\langle u|=\begin{pmatrix}\overline{u_1}&\overline{u_2}\end{pmatrix}.
$$

When a bra is followed by a ket, we get an **inner product**, a complex number:

$$
\langle u|v\rangle=u^\dagger v.
$$

When a ket is followed by a bra, we get an **outer product**, a matrix:

$$
|u\rangle\langle v|=u v^\dagger.
$$

Therefore, our projection matrix can be written as

$$
\boxed{P=|e\rangle\langle e|.}
$$

For the computational basis, the two one-dimensional projectors are

$$
P_0=|0\rangle\langle0|
=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
P_1=|1\rangle\langle1|
=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

**Editorial clarification:** A projector by itself is a linear map, but applying an unnormalized projector is not the complete physical rule for an individual measurement outcome. The measurement postulate also specifies an outcome probability and—when the probability is nonzero—the normalized post-measurement state. The lecturer is using projection here to build the underlying linear algebra.

### 10.2 Matrix entries as inner products — supplied slide

The supplied slide adds the following formula for a matrix $A$ in an orthonormal basis $\{\mathbf e_i\}$:

$$
\boxed{A_{ij}=\langle\mathbf e_i,A\mathbf e_j\rangle
=\mathbf e_i^\dagger A\mathbf e_j.}
$$

This means the entry in **row $i$, column $j$** can be found by applying $A$ to basis vector $\mathbf e_j$ and taking its inner product with $\mathbf e_i$.

The slide also gives the outer-product reconstruction:

$$
A=\sum_{i,j} A_{ij}\,\mathbf e_i\mathbf e_j^\dagger.
$$

For the standard two-dimensional basis, the slide lists

$$
X=\mathbf e_1\mathbf e_2^\dagger+\mathbf e_2\mathbf e_1^\dagger,
$$

$$
Z=\mathbf e_1\mathbf e_1^\dagger-\mathbf e_2\mathbf e_2^\dagger,
$$

$$
I=\mathbf e_1\mathbf e_1^\dagger+\mathbf e_2\mathbf e_2^\dagger.
$$

**Editorial note:** This short subsection reproduces the content of the final **supplied** slide, to align the transcription with the slides; the original spoken transcription does not develop the full reconstruction formula in the same place.

---

## 11. The adjoint, or conjugate transpose, of a matrix

**Professor:** We have used the dagger symbol for a vector. We can also define it for any matrix $A$. The **adjoint**, written $A^\dagger$, is obtained by **transposing the matrix and taking the complex conjugate of every entry**.

In other words, first interchange rows and columns, and then replace each complex number by its conjugate. Equivalently, you may conjugate first and transpose second:

$$
\boxed{A^\dagger=\overline A^{\,T}.}
$$

For example, suppose

$$
A=\begin{pmatrix}1&i\\2&3-i\end{pmatrix}.
$$

Then its transpose is $A^T=\begin{pmatrix}1&2\\i&3-i\end{pmatrix}$, and its adjoint is

$$
A^\dagger=\begin{pmatrix}1&2\\-i&3+i\end{pmatrix}.
$$

**Editorial note:** This numerical matrix is a **worked illustration of the stated rule**, not a confidently recoverable verbatim example from the audio transcript. The audio contains fragmented matrix entries in this passage; no corresponding slide was supplied to disambiguate them.

### 11.1 Moving an operator across an inner product

**Professor:** This adjoint has an important property. If we take the inner product of $\mathbf u$ with $A\mathbf v$, then we can move the matrix to the other side by taking its adjoint:

$$
\boxed{\langle\mathbf u,A\mathbf v\rangle
=\langle A^\dagger\mathbf u,\mathbf v\rangle.}
$$

Equivalently,

$$
\langle A\mathbf u,\mathbf v\rangle
=\langle\mathbf u,A^\dagger\mathbf v\rangle.
$$

This is a useful identity to verify as an exercise; it gives you practice with matrix products and conjugate transposes. We will see why the adjoint becomes important.

### 11.2 Hermitian matrices

**Professor:** A matrix is called **Hermitian** if it is equal to its own adjoint:

$$
\boxed{A=A^\dagger.}
$$

For example, the matrix

$$
A=\begin{pmatrix}0&i\\-i&0\end{pmatrix}
$$

is Hermitian, since transposing and conjugating returns the same matrix.

At this point, I am giving you the definition. We will return later to why Hermitian matrices are important.

**Editorial note:** The recorded numeric example during this discussion is not completely intelligible. The matrix above is a mathematically correct illustrative example of the professor's stated definition; it should not be treated as a verbatim reconstruction of the indistinct figures on the board.

### 11.3 Recap before moving on

**Professor:** So far we have defined a linear map, seen that a linear map can be represented by a matrix, and worked through several examples. We introduced the **adjoint**, and we introduced the term **Hermitian**. I do not expect all the significance to be obvious immediately. We are building the ingredients that we need for quantum computing.

---

## 12. Invertible transformations

**Professor:** Another important property of a linear map is whether it is **invertible**. Suppose I give you $T(\mathbf x)$. Can you determine what $\mathbf x$ was?

If you can uniquely recover the input vector, the map is invertible. You can **undo** the transformation and get back to where you started.

Consider **reflection** about the $x$-axis. If I give you the reflected point, you recover the original by reflecting again. A rotation is also invertible: if I rotate everything by 20 degrees, I can undo it by rotating 20 degrees in the opposite direction. Multiplication by 2 is invertible as well; we undo it by multiplying by $1/2$.

### 12.1 Projection is not invertible

**Professor:** What would be a transformation that is **not** invertible? We have already seen one: **projection**. Suppose every point $(x,y)$ goes to $(x,0)$. If I know only the result $(x,0)$, I cannot tell what the original $y$ coordinate was. Many input points have the same output.

That is why projection is not invertible. In particular, a measurement generally loses information about the original unknown state. But when we apply ordinary quantum **gates** to an isolated qubit, the state changes reversibly; those operations must be invertible.

**Student question (paraphrased):** Can a map that reduces dimension be invertible?

**Professor:** A linear map from a higher-dimensional vector space into a strictly lower-dimensional one cannot have an inverse that uniquely recovers every input. It must lose information about at least one independent direction.

### 12.2 The inverse matrix $A^{-1}$

**Professor:** If $A$ is invertible, we denote its inverse by $A^{-1}$. This is the transformation that undoes $A$:

$$
A^{-1}(A\mathbf v)=\mathbf v.
$$

For a square matrix this means

$$
A^{-1}A=AA^{-1}=I,
$$

where $I$ is the **identity matrix**. The identity transformation leaves all vectors unchanged.

### 12.3 Undoing a sequence of operations

**Professor:** Suppose we first apply $A$ and then $B$:

$$
\mathbf v\xrightarrow{A}A\mathbf v\xrightarrow{B}BA\mathbf v.
$$

How do you undo the complete operation? You must undo $B$ **first**, then undo $A$. So the inverse of the combined operation is

$$
\boxed{(BA)^{-1}=A^{-1}B^{-1}.}
$$

Likewise,

$$
(ABC)^{-1}=C^{-1}B^{-1}A^{-1}.
$$

It is like undoing operations from a stack: the **last operation performed is the first to be undone**.

### 12.4 The $X$, $Z$, and $H$ gates undo themselves

**Professor:** Let us see which inverses we have already encountered.

The $X$ gate swaps $|0\rangle$ and $|1\rangle$. If you apply it twice, you return to the original state. Therefore,

$$
X^2=I,\qquad X^{-1}=X.
$$

The $Z$ gate multiplies the $|1\rangle$ amplitude by $-1$. If you do that again, $(-1)(-1)=1$. So

$$
Z^2=I,\qquad Z^{-1}=Z.
$$

What about the Hadamard gate? Recall

$$
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

You can check by matrix multiplication that

$$
H^2
=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I.
$$

Thus,

$$
\boxed{H^{-1}=H.}
$$

**Professor:** You can also check this by starting with $|0\rangle$. The first Hadamard gives $(|0\rangle+|1\rangle)/\sqrt2$. Applying Hadamard again, and using linearity, gives back $|0\rangle$. The same works for $|1\rangle$. Since we know where both basis states go, we know what happens to every state.

**Editorial correction to the spoken geometric shortcut:** Although the transcript informally describes undoing $H$ by a reverse 45-degree rotation, the supplied slide distinguishes Hadamard from a 45-degree rotation. The reliable argument is **$H^2=I$**, or the reflection geometry of the matrix.

---

## 13. Which transformations are allowed as quantum gates?

**Professor:** This brings us back to the question we asked: if you give me a qubit, what kinds of operations am I allowed to perform on it without measuring it?

We want operations that are **linear**. We have already discussed why that matters: knowing what happens to $|0\rangle$ and $|1\rangle$ determines what happens to every superposition.

We also want these ordinary, isolated-system gate operations to be **reversible**. We should be able to undo the operation and return to the initial state.

But there is an additional condition. A qubit is represented by a **unit vector**, and the transformed state must still be a unit vector. We cannot perform an arbitrary linear map that changes its length. In fact, the operations we are interested in preserve **inner products**, and therefore preserve lengths and orthogonality.

### 13.1 Orthonormal bases must remain orthonormal

**Professor:** Think of an orthonormal basis $\mathbf e_1,\mathbf e_2$. Suppose we apply a transformation $T$. We require the images $T(\mathbf e_1)$ and $T(\mathbf e_2)$ to be **orthonormal** as well.

This means two things:

1. Each output basis vector still has length **1**.
2. The output basis vectors are still **orthogonal** to one another.

In the real-plane picture, a rotation or a reflection has this property. These operations preserve lengths and angles. But a shear generally does not, because it changes the angle between the axes. And multiplying both coordinates by 2, although linear and invertible, is not allowed as a standalone one-qubit gate, because a unit vector would become a vector of length 2.

For example,

$$
\begin{pmatrix}x\\y\end{pmatrix}
\longmapsto
\begin{pmatrix}2x\\2y\end{pmatrix}
$$

is linear but not length-preserving.

**Student question (paraphrased):** Is this related to isometries?

**Professor:** Yes, that is the idea: the inner products, lengths, and geometric relationships are preserved. You do not need to learn the separate terminology of isometries for now. We will call these transformations **unitary**.

**Editorial clarification:** We are talking specifically about **unitary operations on a closed quantum system**. General quantum processes involving measurement, noise, or discarding an environment are not all described by a single unitary on the subsystem alone.

---

## 14. Unitary matrices

**Professor:** Let us express this property using a matrix. Remember that the **columns** of a transformation matrix tell us the images of the basis vectors. Therefore, if a transformation sends an orthonormal basis to an orthonormal basis, the **columns of its matrix must be orthonormal**.

This is a definition of a **unitary matrix**. If $U$ is a square matrix, it is unitary when its columns are orthonormal.

### 14.1 Example: Checking the columns

Suppose the first column is

$$
\mathbf c_1=\frac1{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}
$$

and the second column is initially proposed as

$$
\mathbf c_2=\frac1{\sqrt2}\begin{pmatrix}i\\i\end{pmatrix}.
$$

Both columns have length 1:

$$
\|\mathbf c_1\|^2=\frac12+\frac12=1,
\qquad
\|\mathbf c_2\|^2=\frac12+\frac12=1.
$$

But are they perpendicular? We must calculate their **complex inner product**:

$$
\begin{aligned}
\langle\mathbf c_1,\mathbf c_2\rangle
&=\frac12\bigl(\overline1\,i+\overline i\,i\bigr)\\
&=\frac12(i+1)\ne0.
\end{aligned}
$$

So those two vectors do not form an orthonormal pair, and the matrix with these columns is **not unitary**.

**Professor:** But suppose I change the second column to

$$
\mathbf c_2'=\frac1{\sqrt2}\begin{pmatrix}i\\1\end{pmatrix}.
$$

Now

$$
\begin{aligned}
\langle\mathbf c_1,\mathbf c_2'\rangle
&=\frac12\bigl(i+(-i)\cdot1\bigr)\\
&=0.
\end{aligned}
$$

Both vectors still have length 1, so now the columns are orthonormal. The resulting matrix

$$
U=\frac1{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}
$$

is unitary.

**Editorial confidence note:** This is the best-supported interpretation of the spoken example involving the entries $1$ and $i$; the particular matrix was not visible in the supplied slide pages. The conclusion and calculations have been checked, but the numerical entries of this unsupplied slide should not be treated as independently verified.

### 14.2 The matrix equation $U^\dagger U=I$

**Professor:** There is a compact way of checking whether a matrix is unitary:

$$
\boxed{U^\dagger U=I.}
$$

Here $U^\dagger$ is the conjugate transpose and $I$ is the identity matrix. At first this formula may look unfamiliar, so let us see why it means the columns are orthonormal.

Suppose the columns of $U$ are $\mathbf u_1,\mathbf u_2,\ldots,\mathbf u_n$. Then we can write

$$
U=\begin{pmatrix}\vline&\vline&&\vline\\
\mathbf u_1&\mathbf u_2&\cdots&\mathbf u_n\\
\vline&\vline&&\vline\end{pmatrix}.
$$

When we form $U^\dagger$, these conjugated columns become rows. When we multiply $U^\dagger U$, the entry in row $i$, column $j$ is

$$
(U^\dagger U)_{ij}=\langle\mathbf u_i,\mathbf u_j\rangle.
$$

What is the value of that inner product?

- If $i=j$, it is $\langle\mathbf u_i,\mathbf u_i\rangle=1$, because the column has length 1.
- If $i\ne j$, it is $0$, because different columns are orthogonal.

So the product has 1s on the diagonal and 0s elsewhere. That is exactly the identity matrix:

$$
U^\dagger U=I.
$$

**Professor:** This explains the formula. It is just a compact way to say that the columns form an orthonormal basis.

For a **square** unitary matrix, we also have $UU^\dagger=I$. Hence its inverse is simply its adjoint:

$$
\boxed{U^{-1}=U^\dagger.}
$$

That is why these transformations are reversible.

### 14.3 Why unitary matrices preserve inner products

**Professor:** Let us take two vectors $\mathbf u$ and $\mathbf v$ and apply the same unitary matrix $U$ to both. What happens to their inner product?

$$
\begin{aligned}
\langle U\mathbf u,U\mathbf v\rangle
&=(U\mathbf u)^\dagger(U\mathbf v)\\
&=\mathbf u^\dagger U^\dagger U\mathbf v\\
&=\mathbf u^\dagger I\mathbf v\\
&=\langle\mathbf u,\mathbf v\rangle.
\end{aligned}
$$

Therefore,

$$
\boxed{\langle U\mathbf u,U\mathbf v\rangle
=\langle\mathbf u,\mathbf v\rangle.}
$$

So a unitary transformation **preserves inner products**. In particular, it preserves squared lengths:

$$
\|U\mathbf v\|^2
=\langle U\mathbf v,U\mathbf v\rangle
=\langle\mathbf v,\mathbf v\rangle
=\|\mathbf v\|^2.
$$

In the real-plane picture, this is why lengths and angles are preserved. You can think of rotations and reflections, although complex transformations cannot all be visualized as simple rotations of a two-dimensional sheet.

### 14.4 Why unitarity is essential for qubits

**Professor:** Suppose we begin with a valid qubit

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\qquad |\alpha|^2+|\beta|^2=1.
$$

We apply some matrix $M$ and obtain

$$
|\psi'\rangle=M|\psi\rangle
=\alpha'|0\rangle+\beta'|1\rangle.
$$

How do we know that the new state is also valid? In other words, why should

$$
|\alpha'|^2+|\beta'|^2=1
$$

still be true?

For an arbitrary matrix, it is not guaranteed. But if $M$ is **unitary**, it preserves the norm. So if the initial vector has length 1, the output vector also has length 1. This is why the gates we have been discussing are unitary matrices.

For example, consider the Hadamard gate:

$$
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

In this case $H^\dagger=H$ because the matrix is real and symmetric. We have already checked that $H^2=I$. Therefore

$$
H^\dagger H=H^2=I,
$$

so $H$ is unitary. The same is true of $X$ and $Z$.

**Professor:** Whenever you see an ordinary quantum **gate** in this unitary circuit model, it is represented by a unitary matrix. That is how the operation preserves the normalization of quantum states. Some other topics—such as Hermitian matrices, additional gates, and multiple qubits—will come later.

### 14.5 Contrast with a nonunitary matrix

**Professor:** If a matrix has columns that are not perpendicular, or if one of its columns does not have length 1, then it is **not unitary**. The scaling, shear, and projection examples we looked at are not unitary. They may be perfectly valid linear maps in ordinary linear algebra, but they do not serve as reversible, norm-preserving gates on an isolated qubit.

---

## 15. Closing recap and questions

**Professor:** I think we have covered quite a lot today. We discussed linear maps, how matrices represent them, their adjoints, invertibility, and unitary matrices. I want you to revisit the exercises so that these ideas become comfortable. We have been discussing **one qubit**. Next time, we will move towards **two qubits**, where the **tensor product** becomes important.

### 15.1 Questions about linearity and inner products

**Student question (paraphrased):** Does a unitary transformation make the inner-product map linear?

**Professor:** The inner product already has its own algebraic properties. For example, with our convention, it is linear in the **second** argument:

$$
\langle\mathbf u,\alpha\mathbf v+\beta\mathbf w\rangle
=\alpha\langle\mathbf u,\mathbf v\rangle
+\beta\langle\mathbf u,\mathbf w\rangle.
$$

The important additional statement about a unitary matrix $U$ is that it **preserves** inner products:

$$
\langle U\mathbf u,U\mathbf v\rangle
=\langle\mathbf u,\mathbf v\rangle.
$$

Those are different properties. An arbitrary linear transformation need not preserve the inner product.

**Editorial clarification:** With $\langle u,v\rangle=u^\dagger v$, the inner product is **conjugate-linear in the first argument**, not complex-linear in both arguments.

### 15.2 How much additional study is necessary?

**Student question (paraphrased):** Do we need to read another linear algebra book?

**Professor:** I would not recommend going off in several different directions right now. We have already recommended quantum-computing textbooks, and they contain the relevant linear algebra review. What we are covering, together with the assigned exercises, should be enough to begin. If matrix multiplication has become unfamiliar, please revise it and practice the problems.

**Student question (paraphrased):** Do we need to learn what an isometry is?

**Professor:** No, you do not need the separate term right now. I mentioned it because a student used it. The key concept for us is a **unitary transformation**, which preserves inner products and lengths. These geometric pictures are useful to begin with, but as you work with complex vectors and higher-dimensional spaces, you should become comfortable with the algebra.

### 15.3 Books, lectures, and resources

**Student question (paraphrased):** Are there beginner-friendly textbooks or videos we can consult?

**Professor:** The standard reference I mentioned is the book by **Nielsen and Chuang** on quantum computation and quantum information. There are also online lecture resources. If you want a more elementary lecture series, you might look at **Ryan O'Donnell** at Carnegie Mellon University. But first make sure you are reasonably comfortable with linear algebra.

Another book mentioned is **Quantum Computing for Everyone** by **Chris Bernhardt**. I have not gone through it carefully, but it should also cover introductory material. Khan Academy can be useful for reviewing basic linear algebra. There is no need to get too far into additional topics at the expense of doing the assigned problems.

**Student question (paraphrased):** Will we use calculus in this material?

**Professor:** I do not expect us to need calculus in what we are doing here. What you most need is comfort with vectors and matrices.

**Student question (paraphrased):** Will there be Qiskit programming exercises?

**Professor:** Yes, we will have exercises involving Qiskit when we come to the programming portion. For now, work through the foundations.

### 15.4 Linear dependence and determinants

**Student question (paraphrased):** Can we say that vectors are linearly dependent if the determinant of the matrix formed from them is zero?

**Professor:** For a **square matrix**, yes: a zero determinant means its columns are linearly dependent. I have deliberately not introduced determinants yet because I do not want to bring in too many concepts at once. We may return to determinants when we talk about eigenvalues.

For example, if two vectors live in $\mathbb R^2$, you can form a $2\times2$ matrix and check its determinant. But if you have only two vectors in a ten-dimensional space, the matrix with those two vectors as columns would be $10\times2$. The ordinary determinant is not defined for a nonsquare matrix.

### 15.5 Multiple qubits, the Bloch sphere, and tensor products

**Student question (paraphrased):** Why is a single qubit described using complex coordinates? How is this related to the Bloch sphere, and what happens for several qubits?

**Professor:** For one qubit, you have two **complex** amplitudes $\alpha$ and $\beta$. Each complex number has a real and imaginary part, so it initially looks like four real coordinates. But they are not arbitrary: we require

$$
|\alpha|^2+|\beta|^2=1.
$$

That normalization condition reduces the number of independent real parameters from four to three. The Bloch-sphere picture introduced in the earlier lecture is a way to visualize the state more economically.

**Editorial clarification:** There is an additional identification of states differing only by an **overall global phase**. After accounting for normalization **and** global phase, a pure one-qubit state has **two physically relevant real parameters**, customarily represented by the Bloch-sphere angles $\theta$ and $\phi$. The professor's reference to three parameters describes the count **after normalization but before removing global phase**.

**Student question (paraphrased):** For several qubits, can we just use a Cartesian product?

**Professor:** We will use the **tensor product**, not simply the Cartesian product. There is an important difference, and this is where phenomena such as entanglement become relevant. Each individual qubit can be described using its own Bloch sphere, but an entangled multi-qubit state cannot generally be specified just by giving the separate states of the individual qubits.

**Student question (paraphrased):** What is the next topic?

**Professor:** The next major topic is the **tensor product**, in preparation for discussing multiple qubits.

### 15.6 Assignments, session replays, and administrative questions

**Participants and course support:** There is a brief discussion about the availability of the annotated notes, session replays, assignments, and solutions in the Learning Management System (LMS). Course support explains that learners should look in the LMS rather than expect an individual email notification about each upload. They are also directed to the community/support channel for guidance about accessing course materials and assignments. The transcript's name for the communication channel is not clear enough to verify, so it is not standardized here.

**Professor:** I will share more problem-solving exercises, and we can discuss questions at the beginning of the next session. We will also coordinate when the solutions are released.

**Student question (paraphrased):** Can we discuss unitary matrices with determinant 1?

**Professor:** I have not introduced determinants formally yet. We will discuss that later rather than adding it now.

**Professor:** Thank you. We will stop here and continue with multiple qubits in the next lecture.

---

## Editorial correction register

The following entries make the substantial corrections transparent without altering the teaching sequence.

| Recorded or ambiguous wording | Correction or treatment | Evidence |
|---|---|---|
| “Hard marked” / “hard marked basis” | **Hadamard basis**; $\mathbf h_\pm=(1,\pm1)^T/\sqrt2$ | Supplied slides 2/49 and 11/49 |
| “Alpha square plus beta square” | For complex amplitudes, **$|\alpha|^2+|\beta|^2=1$** | Supplied slide 3/49 |
| “Bra notation” referring to $|\psi\rangle$ | $|\psi\rangle$ is a **ket**; $\langle\psi|$ is a bra | Consistent mathematical terminology and the transcript's later explanation |
| Hadamard described as “rotation by 45 degrees” | The Hadamard **basis** has diagonal directions, but the **Hadamard matrix** is a reflection across a line at $22.5^\circ$ in the real-plane diagram | Supplied slide 9/49 |
| 90-degree rotation matrix garbled in audio | $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ for a counterclockwise quarter-turn | Supplied slide 7/49 |
| $ZX$ matrix incomplete / repeated numbers | $ZX=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ | Recalculated from the confirmed $X$, $Z$ matrices |
| “Conjugate transpose is linear” | A map $A\mapsto A^\dagger$ on matrices is **conjugate-linear**, not complex-linear; it is a matrix operation, not the same as multiplying a vector by a fixed matrix | The transcript has a contradictory exchange; no corresponding slide was provided |
| “The probability is $\alpha_1$ square” | **$|\alpha_1|^2$** is the measurement probability | Slide-backed qubit norm rule and the transcript's basis-measurement discussion |
| “Unit identity matrix” | **Unitary matrix**; $U^\dagger U=I$ | The transcript's explanation of unitary gates |
| “Nielsen and Chung” | **Nielsen and Chuang** | Proper name of the referenced textbook authors |
| “Quiz kit” | **Qiskit** | Quantum-computing programming context |
| “Helbert space” / Bloch sphere parameter count | **Hilbert space**; normalization leaves three real parameters, global-phase equivalence leaves two physical parameters for a pure qubit | The transcript refers to Bloch-sphere material from the earlier lecture |

**End of corrected transcription.**
