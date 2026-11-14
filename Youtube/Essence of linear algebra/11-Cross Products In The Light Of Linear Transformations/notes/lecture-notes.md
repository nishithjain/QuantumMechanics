# Lecture 11 — Cross Products in the Light of Linear Transformations

> **Learning goal:** Understand why the 3D cross product determinant mnemonic works, and how its algebraic formula is connected to its geometric meaning through linear transformations and duality.

These notes follow the lecturer's sequence. The video assumes that you have watched the earlier lessons on determinants and duality.

## 1. Where we left off: the unusual 3D determinant

In the previous lecture, we learned a computational method for finding the cross product of two 3D vectors.

Given two vectors $\mathbf v$ and $\mathbf w$, write:

$$
\mathbf v\times\mathbf w=
\det\begin{bmatrix}
\hat{\mathbf i}&v_x&w_x\\
\hat{\mathbf j}&v_y&w_y\\
\hat{\mathbf k}&v_z&w_z
\end{bmatrix}.
$$

The first column contains the basis-vector symbols $\hat{\mathbf i}$, $\hat{\mathbf j}$, and $\hat{\mathbf k}$, while the other columns contain the coordinates of $\mathbf v$ and $\mathbf w$.

If we expand the determinant as though those basis-vector symbols were algebraic entries, we get a combination such as:

$$
a\hat{\mathbf i}+b\hat{\mathbf j}+c\hat{\mathbf k}.
$$

We interpret $a,b,c$ as the coordinates of the resulting vector.

The previous lecture gave us the geometric properties of that result:

- It is perpendicular to both $\mathbf v$ and $\mathbf w$.
- Its length equals the area of the parallelogram spanned by $\mathbf v$ and $\mathbf w$.
- Its direction follows the right-hand rule.

But why should this strange determinant calculation produce exactly that vector? The lecturer wants to explain the reason rather than asking us to simply believe it.

## 2. A quick reminder: duality

The previous dot-product lecture introduced **duality**.

The idea is:

**Every linear transformation from a vector space to the number line can be represented by taking a dot product with one particular vector.**

For a transformation from 3D to 1D, its matrix has one row and three columns:

$$
T(\mathbf r)=
\begin{bmatrix}a&b&c\end{bmatrix}
\begin{bmatrix}x\\y\\z\end{bmatrix}
=ax+by+cz.
$$

Turn the row of numbers into a column vector:

$$
\mathbf p=\begin{bmatrix}a\\b\\c\end{bmatrix}.
$$

Then the same transformation can be written as:

$$
\boxed{T(\mathbf r)=\mathbf p\cdot\mathbf r}.
$$

The vector $\mathbf p$ is called the **dual vector** of the transformation.

So instead of thinking about a transformation that takes a 3D vector and returns a number, we can think about taking a dot product with a specific 3D vector.

## 3. Recall the 2D cross product

In 2D, the cross-product operation is a signed number.

Given two 2D vectors $\mathbf v$ and $\mathbf w$, put their coordinates into the columns of a 2 × 2 matrix:

$$
\mathbf v\times\mathbf w=
\det\begin{bmatrix}
v_x&w_x\\
v_y&w_y
\end{bmatrix}.
$$

The result is the signed area of the parallelogram they span.

The determinant is useful because it measures how a linear transformation scales area, including whether orientation is flipped.

The lecturer uses this familiar 2D idea as a stepping stone to understand the 3D cross product.

## 4. A related 3D idea: three vectors and signed volume

Imagine three 3D vectors $\mathbf r,\mathbf v,\mathbf w$.

Put them into the columns of a 3 × 3 matrix:

$$
\det\begin{bmatrix}
r_x&v_x&w_x\\
r_y&v_y&w_y\\
r_z&v_z&w_z
\end{bmatrix}.
$$

Geometrically, this determinant is the **signed volume** of the parallelepiped spanned by the three vectors.

Its magnitude is the ordinary volume. Its sign records orientation.

The lecturer points out that this is not itself the usual 3D cross product: it takes three vectors and returns a number. The actual cross product takes two vectors and returns a vector.

