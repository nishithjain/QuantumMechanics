# Lecture 16 — Abstract Vector Spaces

> **Learning goal:** Understand why vectors do not have to be arrows or lists of numbers, how functions can behave like vectors, how differentiation can be represented by a matrix, and why mathematicians define vector spaces using abstract rules called axioms.

These notes follow the lecturer's progression. The lecture revisits the question “What are vectors?” and gradually moves from familiar arrows to functions, polynomials, and the abstract idea of a vector space.

## 1. The big question: what is a vector?

At the beginning of the series, vectors were introduced as arrows in a 2D or 3D space. We also learned to describe those arrows using lists of numbers, such as:

$$
\mathbf v=\begin{bmatrix}3\\2\end{bmatrix}.
$$

But which one is the vector itself?

- Is the vector fundamentally an arrow, with numbers used only as a convenient description?
- Is it fundamentally a list of numbers, with the arrow serving as a picture?
- Or are arrows and number lists two different ways of representing something more general?

The lecturer points out that higher-dimensional lists are easy to write down. For example, a 100-dimensional vector can simply be a list of 100 numbers. Visualizing 100 perpendicular directions is much harder.

There is another clue from earlier lectures: when we change basis, the coordinates change, but the underlying vector and geometric properties do not. Determinants still describe area scaling, and eigenvectors still remain on their own span, even when we use a different coordinate system.

This suggests that coordinates are a description of a vector, rather than necessarily being the vector's deepest identity.

**The question for this lecture:** What is the common idea behind arrows, number lists, and other objects that can be added and scaled?

## 2. Functions can also behave like vectors

The lecturer temporarily moves away from arrows and number lists and considers functions.

A function is a rule that takes an input and produces an output. For example:

$$
f(x)=x^2,\qquad g(x)=2x+1.
$$

We can add two functions in a natural way: evaluate both at the same input, then add their outputs.

The sum is defined by:

$$
\boxed{(f+g)(x)=f(x)+g(x)}.
$$

For example, using the functions above:

$$
\begin{aligned}
(f+g)(x)
&=x^2+(2x+1)\\
&=x^2+2x+1.
\end{aligned}
$$

At $x=2$:

$$
f(2)=4,\qquad g(2)=5,
$$

so:

$$
(f+g)(2)=4+5=9.
$$

This is similar to adding vectors coordinate by coordinate. The difference is that a function has a value for every input in its domain, so we can think of it as having an enormous, potentially infinite, collection of coordinates.

### 2.1 Scaling a function

We can also multiply a function by a real number. We simply multiply every output by that number:

$$
\boxed{(cf)(x)=c\,f(x)}.
$$

For example, if $f(x)=x^2$, then:

$$
(3f)(x)=3x^2.
$$

At $x=2$, the original output is 4 and the scaled output is 12.

So functions support the same two basic operations that vectors do:

1. Adding two objects.
2. Multiplying an object by a scalar.

That is the first reason functions can be treated as vector-like objects.

## 3. A transformation can take one function and produce another

In earlier lessons, a linear transformation took a vector as input and produced another vector.

We can do something similar with functions: take one function as input and produce another function as output.

A familiar example from calculus is differentiation.

If:

$$
f(x)=x^2,
$$

then differentiating it gives:

$$
f'(x)=2x.
$$

The input is a function, and the output is also a function.

In this setting, the lecturer notes that the word **operator** is often used instead of transformation. Here, the derivative operator takes a function and returns its derivative.

## 4. What does it mean for a transformation of functions to be linear?

The lecturer returns to the general definition of linearity.

A transformation $T$ is linear if it preserves two operations:

### 4.1 Additivity

Adding two inputs first and then transforming must give the same result as transforming each input separately and adding the outputs:

$$
\boxed{T(\mathbf v+\mathbf w)=T(\mathbf v)+T(\mathbf w)}.
$$

For functions, replace the vectors with functions:

$$
\boxed{T(f+g)=T(f)+T(g)}.
$$

### 4.2 Compatibility with scaling

Scaling the input first and then transforming must give the same result as transforming first and scaling the output:

$$
\boxed{T(c\mathbf v)=cT(\mathbf v)}.
$$

For functions:

$$
\boxed{T(cf)=cT(f)}.
$$

A linear transformation therefore preserves addition and scalar multiplication.

### 4.3 Why these two properties matter

In the earlier geometric lessons, we visualized linearity by observing that grid lines remain parallel and evenly spaced. That picture is useful for transformations of ordinary 2D space.

