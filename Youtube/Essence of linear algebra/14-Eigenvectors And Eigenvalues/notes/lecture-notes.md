# Lecture 14 — Eigenvectors and Eigenvalues

> **Learning goal:** Understand what eigenvectors and eigenvalues mean geometrically, how the determinant helps us find them, why some transformations have no real eigenvectors, and how an eigenbasis can make repeated matrix operations much easier.

This lesson follows the lecturer's sequence. It builds on matrices as linear transformations, determinants, linear systems, and change of basis.

## 1. Why this topic can feel unintuitive

Eigenvectors and eigenvalues can seem like a collection of strange calculations if we do not first understand what a matrix does to space.

The lecturer emphasizes that the foundations matter:

- A **matrix** can represent a linear transformation: a rule that moves vectors around while preserving vector addition and scalar multiplication.
- A **determinant** tells us whether a square transformation preserves area/volume or squashes space into a lower dimension.
- A **linear system** helps us find vectors that a transformation sends to zero.
- **Change of basis** lets us describe the same transformation from a different coordinate perspective.

The purpose of this lecture is to connect these ideas to one geometric question:

**Are there any special vectors that do not get turned away from their original line when a transformation acts on them?**

## 2. Start with a 2D transformation

Consider the matrix:

$$
A=\begin{bmatrix}3&1\\0&2\end{bmatrix}.
$$

Remember how to read a matrix as a transformation: its columns tell us where the standard basis vectors land.

The standard basis vectors are:

$$
\hat{\mathbf i}=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\hat{\mathbf j}=\begin{bmatrix}0\\1\end{bmatrix}.
$$

Apply $A$ to each one:

$$
A\hat{\mathbf i}
=
\begin{bmatrix}3&1\\0&2\end{bmatrix}
\begin{bmatrix}1\\0\end{bmatrix}
=
\begin{bmatrix}3\\0\end{bmatrix}.
$$

So $\hat{\mathbf i}$ moves to $(3,0)$, which is three times its original vector.

Similarly:

$$
A\hat{\mathbf j}
=
\begin{bmatrix}3&1\\0&2\end{bmatrix}
\begin{bmatrix}0\\1\end{bmatrix}
=
\begin{bmatrix}1\\2\end{bmatrix}.
$$

The matrix therefore sends the horizontal unit vector to $(3,0)$, and the vertical unit vector to $(1,2)$.

A general vector will usually change both its length and direction. In particular, its new tip will usually no longer lie on the same line through the origin as its old tip.

## 3. The special vectors that stay on their own line

Imagine drawing a line from the origin through a vector's tip. This line is called the vector's **span**.

Most vectors are moved off their original span by the transformation. But some special vectors remain on their own span.

That means the transformation does nothing to their direction. It only:

- stretches them;
- squishes them;
- or flips them and changes their length.

These special non-zero vectors are called **eigenvectors**.

The number describing the stretch, squish, or flip is the corresponding **eigenvalue**.

### 3.1 First special direction: the x-axis

The vector $\hat{\mathbf i}=(1,0)$ is sent to:

$$
A\begin{bmatrix}1\\0\end{bmatrix}
=
\begin{bmatrix}3\\0\end{bmatrix}
=3\begin{bmatrix}1\\0\end{bmatrix}.
$$

It stays on the x-axis and becomes three times as long.

Therefore:

- $(1,0)$ is an eigenvector.
- Its eigenvalue is $3$.
- Every non-zero vector along the x-axis is also an eigenvector with eigenvalue $3$.

Why do all vectors on the x-axis have the same property? Because of linearity. If $\mathbf v$ is stretched by 3, then any scalar multiple $c\mathbf v$ is also stretched by 3:

$$
A(c\mathbf v)=cA\mathbf v=c(3\mathbf v)=3(c\mathbf v).
$$

### 3.2 A less obvious special direction: (-1, 1)

The vector $(-1,1)$ is another eigenvector for this transformation.

Check it:

$$
\begin{aligned}
A\begin{bmatrix}-1\\1\end{bmatrix}
&=
\begin{bmatrix}3&1\\0&2\end{bmatrix}
\begin{bmatrix}-1\\1\end{bmatrix}\\
&=
\begin{bmatrix}-3+1\\0+2\end{bmatrix}\\
&=
\begin{bmatrix}-2\\2\end{bmatrix}\\
&=
2\begin{bmatrix}-1\\1\end{bmatrix}.
\end{aligned}
$$

It remains on its original diagonal line and is stretched by a factor of 2.

So:

- $(-1,1)$ is an eigenvector.
- Its eigenvalue is $2$.
- Every non-zero vector on the line through $(-1,1)$ is also an eigenvector with eigenvalue $2$.

### 3.3 What about a general vector?

Try $(1,2)$:

$$
A\begin{bmatrix}1\\2\end{bmatrix}
=
\begin{bmatrix}3+2\\4\end{bmatrix}
=
\begin{bmatrix}5\\4\end{bmatrix}.
$$

The result $(5,4)$ is not a scalar multiple of $(1,2)$. The direction has changed, so $(1,2)$ is not an eigenvector.

For this example, the two eigenvector directions are:

- the x-axis, with eigenvalue $3$;
- the line through $(-1,1)$, with eigenvalue $2$.

## 4. The formal equation: A v = λ v

The geometric idea can be written compactly:

$$
\boxed{A\mathbf v=\lambda\mathbf v}.
$$

Every symbol has a role:

- $A$: the matrix representing the transformation;
- $\mathbf v$: a non-zero eigenvector;
- $\lambda$: the eigenvalue, a scalar number;
- $A\mathbf v$: the vector after the transformation;
- $\lambda\mathbf v$: the original vector scaled by $\lambda$.

The equation says that applying the matrix has the same effect as simply scaling the eigenvector.

### 4.1 Positive, negative, and zero eigenvalues

The eigenvalue does not have to be positive.

- If $\lambda=3$, the vector is stretched to three times its length.
- If $\lambda=\frac12$, it is squished to half its length.
- If $\lambda=-\frac12$, it is flipped to the opposite direction and squished to half its length.
- If $\lambda=1$, it stays exactly where it is.
- If $\lambda=0$, it is sent to the zero vector. The original vector must still be non-zero to qualify as an eigenvector.

An eigenvector is allowed to point in the opposite direction after the transformation. What matters is that it stays on the same line through the origin.

## 5. Why eigenvectors are useful: the axis of a 3D rotation

Imagine a 3D object rotating around a fixed axis.

Most vectors move as the object rotates. But a vector pointing along the rotation axis stays on that axis.

That direction is an eigenvector of the rotation.

For a pure rotation, lengths are preserved. Therefore, the vector along the rotation axis is not stretched or squished:

$$
A\mathbf v=1\mathbf v.
$$

Its eigenvalue is $1$.

This is useful because describing a 3D rotation using its axis and angle can be more intuitive than trying to understand every entry of a 3 × 3 matrix.

## 6. A more revealing way to understand a transformation

A matrix can always be understood by looking at where its basis vectors land. But that description depends on the coordinate system.

Eigenvectors reveal special directions that are intrinsic to the transformation: directions that the transformation only scales.

They can therefore expose the central behavior of a transformation more clearly than simply reading its columns.

The lecturer now turns from the geometric meaning to the calculation method.

## 7. Turn the eigenvector equation into a linear system

Start with:

$$
A\mathbf v=\lambda\mathbf v.
$$

The left side is matrix-vector multiplication. The right side is scalar-vector multiplication.

To make both sides look like matrix-vector multiplication, use the identity matrix.

The identity matrix leaves every vector unchanged:

$$
I\mathbf v=\mathbf v.
$$

Therefore:

$$
\lambda\mathbf v=\lambda I\mathbf v.
$$

For a 2D problem:

$$
\lambda I=
\begin{bmatrix}\lambda&0\\0&\lambda\end{bmatrix}.
$$

This matrix scales both coordinate directions by $\lambda$.

Now rewrite the eigenvector equation:

$$
A\mathbf v=\lambda I\mathbf v.
$$

Move everything to the left:

$$
A\mathbf v-\lambda I\mathbf v=0.
$$

Factor out the common vector:

$$
\boxed{(A-\lambda I)\mathbf v=0}.
$$

This is now a homogeneous system of linear equations.

We are looking for a **non-zero** vector $\mathbf v$ that the matrix $A-\lambda I$ sends to zero.

## 8. Why the determinant must equal zero

There is always one uninteresting solution to:

$$
(A-\lambda I)\mathbf v=0,
$$

namely $\mathbf v=0$.

But the zero vector cannot be an eigenvector. We need a non-zero solution.

The lecturer connects this to determinants and linear systems:

- If a square matrix has a non-zero determinant, it is invertible.
- An invertible matrix sends only the zero vector to zero.
- Therefore, if a non-zero solution exists, the matrix must be non-invertible.
- A square matrix is non-invertible exactly when its determinant is zero.

So the condition for a possible eigenvalue is:

$$
\boxed{\det(A-\lambda I)=0}.
$$

This equation is called the **characteristic equation**.

Its left-hand side, when expanded, becomes a polynomial in $\lambda$, called the **characteristic polynomial**.

The values of $\lambda$ that solve this equation are the eigenvalues.

## 9. The lecturer's first determinant example

The lecturer considers:

$$
A=\begin{bmatrix}2&2\\1&3\end{bmatrix}.
$$

Subtract $\lambda$ from the diagonal entries:

$$
A-\lambda I=
\begin{bmatrix}
2-\lambda&2\\
1&3-\lambda
\end{bmatrix}.
$$

For a 2 × 2 matrix:

$$
\det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc.
$$

Therefore:

$$
\begin{aligned}
\det(A-\lambda I)
&=(2-\lambda)(3-\lambda)-(2)(1)\\
&=6-5\lambda+\lambda^2-2\\
&=\lambda^2-5\lambda+4.
\end{aligned}
$$

Set the determinant equal to zero:

$$
\lambda^2-5\lambda+4=0.
$$

Factor:

$$
(\lambda-1)(\lambda-4)=0.
$$

So the eigenvalues are:

$$
\boxed{\lambda=1\quad\text{or}\quad\lambda=4}.
$$

The lecture uses $\lambda=1$ to illustrate the idea that the adjusted matrix becomes singular and sends some non-zero vector to zero.

**Important:** The determinant calculation finds possible eigenvalues. We still need to solve the corresponding linear system to find their eigenvectors.

## 10. Connect the determinant condition back to geometry

Suppose we find an eigenvalue $\lambda$ for which:

$$
\det(A-\lambda I)=0.
$$

That means the transformation represented by $A-\lambda I$ squashes the plane onto a line or into an even lower-dimensional space.

Consequently, at least one non-zero vector $\mathbf v$ is sent to zero:

$$
(A-\lambda I)\mathbf v=0.
$$

Rearranging gives:

$$
A\mathbf v=\lambda\mathbf v.
$$

That is precisely the eigenvector equation.

So the determinant method is not a random algebraic trick. It is looking for a value of $\lambda$ that makes the adjusted transformation collapse at least one direction.

## 11. Find eigenvalues and eigenvectors for the opening example

Return to:

$$
A=\begin{bmatrix}3&1\\0&2\end{bmatrix}.
$$

First calculate:

$$
A-\lambda I=
\begin{bmatrix}
3-\lambda&1\\
0&2-\lambda
\end{bmatrix}.
$$

Its determinant is:

$$
\begin{aligned}
\det(A-\lambda I)
&=(3-\lambda)(2-\lambda)-(1)(0)\\
&=(3-\lambda)(2-\lambda).
\end{aligned}
$$