However, this signed-volume idea gets us close to the answer.

## 5. Turn one of the vectors into a variable

Keep $\mathbf v$ and $\mathbf w$ fixed, but allow the first vector to vary. Call it $\mathbf r=(x,y,z)$.

Define a function:

$$
\boxed{T(\mathbf r)=
\det\begin{bmatrix}
x&v_x&w_x\\
y&v_y&w_y\\
z&v_z&w_z
\end{bmatrix}}.
$$

This function takes a 3D input vector and returns one number:

$$
T:\mathbb R^3\longrightarrow\mathbb R.
$$

What does the number mean?

For each input $\mathbf r$:

1. Form the parallelepiped spanned by $\mathbf r,\mathbf v,\mathbf w$.
2. Calculate its volume.
3. Give the volume a positive or negative sign according to orientation.

That signed volume is the output of $T$.

At first, this function may seem like an unusual thing to define. The lecturer asks us to explore its properties because it reveals the cross product.

## 6. Why is this function linear?

The lecturer states that $T$ is linear and invites viewers to verify this using properties of determinants.

A useful way to see the idea is to expand the determinant. Since $\mathbf v$ and $\mathbf w$ are fixed, the result has the form:

$$
T(x,y,z)=A x+B y+C z,
$$

where $A,B,C$ depend only on the fixed vectors $\mathbf v$ and $\mathbf w$.

There are no squared terms, products such as $xy$, or other nonlinear expressions in the input coordinates.

A function of this form is linear. It also means that $T$ can be represented by a 1 × 3 matrix:

$$
T(\mathbf r)=
\begin{bmatrix}A&B&C\end{bmatrix}
\begin{bmatrix}x\\y\\z\end{bmatrix}.
$$

## 7. Bring in duality: there must be a vector $\mathbf p$

Because $T$ is a linear transformation from 3D to the number line, duality tells us there is a unique vector $\mathbf p$ such that:

$$
\boxed{T(\mathbf r)=\mathbf p\cdot\mathbf r}
$$

for every input vector $\mathbf r$.

Write $\mathbf p=(p_x,p_y,p_z)$. Then:

$$
\mathbf p\cdot\mathbf r=p_xx+p_yy+p_zz.
$$

The question is now:

**Which vector $\mathbf p$ makes the dot product equal to the signed-volume determinant for every possible $\mathbf r$?**

The lecturer answers this question in two different ways: computationally and geometrically.

## 8. Computational answer: the determinant mnemonic

Expand the determinant defining $T$:

$$
T(\mathbf r)=
\det\begin{bmatrix}
x&v_x&w_x\\
y&v_y&w_y\\
z&v_z&w_z
\end{bmatrix}.
$$

Expanding along the first column gives:

$$
\begin{aligned}
T(\mathbf r)={}&
x(v_yw_z-v_zw_y)\\
&-y(v_xw_z-v_zw_x)\\
&+z(v_xw_y-v_yw_x).
\end{aligned}
$$

Group the coefficients of $x,y,z$:

$$
T(\mathbf r)=
(v_yw_z-v_zw_y)x
+(v_zw_x-v_xw_z)y
+(v_xw_y-v_yw_x)z.
$$

Compare this with:

$$
\mathbf p\cdot\mathbf r=p_xx+p_yy+p_zz.
$$

The coordinates of $\mathbf p$ must therefore be:

$$
\boxed{
\mathbf p=
\begin{bmatrix}
v_yw_z-v_zw_y\\
v_zw_x-v_xw_z\\
v_xw_y-v_yw_x
\end{bmatrix}}.
$$

This is exactly the component formula produced by the familiar determinant mnemonic:

$$
\boxed{\mathbf p=\mathbf v\times\mathbf w}.
$$

### 8.1 Why the basis-vector symbols appear in the mnemonic

When we expand the determinant containing $\hat{\mathbf i},\hat{\mathbf j},\hat{\mathbf k}$, those symbols collect the coefficients of the x, y, and z terms.

