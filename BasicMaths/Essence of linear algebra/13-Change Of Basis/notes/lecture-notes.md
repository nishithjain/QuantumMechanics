# Lecture 13 — Change of Basis

> **Learning goal:** Understand how the same vector or linear transformation can have different coordinate descriptions depending on the chosen basis, and learn how to convert between those descriptions.

These notes follow the lecture's teaching sequence. This section uses two coordinate systems: the standard system (our system) and Jennifer's system.

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

**Interactive:** Step through **Build the vector** to see $3\hat{\mathbf i}+2\hat{\mathbf j}$ assembled on the grid—first the horizontal contribution, then the vertical piece, then the result $(3,2)$.

<iframe
 src="../animations/animation-03-coordinates-basis-instructions.html"
 title="Coordinates as instructions combining basis vectors"
 width="100%"
 height="1050"
 style="max-width:1100px;border:1px solid #dce4ef;border-radius:12px;background:#f4f7fb;"
 loading="lazy">
</iframe>

<p><a href="../animations/animation-03-coordinates-basis-instructions.html">Open Animation 03 — coordinates and basis in full tab</a> if the embed does not load.</p>

**Key idea:** Coordinates only have meaning relative to a chosen set of basis vectors.

## 2. A different person can use a different basis

Let's understand this with a simple example. The most important idea is:

**You and Jennifer are describing the same physical space, but you are using different reference directions to describe it.**

Imagine you and Jennifer are standing in the same room. You describe directions using the usual horizontal and vertical directions. Jennifer chooses two different directions as her reference directions.

### 2.1 First, your coordinate system

You use the standard basis vectors:

- $\hat{\mathbf i}=(1,0)$: one step to the right.
- $\hat{\mathbf j}=(0,1)$: one step upward.

For example, the point $P=(3,2)$ means:

1. Move 3 units to the right.
2. Move 2 units upward.

So you describe the point as:

$$
P=3\hat{\mathbf i}+2\hat{\mathbf j}=(3,2).
$$

### 2.2 Jennifer chooses different basis vectors

Jennifer does not want to use your horizontal and vertical directions. Instead, she chooses (written in **our** standard coordinates):

$$
\mathbf b_1=\begin{bmatrix}2\\1\end{bmatrix},
\qquad
\mathbf b_2=\begin{bmatrix}-1\\1\end{bmatrix}.
$$

What these mean in the plane:

- $\mathbf b_1=(2,1)$: move 2 units right and 1 unit up.
- $\mathbf b_2=(-1,1)$: move 1 unit left and 1 unit up.

Jennifer uses these two directions instead of your “right” and “up” directions. Her first coordinate scales $\mathbf b_1$, her second scales $\mathbf b_2$, and she adds the two scaled vectors.

### 2.3 What does Jennifer's $(1,0)$ mean?

This is a crucial point. When Jennifer says

$$
(1,0)_J,
$$

she means:

- take 1 copy of her first basis vector $\mathbf b_1$;
- take 0 copies of her second basis vector $\mathbf b_2$.

Therefore

$$
\begin{aligned}
(1,0)_J
&=1\mathbf b_1+0\mathbf b_2\\
&=(2,1).
\end{aligned}
$$

| Coordinate description | What it means in our system |
|------------------------|-----------------------------|
| Our $(1,0)$ | $(1,0)$ — one step right |
| Jennifer's $(1,0)_J$ | $(2,1)$ — two right, one up |

The pair $(1,0)$ does **not** have a fixed physical meaning until you know which basis is being used.

From Jennifer's point of view, her own basis vectors have coordinates

$$
\mathbf b_1=\begin{bmatrix}1\\0\end{bmatrix}_{J},
\qquad
\mathbf b_2=\begin{bmatrix}0\\1\end{bmatrix}_{J},
$$

because her basis vectors define what $(1,0)$ and $(0,1)$ mean **in her system**.

### 2.4 What does Jennifer's $(0,1)$ mean?

Similarly,

$$
\begin{aligned}
(0,1)_J
&=0\mathbf b_1+1\mathbf b_2\\
&=(-1,1).
\end{aligned}
$$

So Jennifer's coordinate $(0,1)$ represents the vector $(-1,1)$ in our standard coordinates.

### 2.5 Describe the same point in both systems

Suppose you want to describe the physical point

$$
P=(3,2).
$$

You write

$$
P=3\hat{\mathbf i}+2\hat{\mathbf j}.
$$

