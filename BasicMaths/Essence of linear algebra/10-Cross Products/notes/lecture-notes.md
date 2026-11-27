# Lecture 10 — Cross Products

> **Learning goal:** Understand what the cross product represents geometrically in 2D and 3D, how orientation affects its sign, and how determinants are used to calculate it.

These notes follow the lecture's order. This chapter covers the standard introduction to cross products. the deeper connection to linear transformations and duality will be explored in the next chapter.

## 1. What this lecture is about

The previous lecture explored dot products and their connection to linear transformations. This lecture does something similar for cross products, but splits the subject into two chapters:

- This chapter covers the main ideas students are usually taught about cross products.
- The next chapter will explain a less commonly taught, deeper connection using duality.

This section starts in 2D, where the cross product is a signed number, and then moves to the true 3D cross product, which is a vector.

## 2. Start in 2D: two vectors form a parallelogram

Take two vectors, $\mathbf v$ and $\mathbf w$, starting at the origin.

To picture the parallelogram they span:

1. Move a copy of $\mathbf v$ so its tail starts at the tip of $\mathbf w$.
2. Move a copy of $\mathbf w$ so its tail starts at the tip of $\mathbf v$.
3. The four sides enclose a parallelogram.

The 2D cross product is connected to the area of this parallelogram.

But there is an important extra detail: **orientation**. The answer is not always just a positive area. It is a signed area.

## 3. Orientation decides whether the 2D cross product is positive or negative

Use the relative position of the two vectors:

- If $\mathbf v$ is on the **right** of $\mathbf w$, then $\mathbf v\times\mathbf w$ is positive.
- If $\mathbf v$ is on the **left** of $\mathbf w$, then $\mathbf v\times\mathbf w$ is negative.

The magnitude is the area of the parallelogram. The sign records its orientation.

### 3.1 Order matters

Swapping the two vectors reverses the sign:

$$
\boxed{\mathbf v\times\mathbf w=-(\mathbf w\times\mathbf v)}.
$$

This is different from the dot product, where swapping the vectors does not change the result.

### 3.2 Remember the basis-vector order

Suggests remembering the order of the standard basis vectors:

$$
\boxed{\hat{\mathbf i}\times\hat{\mathbf j}>0}.
$$

The order of the basis vectors defines the positive orientation. This section uses this as a way to remember which side counts as positive.

### 3.3 Example from the lecture

Suppose the parallelogram has area 7 and $\mathbf v$ is on the left of $\mathbf w$.

The signed area is therefore:

$$
\boxed{\mathbf v\times\mathbf w=-7}.
$$

The geometric area is 7, but the cross product is negative because of orientation.

## 4. Calculate the 2D cross product using a determinant

We do not want to need a diagram or a supplied area every time. The determinant gives us a direct calculation.

Write the coordinates of $\mathbf v$ as the first column and the coordinates of $\mathbf w$ as the second column:

$$
\mathbf v\times\mathbf w
=
\det\begin{bmatrix}
v_x&w_x\\
v_y&w_y
\end{bmatrix}.
$$

For a 2 × 2 matrix, this becomes:

$$
\boxed{\mathbf v\times\mathbf w=v_xw_y-w_xv_y}.
$$

Why does a determinant appear?

The matrix with $\mathbf v$ and $\mathbf w$ as its columns represents a linear transformation that sends:

- $\hat{\mathbf i}$ to $\mathbf v$;
- $\hat{\mathbf j}$ to $\mathbf w$.

The unit square formed by the two basis vectors has area 1. Under this transformation, that square becomes the parallelogram formed by $\mathbf v$ and $\mathbf w$.

The determinant measures the signed factor by which areas change:

- its magnitude tells us the area-scaling factor;
- its sign tells us whether orientation was preserved or flipped.

Since the original square had area 1, the determinant is exactly the signed area of the new parallelogram.

### 4.1 Worked example from the lecture

Let

$$
\mathbf v=(-3,1),\qquad \mathbf w=(2,1).
$$

Put their coordinates into the columns:

$$
\mathbf v\times\mathbf w
=
\det\begin{bmatrix}
-3&2\\
1&1
\end{bmatrix}.
$$

Calculate:

$$
=(-3)(1)-(2)(1)
=-3-2
=\boxed{-5}.
$$

Therefore:

- The parallelogram's ordinary area is $5$.
- The signed cross product is $-5$.
- The negative sign indicates the orientation described in the lecture: $\mathbf v$ is on the left of $\mathbf w$.

