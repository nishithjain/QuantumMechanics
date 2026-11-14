# Lecture 06 — The Determinant

> **Learning goal:** Understand what a determinant represents geometrically: how a linear transformation scales area in 2D and volume in 3D, and how its sign describes orientation.

These notes follow the lecturer's sequence. The lecture emphasizes the meaning of the determinant more than memorizing a calculation procedure.

## 1. Why measure what a transformation does to space?

In the previous videos, we learned that a linear transformation can move vectors and reshape the grid. Some transformations make space look stretched out; others squeeze it together.

The lecturer now asks a useful question:

**Can we measure exactly how much a transformation stretches or squishes space?**

Rather than measuring every line or every point, begin by measuring what happens to the **area** of a region.

For example, imagine a small square on a sheet of graph paper. After a transformation, it may become a larger rectangle, a slanted parallelogram, or something flatter. Comparing its area before and after gives us a single number describing the area change.

That number is closely connected to the determinant.

## 2. First example: stretching a unit square into a rectangle

Consider the 2D matrix whose columns are $(3,0)$ and $(0,2)$:

$$
A=\begin{bmatrix}3&0\\0&2\end{bmatrix}.
$$

Remember the column rule from the earlier lectures:

- The first column tells us where $\hat{\mathbf i}=(1,0)$ goes.
- The second column tells us where $\hat{\mathbf j}=(0,1)$ goes.

So this transformation:

- stretches $\hat{\mathbf i}$ by a factor of 3 along the x direction;
- stretches $\hat{\mathbf j}$ by a factor of 2 along the y direction.

Focus on the unit square whose bottom edge lies along $\hat{\mathbf i}$ and whose left edge lies along $\hat{\mathbf j}$.

Before transformation:

$$
\text{width}=1,\quad \text{height}=1,\quad
\text{area}=1\times1=1.
$$

After transformation, the square becomes a rectangle:

$$
\text{width}=3,\quad \text{height}=2,\quad
\text{area}=3\times2=6.
$$

The area has increased from 1 to 6. Therefore, this transformation scales area by a factor of 6.

The determinant of this matrix is 6. Later in the lecture, the lecturer gives the calculation rule; for now, concentrate on the meaning.

**Intuition:** the transformation stretches one direction three times and the perpendicular direction two times, so the area becomes $3\times2=6$ times as large.

## 3. Second example: a shear can change shape without changing area

Now consider the matrix whose columns are $(1,0)$ and $(1,1)$:

$$
A=\begin{bmatrix}1&1\\0&1\end{bmatrix}.
$$

Its columns tell us:

- $\hat{\mathbf i}$ stays at $(1,0)$;
- $\hat{\mathbf j}$ moves to $(1,1)$.

This transformation is a **shear**. A shear slants a shape sideways. Think of pushing the top of a rectangular stack of cards sideways while keeping the bottom in place.

The unit square becomes a parallelogram. Its shape changes, but its area remains 1.

Why? The base remains 1 unit long, and the perpendicular height remains 1 unit. The slanted side is not the height; height means the perpendicular distance between the base and the opposite side.

$$
\text{Area of parallelogram}
=\text{base}\times\text{perpendicular height}
=1\times1=1.
$$

So this transformation changes the shape but does not change area. Its determinant is 1.

> A transformation does not have to preserve the shape of a region to preserve its area.

## 4. Why one unit square tells us about every region

At this point, we have looked at one special unit square. Why should that tell us what happens to a completely different shape?

The lecturer builds the reasoning in two stages.

### 4.1 Every grid square is scaled by the same factor

A linear transformation keeps grid lines parallel and evenly spaced in the corresponding transformed grid.

If a unit square becomes a parallelogram with a particular area, then a larger grid square is made from several unit-square-sized pieces and its area changes by that same overall factor.

The same scaling factor applies to small and large grid squares.

### 4.2 Other shapes can be approximated by small squares

A region does not have to be a perfect grid square. We can cover it with many small grid squares.

The smaller the squares, the more accurately their collection can approximate the region's boundary. The lecturer points out that we can make this approximation arbitrarily good by using sufficiently small squares.

If every one of those small squares has its area multiplied by the same factor, then the total area of the whole region is multiplied by that factor too.

This gives us a powerful conclusion:

**A linear transformation scales the area of every 2D region by one common factor.**

That special factor is called the **determinant** of the transformation.

## 5. What the determinant tells us

The lecturer gives several examples of what different determinant values mean.

