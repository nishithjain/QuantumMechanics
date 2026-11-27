# Lecture 07 — Inverse Matrices, Column Space and Null Space

> **Learning goal:** Understand how inverse matrices, column space, rank, and null space describe the solutions of linear systems when viewed as linear transformations.

These notes follow the teaching order. The lecture focuses on geometric intuition rather than teaching the computational procedures for finding inverses, ranks, or null spaces.

## 1. The purpose of this lecture: connect transformations to equations

So far, the series has used a visual viewpoint: a matrix represents a linear transformation that moves vectors and reshapes space.

This lecture uses that same viewpoint to understand four ideas:

- inverse matrices;
- column space;
- rank;
- null space (also called the kernel).

Explicitly says that this video will not teach the procedures for computing these objects. Those methods are often taught using **Gaussian elimination** and **row echelon form**. The goal here is to build intuition for what the objects mean. In practice, software is often used to perform the calculations.

## 2. Why linear algebra is useful: solving systems of equations

One major reason linear algebra is used across technical disciplines is that it helps solve **systems of equations**.

A system of equations is a collection of equations involving unknown variables. For example:

$$
\begin{aligned}
2x+y&=5\\
x+3y&=7
\end{aligned}
$$

Here, $x$ and $y$ are unknown. Each equation gives a condition that the unknown values must satisfy.

Is interested in a special kind of system: within each equation,

- each variable is multiplied only by a constant;
- the resulting terms are added together;
- there are no powers of the variables, products of unknown variables, or other nonlinear functions.

Such a system is called a **linear system of equations**.

For example, $2x+y=5$ is linear. An equation such as $x^2+y=5$ is not linear because it contains a squared variable.

## 3. Organize the equations so they look like matrix multiplication

A convenient way to write a linear system is to place all variable terms on the left and constants on the right.

For example:

$$
\begin{aligned}
2x+y&=5\\
x+3y&=7
\end{aligned}
$$

The coefficients of $x$ and $y$ can be lined up in columns:

$$
\begin{bmatrix}
2&1\\
1&3
\end{bmatrix}
\begin{bmatrix}
x\\y
\end{bmatrix}
=
\begin{bmatrix}
5\\7
\end{bmatrix}.
$$

If a variable is missing from an equation, we use a zero coefficient to keep the columns aligned.

names to the three parts:

$$
\boxed{A\mathbf x=\mathbf v}
$$

- $A$ is the matrix of constant coefficients.
- $\mathbf x$ is the vector of unknown variables.
- $\mathbf v$ is the constant vector on the right-hand side.

This is not just a shorter way to write several equations. It reveals a geometric interpretation.

## 4. The geometric meaning of the equation A x = v

A matrix $A$ represents a linear transformation.

So the equation

$$
A\mathbf x=\mathbf v
$$

asks:

**Which input vector $\mathbf x$, after transformation by $A$, lands exactly on the target vector $\mathbf v$?**

Imagine a transformation as a machine:

1. Put an input vector $\mathbf x$ into the machine.
2. The matrix $A$ transforms it.
3. The output is $A\mathbf x$.
4. We want that output to equal the particular target $\mathbf v$.

This lets us think about a system of several equations as one geometric question: find the input vector that gets mapped to the required output.

### A small numerical example

For the system

$$
\begin{aligned}
2x+y&=5\\
x+3y&=7,
\end{aligned}
$$

the matrix equation is

$$
\begin{bmatrix}2&1\\1&3\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}5\\7\end{bmatrix}.
$$

The vector $(x,y)$ is the input. The matrix transforms it. We seek the input whose output is $(5,7)$.

The lecture now separates the possibilities according to whether the transformation squashes space into a lower dimension. For a 2 × 2 matrix, the determinant tells us whether this collapse occurs:

- non-zero determinant: the transformation keeps the full 2D space;
- zero determinant: the transformation collapses the plane into a line or a point.

## 5. Case one: non-zero determinant — there is an inverse

Start with the case where $A$ has a non-zero determinant.

The transformation does not squash the plane into a lower-dimensional space. In this case, every target vector $\mathbf v$ has exactly one input vector that maps to it.

Why exactly one?

- There is at least one input that maps to $\mathbf v$, because the transformation covers the full output space.
- There cannot be two different inputs mapping to the same output, because the transformation has not collapsed distinct directions together.

So we can reverse the transformation and trace the target $\mathbf v$ back to its unique input $\mathbf x$.

## 6. The inverse matrix: playing the transformation backwards

The reverse transformation is called the **inverse** of $A$, written:

$$
A^{-1}.
$$

The superscript $-1$ is notation for the inverse; it does not mean that every entry in the matrix is raised to the power $-1$.