## 5. What happens when the vectors change?

Encourages developing an intuition for how the parallelogram's area changes.

### 5.1 Perpendicular vectors give a large area

For vectors with fixed lengths, the parallelogram is largest when the vectors are perpendicular.

If the vectors point in very similar directions, the parallelogram becomes narrow and its area is smaller.

If the vectors point along the same line, the parallelogram collapses and its area is zero.

### 5.2 Scaling a vector scales the area

Suppose we multiply $\mathbf v$ by 3.

The parallelogram becomes three times as wide in the corresponding direction, so its area is multiplied by 3.

The cross product therefore obeys:

$$
\boxed{(3\mathbf v)\times\mathbf w
=3(\mathbf v\times\mathbf w)}.
$$

This is an observation about how the 2D signed-area operation changes when a vector is scaled.

## 6. The true cross product is a 3D vector

Makes an important distinction: the 2D signed-area operation just described is a useful mathematical operation, but it is technically not the true cross product as commonly defined.

The true cross product takes two 3D vectors and produces another 3D vector:

$$
\boxed{\mathbf v,\mathbf w\in\mathbb R^3
\quad\Longrightarrow\quad
\mathbf v\times\mathbf w\in\mathbb R^3}.
$$

The parallelogram formed by the two input vectors still matters.

The resulting cross-product vector has two defining geometric properties:

1. Its **length** is the area of the parallelogram.
2. Its **direction** is perpendicular to the plane of the parallelogram.

There are two possible perpendicular directions: one side of the plane or the opposite side. The right-hand rule chooses which one.

## 7. The right-hand rule

To determine the direction of $\mathbf v\times\mathbf w$:

1. Point the forefinger of your **right hand** in the direction of $\mathbf v$.
2. Point your middle finger in the direction of $\mathbf w$.
3. Your thumb points in the direction of $\mathbf v\times\mathbf w$.

The order matters. If you swap $\mathbf v$ and $\mathbf w$, the cross-product vector points in the opposite direction.

The right-hand rule is a way to choose between the two directions perpendicular to the parallelogram.

## 8. Worked 3D example from the lecture

Chooses:

- $\mathbf v$: length 2, pointing straight up in the positive z direction;
- $\mathbf w$: length 2, pointing in the positive y direction.

In unit-vector notation:

$$
\mathbf v=2\hat{\mathbf k},
\qquad
\mathbf w=2\hat{\mathbf j}.
$$

The vectors are perpendicular and both have length 2. They form a square:

$$
\text{Area}=2\times2=4.
$$

Therefore, the cross-product vector must have length 4.

Using the right-hand rule, its direction is the negative x direction. Thus:

$$
\boxed{\mathbf v\times\mathbf w=-4\hat{\mathbf i}}.
$$

Notice both pieces of information:

- Magnitude: 4, the parallelogram's area.
- Direction: negative x, determined by the right-hand rule.

## 9. The 3D determinant mnemonic

For more general calculations, This section presents a determinant-based process.

Write the basis vectors in the first column, then put the coordinates of $\mathbf v$ and $\mathbf w$ in the second and third columns:

$$
\mathbf v\times\mathbf w
=
\det\begin{bmatrix}
\hat{\mathbf i}&v_x&w_x\\
\hat{\mathbf j}&v_y&w_y\\
\hat{\mathbf k}&v_z&w_z
\end{bmatrix}.
$$

This notation can look strange. A matrix normally contains numbers, so what does it mean to put vectors such as $\hat{\mathbf i}$, $\hat{\mathbf j}$, and $\hat{\mathbf k}$ into its entries?

Explain that students are often told to treat this as a notational trick:

1. Expand the determinant as if the basis vectors were symbols.
2. The result is a linear combination of $\hat{\mathbf i}$, $\hat{\mathbf j}$, and $\hat{\mathbf k}$.
3. Interpret that linear combination as a 3D vector.

there is a deeper reason this works. It is not merely a random trick. The determinant and the basis vectors have a meaningful geometric connection, which the next chapter will explain using duality.

For this lecture, the important thing is to understand what the resulting vector represents geometrically.

### 9.1 The expanded component formula

Expanding the determinant gives:

$$
\begin{aligned}
\mathbf v\times\mathbf w
={}&(v_yw_z-v_zw_y)\hat{\mathbf i}\\
&-(v_xw_z-v_zw_x)\hat{\mathbf j}\\
&+(v_xw_y-v_yw_x)\hat{\mathbf k}.
\end{aligned}
$$