| Determinant | Effect on area |
|---:|---|
| $3$ | Every region's area becomes 3 times as large. |
| $\frac12$ | Every region's area becomes half as large. |
| $0$ | Every region is flattened so that its resulting area is zero. |

### 5.1 A determinant of zero

A 2D transformation can squash the entire plane onto a line, or even onto a single point.

A line has no 2D area. A single point also has no 2D area. So every original region ends up with area zero.

This is why a determinant of zero is important: it tells us that the transformation has collapsed the 2D space into something lower-dimensional.

The lecturer says this will become useful in later videos. For now, remember the geometric meaning.

## 6. The lecturer's correction: determinants can be negative

So far, we have described the determinant as an area-scaling factor. But the lecturer pauses to clarify that this is not the complete story.

How can an area be scaled by a negative number? Ordinary area is never negative.

The missing idea is **orientation**.

### 6.1 What does orientation mean in 2D?

Think of the plane as a sheet of paper. A transformation may flip the sheet over, just as turning a sheet of paper over exposes its other side.

Such a transformation reverses the orientation of the plane.

The lecturer also gives a way to recognize this using the basis vectors:

- Start with $\hat{\mathbf i}$ and $\hat{\mathbf j}$ in their standard positions.
- Notice their relative arrangement: $\hat{\mathbf j}$ is to the left of $\hat{\mathbf i}$ in the lecturer's diagram.
- If after transformation $\hat{\mathbf j}$ is on the other side, to the right of $\hat{\mathbf i}$, the orientation has been inverted.

Whenever orientation is inverted, the determinant is negative.

### 6.2 The absolute value tells us the area-scaling amount

The sign and magnitude have different jobs:

- The **sign** tells us whether orientation is preserved or reversed.
- The **absolute value** tells us the factor by which area is scaled.

For example, if the determinant is $-3$:

- the orientation is flipped;
- the area becomes 3 times as large.

It does not mean that the physical area is negative.

## 7. A negative determinant example

The lecturer considers the matrix whose columns are $(1,1)$ and $(2,-1)$:

$$
A=\begin{bmatrix}1&2\\1&-1\end{bmatrix}.
$$

The lecturer states that its determinant is $-3$.

What does that tell us?

1. The negative sign means the transformation reverses orientation.
2. The magnitude is $|-3|=3$.
3. Therefore, every region's area becomes three times as large, while its orientation is flipped.

The calculation formula introduced later in the lecture confirms this:

$$
\det(A)=(1)(-1)-(2)(1)=-1-2=-3.
$$

## 8. Why does the determinant pass through zero when orientation flips?

The lecturer now gives a geometric way to understand why negative values make sense.

Imagine gradually moving $\hat{\mathbf i}$ closer and closer to $\hat{\mathbf j}$.

As the two vectors approach alignment:

- the parallelogram they form becomes thinner;
- its area gets smaller;
- the determinant approaches zero.

When the two vectors line up perfectly, the parallelogram has zero area. The determinant is zero.

Now continue the movement beyond that point. The two vectors have effectively passed through one another in orientation. The determinant continues into negative values.

This is a helpful intuition: the determinant does not suddenly jump from a positive area to a negative area. It passes through zero at the moment the plane is flattened, and then becomes negative when orientation has reversed.

## 9. Extending the idea from 2D to 3D: volume

The lecturer now asks what the determinant should mean in three dimensions.

The same principle applies, but the quantity being scaled changes:

- In 2D, the determinant measures the area-scaling factor.
- In 3D, the determinant measures the volume-scaling factor.

### 9.1 Start with a unit cube

In 2D, the easiest shape to follow was a unit square with area 1.

In 3D, use a unit cube whose edges lie along the three standard basis vectors:

$$
\hat{\mathbf i}=(1,0,0),\quad
\hat{\mathbf j}=(0,1,0),\quad
\hat{\mathbf k}=(0,0,1).
$$

Its dimensions are $1\times1\times1$, so its volume is:

$$
V=1\times1\times1=1.
$$

After a 3D linear transformation, the cube may become a slanted box-like shape. The lecturer calls this a **parallelepiped**.

A parallelepiped is the 3D counterpart of a parallelogram: its faces are parallelograms, and its edges can be slanted.

Because the original cube had volume 1, the volume of the resulting parallelepiped tells us the magnitude of the volume-scaling factor.

In other words:

$$
|\det(A)|=\text{volume of the transformed unit cube}.
$$