two intuitive examples:

### Example A: reversing a rotation

- $A$: rotate counterclockwise by 90°.
- $A^{-1}$: rotate clockwise by 90°.

Applying the clockwise rotation undoes the counterclockwise rotation.

### Example B: reversing a shear

- $A$: shear to the right, moving $\hat{\mathbf j}$ one unit to the right.
- $A^{-1}$: shear to the left by the corresponding amount.

The reverse transformation restores the original positions.

### The defining property of an inverse

If we first apply $A$, and then apply $A^{-1}$, we return to where we started:

$$
A^{-1}(A\mathbf x)=\mathbf x.
$$

In matrix notation, applying one transformation after another is represented by matrix multiplication. Therefore,

$$
\boxed{A^{-1}A=I}.
$$

Here, $I$ is the **identity matrix**.

For a 2 × 2 transformation, the identity matrix is

$$
I=\begin{bmatrix}1&0\\0&1\end{bmatrix}.
$$

It represents doing nothing:

- $\hat{\mathbf i}=(1,0)$ stays where it is;
- $\hat{\mathbf j}=(0,1)$ stays where it is.

The lecture states the core inverse property in this order, $A^{-1}A=I$. For square invertible matrices, the reverse order also holds: $AA^{-1}=I$.

## 7. Use the inverse to solve the system

We start with:

$$
A\mathbf x=\mathbf v.
$$

Apply the inverse transformation to both sides:

$$
A^{-1}(A\mathbf x)=A^{-1}\mathbf v.
$$

Because $A^{-1}A=I$,

$$
I\mathbf x=A^{-1}\mathbf v.
$$

The identity matrix leaves a vector unchanged, so:

$$
\boxed{\mathbf x=A^{-1}\mathbf v}.
$$

Geometrically, this means we start at the target vector $\mathbf v$ and run the transformation backwards to find the original input.

Notes that in practice, a computer is often used to calculate the inverse.

### Worked example: find the unique input

Use

$$
A=\begin{bmatrix}2&1\\1&3\end{bmatrix},
\qquad
\mathbf v=\begin{bmatrix}5\\7\end{bmatrix}.
$$

The solution is $\mathbf x=(x,y)$. We can verify that $(x,y)=(\frac85,\frac95)$ satisfies the system:

$$
2\left(\frac85\right)+\frac95=\frac{25}{5}=5,
$$

$$
\frac85+3\left(\frac95\right)=\frac{35}{5}=7.
$$

So

$$
\mathbf x=\begin{bmatrix}8/5\\9/5\end{bmatrix}.
$$

This is an added arithmetic illustration of the equation-solving idea; the lecture itself does not teach the inverse-computation method.

## 8. The same idea works in higher dimensions

We now generalizes the idea beyond two equations and two unknowns.

If the number of equations equals the number of unknowns, the matrix is square. The same geometric picture applies:

- $A$ transforms an input vector $\mathbf x$;
- we want the output to equal $\mathbf v$;
- if $A$ does not squash the full space into a lower dimension, it has an inverse;
- applying $A^{-1}$ to $\mathbf v$ gives the unique input.

For a 3 × 3 matrix, a non-zero determinant means 3D space is not collapsed into a plane, line, or point. The transformation can be reversed.

## 9. Case two: zero determinant — no inverse

Now consider a matrix whose determinant is zero.

Its transformation squashes space into a smaller dimension. For example:

- a 2D plane may be squashed onto a line;
- a 3D space may be squashed onto a plane;
- a 3D space may be squashed onto a line or a point.

Why can we not reverse such a transformation?

Imagine that many different input points are flattened onto the same line. Once the transformation has happened, the output does not tell us which of those original points we started with.

To reverse it uniquely, we would need to send one output vector back to many possible input vectors. But a function assigns one output to each input; the proposed reverse would not be a function if one input had many possible outputs.

this as trying to “unsquish” a line back into a plane. A single point on the line could have come from an entire line of original points. There is no unique way to recover which one.

Therefore, a zero-determinant transformation has no inverse matrix.

## 10. No inverse does not automatically mean no solution

This is a very important distinction.

Even if $A$ has no inverse, the equation

$$
A\mathbf x=\mathbf v
$$

may still have a solution.

Suppose a 2D transformation squashes the entire plane onto the x-axis. Its possible outputs all lie on that line.

- If the target $\mathbf v$ lies on the x-axis, at least one input may map to it.
- If the target $\mathbf v$ lies somewhere off the x-axis, no input can map to it.

So the existence of a solution depends on whether the target vector is among the outputs that the transformation can produce.

for more precise language to describe that set of possible outputs.

