# Lecture 09 — Dot Products and Duality

> **Learning goal:** Understand the dot product in its numerical and geometric forms, then see why a vector can also represent a linear transformation from a multi-dimensional space to the number line.

These notes follow the sequence. The lecture first reviews the familiar dot product, then develops the deeper connection called **duality**. The emphasis is intuition rather than formal proofs.

## 1. Why introduce dot products this late?

Dot products are often introduced near the beginning of a linear algebra course. Deliberately postpones them because the usual introduction needs only basic vector knowledge, while a deeper understanding of their role becomes clearer after learning about linear transformations.

The lecture begins with the standard numerical and geometric interpretations, then asks a bigger question:

**Why should multiplying matching coordinates and adding them have anything to do with projecting one vector onto another?**

The answer will involve linear transformations from multiple dimensions down to one dimension, and a surprising correspondence called duality.

## 2. The numerical definition of the dot product

Take two vectors that have the same number of coordinates.

To calculate their dot product:

1. Pair up coordinates in the same position.
2. Multiply each pair.
3. Add all the products.

For two-dimensional vectors:

$$
\begin{bmatrix}1\\2\end{bmatrix}\cdot
\begin{bmatrix}3\\4\end{bmatrix}
=1(3)+2(4)=3+8=\boxed{11}.
$$

For the four-dimensional example in the lecture:

$$
(6,2,8,3)\cdot(1,8,5,3)
$$

$$
=6(1)+2(8)+8(5)+3(3)
=6+16+40+9
=\boxed{71}.
$$

In general, if

$$
\mathbf v=(v_1,v_2,\ldots,v_n),\qquad
\mathbf w=(w_1,w_2,\ldots,w_n),
$$

then

$$
\boxed{\mathbf v\cdot\mathbf w=
v_1w_1+v_2w_2+\cdots+v_nw_n}.
$$

Both vectors must have the same number of coordinates for this definition.

## 3. The geometric meaning: projection

The numerical rule is easy to calculate, but it does not immediately explain what the result means.

Here is a geometric interpretation.

Imagine two vectors, $\mathbf v$ and $\mathbf w$, starting at the origin.

1. Draw the line that passes through the origin and the tip of $\mathbf v$.
2. Project $\mathbf w$ onto that line.
3. Take the **signed length** of that projection.
4. Multiply it by the length of $\mathbf v$.

The result is the dot product:

$$
\boxed{\mathbf v\cdot\mathbf w
=\|\mathbf v\|\times
\text{signed length of }\operatorname{proj}_{\mathbf v}(\mathbf w)}.
$$

**Interactive:** Drag $\mathbf w$, change the angle between the vectors, or use presets (same direction, perpendicular, opposite). Watch the projection onto the line through $\mathbf v$ and see how the signed projection length times $\|\mathbf v\|$ matches $\mathbf v\cdot\mathbf w$.

<iframe
  src="../animations/animation-03-dot-product-projection.html"
  title="Dot product as signed projection onto v"
  width="100%"
  height="920"
  style="max-width:1150px;border:1px solid #dce4ef;border-radius:12px;background:#f4f7fb;"
  loading="lazy">
</iframe>

<p><a href="../animations/animation-03-dot-product-projection.html">Open Animation 03 — dot product projection in full tab</a> if the embed does not load.</p>

The word *signed* matters. If the projection points in the opposite direction to $\mathbf v$, its length is treated as negative.

### 3.1 Same direction, perpendicular, and opposite direction

The angle between the vectors gives us a quick way to understand the sign.

| Relationship | Dot product |
|---|---|
| Generally point in the same direction | Positive |
| Perpendicular (90° apart) | Zero |
| Generally point in opposite directions | Negative |

The familiar angle formula expresses this relationship:

$$
\boxed{\mathbf v\cdot\mathbf w
=\|\mathbf v\|\,\|\mathbf w\|\cos\theta}
$$

where $\theta$ is the angle between the two vectors.

Why does this formula fit the projection picture? The signed projection length of $\mathbf w$ onto the direction of $\mathbf v$ is $\|\mathbf w\|\cos\theta$. Multiplying by $\|\mathbf v\|$ gives the formula.

### 3.2 A simple example

Suppose $\|\mathbf v\|=4$, $\|\mathbf w\|=3$, and the angle between them is 60°.

$$
\mathbf v\cdot\mathbf w
=4\times3\times\cos60^\circ
=12\times\frac12
=\boxed{6}.
$$

The projection of $\mathbf w$ onto the direction of $\mathbf v$ has length $3/2$. Multiplying that by 4 gives 6.

## 4. Why does the order not matter?

The projection explanation can feel asymmetric:

- Project $\mathbf w$ onto $\mathbf v$, then multiply by the length of $\mathbf v$.
- Or project $\mathbf v$ onto $\mathbf w$, then multiply by the length of $\mathbf w$.

These look like different operations. Yet the dot product is symmetric:

$$
\boxed{\mathbf v\cdot\mathbf w=\mathbf w\cdot\mathbf v}.
$$

The reasoning builds an intuition for this in two stages.

### 4.1 First imagine vectors with equal lengths

If $\mathbf v$ and $\mathbf w$ have the same length, the two projection constructions are mirror images of one another.

Projecting $\mathbf w$ onto $\mathbf v$ and multiplying by $\|\mathbf v\|$ gives the same result as projecting $\mathbf v$ onto $\mathbf w$ and multiplying by $\|\mathbf w\|$.

### 4.2 Now scale one vector

Suppose we double $\mathbf v$, changing it to $2\mathbf v$.

Using the first interpretation:

- The projection of $\mathbf w$ onto the line through $\mathbf v$ has the same length, because the line's direction has not changed.
- The length of the vector we multiply by has doubled.
- So the dot product doubles.

Using the other interpretation:

- The projection of $\mathbf v$ onto $\mathbf w$ doubles in length.
- The length of $\mathbf w$ stays the same.
- So the dot product again doubles.

Both interpretations respond to scaling in the same way. The symmetry argument for equal-length vectors therefore extends to unequal lengths.

This helps explain why swapping the order does not change the result.

## 5. The deeper question: why does coordinate multiplication connect to projection?

At this point, Return to the puzzle:

Why should the numerical process of multiplying matching coordinates and adding them be related to projection?

The answer is to introduce a new kind of linear transformation: one that takes a vector in a multi-dimensional space and outputs a single number.

This is a transformation from 2D space to the number line.

## 6. Linear transformations from 2D to 1D

So far, many transformations in the series have taken vectors in 2D to other vectors in 2D, or vectors in 3D to other vectors in 3D.

Now consider a transformation that accepts a 2D vector, such as $(x,y)$, but outputs just one number.

For example:

$$
T(x,y)=x-2y.
$$

The input has two coordinates, but the output has one.

### 6.1 A visual test for linearity

Intentionally avoids formal definitions at this point and uses a visual property.

Imagine a line of evenly spaced dots in the input space. Apply the transformation and look at where those dots land on the number line.

- If the output dots remain evenly spaced, the transformation passes this visual test for linearity.
- If some evenly spaced input dots become unevenly spaced outputs, the transformation is not linear.

The key idea is that a linear transformation preserves this regular spacing.

### 6.2 A 1 × 2 matrix describes the transformation

As with the higher-dimensional transformations in earlier lectures, the transformation is completely determined by where the basis vectors land.

But now each basis vector lands on a single number:

- $\hat{\mathbf i}$ lands on one number.
- $\hat{\mathbf j}$ lands on another number.

Those two numbers form a 1 × 2 matrix:

$$
\begin{bmatrix}a&b\end{bmatrix}.
$$

The transformation acts on an input vector by matrix-vector multiplication:

$$
\begin{bmatrix}a&b\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=ax+by.
$$

## 7. Worked example: a transformation to the number line

Choose a transformation that sends:

$$
\hat{\mathbf i}\longmapsto 1,\qquad
\hat{\mathbf j}\longmapsto -2.
$$

Its matrix is:

$$
T=\begin{bmatrix}1&-2\end{bmatrix}.
$$

Consider the input vector $(4,3)$.

Break it into its basis-vector contributions:

$$
(4,3)=4\hat{\mathbf i}+3\hat{\mathbf j}.
$$

Because the transformation is linear, its output is:

$$
4(1)+3(-2)=4-6=\boxed{-2}.
$$

Numerically, this is just matrix-vector multiplication:

$$
\begin{bmatrix}1&-2\end{bmatrix}
\begin{bmatrix}4\\3\end{bmatrix}
=-2.
$$

Notice how similar this calculation looks to a dot product. The 1 × 2 matrix can be thought of as a 2D vector written sideways:

$$
\begin{bmatrix}1&-2\end{bmatrix}
\quad\longleftrightarrow\quad
\begin{bmatrix}1\\-2\end{bmatrix}.
$$

We now explores whether this numerical similarity has a deeper geometric meaning.

## 8. Build a projection onto a diagonal number line

Imagine taking a copy of the number line and placing it diagonally in the 2D plane, with zero at the origin.

The point labelled 1 on this diagonal number line is represented by a 2D unit vector. This section gives it the name:

$$
\hat{\mathbf u}.
$$

Because it is a unit vector:

$$
\|\hat{\mathbf u}\|=1.
$$

Now project every 2D input vector straight onto this diagonal line. The output is the number where the projection lands on the number line.