Set it to zero:

$$
(3-\lambda)(2-\lambda)=0.
$$

Therefore:

$$
\boxed{\lambda=3\quad\text{or}\quad\lambda=2}.
$$

### 11.1 Find the eigenvectors for λ = 3

Substitute $\lambda=3$:

$$
A-3I=
\begin{bmatrix}0&1\\0&-1\end{bmatrix}.
$$

Solve:

$$
\begin{bmatrix}0&1\\0&-1\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}.
$$

The equations say:

$$
y=0.
$$

There is no restriction on $x$, except that the vector must be non-zero.

So all eigenvectors for $\lambda=3$ have the form:

$$
\boxed{\mathbf v=t\begin{bmatrix}1\\0\end{bmatrix},\quad t\ne0}.
$$

These are exactly the non-zero vectors on the x-axis.

### 11.2 Find the eigenvectors for λ = 2

Substitute $\lambda=2$:

$$
A-2I=
\begin{bmatrix}1&1\\0&0\end{bmatrix}.
$$

Solve:

$$
\begin{bmatrix}1&1\\0&0\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}.
$$

The first equation is:

$$
x+y=0.
$$

Therefore:

$$
x=-y.
$$

All non-zero solutions are:

$$
\boxed{\mathbf v=t\begin{bmatrix}-1\\1\end{bmatrix},\quad t\ne0}.
$$

These are exactly the vectors along the diagonal direction from the geometric example.

The algebra has recovered the same two special directions that we found by looking at the transformation.

## 12. A transformation may have no real eigenvectors: 90-degree rotation

Now consider a 90-degree counterclockwise rotation:

$$
R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}.
$$

Every non-zero real vector is turned by 90 degrees. It cannot remain on its original line.

Calculate the characteristic determinant:

$$
R-\lambda I=
\begin{bmatrix}
-\lambda&-1\\
1&-\lambda
\end{bmatrix}.
$$

Then:

$$
\det(R-\lambda I)=\lambda^2+1.
$$

Set it to zero:

$$
\lambda^2+1=0.
$$

So:

$$
\lambda^2=-1
\quad\Longrightarrow\quad
\lambda=\pm i.
$$

These are imaginary (complex) numbers, not real numbers.

Therefore, this 2D rotation has **no real eigenvalues and no real eigenvectors**.

The lecturer's point is that a real vector in the plane cannot be rotated by 90 degrees and still stay on its original line.

## 13. Another example: a shear

A shear slants the plane. In the lecturer's example, the horizontal basis vector remains fixed, while the vertical basis vector moves one unit to the right.

The matrix is:

$$
S=\begin{bmatrix}1&1\\0&1\end{bmatrix}.
$$

The characteristic determinant is:

$$
\begin{aligned}
\det(S-\lambda I)
&=\det\begin{bmatrix}1-\lambda&1\\0&1-\lambda\end{bmatrix}\\
&=(1-\lambda)^2.
\end{aligned}
$$

The only eigenvalue is:

$$
\boxed{\lambda=1}.
$$

To find the eigenvectors:

$$
S-I=
\begin{bmatrix}0&1\\0&0\end{bmatrix}.
$$

The equation $(S-I)\mathbf v=0$ gives $y=0$.

Thus all non-zero vectors along the x-axis are eigenvectors, and they remain fixed.

There are no other eigenvector directions.

This illustrates an important distinction: having an eigenvalue does not guarantee that there are enough independent eigenvectors to span the entire space.

## 14. One eigenvalue can have many eigenvectors: uniform scaling

Consider a transformation that scales every vector in the plane by 2:

$$
B=\begin{bmatrix}2&0\\0&2\end{bmatrix}=2I.
$$

For every vector $\mathbf v$:

$$
B\mathbf v=2\mathbf v.
$$

So every non-zero vector is an eigenvector with eigenvalue 2.

There is only one distinct eigenvalue, but there are infinitely many eigenvector directions.