This formula is included to make the determinant mnemonic easier to interpret. The lecture emphasizes the determinant process and its geometric meaning.

### 9.2 Check the lecture's 3D example using the formula

For

$$
\mathbf v=(0,0,2),\qquad \mathbf w=(0,2,0),
$$

the determinant mnemonic is:

$$
\mathbf v\times\mathbf w
=
\det\begin{bmatrix}
\hat{\mathbf i}&0&0\\
\hat{\mathbf j}&0&2\\
\hat{\mathbf k}&2&0
\end{bmatrix}.
$$

Only the x component is nonzero:

$$
(0)(0)-(2)(2)=-4.
$$

Therefore:

$$
\mathbf v\times\mathbf w=-4\hat{\mathbf i},
$$

matching the geometric right-hand-rule result.

## 10. What the next chapter will explain

Deliberately, separates the standard cross-product introduction from its deeper explanation.

The next chapter will use the idea of **duality**, introduced in the previous dot-product lecture, to explain why the determinant mnemonic works and why the basis vectors appear in the first column.

this deeper topic may be beyond what is essential for an introductory linear algebra course. It is optional for anyone who wants to understand the underlying geometry more fully.

## 11. Key takeaways

- In 2D, the cross-product operation gives the signed area of the parallelogram spanned by two vectors.
- Orientation determines the sign.
- Swapping the vectors reverses the sign: $\mathbf v\times\mathbf w=-(\mathbf w\times\mathbf v)$.
- The 2D signed area is computed with a 2 × 2 determinant.
- The determinant appears because it measures signed area scaling under a linear transformation.
- In 3D, the true cross product is a vector.
- Its length equals the area of the parallelogram formed by the two input vectors.
- Its direction is perpendicular to that parallelogram and is chosen by the right-hand rule.
- The 3D determinant with $\hat{\mathbf i},\hat{\mathbf j},\hat{\mathbf k}$ is a computational mnemonic whose deeper justification is reserved for the next lecture.

## 12. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| The 2D cross product is an ordinary positive area. | It is a signed area; orientation determines its sign. |
| Swapping the two vectors leaves the cross product unchanged. | Swapping them reverses the sign or direction. |
| The true cross product of two 3D vectors is a number. | It is a 3D vector. |
| The 3D cross product points in the same plane as the two inputs. | It is perpendicular to the plane they span. |
| The length of the 3D cross product is the sum of the input lengths. | Its length is the parallelogram's area. |
| The determinant notation with basis vectors is just random decoration. | The lecture says there is a deeper reason, which will be explained through duality in the next chapter. |

## 13. Check your understanding

Try answering these questions before looking at the answers.

1. What shape do two 2D vectors span?
2. What does the 2D cross product represent?
3. What determines whether the 2D cross product is positive or negative?
4. What happens when the order of the two vectors is swapped?
5. How do you calculate the 2D cross product using a determinant?
6. Why does a determinant measure the parallelogram's signed area?
7. What happens to the parallelogram's area when one vector is scaled by 3?
8. What is different about the true 3D cross product?
9. What determines the magnitude of the 3D cross product?
10. How does the right-hand rule determine its direction?
11. For $\mathbf v=2\hat{\mathbf k}$ and $\mathbf w=2\hat{\mathbf j}$, what is the cross product?
12. Why does the 3D determinant mnemonic contain $\hat{\mathbf i}$, $\hat{\mathbf j}$, and $\hat{\mathbf k}$?

### Answers

1. A parallelogram.
2. The signed area of that parallelogram.
3. The orientation or relative left/right ordering of the vectors.
4. The sign reverses: $\mathbf v\times\mathbf w=-(\mathbf w\times\mathbf v)$.
5. $\det\begin{bmatrix}v_x&w_x\\v_y&w_y\end{bmatrix}=v_xw_y-w_xv_y$.
6. The determinant measures signed area scaling, and the original unit square has area 1.
7. The area and signed cross-product value are multiplied by 3.
8. It produces a 3D vector rather than a signed number.
9. The area of the parallelogram formed by the two input vectors.
10. Point the right-hand forefinger along the first vector, middle finger along the second; the thumb gives the cross-product direction.
11. $-4\hat{\mathbf i}$.
12. They form the basis-vector components of the resulting 3D vector in the determinant mnemonic; the deeper justification is the subject of the next chapter.