But the two algebraic properties above are more general. They also make sense for functions, polynomial expressions, and other kinds of objects.

The lecturer emphasizes an important consequence: a linear transformation is completely determined by what it does to the basis vectors.

Why? Because every vector can be built by scaling and adding basis vectors. If we know where each basis vector goes, linearity tells us where every combination of them goes.

The same principle will work for functions.

## 5. Differentiation is a linear transformation

The derivative operator satisfies both properties of linearity.

Let $D$ represent differentiation. Then:

### Additivity

$$
\boxed{D(f+g)=Df+Dg}.
$$

This says that differentiating the sum of two functions gives the sum of their derivatives.

Example:

$$
f(x)=x^2,\qquad g(x)=x.
$$

Differentiate their sum:

$$
\begin{aligned}
D(f+g)
&=D(x^2+x)\\
&=2x+1.
\end{aligned}
$$

Differentiate separately and add:

$$
Df+Dg=2x+1.
$$

Both methods give the same answer.

### Scaling

$$
\boxed{D(cf)=cDf}.
$$

For example:

$$
D(3x^2)=6x=3(2x)=3D(x^2).
$$

So differentiation preserves both addition and scalar multiplication. It is therefore a linear transformation on a suitable space of differentiable functions.

## 6. Can we describe differentiation using a matrix?

The lecturer now makes a connection that may initially seem surprising:

**Can we represent taking a derivative using matrix-vector multiplication?**

The challenge is that the space of all functions is generally infinite-dimensional. To make the idea manageable, the lecturer restricts attention to polynomials.

A polynomial looks like:

$$
p(x)=5+3x+x^2
$$

or:

$$
q(x)=4x^7-5x^2.
$$

Every individual polynomial has a finite number of terms. However, the collection of all polynomials includes polynomials of arbitrarily large degree.

So the whole polynomial space needs an unlimited sequence of basis functions.

## 7. Choose a basis for polynomials

A polynomial is already written as a sum of multiples of powers of $x$. Therefore, a natural basis is:

$$
\begin{aligned}
b_0(x)&=1\\
b_1(x)&=x\\
b_2(x)&=x^2\\
b_3(x)&=x^3\\
&\vdots
\end{aligned}
$$

These basis functions play the same role as $\hat{\mathbf i}$, $\hat{\mathbf j}$, and $\hat{\mathbf k}$ in ordinary geometric vector spaces.

The difference is that there are infinitely many basis functions.

### 7.1 A polynomial becomes a coordinate list

Consider:

$$
p(x)=x^2+3x+5.
$$

Rewrite it in the order of the basis:

$$
p(x)=5(1)+3(x)+1(x^2).
$$

Its coordinates in this basis are:

$$
\boxed{[5,3,1,0,0,\ldots]}.
$$

Why are there zeros?

Because the polynomial has no $x^3$, $x^4$, or higher-degree terms.

Another example:

$$
q(x)=4x^7-5x^2.
$$

Its coordinates are:

$$
\boxed{[0,0,-5,0,0,0,0,4,0,\ldots]}.
$$

The coefficient of $x^2$ is $-5$, and the coefficient of $x^7$ is $4$.

Every individual polynomial has only finitely many non-zero coefficients, followed by an infinite tail of zeros.

This is how we can treat polynomials as vectors with infinitely many possible coordinates.

## 8. Construct the matrix representing differentiation

Now that we have a basis, we can construct a matrix for the derivative operator.

Recall the basic differentiation rule:

$$
\frac{d}{dx}(x^n)=nx^{n-1}.
$$

Apply it to the first few basis functions:

| Basis function | Derivative | Coordinates in polynomial basis |
|---|---|---|
| $1$ | $0$ | $[0,0,0,\ldots]$ |
| $x$ | $1$ | $[1,0,0,\ldots]$ |
| $x^2$ | $2x$ | $[0,2,0,\ldots]$ |
| $x^3$ | $3x^2$ | $[0,0,3,0,\ldots]$ |
| $x^4$ | $4x^3$ | $[0,0,0,4,\ldots]$ |

Remember the earlier principle:

**The columns of a transformation matrix are the transformed versions of the basis vectors.**

So we put the coordinates of each differentiated basis function into the corresponding column.

The resulting infinite matrix begins:

$$
\boxed{
D=
\begin{bmatrix}
0&1&0&0&0&\cdots\\
0&0&2&0&0&\cdots\\
0&0&0&3&0&\cdots\\
0&0&0&0&4&\cdots\\
0&0&0&0&0&\cdots\\
\vdots&\vdots&\vdots&\vdots&\vdots&\ddots
\end{bmatrix}
}
$$