This is different from the shear example, where only one line of eigenvectors exists.

## 15. An eigenbasis: choose eigenvectors as the coordinate directions

The lecturer now returns to the idea of changing basis.

Imagine choosing a basis in which both basis vectors are eigenvectors.

For example:

- The first basis vector is multiplied by $-1$.
- The second basis vector is multiplied by $2$.

The transformation matrix in that basis is:

$$
D=\begin{bmatrix}-1&0\\0&2\end{bmatrix}.
$$

Notice that the eigenvalues appear on the diagonal, and all the other entries are zero.

A matrix with zeros everywhere except possibly on the main diagonal is called a **diagonal matrix**.

A basis made entirely of eigenvectors is called an **eigenbasis**.

Why is this useful?

Because the transformation becomes very easy to understand: each coordinate direction is simply scaled by its corresponding eigenvalue.

## 16. Why diagonal matrices make repeated transformations easier

Suppose we apply the same transformation many times.

With a diagonal matrix:

$$
D=\begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix},
$$

applying it once scales the first coordinate by $\lambda_1$ and the second by $\lambda_2$.

Applying it twice scales them by:

$$
\lambda_1^2,\qquad \lambda_2^2.
$$

Applying it 100 times scales them by:

$$
\lambda_1^{100},\qquad \lambda_2^{100}.
$$

Therefore:

$$
\boxed{
D^{100}=
\begin{bmatrix}
\lambda_1^{100}&0\\
0&\lambda_2^{100}
\end{bmatrix}}.
$$

Compare that with calculating the 100th power of a general non-diagonal matrix, which can involve much more work.

## 17. Changing to an eigenbasis

Usually, the standard basis vectors are not eigenvectors.

But if we can find enough independent eigenvectors to form a basis, we can change our coordinate system so that those eigenvectors become the new basis vectors.

Let the eigenvectors be the columns of a matrix $P$:

$$
P=\begin{bmatrix}|&|\\
\mathbf v_1&\mathbf v_2\\
|&|
\end{bmatrix}.
$$

Let $M$ be the original transformation matrix.

From the previous lecture on change of basis, the matrix in the new basis is:

$$
\boxed{D=P^{-1}MP}.
$$

Here:

- $P$ converts eigenbasis coordinates into standard coordinates.
- $M$ applies the original transformation.
- $P^{-1}$ converts the result back into eigenbasis coordinates.

Because the new basis vectors are eigenvectors, the resulting matrix $D$ is diagonal. Its diagonal entries are the corresponding eigenvalues.

This process is called **diagonalization**.

Rearranging:

$$
M=PDP^{-1}.
$$

For powers:

$$
\boxed{M^n=PD^nP^{-1}}.
$$

This gives us a practical strategy:

1. Find the eigenvalues.
2. Find enough independent eigenvectors to form an eigenbasis.
3. Put the eigenvectors into the columns of $P$.
4. Construct the diagonal matrix $D$ from their eigenvalues.
5. Calculate $D^n$, which is easy.
6. Convert back using $P$ and $P^{-1}$.

## 18. Not every matrix can be diagonalized

The lecturer gives the shear as an example.

Its eigenvectors all lie on the x-axis. A single line cannot provide two linearly independent vectors in 2D.

So there is no eigenbasis for the shear, and it cannot be diagonalized using an ordinary basis of eigenvectors.

The key requirement is not merely having eigenvalues. We need enough linearly independent eigenvectors to span the full space.

For an $n$-dimensional space, we need $n$ linearly independent eigenvectors.

## 19. Complete lecture recap

The lecturer's reasoning follows this chain:

1. A matrix represents a transformation of space.
2. Most vectors change direction under that transformation.
3. Some special vectors remain on their original span.
4. Those vectors are eigenvectors.
5. Their scaling factors are eigenvalues.
6. The equation $A\mathbf v=\lambda\mathbf v$ describes this property.
7. Rearranging gives $(A-\lambda I)\mathbf v=0$.
8. A non-zero solution requires $\det(A-\lambda I)=0$.
9. Solve that determinant equation to find eigenvalues.
10. Substitute each eigenvalue back into the linear system to find its eigenvectors.
11. If enough independent eigenvectors exist, they can form an eigenbasis.
12. In an eigenbasis, the transformation matrix becomes diagonal.
13. Diagonal matrices make repeated applications of a transformation much easier to calculate.

## 20. Formula reference

| Concept | Formula |
|---|---|
| Eigenvector equation | $A\mathbf v=\lambda\mathbf v$ |
| Rearranged equation | $(A-\lambda I)\mathbf v=0$ |
| Characteristic equation | $\det(A-\lambda I)=0$ |
| Eigenbasis change of basis | $D=P^{-1}MP$ |
| Original matrix from diagonal form | $M=PDP^{-1}$ |
| Matrix power using diagonalization | $M^n=PD^nP^{-1}$ |
| Power of a diagonal matrix | $D^n=\operatorname{diag}(\lambda_1^n,\ldots,\lambda_n^n)$ |

## 21. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| Every vector is an eigenvector. | Only non-zero vectors that remain on their original span are eigenvectors. |
| An eigenvector must remain exactly the same length. | It can stretch, shrink, or flip. |
| An eigenvalue must be positive. | It can be negative, zero, or complex, depending on the setting. |
| Every matrix has real eigenvectors. | A 90-degree 2D rotation has no real eigenvectors. |
| Finding eigenvalues completes the problem. | We must also solve for the corresponding eigenvectors. |
| One eigenvalue means one eigenvector. | An eigenvalue can have an entire line or even a whole plane of eigenvectors. |
| Every matrix can be diagonalized. | It needs enough independent eigenvectors to form a basis. |
| Diagonalization changes the underlying transformation. | It changes the coordinate description, not the geometric transformation. |

## 22. Check your understanding

1. What does it mean geometrically for a vector to be an eigenvector?
2. What is the difference between an eigenvector and its eigenvalue?
3. Why is the x-axis an eigenvector direction for the matrix $\begin{bmatrix}3&1\\0&2\end{bmatrix}$?
4. Verify that $(-1,1)$ is an eigenvector of that matrix.
5. Why do we rewrite $\lambda\mathbf v$ as $\lambda I\mathbf v$?
6. Why must $\det(A-\lambda I)=0$ for a non-zero eigenvector to exist?
7. What are the eigenvalues of the opening example?
8. Why does a 90-degree rotation in 2D have no real eigenvectors?
9. What are the eigenvectors of the shear in the lecture?
10. What is an eigenbasis?
11. Why does diagonalization make repeated matrix powers easier?
12. Why can the shear not be diagonalized using an eigenbasis in 2D?

### Answers

1. The transformed vector stays on the same line through the origin; it may be scaled or flipped.
2. The eigenvector is the special direction; the eigenvalue is the scalar factor applied to it.
3. $A(1,0)=(3,0)=3(1,0)$.
4. $A(-1,1)=(-2,2)=2(-1,1)$.
5. It lets us express both sides as matrix-vector multiplication and factor out the vector.
6. A non-zero solution to the homogeneous system exists only when the square matrix is singular, which is equivalent to a zero determinant.
7. $3$ and $2$.
8. Every non-zero real vector is turned 90 degrees away from its original line.
9. All non-zero vectors along the x-axis.
10. A basis whose vectors are all eigenvectors of the transformation.
11. Powers of a diagonal matrix are found by raising each diagonal entry to that power.
12. Its eigenvectors all lie on one line, so there are not two independent eigenvectors to form a 2D basis.

## 23. Scope note: the final puzzle

The lecturer mentions a puzzle shown on screen near the end of the video, but the supplied transcript does not contain the puzzle's actual wording or data. It is therefore not reconstructed here. The transcript does state that the next and final video in the series will discuss abstract vector spaces.