## 11. Rank: how many dimensions survive the transformation?

Consider a 3D transformation.

- If all outputs lie on a line, the output has one dimension. The transformation has **rank 1**.
- If all outputs lie on a plane, the output has two dimensions. The transformation has **rank 2**.
- If the outputs fill all of 3D space, the transformation has **rank 3**.

Defines rank as:

$$
\boxed{\text{rank}=\text{number of dimensions in the output space}}.
$$

For a 2 × 2 matrix, rank 2 is the maximum possible. It means the transformation still spans the full 2D plane and its determinant is non-zero.

For a 3 × 3 matrix:

- rank 3 means full 3D output space;
- rank 2 means the output is a plane;
- rank 1 means the output is a line;
- rank 0 means every vector is sent to the origin.

Rank 2 in 3D is still a collapsed transformation, but it has retained more dimensions than rank 1.

## 12. Column space: the set of all possible outputs

We now names the set of all possible outputs of a matrix transformation.

This set is called the **column space** of the matrix.

Why that name?

The columns of a matrix tell us where the standard basis vectors land. Any input vector is a combination of the standard basis vectors. Because the transformation is linear, its output is the same combination of the transformed basis vectors.

Therefore, every possible output is a linear combination of the columns of $A$.

The set of all linear combinations of the columns is called their **span**.

So:

$$
\boxed{\operatorname{Col}(A)=\text{span of the columns of }A}.
$$

In simpler language, the column space contains every vector the matrix can possibly produce.

### Example

Consider

$$
A=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$

Its columns are

$$
\mathbf c_1=\begin{bmatrix}2\\1\end{bmatrix},
\qquad
\mathbf c_2=\begin{bmatrix}1\\2\end{bmatrix}.
$$

The column space contains all vectors of the form

$$
s\begin{bmatrix}2\\1\end{bmatrix}
+t\begin{bmatrix}1\\2\end{bmatrix},
$$

where $s$ and $t$ can be any real numbers.

These two columns point in different, non-parallel directions, so their span is the entire 2D plane.

The determinant is $2(2)-1(1)=3$, which is non-zero, consistent with the fact that the output fills the plane.

## 13. Rank is the dimension of the column space

Sharpens the definition of rank:

$$
\boxed{\operatorname{rank}(A)=\dim(\operatorname{Col}(A))}.
$$

That means rank counts how many independent directions are available in the output.

| Output set | Dimension | Rank |
|---|---:|---:|
| A line | 1 | 1 |
| A plane | 2 | 2 |
| All of 3D space | 3 | 3 |

When rank is as high as it can be—equal to the number of columns—we call the matrix **full rank**.

For an $n$-column matrix, full column rank means rank $n$.

Also points out that the zero vector is always in the column space. A linear transformation must keep the origin fixed, so the zero input always produces the zero output.

## 14. Null space: all inputs that become zero

Now changes attention from outputs to inputs.

For a full-rank transformation, the only input that lands at the origin is the zero vector itself.

But when a transformation squashes space into a lower dimension, many different inputs can be sent to the zero vector.

The set of all such inputs is called the **null space** or the **kernel** of the matrix.

$$
\boxed{\operatorname{Null}(A)=\{\mathbf x:A\mathbf x=\mathbf 0\}}.
$$

Read this as: the null space contains every input vector $\mathbf x$ that the matrix transforms into the zero vector.

### 14.1 Example: a 2D plane squashed onto a line

Consider

$$
A=\begin{bmatrix}1&1\\0&0\end{bmatrix}.
$$

For an input vector

$$
\mathbf x=\begin{bmatrix}x\\y\end{bmatrix},
$$

the output is

$$
A\mathbf x=
\begin{bmatrix}x+y\\0\end{bmatrix}.
$$

To find the null space, ask when the output is zero:

$$
\begin{bmatrix}x+y\\0\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}.
$$

This requires

$$
x+y=0,\quad\text{so}\quad y=-x.
$$

Therefore, all vectors of the form

$$
\begin{bmatrix}t\\-t\end{bmatrix}
=t\begin{bmatrix}1\\-1\end{bmatrix}
$$

belong to the null space.

These vectors form a line. Every vector on that line is squashed to the origin by $A$.

For instance,

$$
A\begin{bmatrix}1\\-1\end{bmatrix}
=
\begin{bmatrix}1-1\\0\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}.
$$

### 14.2 What happens in 3D?

two geometric examples:

- If 3D space is squashed onto a plane, there is a line of input vectors that land at the origin.
- If 3D space is squashed onto a line, there is a plane of input vectors that land at the origin.

The null space describes the input directions that are completely lost by the transformation.

For example, consider the matrix