Jennifer describes the **same** point using her basis. She needs numbers $a$ and $b$ such that

$$
P=a\mathbf b_1+b\mathbf b_2.
$$

Substitute her basis vectors:

$$
(3,2)=a(2,1)+b(-1,1).
$$

This gives the system

$$
2a-b=3,
\qquad
a+b=2.
$$

Solving,

$$
a=\frac{5}{3},
\qquad
b=\frac{1}{3}.
$$

Therefore Jennifer describes the exact same point as

$$
\boxed{P=\left(\tfrac{5}{3},\tfrac{1}{3}\right)_J}.
$$

**Interactive:** The dot $P$ stays fixed. Compare **Your route** $(3,2)$ via î and ĵ with **Jennifer’s route** $\left(\tfrac{5}{3},\tfrac{1}{3}\right)_J$ via $\mathbf b_1$ and $\mathbf b_2$, or play **Compare both** to see two paths to the same place.

<iframe
 src="../animations/animation-04-same-point-change-of-basis.html"
 title="Same point P in standard and Jennifer coordinates"
 width="100%"
 height="920"
 style="max-width:1100px;border:1px solid #dce4ef;border-radius:12px;background:#f4f7fb;"
 loading="lazy">
</iframe>

<p><a href="../animations/animation-04-same-point-change-of-basis.html">Open Animation 04 — same point, two coordinate systems in full tab</a> if the embed does not load.</p>

### 2.6 The big takeaway

**Same physical point, different coordinate descriptions**

| Your coordinates | Jennifer's coordinates |
|------------------|----------------------|
| $(3,2)$ — $3\hat{\mathbf i}+2\hat{\mathbf j}$ | $\left(\tfrac{5}{3},\tfrac{1}{3}\right)_J$ — $\tfrac{5}{3}\mathbf b_1+\tfrac{1}{3}\mathbf b_2$ |

Both descriptions locate exactly the same place in the plane.

**Why this matters:** Later, when you study matrices and linear transformations, the same transformation can have different matrix representations depending on which basis you choose.

**Remember:**

> A vector (or point) is the actual geometric object. Coordinates are just the numbers we use to describe that object relative to a chosen basis.

We are not looking at different physical vectors. We are using different coordinate languages to describe the same space.

## 3. The grid is a visual aid, not the space itself

Note that the familiar square grid is just a way to visualize our coordinate system.

Space itself does not come with a built-in grid.

Jennifer could draw her own grid based on her basis vectors:

- The origin is the same for both coordinate systems.
- Her axes point in the directions of $\mathbf b_1$ and $\mathbf b_2$.
- Her grid spacing is determined by those basis vectors.

The grid changes because the basis changes. The underlying vectors and points do not.

## 4. Build the change-of-basis matrix

Imagine Jennifer is speaking a different coordinate language from you. The matrix is a **translator** between Jennifer's coordinate language and yours.

Let's understand why.

### 4.1 Remember Jennifer's two directions

Jennifer uses these two basis vectors (written in **our** standard coordinates):

$$
\mathbf b_1=(2,1),
\qquad
\mathbf b_2=(-1,1).
$$

| Basis vector | Meaning in the plane |
|--------------|----------------------|
| $\mathbf b_1$ | $(2,1)$ — 2 steps right and 1 step up |
| $\mathbf b_2$ | $(-1,1)$ — 1 step left and 1 step up |

You describe directions using ordinary horizontal and vertical coordinates. Jennifer describes directions using her two chosen directions.

### 4.2 What does Jennifer mean when she says $(2,3)$?

Suppose Jennifer gives you these coordinates:

$$
\mathbf c_J=\begin{bmatrix}2\\3\end{bmatrix}.
$$

She is **not** saying “2 steps right and 3 steps up.” Instead she means:

- take 2 copies of her first direction $\mathbf b_1$;
- take 3 copies of her second direction $\mathbf b_2$.

In other words,

$$
2\mathbf b_1+3\mathbf b_2.
$$

Substitute the actual directions:

$$
\begin{aligned}
2\mathbf b_1+3\mathbf b_2
&=2(2,1)+3(-1,1)\\
&=(4,2)+(-3,3)\\
&=\boxed{(1,5)}.
\end{aligned}
$$

So Jennifer's coordinates $(2,3)$ describe the same vector as $(1,5)$ in your coordinate system.

### 4.3 Where does the matrix come from?