This defines a transformation:

$$
T:\mathbb R^2\longrightarrow\mathbb R.
$$

It takes a 2D vector and returns one number. Note that this transformation is linear, using the evenly-spaced-dots intuition.

An important distinction:

- The input vector $\hat{\mathbf u}$ is a 2D vector.
- The output of the transformation is a number on the number line.
- The diagonal line is drawn inside the 2D picture to help us visualize the number line; that does not change the fact that the output is one-dimensional.

## 9. The surprising symmetry: where do the basis vectors land?

To find the 1 × 2 matrix for this projection transformation, we need to find where $\hat{\mathbf i}$ and $\hat{\mathbf j}$ land.

Use a clever symmetry argument.

### 9.1 Where does $\hat{\mathbf i}$ land?

Both $\hat{\mathbf i}$ and $\hat{\mathbf u}$ are unit vectors.

Projecting $\hat{\mathbf i}$ onto the line through $\hat{\mathbf u}$ is geometrically symmetric to projecting $\hat{\mathbf u}$ onto the x-axis.

But projecting $\hat{\mathbf u}$ onto the x-axis simply gives its x-coordinate, $u_x$.

Therefore, the number where $\hat{\mathbf i}$ lands on the diagonal number line is:

$$
\boxed{u_x}.
$$

### 9.2 Where does $\hat{\mathbf j}$ land?

The same reasoning applies to the y direction.

Projecting $\hat{\mathbf j}$ onto the line through $\hat{\mathbf u}$ is symmetric to projecting $\hat{\mathbf u}$ onto the y-axis.

The y-coordinate of $\hat{\mathbf u}$ is $u_y$.

Therefore, the number where $\hat{\mathbf j}$ lands is:

$$
\boxed{u_y}.
$$

### 9.3 The matrix of the projection transformation

The two basis vectors land at $u_x$ and $u_y$, so the matrix is:

$$
\boxed{\begin{bmatrix}u_x&u_y\end{bmatrix}}.
$$

Apply this transformation to any vector $\mathbf v=(v_x,v_y)$:

$$
\begin{bmatrix}u_x&u_y\end{bmatrix}
\begin{bmatrix}v_x\\v_y\end{bmatrix}
=u_xv_x+u_yv_y.
$$

But this is exactly the dot product:

$$
\boxed{\mathbf u\cdot\mathbf v}.
$$

Since $\mathbf u$ is a unit vector, this dot product is the signed length of the projection of $\mathbf v$ onto the direction of $\mathbf u$.

This is the key connection this lesson wanted to reveal.

## 10. Why dotting with a unit vector gives a projection length

For a unit vector $\hat{\mathbf u}$, the angle formula gives:

$$
\mathbf v\cdot\hat{\mathbf u}
=\|\mathbf v\|\,\|\hat{\mathbf u}\|\cos\theta.
$$

Since $\|\hat{\mathbf u}\|=1$,

$$
\boxed{\mathbf v\cdot\hat{\mathbf u}
=\|\mathbf v\|\cos\theta}.
$$

The right-hand side is the signed length of the projection of $\mathbf v$ onto the direction of $\hat{\mathbf u}$.

So:

**Dotting a vector with a unit vector tells us how far along that unit vector's direction the original vector reaches.**

If the projection is in the opposite direction, the result is negative.

## 11. What changes when the vector is not a unit vector?

We now scales the unit vector $\hat{\mathbf u}$ by a factor of 3.

The new vector is:

$$
\mathbf a=3\hat{\mathbf u}.
$$

Its coordinates, and therefore the entries of the associated 1 × 2 matrix, are also multiplied by 3.

So the corresponding transformation is:

$$
\begin{bmatrix}3u_x&3u_y\end{bmatrix}.
$$

For an arbitrary vector $\mathbf v$, its output is:

$$
3u_xv_x+3u_yv_y
=3(\mathbf u\cdot\mathbf v).
$$

Geometrically, this means:

1. Project $\mathbf v$ onto the diagonal number line.
2. Take the signed length of that projection.
3. Multiply it by 3.

More generally, for any non-unit vector $\mathbf a$:

$$
\boxed{\mathbf a\cdot\mathbf v
=\|\mathbf a\|\times
\text{signed projection length of }\mathbf v
\text{ onto }\mathbf a}.
$$

This returns us to the geometric interpretation from the beginning of the lecture.

## 12. The big idea: duality

Now connects all the pieces.

We started with a vector and a familiar numerical operation called the dot product.

Then we considered a linear transformation from 2D space to the number line, defined geometrically by projecting onto a diagonal line.

Because the transformation is linear, it must have a 1 × 2 matrix.

That matrix can be viewed as a 2D vector written sideways. Applying it to an input vector is numerically the same as taking a dot product with the corresponding vector.