The absolute value is used here because ordinary volume is non-negative. The signed determinant additionally records orientation.

### 9.2 What does a zero determinant mean in 3D?

A 3D transformation with determinant zero squashes all space into something with zero volume.

The result could be:

- a flat plane;
- a line;
- a single point.

All of these have zero 3D volume.

The lecturer connects this to an earlier chapter: this is what it means for the columns of the matrix to be **linearly dependent**.

### 9.3 Why does linear dependence cause zero volume?

The columns of a 3D transformation matrix are the three transformed basis vectors. They are the three edge directions of the parallelepiped formed from the transformed unit cube.

If those three vectors are linearly dependent, one of them can be described using the others.

That means the three vectors do not provide three independent directions in space. They lie in a plane or along a line (or collapse even further).

A genuine 3D volume needs three independent directions. Without them, the parallelepiped is flat or collapsed, and its volume is zero.

**Remember:** for a square 3 × 3 matrix, determinant zero and linearly dependent columns are equivalent statements.

## 10. Negative determinants in 3D: the right-hand rule

How do we understand orientation in three dimensions?

The lecturer uses the **right-hand rule**.

1. Point the index finger of your right hand in the direction of $\hat{\mathbf i}$.
2. Point your middle finger in the direction of $\hat{\mathbf j}$.
3. Your thumb points in the direction of $\hat{\mathbf k}$.

This is the standard right-handed orientation of the three basis directions.

After a transformation:

- If the transformed directions still fit this right-hand arrangement, orientation is preserved and the determinant is positive.
- If the transformed directions only fit the corresponding arrangement using your left hand, orientation has been flipped and the determinant is negative.

So in 3D, just as in 2D, the determinant's sign tells us whether orientation is preserved or reversed.

## 11. How to calculate a 2 × 2 determinant

After explaining the meaning, the lecturer introduces the calculation formula.

For a 2 × 2 matrix

$$
A=\begin{bmatrix}a&b\\c&d\end{bmatrix},
$$

the determinant is:

$$
\boxed{\det(A)=ad-bc}.
$$

Read this as:

1. Multiply the top-left entry $a$ by the bottom-right entry $d$.
2. Multiply the top-right entry $b$ by the bottom-left entry $c$.
3. Subtract the second product from the first.

### 11.1 Why does the $ad$ part make sense?

The lecturer first imagines that both $b$ and $c$ are zero:

$$
A=\begin{bmatrix}a&0\\0&d\end{bmatrix}.
$$

In this special case:

- $a$ tells us how much the x-direction is stretched;
- $d$ tells us how much the y-direction is stretched.

The unit square becomes a rectangle with side lengths $a$ and $d$, so its signed area-scaling factor is $ad$.

For positive $a$ and $d$, the ordinary area is $ad$.

### 11.2 What if only one of $b$ or $c$ is zero?

The lecturer points out that if either $b$ or $c$ is zero, the transformed shape is still a parallelogram whose base and perpendicular height give an area of $ad$ (with the sign interpreted through orientation).

For example, if $c=0$,

$$
A=\begin{bmatrix}a&b\\0&d\end{bmatrix},
$$

the first basis vector is $(a,0)$, and the second is $(b,d)$. The base has length $|a|$, while the perpendicular height is $|d|$. The sideways slant $b$ does not change that height.

Thus the area magnitude is $|ad|$, and the signed determinant is $ad$.

### 11.3 What does the $bc$ term do?

When both $b$ and $c$ are non-zero, the transformed parallelogram is affected by both off-diagonal entries.

The lecturer gives an intuitive description: the $bc$ term accounts for how the parallelogram is stretched or squished in the diagonal direction. A diagram in the original lecture is suggested for a more precise geometric intuition.

The full formula subtracts this contribution:

$$
\det(A)=ad-bc.
$$

The lecturer does not develop a complete algebraic derivation of the $bc$ term in the spoken explanation. The important takeaway at this point is the formula and its connection to the area/orientation interpretation.

### 11.4 Practice the calculation

The lecturer emphasizes that the best way to become comfortable calculating 2 × 2 determinants is to practise several examples.

For example:

$$
\begin{bmatrix}3&0\\0&2\end{bmatrix}
\quad\Rightarrow\quad
\det(A)=3(2)-0(0)=6.
$$

$$
\begin{bmatrix}1&1\\0&1\end{bmatrix}
\quad\Rightarrow\quad
\det(A)=1(1)-1(0)=1.
$$

