# Lecture 13 — Change of Basis

> **Learning goal:** Understand how the same vector or linear transformation can have different coordinate descriptions depending on the chosen basis, and learn how to convert between those descriptions.

These notes follow the lecture's teaching sequence. The lecturer uses two coordinate systems: the standard system (our system) and Jennifer's system.

## 1. Coordinates are instructions for combining basis vectors

Imagine a vector whose standard coordinates are:

$$
\begin{bmatrix}3\\2\end{bmatrix}.
$$

In the familiar grid, this means move 3 units right and 2 units up.

The linear-algebra interpretation is slightly different: coordinates are scalars that multiply special unit vectors.

The standard basis vectors are:

$$
\hat{\mathbf i}=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\hat{\mathbf j}=\begin{bmatrix}0\\1\end{bmatrix}.
$$

So the vector $(3,2)$ means:

$$
3\hat{\mathbf i}+2\hat{\mathbf j}.
$$

In other words, scale the first basis vector by 3, scale the second by 2, and add the results.

**Key idea:** Coordinates only have meaning relative to a chosen set of basis vectors.

## 2. A different person can use a different basis

The lecturer introduces a friend, Jennifer, who describes the same 2D space using two different basis vectors:

$$
\mathbf b_1=\begin{bmatrix}2\\1\end{bmatrix},
\qquad
\mathbf b_2=\begin{bmatrix}-1\\1\end{bmatrix}.
$$

These coordinates are written in our standard coordinate system.

Jennifer's basis vectors mean:

- Her first coordinate scales $\mathbf b_1$.
- Her second coordinate scales $\mathbf b_2$.
- She adds the two scaled vectors.

From Jennifer's point of view, her own basis vectors have coordinates:

$$
\mathbf b_1=\begin{bmatrix}1\\0\end{bmatrix}_{J},
\qquad
\mathbf b_2=\begin{bmatrix}0\\1\end{bmatrix}_{J}.
$$

That is because her basis vectors define what the coordinate pairs $(1,0)$ and $(0,1)$ mean in her system.

We are not looking at different physical vectors. We are using different coordinate languages to describe the same space.

## 3. The grid is a visual aid, not the space itself

The lecturer points out that the familiar square grid is just a way to visualize our coordinate system.

Space itself does not come with a built-in grid.

Jennifer could draw her own grid based on her basis vectors:

- The origin is the same for both coordinate systems.
- Her axes point in the directions of $\mathbf b_1$ and $\mathbf b_2$.
- Her grid spacing is determined by those basis vectors.

The grid changes because the basis changes. The underlying vectors and points do not.

## 4. Build the change-of-basis matrix

To translate Jennifer's coordinates into our standard coordinates, put Jennifer's basis vectors into the columns of a matrix:

$$
A=
\begin{bmatrix}
|&|\\
\mathbf b_1&\mathbf b_2\\
|&|
\end{bmatrix}
=
\begin{bmatrix}
2&-1\\
1&1
\end{bmatrix}.
$$

This matrix is the **change-of-basis matrix from Jennifer's coordinates to standard coordinates**.

Why does this work?

Suppose Jennifer describes a vector using coordinates:

$$
\mathbf c_J=\begin{bmatrix}a\\b\end{bmatrix}.
$$

She means:

$$
a\mathbf b_1+b\mathbf b_2.
$$

Multiplying by $A$ performs exactly that combination:

$$
\boxed{\mathbf c_{\text{standard}}=A\mathbf c_J}.
$$

The columns of $A$ are Jennifer's basis vectors written in our language.

## 5. Worked example: Jennifer's coordinates to ours

Jennifer describes a vector as:

$$
\mathbf c_J=\begin{bmatrix}-1\\2\end{bmatrix}.
$$

That means:

$$
-\mathbf b_1+2\mathbf b_2.
$$

Substitute the basis vectors:

$$
-\begin{bmatrix}2\\1\end{bmatrix}
+2\begin{bmatrix}-1\\1\end{bmatrix}
=
\begin{bmatrix}-2\\-1\end{bmatrix}
+\begin{bmatrix}-2\\2\end{bmatrix}
=
\boxed{\begin{bmatrix}-4\\1\end{bmatrix}}.
$$

The matrix multiplication gives the same answer:

$$
A\begin{bmatrix}-1\\2\end{bmatrix}
=
\begin{bmatrix}2&-1\\1&1\end{bmatrix}
\begin{bmatrix}-1\\2\end{bmatrix}
=
\begin{bmatrix}-4\\1\end{bmatrix}.
$$