The conclusion is:

**Every linear transformation from a vector space to the number line corresponds to a unique vector in that space, in the sense that applying the transformation is the same as taking the dot product with that vector.**

This is an example of **duality**.

### 12.1 What does duality mean?

duality loosely as a natural but surprising correspondence between two different kinds of mathematical objects.

In this example:

- A vector corresponds to a linear transformation from the space to one dimension.
- A linear transformation from the space to one dimension corresponds to a vector.

The vector can be thought of as the physical representation of the transformation it encodes.

Instead of imagining an entire space being moved onto a number line, we can often use a vector and a dot product as a compact way to describe the same operation.

Emphasis: this is a conceptual connection, not merely two numerical procedures that happen to look alike.

## 13. Final summary

There are two useful levels at which to understand the dot product.

### The practical geometric view

The dot product:

- measures how much two vectors point in the same direction;
- is positive when they generally point the same way;
- is zero when they are perpendicular;
- is negative when they generally point in opposite directions;
- gives the length of one vector multiplied by the signed projection length of the other onto it.

### The deeper transformation view

A vector also encodes a linear transformation from the vector space to the number line.

Applying that transformation is equivalent to taking the dot product with the vector.

This correspondence between vectors and number-valued linear transformations is the duality introduced in the lecture.

The next video will show another example of duality through the **cross product**.

## 14. Key formulas

**Coordinate definition**

$$
\mathbf v\cdot\mathbf w=\sum_{i=1}^{n}v_iw_i.
$$

**Angle and projection definition**

$$
\mathbf v\cdot\mathbf w
=\|\mathbf v\|\,\|\mathbf w\|\cos\theta.
$$

**Symmetry**

$$
\mathbf v\cdot\mathbf w=\mathbf w\cdot\mathbf v.
$$

**A 2D-to-1D linear map**

$$
\begin{bmatrix}a&b\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=ax+by.
$$

**Projection onto a unit vector**

$$
\mathbf v\cdot\hat{\mathbf u}
=\|\mathbf v\|\cos\theta.
$$

**The duality connection**

$$
T(\mathbf v)=
\begin{bmatrix}u_x&u_y\end{bmatrix}
\begin{bmatrix}v_x\\v_y\end{bmatrix}
=\mathbf u\cdot\mathbf v.
$$

## 15. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| The dot product is just coordinate multiplication and addition. | That is the numerical rule; geometrically it measures a signed projection scaled by the other vector's length. |
| The dot product is always positive. | It can be positive, zero, or negative depending on the angle. |
| The order changes the result because the projection process looks different. | The dot product is symmetric: $\mathbf v\cdot\mathbf w=\mathbf w\cdot\mathbf v$. |
| A dot product with a unit vector gives the full length of the original vector. | It gives the signed component of the original vector along the unit vector's direction. |
| The diagonal number line's outputs are still 2D vectors. | The diagonal is a visual embedding; the transformation's output is one number. |
| Duality means vectors and transformations are literally the same object. | It means there is a natural correspondence: each such linear transformation can be represented by a unique vector through the dot product. |

## 16. Check your understanding

Try these before reading the answers.

1. Calculate $(1,2)\cdot(3,4)$.
2. What does a zero dot product tell you about two nonzero vectors?
3. Why can a dot product be negative?
4. Why is $\mathbf v\cdot\mathbf w=\mathbf w\cdot\mathbf v$?
5. What does a 1 × 2 matrix do to a 2D input vector?
6. If a linear transformation sends $\hat{\mathbf i}$ to 1 and $\hat{\mathbf j}$ to −2, what is its matrix?
7. What is the output of that transformation for input $(4,3)$?
8. If $\hat{\mathbf u}$ is a unit vector, what does $\mathbf v\cdot\hat{\mathbf u}$ represent?
9. Why are the entries of the projection matrix onto the line through $\hat{\mathbf u}$ equal to $u_x$ and $u_y$?
10. What is the duality connection in this lecture?

### Answers

1. $1(3)+2(4)=11$.
2. They are perpendicular.
3. The signed projection points in the direction opposite to the vector used as the projection axis.
4. The projection-and-scaling interpretations give the same result; algebraically, coordinate multiplication is commutative.
5. It maps the two input coordinates to one number.
6. $[1\ \ -2]$.
7. $1(4)-2(3)=-2$.
8. The signed length of the projection of $\mathbf v$ onto the direction of $\hat{\mathbf u}$.
9. By the symmetry of the projection geometry: projecting each standard basis vector onto the line through $\hat{\mathbf u}$ gives the corresponding coordinate of $\hat{\mathbf u}$.
10. A vector corresponds to a linear transformation to the number line, and applying that transformation is the same as taking a dot product with the vector.