$$
A=\begin{bmatrix}1&0&0\\0&0&0\\0&0&0\end{bmatrix}.
$$

It maps

$$
(x,y,z)\longmapsto(x,0,0).
$$

Its output lies on the x-axis (rank 1). The null space is all vectors with $x=0$:

$$
\operatorname{Null}(A)=
\left\{
\begin{bmatrix}0\\y\\z\end{bmatrix}:y,z\in\mathbb R
\right\}.
$$

That is the entire yz-plane. Every vector in that plane is transformed to $(0,0,0)$.

## 15. Null space and solving a system with a zero target

Return to the equation:

$$
A\mathbf x=\mathbf v.
$$

If the target vector is the zero vector, the equation becomes:

$$
A\mathbf x=\mathbf 0.
$$

By definition, all solutions to this equation are exactly the vectors in the null space of $A$.

So the null space is not just a geometric curiosity. It tells us all possible solutions to the homogeneous system (a system whose right-hand side is zero).

## 16. Putting the ideas together

Summarizes the geometric viewpoint:

- Every linear system $A\mathbf x=\mathbf v$ corresponds to a linear transformation.
- If the transformation has an inverse, we can reverse it to find the unique input.
- If there is no inverse, the column space tells us which target vectors can be reached at all.
- The null space tells us which input vectors are mapped to zero, and therefore describes all solutions when the target is zero.

For a general target $\mathbf v$, a solution exists exactly when $\mathbf v$ belongs to the column space. If a solution exists but the null space contains nonzero vectors, then adding any null-space vector to a solution gives another solution:

$$
A(\mathbf x_0+\mathbf n)
=A\mathbf x_0+A\mathbf n
=\mathbf v+\mathbf 0
=\mathbf v.
$$

This last equation is an additional useful consequence of the definitions.

## 17. Scope of this lecture and what comes next

Explicitly limits the scope:

- The video does not teach how to compute inverses, rank, column space, or null space.
- It does not cover all cases where the number of equations differs from the number of unknowns.
- The emphasis is on geometric intuition, so future study of the computational methods has a clearer meaning.

The next video will be a brief footnote about **non-square matrices**. After that, this lesson plans to discuss dot products through the lens of linear transformations.

## 18. Key takeaways

- A linear system can be written as $A\mathbf x=\mathbf v$.
- Geometrically, this asks which input $\mathbf x$ is transformed by $A$ into the target $\mathbf v$.
- If a square matrix has non-zero determinant, it has an inverse and each target has exactly one input.
- The inverse undoes the transformation: $A^{-1}A=I$.
- A zero determinant means the transformation collapses space and has no inverse.
- A zero determinant does **not** automatically mean that a particular system has no solution.
- The column space is the set of all possible outputs: the span of the matrix's columns.
- Rank is the dimension of the column space.
- The null space is the set of inputs mapped to zero.
- When $\mathbf v=\mathbf 0$, the solutions of $A\mathbf x=\mathbf 0$ are exactly the null space.

## 19. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| $A^{-1}$ means taking the reciprocal of every entry. | It is the matrix representing the reverse transformation. |
| A zero determinant means no equation solution is possible. | A solution can exist if the target lies in the column space. |
| Column space is the same as the input space. | Column space is the set of outputs the matrix can produce. |
| Rank counts the number of nonzero entries. | Rank counts the dimension of the column space. |
| Null space is the set of outputs that are zero. | It is the set of **inputs** that map to the zero output. |
| If a system has no inverse, it cannot be solved. | It may have no solution or multiple solutions, depending on the target and the null space. |

## 20. Check your understanding

1. What does $A\mathbf x=\mathbf v$ ask geometrically?
2. What does an inverse transformation do?
3. What does $A^{-1}A=I$ mean?
4. If a 2D transformation squashes the plane onto a line, does it have an inverse?
5. Does zero determinant guarantee that every target vector has no solution?
6. What is the column space?
7. What does rank measure?
8. What is the null space?
9. If the right-hand side is zero, what set contains all solutions?
10. If $\mathbf x_0$ is one solution to $A\mathbf x=\mathbf v$, what happens when we add a null-space vector to it?

### Answers

1. Find an input vector that the transformation maps to the target vector.
2. It reverses the original transformation.
3. Applying $A$, then $A^{-1}$, returns every vector to its starting point.
4. No. The transformation has collapsed a dimension and cannot be uniquely reversed.
5. No. A solution exists if the target is in the column space.
6. The set of all possible outputs, equal to the span of the matrix columns.
7. The dimension of the column space.
8. All input vectors mapped to zero.
9. The null space.
10. It produces another solution, because the added vector maps to zero.