So Jennifer's coordinate pair $(-1,2)$ describes the same vector that we call $(-4,1)$.

## 6. Why matrix multiplication is a transformation

The lecturer connects this to the earlier lesson on linear transformations.

A matrix whose columns are the images of the standard basis vectors tells us where those basis vectors go.

For this matrix:

$$
A\hat{\mathbf i}=\mathbf b_1,
\qquad
A\hat{\mathbf j}=\mathbf b_2.
$$

So geometrically, $A$ moves the standard basis vectors to Jennifer's basis vectors.

If we start with a vector described in Jennifer's coordinates and apply $A$, we get the actual vector expressed in our standard coordinates.

The lecturer describes this as correcting our initial "misconception" of what Jennifer means by a pair of numbers: we first interpret the numbers using our own basis, then the transformation moves that interpretation to the vector Jennifer intended.

## 7. Convert from standard coordinates to Jennifer's coordinates

To go in the opposite direction, use the inverse matrix.

The inverse transformation reverses what $A$ does:

$$
\boxed{\mathbf c_J=A^{-1}\mathbf c_{\text{standard}}}.
$$

For Jennifer's basis matrix:

$$
A=
\begin{bmatrix}2&-1\\1&1\end{bmatrix},
$$

the inverse is:

$$
A^{-1}=
\begin{bmatrix}
\frac13&\frac13\\
-\frac13&\frac23
\end{bmatrix}.
$$

The two matrices undo one another:

$$
A^{-1}A=I,
\qquad AA^{-1}=I.
$$

## 8. Worked example: our coordinates to Jennifer's

We describe a vector in standard coordinates as:

$$
\mathbf c_{\text{standard}}=
\begin{bmatrix}3\\2\end{bmatrix}.
$$

To find Jennifer's coordinates:

$$
\begin{aligned}
\mathbf c_J
&=A^{-1}\mathbf c_{\text{standard}}\\
&=
\begin{bmatrix}
\frac13&\frac13\\
-\frac13&\frac23
\end{bmatrix}
\begin{bmatrix}3\\2\end{bmatrix}\\
&=
\boxed{\begin{bmatrix}\frac53\\\frac13\end{bmatrix}}.
\end{aligned}
$$

Check by rebuilding the vector from Jennifer's basis:

$$
\frac53\begin{bmatrix}2\\1\end{bmatrix}
+\frac13\begin{bmatrix}-1\\1\end{bmatrix}
=
\begin{bmatrix}3\\2\end{bmatrix}.
$$

Both descriptions refer to the same vector.

## 9. A change of basis also changes the matrix of a transformation

So far, we have converted the coordinates of individual vectors.

But a linear transformation is also represented by a matrix, and that matrix depends on the basis being used.

The lecturer uses a 90-degree counterclockwise rotation as an example.

In standard coordinates, the rotation matrix is:

$$
M=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}.
$$

Why these columns?

- The first column tells us where $\hat{\mathbf i}$ goes: $(0,1)$.
- The second column tells us where $\hat{\mathbf j}$ goes: $(-1,0)$.

This is the same geometric rotation, but the matrix was built using our standard basis and standard coordinates.

Jennifer needs a matrix that tells her where **her** basis vectors go, with the results expressed in **her** coordinates.

Simply changing the coordinates of the columns of $M$ is not enough, because those columns describe what happens to our basis vectors, not Jennifer's.

## 10. The three-step process for changing a transformation matrix

Start with a vector expressed in Jennifer's coordinates.

To apply the transformation correctly:

1. Convert Jennifer's coordinates into standard coordinates using $A$.
2. Apply the transformation in standard coordinates using $M$.
3. Convert the result back into Jennifer's coordinates using $A^{-1}$.

As a matrix product, the order is:

$$
\boxed{M_J=A^{-1}MA}.
$$

Remember that matrices act from right to left:

- $A$ converts Jennifer coordinates to standard coordinates.
- $M$ performs the transformation in standard coordinates.
- $A^{-1}$ converts the transformed vector back to Jennifer coordinates.

The final matrix $M_J$ takes Jennifer coordinates as input and returns Jennifer coordinates as output.

## 11. Worked example: 90-degree rotation in Jennifer's coordinates

We already have:

$$
A=
\begin{bmatrix}2&-1\\1&1\end{bmatrix},
\quad
A^{-1}=
\begin{bmatrix}\frac13&\frac13\\-\frac13&\frac23\end{bmatrix},
\quad
M=
\begin{bmatrix}0&-1\\1&0\end{bmatrix}.
$$

Calculate:

$$
M_J=A^{-1}MA.
$$

The result is:

$$
\boxed{
M_J=
\begin{bmatrix}
\frac13&-\frac23\\
\frac53&-\frac13
\end{bmatrix}}.
$$

This is the same 90-degree counterclockwise rotation, but represented in Jennifer's coordinate system.

If Jennifer multiplies this matrix by the coordinates of any vector in her system, she gets the rotated vector, still expressed in her system.

## 12. The "change of perspective" intuition

The lecturer gives a useful way to remember the expression:

$$
A^{-1}MA.
$$

Think of $M$ as the transformation described from our perspective.

The two outer matrices shift the description into and out of another coordinate system:

- $A$: Jennifer's coordinates to our coordinates.
- $M$: perform the transformation as we describe it.
- $A^{-1}$: return to Jennifer's coordinates.

The result is the same geometric transformation, but described in Jennifer's language.

The lecturer calls this a kind of mathematical empathy: seeing the same transformation from someone else's coordinate perspective.

## 13. Why change of basis matters

The lecturer closes by pointing toward the next topic: eigenvectors and eigenvalues.

Alternate coordinate systems are useful because a transformation can sometimes become much easier to understand when represented in a suitable basis.

The next video will give an important example of why this matters.

## 14. Quick reference: which matrix do I use?

| Goal | Formula | Meaning |
|---|---|---|
| Jennifer coordinates → standard coordinates | $\mathbf c_S=A\mathbf c_J$ | Combine Jennifer's basis vectors |
| Standard coordinates → Jennifer coordinates | $\mathbf c_J=A^{-1}\mathbf c_S$ | Express the vector in Jennifer's basis |
| Transformation matrix in Jennifer's basis | $M_J=A^{-1}MA$ | Convert in, transform, convert back |
| Jennifer's basis matrix | $A=[\mathbf b_1\ \mathbf b_2]$ | Basis vectors as columns |

## 15. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| A vector changes when we change its coordinates. | The vector stays the same; only its coordinate description changes. |
| The grid is part of space itself. | A grid is a visualization of a chosen coordinate system. |
| The columns of $A$ are Jennifer's coordinates for her basis vectors. | They are Jennifer's basis vectors written in standard coordinates. |
| $A$ and $A^{-1}$ do the same conversion. | $A$ converts Jennifer → standard; $A^{-1}$ converts standard → Jennifer. |
| To change a transformation matrix, just convert its columns. | The matrix must describe where the new basis vectors land, in the new coordinates; use $A^{-1}MA$. |
| $A^{-1}MA$ describes a different geometric transformation. | It describes the same transformation in a different basis. |

## 16. Check your understanding

1. What do the coordinates $(3,2)$ mean in the standard basis?
2. What are Jennifer's two basis vectors in standard coordinates?
3. What does Jennifer mean by coordinates $(-1,2)$?
4. What matrix converts Jennifer coordinates into standard coordinates?
5. What matrix converts standard coordinates into Jennifer coordinates?
6. Why is the inverse needed for the reverse conversion?
7. What do the columns of a transformation matrix represent?
8. Why can't we simply reuse the standard rotation matrix in Jennifer's coordinate system?
9. What are the three steps represented by $A^{-1}MA$?
10. What is the 90-degree rotation matrix in Jennifer's basis?

### Answers

1. $3\hat{\mathbf i}+2\hat{\mathbf j}$: three units along the standard x basis vector and two along the standard y basis vector.
2. $\mathbf b_1=(2,1)$ and $\mathbf b_2=(-1,1)$.
3. $-1\mathbf b_1+2\mathbf b_2=(-4,1)$ in standard coordinates.
4. $A=\begin{bmatrix}2&-1\\1&1\end{bmatrix}$.
5. $A^{-1}=\begin{bmatrix}1/3&1/3\\-1/3&2/3\end{bmatrix}$.
6. The inverse reverses the original coordinate conversion.
7. The images of the basis vectors, expressed in the coordinate system being used.
8. Its columns describe where the standard basis vectors go, not where Jennifer's basis vectors go.
9. Convert Jennifer → standard, apply the transformation, convert standard → Jennifer.
10. $\begin{bmatrix}1/3&-2/3\\5/3&-1/3\end{bmatrix}$.