We want to make this translation automatic. Put Jennifer's basis vectors in the **columns** of a matrix:

$$
A=
\begin{bmatrix}
2&-1\\
1&1
\end{bmatrix}.
$$

Why columns?

- The first column stores Jennifer's first direction $\mathbf b_1$.
- The second column stores Jennifer's second direction $\mathbf b_2$.

Think of $A$ as a translator that remembers both of Jennifer's directions. This is the **change-of-basis matrix from Jennifer's coordinates to standard coordinates**.

Equivalently,

$$
A=
\begin{bmatrix}
|&|\\
\mathbf b_1&\mathbf b_2\\
|&|
\end{bmatrix}.
$$

### 4.4 See the translation happen

Jennifer gives us

$$
\mathbf c_J=\begin{bmatrix}2\\3\end{bmatrix}.
$$

Multiply:

$$
A\mathbf c_J=
\begin{bmatrix}
2&-1\\
1&1
\end{bmatrix}
\begin{bmatrix}
2\\3
\end{bmatrix}
=
\begin{bmatrix}
2(2)+(-1)(3)\\
1(2)+1(3)
\end{bmatrix}
=
\boxed{\begin{bmatrix}1\\5\end{bmatrix}}.
$$

**Translation complete:** Jennifer's $(2,3)$ becomes your $(1,5)$.

In general, multiplying by $A$ performs the linear combination $a\mathbf b_1+b\mathbf b_2$ when $\mathbf c_J=\begin{bmatrix}a\\b\end{bmatrix}$.

### 4.5 Try it yourself

**Interactive:** Change Jennifer's coordinates $(a,b)$ and watch $A\mathbf c_J=(2a-b,\,a+b)$ produce the same vector as $a\mathbf b_1+b\mathbf b_2$ in standard coordinates. Try $(2,3)\to(1,5)$ or the §5 example $(-1,2)\to(-4,1)$.

<iframe
 src="../animations/animation-01-coordinate-converter.html"
 title="Jennifer to standard coordinate converter"
 width="100%"
 height="720"
 style="max-width:980px;border:1px solid #dce4ef;border-radius:12px;background:#f4f7fb;"
 loading="lazy">
</iframe>

<p><a href="../animations/animation-01-coordinate-converter.html">Open Animation 01 — coordinate converter in full tab</a> if the embed does not load.</p>

### 4.6 The most important thing to remember

| What | Meaning |
|------|---------|
| Jennifer's coordinates | How many copies of each of her basis directions to use |
| Matrix columns | The actual directions Jennifer chose, written in your coordinate system |
| Matrix multiplication | Combines those directions in the quantities Jennifer specified |
| Result | The same vector expressed in your standard coordinates |

**Remember:**

> The columns of the matrix are Jennifer's directions. Multiplying the matrix by Jennifer's coordinates tells us where those directions take us in our coordinate system.

That is why

$$
\boxed{\mathbf c_{\text{standard}}=A\mathbf c_J}.
$$

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

This connects this to the earlier lesson on linear transformations.

A matrix whose columns are the images of the standard basis vectors tells us where those basis vectors go.

For this matrix:

$$
A\hat{\mathbf i}=\mathbf b_1,
\qquad
A\hat{\mathbf j}=\mathbf b_2.
$$

So geometrically, $A$ moves the standard basis vectors to Jennifer's basis vectors.

If we start with a vector described in Jennifer's coordinates and apply $A$, we get the actual vector expressed in our standard coordinates.

this as correcting our initial "misconception" of what Jennifer means by a pair of numbers: we first interpret the numbers using our own basis, then the transformation moves that interpretation to the vector Jennifer intended.

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

Use a 90-degree counterclockwise rotation as an example.

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

a useful way to remember the expression:

$$
A^{-1}MA.
$$

Think of $M$ as the transformation described from our perspective.

The two outer matrices shift the description into and out of another coordinate system:

- $A$: Jennifer's coordinates to our coordinates.
- $M$: perform the transformation as we describe it.
- $A^{-1}$: return to Jennifer's coordinates.

The result is the same geometric transformation, but described in Jennifer's language.

this a kind of mathematical empathy: seeing the same transformation from someone else's coordinate perspective.

## 13. Why change of basis matters

In closing, pointing toward the next topic: eigenvectors and eigenvalues.

Alternate coordinate systems are useful because a transformation can sometimes become much easier to understand when represented in a suitable basis.

The next chapter will give an important example of why this matters.

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