Notice the pattern:

- Most entries are zero.
- The positive integers appear just above the main diagonal.
- Each column describes the derivative of one basis function.

The matrix is infinite because the polynomial basis contains infinitely many powers of $x$.

## 9. Watch matrix multiplication perform differentiation

The lecturer demonstrates the matrix using:

$$
p(x)=x^3+5x^2+4x+5.
$$

Its coordinate list is:

$$
\mathbf p=
\begin{bmatrix}
5\\4\\5\\1\\0\\\vdots
\end{bmatrix}.
$$

Place this coordinate vector to the right of the derivative matrix:

$$
D\mathbf p=
\begin{bmatrix}
0&1&0&0&\cdots\\
0&0&2&0&\cdots\\
0&0&0&3&\cdots\\
0&0&0&0&\cdots\\
\vdots&\vdots&\vdots&\vdots&\ddots
\end{bmatrix}
\begin{bmatrix}
5\\4\\5\\1\\0\\\vdots
\end{bmatrix}.
$$

Let's calculate each output coordinate.

### First output coordinate

The first row gives:

$$
0(5)+1(4)+0(5)+0(1)=4.
$$

This becomes the constant term of the derivative.

It corresponds to:

$$
\frac{d}{dx}(4x)=4.
$$

### Second output coordinate

The second row gives:

$$
0(5)+0(4)+2(5)+0(1)=10.
$$

This becomes the coefficient of $x$.

It corresponds to:

$$
\frac{d}{dx}(5x^2)=10x.
$$

### Third output coordinate

The third row gives:

$$
0(5)+0(4)+0(5)+3(1)=3.
$$

This becomes the coefficient of $x^2$.

It corresponds to:

$$
\frac{d}{dx}(x^3)=3x^2.
$$

All remaining coordinates are zero.

Therefore:

$$
D\mathbf p=
\begin{bmatrix}
4\\10\\3\\0\\\vdots
\end{bmatrix}.
$$

Translate the coordinates back into a polynomial:

$$
\boxed{p'(x)=4+10x+3x^2}.
$$

This is exactly what ordinary calculus gives:

$$
\frac{d}{dx}(x^3+5x^2+4x+5)=3x^2+10x+4.
$$

The matrix and differentiation are doing precisely the same job.

## 10. Why this matrix representation works

The derivative matrix can be constructed by differentiating each basis function and placing its coordinate representation into the corresponding column.

This works because differentiation is linear.

If we know the derivative of every basis function, then we know the derivative of every polynomial made by adding and scaling those basis functions.

The lecturer's surprising conclusion is that two operations that initially look completely different are actually examples of the same general mathematical structure:

- Matrix-vector multiplication transforms a coordinate vector.
- Differentiation transforms a function into another function.

Both can represent linear transformations.

## 11. Other linear-algebra ideas also apply to functions

The lecturer points out that many concepts from earlier lessons have counterparts in function spaces.

For example:

| Ordinary vector language | Function-space language |
|---|---|
| Vector | Function |
| Vector space | Function space |
| Linear transformation | Linear operator |
| Eigenvector | Eigenfunction |
| Dot product | Inner product |

An eigenfunction, for example, is a non-zero function that is transformed into a scalar multiple of itself by an operator.

The terminology can change, but the underlying linear-algebra ideas remain closely related.

## 12. So, what is a vector?

We can now return to the question from the beginning.

A vector can be:

- An arrow in 2D or 3D space.
- A list of numbers.
- A function.
- A polynomial.
- Another kind of mathematical object.

The important thing is not how the object looks.

The important thing is whether we can define:

1. Addition of two objects.
2. Multiplication of an object by a scalar.

And whether these operations obey the appropriate rules.

This leads to the abstract mathematical concept of a **vector space**.

## 13. What is a vector space?

A vector space is a collection of objects, called vectors, together with two operations:

- Vector addition.
- Scalar multiplication.

The operations must satisfy a set of rules called **axioms**.

An axiom is a rule that we require to be true as part of the mathematical definition.

The lecturer describes these rules as an interface between mathematicians:

- A mathematician proves a theorem using only the axioms.
- Another person can define a completely different kind of mathematical object.
- If that new collection satisfies the same axioms, the theorem can be applied to it too.

This is the power of abstraction: we do not need to rebuild linear algebra for every new kind of vector.

## 14. The eight vector-space axioms

The lecturer says there are eight axioms and describes them as a checklist for addition and scalar multiplication. The transcript does not reproduce the exact on-screen list, so the following is a standard formulation of the eight axioms for a vector space over the real numbers.

Let $\mathbf u,\mathbf v,\mathbf w$ be vectors and $a,b$ be real scalars.

### Rules for vector addition

**1. Commutativity**

$$
\mathbf u+\mathbf v=\mathbf v+\mathbf u.
$$

The order of adding vectors does not matter.

**2. Associativity**

$$
(\mathbf u+\mathbf v)+\mathbf w
=\mathbf u+(\mathbf v+\mathbf w).
$$

The grouping of additions does not matter.

**3. Existence of a zero vector**

There must be a zero vector $\mathbf 0$ such that:

$$
\mathbf v+\mathbf 0=\mathbf v.
$$

Adding zero leaves a vector unchanged.

**4. Existence of additive inverses**

For every vector $\mathbf v$, there must be an opposite vector $-\mathbf v$ such that:

$$
\mathbf v+(-\mathbf v)=\mathbf 0.
$$

A vector plus its opposite gives zero.

### Rules for scalar multiplication

**5. Compatibility of scalar multiplication**

$$
a(b\mathbf v)=(ab)\mathbf v.
$$

Scaling by $b$ and then by $a$ is equivalent to scaling once by their product.

**6. Identity scalar**

$$
1\mathbf v=\mathbf v.
$$

Multiplying a vector by 1 leaves it unchanged.

**7. Distributivity over vector addition**

$$
a(\mathbf u+\mathbf v)=a\mathbf u+a\mathbf v.
$$

Scaling a sum is the same as scaling each vector and then adding.

**8. Distributivity over scalar addition**

$$
(a+b)\mathbf v=a\mathbf v+b\mathbf v.
$$

Adding two scaling factors first is equivalent to scaling separately and adding the results.

These are not eight unrelated tricks. Together, they ensure that addition and scalar multiplication behave consistently enough for the usual results of linear algebra to work.

## 15. A vector space is not necessarily a physical space

The lecturer gives a playful example: imagine someone inventing a set of unusual objects, such as “pi creatures,” and defining their own rules for adding and scaling them.

Do these objects form a vector space?

We do not decide based on what the objects look like.

We check whether their operations satisfy the eight axioms.

If they do, then the objects form a vector space, and the results of linear algebra can be applied to them.

If they do not, we cannot automatically use all the usual vector-space theory.

This is why the axioms are useful: mathematicians can reason about the rules without needing to know every possible kind of object to which those rules might be applied.

## 16. Why textbooks define linear transformations abstractly

Earlier in the series, the lecturer explained linear transformations visually:

- Grid lines remain straight.
- Parallel lines remain parallel.
- Evenly spaced grid lines remain evenly spaced.

That is an intuitive explanation for transformations of ordinary geometric space.

But it does not directly explain how to transform a function or a polynomial.

The abstract definition works in all these settings:

$$
T(\mathbf u+\mathbf v)=T(\mathbf u)+T(\mathbf v)
$$

and

$$
T(c\mathbf v)=cT(\mathbf v).
$$

That is why textbooks generally define linear transformations using additivity and scaling rather than relying only on a geometric picture.

The abstract definition is more widely applicable.

## 17. The lecturer's final analogy: what is the number three?

Think about the number 3.

In everyday life, it might appear as:

- Three apples.
- Three books.
- Three people.

The physical objects differ, but the abstract idea of three is common to all of them.

The lecturer uses this as an analogy for vectors.

A vector might be represented by an arrow, a list of numbers, or a function. These representations look very different, but they can all embody the same abstract mathematical structure.

So mathematicians do not insist that every vector must look like an arrow or a list of numbers.

They define the structure that makes vector operations work.

## 18. Why beginners should still start with arrows

The lecturer does not suggest abandoning geometric intuition.

In fact, he recommends beginning with something concrete and visualizable, such as 2D arrows rooted at the origin.

Why?

Because visual examples help us build intuition about:

- Addition.
- Scalar multiplication.
- Linear transformations.
- Basis vectors.
- Eigenvectors.
- Change of basis.

Once we understand these ideas geometrically, we can recognize the same patterns in functions, polynomials, and other abstract vector spaces.

The abstract theory then becomes a generalization of ideas we already understand.

## 19. The final message of the lecture series

The lecturer concludes the Essence of Linear Algebra series by emphasizing that understanding the intuition is a strong foundation, but it is not a substitute for solving problems.

The purpose of the series is to build a mental picture of why the mathematics works.

Moving forward, working through exercises will make these ideas more fluent and useful.

The central lesson of this final lecture is that linear algebra is not restricted to arrows or lists of numbers. It is a theory about objects that can be added and scaled according to a consistent set of rules.

---

## 20. Formula reference

| Concept | Formula |
|---|---|
| Addition of functions | $(f+g)(x)=f(x)+g(x)$ |
| Scaling a function | $(cf)(x)=cf(x)$ |
| Linearity: additivity | $T(u+v)=T(u)+T(v)$ |
| Linearity: scaling | $T(cv)=cT(v)$ |
| Derivative of a sum | $D(f+g)=Df+Dg$ |
| Derivative of a scaled function | $D(cf)=cDf$ |
| Derivative of a power | $D(x^n)=nx^{n-1}$ |
| Polynomial coordinates | Coefficients in the basis $\{1,x,x^2,\ldots\}$ |
| Derivative matrix entry | $D_{n-1,n}=n$, using zero-based indexing |

## 21. Common misconceptions

| Misconception | Correct understanding |
|---|---|
| Every vector must be an arrow. | Functions and polynomials can also be vectors. |
| A coordinate list is the only way to define a vector. | Coordinates describe an object relative to a chosen basis. |
| Functions cannot be added like vectors. | Functions can be added point by point. |
| Differentiation is unrelated to matrices. | Differentiation is a linear operator and can be represented by a matrix once a basis is chosen. |
| Every polynomial has infinitely many non-zero coefficients. | Each individual polynomial has only finitely many non-zero coefficients, followed by zeros. |
| A vector space must be a physical space. | It is an abstract collection with addition and scalar multiplication satisfying axioms. |
| Axioms are special properties of arrows. | They are general rules that define the allowed operations in a vector space. |
| Abstract linear algebra has no connection to geometry. | Abstract ideas generalize the geometric intuition developed with arrows. |

## 22. Check your understanding

1. Why does changing basis suggest that coordinates are not the entire identity of a vector?
2. How do we define the sum of two functions?
3. What does multiplying a function by a scalar mean?
4. Why is differentiation a linear transformation?
5. What is the difference between a function and an operator?
6. Why does the polynomial basis contain infinitely many functions?
7. What are the coordinates of $x^2+3x+5$?
8. Why does the derivative matrix have positive integers above its main diagonal?
9. What polynomial is represented by the coordinate list $[4,10,3,0,\ldots]$?
10. Why can matrix-vector multiplication represent differentiation?
11. What are the two operations required for a vector space?
12. What is an axiom?
13. Why do mathematicians define vector spaces abstractly?
14. Why is it still useful for beginners to visualize vectors as arrows?

### Answers

1. A vector's coordinates depend on the chosen basis, while the underlying object remains the same.
2. Evaluate both functions at the same input and add their outputs: $(f+g)(x)=f(x)+g(x)$.
3. Multiply every output of the function by that scalar.
4. It preserves addition and scalar multiplication.
5. A function maps an input value to an output value; an operator maps an entire function to another function.
6. Polynomials can have arbitrarily large degrees, so the basis needs every non-negative power of $x$.
7. $[5,3,1,0,\ldots]$.
8. The derivative of $x^n$ is $nx^{n-1}$, so coefficient $n$ moves from the $x^n$ coordinate to the $x^{n-1}$ coordinate.
9. $4+10x+3x^2$.
10. The derivative is linear, and its action on every basis function determines its action on every polynomial.
11. Vector addition and scalar multiplication.
12. A rule that the operations must satisfy as part of the vector-space definition.
13. So theorems can apply to many different kinds of objects without being reproved for each one.
14. Arrows give a concrete visual foundation for understanding the abstract rules.

## 23. The entire series in one conceptual picture

The series began with arrows and gradually developed more general ideas:

1. Vectors as arrows.
2. Vectors as coordinate lists.
3. Vector addition and scalar multiplication.
4. Matrices as linear transformations.
5. Determinants and geometric scaling.
6. Eigenvectors and eigenvalues.
7. Change of basis.
8. Functions and polynomials as vectors.
9. Abstract vector spaces defined through axioms.

The final connection is:

> **Linear algebra is not fundamentally about arrows. It is about the structure created by addition and scalar multiplication, and the transformations that preserve that structure.**