$$
\begin{bmatrix}1&2\\1&-1\end{bmatrix}
\quad\Rightarrow\quad
\det(A)=1(-1)-2(1)=-3.
$$

These match the geometric interpretations discussed earlier.

## 12. What about 3 × 3 determinant calculations?

The lecturer says that a formula also exists for 3D determinants, but emphasizes that learning the meaning is more important than memorizing the calculation.

The lecture does not spell out the full 3 × 3 calculation formula in the spoken transcript. Instead, the lecturer recommends practising with matrices if the calculation procedure is required, and mentions Sal Khan's worked examples as a possible practice resource.

The central conceptual point remains:

- the determinant's magnitude tells us how much volume is scaled;
- its sign tells us whether orientation is preserved or flipped;
- zero means the 3D volume collapses to zero.

## 13. A useful property: determinant of a product

Before moving to the next video, the lecturer poses a question:

If two matrices are multiplied, the determinant of their product is the product of their determinants.

$$
\boxed{\det(AB)=\det(A)\det(B)}
$$

The lecturer asks us to explain why this makes sense in one sentence, rather than trying to justify it by a long numerical calculation.

### Geometric intuition

Suppose transformation $B$ scales area by a factor of 2, and transformation $A$ then scales the resulting area by a factor of 3.

The combined transformation scales area by:

$$
2\times3=6.
$$

That is why the determinant of the combined transformation is the product of the two individual determinants.

The same reasoning applies to volume in 3D. The signed factors also combine correctly when orientation flips are involved.

**One-sentence explanation:** Applying one transformation scales area or volume by its determinant, and applying the next scales the already-transformed area or volume again, so the two scaling factors multiply.

## 14. What comes next?

The lecturer closes by connecting the topic to the next major application of linear algebra: **linear systems of equations**.

The next video will relate the ideas of linear transformations covered so far to systems of linear equations.

## 15. Key takeaways

- A determinant measures the common scaling factor for areas under a 2D linear transformation.
- In 3D, it measures the common scaling factor for volumes.
- The absolute value $|\det(A)|$ tells us the amount of area or volume scaling.
- A positive determinant means orientation is preserved.
- A negative determinant means orientation is reversed.
- A zero determinant means the transformation collapses space into a lower-dimensional shape.
- For a 2 × 2 matrix:

  $$
  \det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc.
  $$

- For a 3 × 3 matrix, determinant zero is equivalent to the columns being linearly dependent.
- Determinants multiply when transformations are composed:

  $$
  \det(AB)=\det(A)\det(B).
  $$

## 16. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| A determinant is just a formula to calculate. | Its central meaning is the signed area- or volume-scaling factor of a linear transformation. |
| A negative determinant means negative physical area. | The magnitude gives the area/volume scaling; the negative sign indicates reversed orientation. |
| A shear always changes area. | A shear can change shape while preserving area. |
| Determinant zero means every point goes to the origin. | It means the whole space is collapsed into a lower-dimensional subspace; the result could be a line or plane, not necessarily one point. |
| In 3D, determinant measures area. | In 3D, it measures volume scaling. |
| A zero determinant is unrelated to matrix columns. | For a square matrix, determinant zero means its columns are linearly dependent. |

## 17. Check your understanding

Try answering before reading the answers.

1. A transformation changes a unit square into a rectangle of width 3 and height 2. What is its area-scaling factor?
2. A shear turns a unit square into a slanted parallelogram but keeps its base and perpendicular height equal to 1. What is its determinant?
3. What does a negative determinant tell you?
4. What does determinant zero mean for a 2D transformation?
5. In 3D, what shape do we get by transforming the unit cube in general?
6. What does determinant zero tell us about the columns of a 3 × 3 matrix?
7. What is the determinant formula for a 2 × 2 matrix?
8. Why does $\det(AB)=\det(A)\det(B)$ make geometric sense?

### Answers

1. $3\times2=6$.
2. $1$, because area is unchanged and orientation is preserved in this shear.
3. Orientation is reversed; the absolute value gives the area/volume scaling amount.
4. The plane is collapsed into a line or point, so every region has zero area.
5. A parallelepiped.
6. The columns are linearly dependent.
7. $ad-bc$, for $\begin{bmatrix}a&b\\c&d\end{bmatrix}$.
8. The first transformation scales area/volume by one factor, and the second scales it again, so the factors multiply.