That is precisely what we just did when we expanded $T(\mathbf r)$ and collected the coefficients of $x,y,z$.

So the first-column basis-vector notation is not arbitrary. It is a compact way to package the three coefficients into the coordinates of the dual vector.

## 9. Geometric answer: what vector represents signed volume?

Now the lecturer asks the same question geometrically.

We want a vector $\mathbf p$ such that:

$$
\mathbf p\cdot\mathbf r
$$

equals the signed volume of the parallelepiped spanned by $\mathbf r,\mathbf v,\mathbf w$.

Think about how to calculate that volume.

### 9.1 Base area multiplied by perpendicular height

Use the parallelogram spanned by $\mathbf v$ and $\mathbf w$ as the base.

Its area is:

$$
A=\text{Area of parallelogram spanned by }\mathbf v,\mathbf w.
$$

The volume is:

$$
\text{Volume}=A\times\text{perpendicular height}.
$$

The important detail is that the height is **not generally the full length of $\mathbf r$**. It is only the component of $\mathbf r$ perpendicular to the base parallelogram.

A vector can be long but lie almost parallel to the base. In that case, its perpendicular component is small, so the volume is small.

### 9.2 Use a perpendicular unit direction

Let $\hat{\mathbf n}$ be a unit vector perpendicular to the plane containing $\mathbf v$ and $\mathbf w$.

The signed perpendicular component of $\mathbf r$ is:

$$
\mathbf r\cdot\hat{\mathbf n}.
$$

Therefore the signed volume can be expressed as:

$$
T(\mathbf r)=A(\mathbf r\cdot\hat{\mathbf n}).
$$

Rearrange:

$$
T(\mathbf r)=(A\hat{\mathbf n})\cdot\mathbf r.
$$

Compare this with the duality form:

$$
T(\mathbf r)=\mathbf p\cdot\mathbf r.
$$

It follows that:

$$
\boxed{\mathbf p=A\hat{\mathbf n}}.
$$

In words, the dual vector must:

- be perpendicular to the plane of $\mathbf v$ and $\mathbf w$;
- have length equal to the area of their parallelogram;
- point in the direction that makes the dot product's sign agree with the signed-volume orientation.

But these are exactly the geometric properties of the cross product!

Thus:

$$
\boxed{\mathbf p=\mathbf v\times\mathbf w}.
$$

## 10. The two answers must be the same vector

We have now found the dual vector in two ways.

**Computational approach**

Expanding the determinant gives the coordinates:

$$
\mathbf p=
(v_yw_z-v_zw_y,\;
v_zw_x-v_xw_z,\;
v_xw_y-v_yw_x).
$$

This is what the determinant mnemonic computes.

**Geometric approach**

The signed-volume interpretation shows that $\mathbf p$ must be perpendicular to both $\mathbf v$ and $\mathbf w$, have length equal to the parallelogram's area, and point in the orientation selected by the right-hand rule.

This is the geometric definition of the cross product.

Both approaches describe the dual vector of the same linear transformation. Since the dual vector is unique, the two answers must be the same.

That is the fundamental reason the determinant calculation and the geometric interpretation of the cross product agree.

## 11. A worked example tying the ideas together

Choose:

$$
\mathbf v=(1,0,0),\qquad
\mathbf w=(0,1,0).
$$

The parallelogram they span is a unit square in the xy-plane.

- Its area is 1.
- A perpendicular direction is the z-axis.
- The right-hand rule chooses the positive z direction.

So geometrically:

$$
\mathbf v\times\mathbf w=(0,0,1).
$$

Now define the signed-volume transformation:

$$
T(x,y,z)=
\det\begin{bmatrix}
x&1&0\\
y&0&1\\
z&0&0
\end{bmatrix}.
$$

Expanding gives:

$$
T(x,y,z)=z.
$$

But:

$$
(0,0,1)\cdot(x,y,z)=z.
$$

So the vector representing this transformation through a dot product is $(0,0,1)$, exactly the cross product found geometrically.

## 12. The complete story in one chain

The lecture's reasoning can be summarized as:

1. Fix two vectors, $\mathbf v$ and $\mathbf w$.
2. Define a function that takes any third vector $\mathbf r$ and returns the signed volume of the parallelepiped formed by the three vectors.
3. This function is a linear transformation from 3D to the number line.
4. By duality, it corresponds to a unique vector $\mathbf p$, and the function is the dot product with $\mathbf p$.
5. Expanding the determinant finds the coordinates of $\mathbf p$. This is the familiar cross-product determinant mnemonic.
6. Interpreting the signed volume as base area times signed perpendicular height shows that $\mathbf p$ is perpendicular to $\mathbf v,\mathbf w$, has length equal to their parallelogram's area, and follows the right-hand-rule orientation.
7. Those are exactly the properties of $\mathbf v\times\mathbf w$.

Therefore, the determinant mnemonic and the geometric cross product are two ways of describing the same vector.

## 13. Key formulas

**Signed-volume transformation**

$$
T(\mathbf r)=
\det\begin{bmatrix}
r_x&v_x&w_x\\
r_y&v_y&w_y\\
r_z&v_z&w_z
\end{bmatrix}.
$$

**Duality**

$$
T(\mathbf r)=\mathbf p\cdot\mathbf r.
$$

**Coordinates of the dual vector**

$$
\mathbf p=
(v_yw_z-v_zw_y,\;
v_zw_x-v_xw_z,\;
v_xw_y-v_yw_x).
$$

**Geometric volume**

$$
T(\mathbf r)=
\text{Base area}\times\text{signed perpendicular height}.
$$

**Cross-product conclusion**

$$
\boxed{\mathbf p=\mathbf v\times\mathbf w}.
$$

## 14. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| The 3D cross product determinant is an arbitrary trick. | It computes the dual vector of a particular signed-volume linear transformation. |
| The determinant function uses three fixed vectors. | In this construction, $\mathbf v,\mathbf w$ are fixed and the first vector $\mathbf r$ is the variable input. |
| The signed volume is always positive. | The determinant is signed; its sign records orientation. |
| Volume is base area multiplied by the full length of $\mathbf r$. | It is base area multiplied by the component of $\mathbf r$ perpendicular to the base plane. |
| Any vector perpendicular to $\mathbf v,\mathbf w$ is their cross product. | Its magnitude and orientation also matter: it must have length equal to the parallelogram area and obey the right-hand rule. |
| The computational and geometric definitions are unrelated. | They are the same unique dual vector, found in two different ways. |

## 15. Check your understanding

Try these questions before reading the answers.

1. What are the inputs and output of the transformation $T$ defined in this lecture?
2. What does $T(\mathbf r)$ represent geometrically?
3. Why is $T$ linear?
4. What does duality tell us about a linear transformation from 3D to the number line?
5. Why does expanding the determinant reveal the coordinates of the dual vector?
6. Why are $\hat{\mathbf i},\hat{\mathbf j},\hat{\mathbf k}$ used in the cross-product determinant mnemonic?
7. How can the volume of the parallelepiped be calculated using a base and height?
8. Why is the full length of $\mathbf r$ not generally the height?
9. What properties must the geometric dual vector have?
10. Why must the computational and geometric answers agree?

### Answers

1. It takes a variable 3D vector $\mathbf r$ and returns one number.
2. The signed volume of the parallelepiped spanned by $\mathbf r,\mathbf v,\mathbf w$.
3. With $\mathbf v,\mathbf w$ fixed, determinant expansion is a linear expression in the coordinates of $\mathbf r$.
4. It can be represented as a dot product with a unique vector in 3D.
5. The coefficients of $r_x,r_y,r_z$ become the three coordinates of the vector in the dot-product representation.
6. They signal that the three collected coefficients are to be interpreted as the x, y, and z coordinates of a vector.
7. Base area multiplied by perpendicular height.
8. Only the component perpendicular to the base plane contributes to the height.
9. It must be perpendicular to both fixed vectors, have length equal to their parallelogram area, and have the orientation that matches signed volume.
10. Both are the unique dual vector of the same linear transformation.
