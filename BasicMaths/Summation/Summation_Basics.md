# Summation Basics for Quantum Computing

## Beginner-friendly notes: Lessons 1–7

These notes explain summation notation from the ground up and then connect it to the quantum-state formula:
$$
|\psi\rangle = \sum_{x\in\{0,1\}^n}\alpha_x|x\rangle
$$
The goal is to understand what each symbol means—not just memorize the formula.

---

## Learning roadmap

1. **Lesson 1:** What summation (Σ) means

2. **Lesson 2:** Variables and indices

3. **Lesson 3:** Powers and expressions inside a summation

4. **Lesson 4:** Double summation

5. **Lesson 5:** Complex numbers and summation

6. **Lesson 6:** Binary strings and summation over them

7. **Lesson 7:** Putting everything together: the quantum-state formula

---

# Lesson 1 — What does summation (Σ) mean?

## 1.1 The basic idea

Summation is a short way of writing “add these things together.”
For example:

$$
2+3+4+5=14
$$
Instead of writing every number with a plus sign, mathematicians use the Greek capital letter Sigma:
$$
\sum
$$
For example:

$$
\sum_{i=2}^{5}i
$$
This means: start at $i=2$, increase $i$ by 1 until it reaches 5, and add each value of $i$.
Expand it:

$$
\sum_{i=2}^{5}i=2+3+4+5=14
$$

## 1.2 Reading the parts

In

$$
\sum_{i=2}^{5}i
$$

- $\sum$: add the terms.

- $i$: the index (a counter).

- $i=2$: the starting value.

- $5$: the ending value.
- The final $i$: the expression to calculate and add.
The upper limit is included. So the values are 2, 3, 4, and 5.

## 1.3 Another example

$$
\sum_{i=1}^{4}i=1+2+3+4=10
$$
**Key idea:** When you see Σ, expand it into ordinary addition first.

---

# Lesson 2 — Variables and indices

## 2.1 What is a variable?

A variable is a symbol that stands for a value.
For example, if $x=5$, then:
$$
2x+3=2(5)+3=13
$$
If $x=10$, the expression has a different value:
$$
2(10)+3=23
$$

## 2.2 What is an index?

In a summation, the index is a counter that tells us which term we are currently calculating.
For example:

$$
\sum_{i=1}^{4}i
$$
The index $i$ takes these values:
$$
1,\ 2,\ 3,\ 4
$$
It is common to use letters such as $i$, $j$, $k$, or $x$ as indices.

## 2.3 The index versus the expression

Consider:

$$
\sum_{i=1}^{4}3i
$$

- $i$ is the counter.

- $3i$ is the expression we calculate for each value of the counter.
| $i$ | Calculation | Term |
|---:|---:|---:|
| 1 | $3\times1$ | 3 |
| 2 | $3\times2$ | 6 |
| 3 | $3\times3$ | 9 |
| 4 | $3\times4$ | 12 |

Therefore:

$$
\sum_{i=1}^{4}3i=3+6+9+12=30
$$

## 2.4 Can we use x instead of i?

Yes. The name of the index does not change the result:
$$
\sum_{i=1}^{4}i=\sum_{x=1}^{4}x=10
$$
The index is often called a **dummy variable** because its name can be changed, provided the expression and limits are changed consistently.

## 2.5 What if the expression does not use the index?

Consider:

$$
\sum_{i=1}^{4}5
$$
The index still takes four values, but the term is always 5:
$$
5+5+5+5=20
$$
**Key idea:** The limits tell you how many terms to add. The expression tells you what each term is.

---

# Lesson 3 — Powers and expressions inside summation

## 3.1 Multiplication is not the same as a power

These expressions mean different things:

| Expression | Meaning | Example when $i=3$ |
|---|---|---:|
| $2i$ | $2\times i$ | 6 |
| $i^2$ | $i\times i$ | 9 |
| $i^3$ | $i\times i\times i$ | 27 |
| $2i^2$ | $2\times i\times i$ | 18 |
Remember: $2i$ is not the same as $i^2$.

## 3.2 Summing squares

Consider:

$$
\sum_{i=1}^{4}i^2
$$
Substitute each value of $i$, square it, and then add:
$$
\begin{aligned}
\sum_{i=1}^{4}i^2
&=1^2+2^2+3^2+4^2\\
&=1+4+9+16\\
&=30
\end{aligned}
$$

## 3.3 Summing cubes

$$
\begin{aligned}
\sum_{i=1}^{3}i^3
&=1^3+2^3+3^3\\
&=1+8+27\\
&=36
\end{aligned}
$$

## 3.4 More complicated expressions

Consider:

$$
\sum_{i=1}^{3}(2i^2+1)
$$
Calculate the entire expression for each value of $i$:

- When $i=1$: $2(1)^2+1=3$
- When $i=2$: $2(2)^2+1=9$
- When $i=3$: $2(3)^2+1=19$
Then add:

$$
3+9+19=31
$$
**Key idea:** Substitute the index into the whole expression, calculate each term, and then add the results.

---

# Lesson 4 — Double summation

## 4.1 Why use two summations?

Sometimes we need to consider combinations of two changing values.
Suppose:

- $i$ can be 1 or 2.

- $j$ can be 1 or 2.
The possible pairs are:

$$
(1,1),\ (1,2),\ (2,1),\ (2,2)
$$
There are $2\times2=4$ combinations.

## 4.2 Reading a double summation

Consider:

$$
\sum_{i=1}^{2}\sum_{j=1}^{2}(i+j)
$$

- The outer summation changes $i$.
- For each fixed value of $i$, the inner summation runs through all values of $j$.
- Calculate $i+j$ for every pair.
- Add all the results.
For $i=1$:

$$
(1+1)+(1+2)=2+3=5
$$
For $i=2$:
$$
(2+1)+(2+2)=3+4=7
$$
Total:
$$
5+7=12
$$
The complete expansion is:
$$
\begin{aligned}
\sum_{i=1}^{2}\sum_{j=1}^{2}(i+j)
&=(1+1)+(1+2)+(2+1)+(2+2)\\
&=2+3+3+4\\
&=12
\end{aligned}
$$

## 4.3 Double summation with multiplication

$$
\sum_{i=1}^{2}\sum_{j=1}^{3}ij
$$
List every pair:

| $i$ | $j$ | $ij$ |
|---:|---:|---:|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 1 | 3 | 3 |
| 2 | 1 | 2 |
| 2 | 2 | 4 |
| 2 | 3 | 6 |
Add the terms:

$$
1+2+3+2+4+6=18
$$
There are $2\times3=6$ combinations.
**Key idea:** The inner index completes its full range for every value of the outer index.

---

# Lesson 5 — Complex numbers and summation

Complex numbers are important in quantum computing because quantum amplitudes can be complex.

## 5.1 The imaginary unit

The imaginary unit is written as $i$ and is defined by:
$$
i=\sqrt{-1}
$$
Therefore:

$$
i^2=-1
$$
**Important:** The letter $i$ can have two different jobs in mathematics:

- In a summation such as $\sum_{i=1}^{4}i$, it is an ordinary index variable.
- In a complex number such as $3+2i$, it is the imaginary unit.
The meaning comes from the context.

## 5.2 What is a complex number?

A complex number has the form:

$$
z=a+bi
$$

- $a$ is the real part.

- $b$ is the imaginary coefficient.

- $i$ is the imaginary unit.
For example, in $3+2i$:
- Real part = 3
- Imaginary coefficient = 2
Examples:
| Number | Real part | Imaginary coefficient |
|---|---:|---:|
| $2+3i$ | 2 | 3 |
| $5-4i$ | 5 | -4 |
| $6$ | 6 | 0 |
| $4i$ | 0 | 4 |

## 5.3 Adding complex numbers

Add real parts together and imaginary parts together:
$$
\begin{aligned}
(2+3i)+(4+5i)
&=(2+4)+(3i+5i)\\
&=6+8i
\end{aligned}
$$
Another example:
$$
(5+2i)+(3-4i)=8-2i
$$

## 5.4 Summing complex numbers

Consider:

$$
\sum_{k=1}^{3}(2+ki)
$$
Substitute $k=1,2,3$:
$$
(2+i)+(2+2i)+(2+3i)
$$
Group real and imaginary parts:
$$
(2+2+2)+(i+2i+3i)=6+6i
$$
The summation process is unchanged. We still substitute, calculate, and add.

## 5.5 Magnitude and magnitude squared

For a complex number $z=a+bi$, its magnitude is:
$$
\lvert z\rvert=\sqrt{a^2+b^2}
$$
For $z=3+4i$:
$$
\lvert z\rvert=\sqrt{3^2+4^2}=5
$$
Its magnitude squared is:
$$
\lvert z\rvert^2=a^2+b^2=3^2+4^2=25
$$
In quantum mechanics, the probability associated with an amplitude $\alpha$ is:

$$
P=\lvert\alpha\rvert^2
$$

This is why magnitude squared is especially important.

---

# Lesson 6 — Binary strings and summation over them

This lesson connects summation to the basis states of qubits.

## 6.1 What is a binary string?

A binary string is a sequence made only of 0s and 1s.
Examples:

- `0` has length 1.
- `10` has length 2.
- `101` has length 3.
- `1101` has length 4.
In quantum computing, binary strings label computational basis states:

| Binary string | Basis state |
|---|---|
| 0 | $\lvert 0\rangle$ |
| 1 | $\lvert 1\rangle$ |
| 00 | $\lvert 00\rangle$ |
| 01 | $\lvert 01\rangle$ |
| 10 | $\lvert 10\rangle$ |
| 11 | $\lvert 11\rangle$ |

## 6.2 What does $\{0,1\}^n$ mean?

It means **the set of every possible binary string of length $n$**.
For $n=1$:
$$
\{0,1\}^1=\{0,1\}
$$
For $n=2$:
$$
\{0,1\}^2=\{00,01,10,11\}
$$
For $n=3$:
$$
\{0,1\}^3=
\{000,001,010,011,100,101,110,111\}
$$
Every extra bit doubles the number of strings:
$$
\boxed{\text{Number of strings}=2^n}
$$
**Correction to a common typo:** The number is $2^n$, not $2n$.

## 6.3 What does the symbol $\in$ mean?

The symbol $\in$ means “belongs to” or “is an element of.”
For example:

$$
01\in\{00,01,10,11\}
$$
This is true because `01` is one of the strings in that set.
Therefore:

$$
x\in\{0,1\}^n
$$
means that $x$ is one of the binary strings of length $n$.

## 6.4 Summing over binary strings

Consider:

$$
\sum_{x\in\{0,1\}^{2}}f(x)
$$
For two bits, the possible strings are:
$$
00,\ 01,\ 10,\ 11
$$
So the summation expands to:
$$
f(00)+f(01)+f(10)+f(11)
$$
This is just ordinary summation, except the index runs over binary strings rather than counting numbers.

---

# Lesson 7 — Decoding the complete quantum-state formula

Now we can put everything together.
The formula is:
$$
\boxed{
|\psi\rangle =
\sum_{x\in\{0,1\}^{n}}\alpha_x|x\rangle
}
$$

## 7.1 Understand every symbol

| Symbol | Beginner-friendly meaning |
|---|---|
| $\lvert \psi\rangle$ | The complete quantum state |
| $\sum$ | Add all the terms |
| $x$ | A binary string, such as 00 or 101 |
| $\in$ | Belongs to |
| $\{0,1\}^n$ | All binary strings of length $n$ |
| $\alpha_x$ | The complex amplitude associated with string $x$ |
| $\lvert x\rangle$ | The basis state labelled by binary string $x$ |

Read the whole expression in plain English:
> A quantum state is a sum of all possible computational basis states. Each basis state is multiplied by its own complex amplitude.

## 7.2 Expand it for one qubit

When $n=1$:
$$
\{0,1\}^1=\{0,1\}
$$
Therefore:

$$
|\psi\rangle=\alpha_0|0\rangle+\alpha_1|1\rangle
$$

There are two basis states and two amplitudes.

## 7.3 Expand it for two qubits

When $n=2$:
$$
\{0,1\}^2=\{00,01,10,11\}
$$
Therefore:

$$
\begin{aligned}
|\psi\rangle={}&
\alpha_{00}|00\rangle\\
&+\alpha_{01}|01\rangle\\
&+\alpha_{10}|10\rangle\\
&+\alpha_{11}|11\rangle
\end{aligned}
$$
There are four basis states and four amplitudes.

## 7.4 Expand it for three qubits

When $n=3$, there are $2^3=8$ binary strings:
$$
\begin{aligned}
|\psi\rangle={}&
\alpha_{000}|000\rangle+
\alpha_{001}|001\rangle\\
&+\alpha_{010}|010\rangle+
\alpha_{011}|011\rangle\\
&+\alpha_{100}|100\rangle+
\alpha_{101}|101\rangle\\
&+\alpha_{110}|110\rangle+
\alpha_{111}|111\rangle
\end{aligned}
$$
There are eight basis states and eight amplitudes.

## 7.5 What are amplitudes?

An amplitude is a number associated with a basis state. It can be real or complex.
For example, a two-qubit state might be:
$$
|\psi\rangle=
\frac12|00\rangle+
\frac{i}{2}|01\rangle+
\frac12|10\rangle-
\frac{i}{2}|11\rangle
$$
The amplitudes are:

| Basis state | Amplitude |
|---|---|
| $\lvert 00\rangle$ | $1/2$ |
| $\lvert 01\rangle$ | $i/2$ |
| $\lvert 10\rangle$ | $1/2$ |
| $\lvert 11\rangle$ | $-i/2$ |

## 7.6 The normalization condition

A valid normalized pure quantum state must satisfy:
$$
\boxed{\sum_x|\alpha_x|^2=1}
$$
In plain English:
> Calculate the squared magnitude of every amplitude and add those values. The total must be 1.
For the example above:
$$
\begin{aligned}
\sum_x|\alpha_x|^2
&=\left|\frac12\right|^2+
\left|\frac{i}{2}\right|^2+
\left|\frac12\right|^2+
\left|-\frac{i}{2}\right|^2\\
&=\frac14+\frac14+\frac14+\frac14\\
&=1
\end{aligned}
$$
This is the total-probability rule.

## 7.7 Why doesn't one measurement reveal all amplitudes?

A quantum state may have many amplitudes in its mathematical description. But measuring the qubits in the computational basis produces one outcome per measurement.
For the equal-amplitude two-qubit state:
$$
|\psi\rangle=
\frac12|00\rangle+
\frac12|01\rangle+
\frac12|10\rangle+
\frac12|11\rangle
$$
each outcome has probability:
$$
\left|\frac12\right|^2=\frac14=25\%
$$
One measurement returns one of `00`, `01`, `10`, or `11`—not all four amplitudes.
To estimate the probabilities, we repeat measurements on identically prepared states. To reconstruct the full quantum state, including phase information, more involved methods such as quantum state tomography are needed.

---

# Quick reference — Important formulas

| Concept | Formula |
|---|---|
| Number of binary strings | $2^n$ |
| Basic summation | $\sum_{i=1}^{n}i$ |
| Sum of squares | $\sum_{i=1}^{n}i^2$ |
| Complex number | $z=a+bi$ |
| Imaginary unit | $i=\sqrt{-1}$, $i^2=-1$ |
| Magnitude squared | $\lvert z\rvert^2=a^2+b^2$ |
| Quantum state | $\lvert\psi\rangle=\sum_x\alpha_x\lvert x\rangle$ |
| Normalization | $\sum_x\lvert\alpha_x\rvert^2=1$ |
| Measurement probability | $P(x)=\lvert\alpha_x\rvert^2$ |

---

# Self-assessment quiz

The quiz is **embedded below** in this document. Scroll down, answer the questions, then click **Check answers**.

> **Cursor / VS Code preview:** If the frame looks empty, use **Markdown: Open Preview to the Side** (`Ctrl+K V`). Some previews block embedded pages; open `Summation_Basics.html` in a browser for the full notes + quiz in one page.

<div class="summation-quiz-embed">
<iframe
  title="Summation and quantum states quiz"
  style="width:100%;min-height:1400px;border:1px solid #dce3ed;border-radius:12px;background:#f5f7fb;"
  loading="lazy"
  srcdoc="&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
&lt;meta charset=&quot;UTF-8&quot;&gt;
&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
&lt;title&gt;Summation and Quantum States — Quiz&lt;/title&gt;
&lt;style&gt;
  body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    max-width: 850px;
    margin: 30px auto;
    padding: 0 18px;
    background: #f5f7fb;
    color: #202938;
  }
  h1, h2 { color: #183b66; }
  .intro, .question, .result {
    background: white;
    border: 1px solid #dce3ed;
    border-radius: 12px;
    padding: 18px;
    margin: 16px 0;
  }
  .question h3 { margin-top: 0; }
  label {
    display: block;
    padding: 7px 9px;
    margin: 5px 0;
    border-radius: 7px;
    cursor: pointer;
  }
  label:hover { background: #f0f5fc; }
  input { margin-right: 8px; }
  button {
    border: 0;
    border-radius: 8px;
    padding: 11px 18px;
    margin: 8px 6px 8px 0;
    background: #1769aa;
    color: white;
    font-size: 15px;
    cursor: pointer;
  }
  button.secondary { background: #596579; }
  button:disabled { opacity: .5; cursor: not-allowed; }
  .feedback { margin-top: 10px; padding: 10px; border-radius: 7px; }
  .correct { background: #e5f7ec; color: #176536; }
  .incorrect { background: #fff0ed; color: #9c3025; }
  .muted { color: #667085; }
  .result { display: none; }
  code { background: #eef2f7; padding: 2px 5px; border-radius: 4px; }
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Summation and Quantum States&lt;/h1&gt;
&lt;p class=&quot;muted&quot;&gt;Beginner quiz covering Lessons 1–7&lt;/p&gt;
&lt;div class=&quot;intro&quot;&gt;
  &lt;strong&gt;Instructions&lt;/strong&gt;
  &lt;ul&gt;
    &lt;li&gt;Choose one answer for every question.&lt;/li&gt;
    &lt;li&gt;Click “Check answers” to see explanations.&lt;/li&gt;
    &lt;li&gt;Your final score will appear at the end.&lt;/li&gt;
    &lt;li&gt;You can reset the quiz and try again.&lt;/li&gt;
  &lt;/ul&gt;
&lt;/div&gt;
&lt;div id=&quot;quiz&quot;&gt;&lt;/div&gt;
&lt;button id=&quot;checkButton&quot; onclick=&quot;checkAnswers()&quot;&gt;Check answers&lt;/button&gt;
&lt;button class=&quot;secondary&quot; onclick=&quot;resetQuiz()&quot;&gt;Reset quiz&lt;/button&gt;
&lt;div id=&quot;result&quot; class=&quot;result&quot;&gt;&lt;/div&gt;
&lt;script&gt;
const questions = [
  {
    lesson: &quot;Lesson 1 — Basic summation&quot;,
    question: &quot;What does the Sigma symbol (Σ) mean?&quot;,
    options: [&quot;Multiply numbers&quot;, &quot;Add terms together&quot;, &quot;Divide terms&quot;],
    answer: 1,
    explanation: &quot;Sigma is the summation symbol. It tells us to add a collection of terms.&quot;
  },
  {
    lesson: &quot;Lesson 1 — Basic summation&quot;,
    question: &quot;Calculate: Σ from i = 1 to 4 of i.&quot;,
    options: [&quot;10&quot;, &quot;4&quot;, &quot;8&quot;],
    answer: 0,
    explanation: &quot;Expand it: 1 + 2 + 3 + 4 = 10.&quot;
  },
  {
    lesson: &quot;Lesson 2 — Variables and indices&quot;,
    question: &quot;In Σ from i = 1 to 4 of 3i, what is i?&quot;,
    options: [&quot;The final answer&quot;, &quot;The index or counter&quot;, &quot;Always the number 3&quot;],
    answer: 1,
    explanation: &quot;The index i takes the values 1, 2, 3 and 4.&quot;
  },
  {
    lesson: &quot;Lesson 2 — Variables and indices&quot;,
    question: &quot;What is Σ from i = 1 to 3 of 5?&quot;,
    options: [&quot;5&quot;, &quot;10&quot;, &quot;15&quot;],
    answer: 2,
    explanation: &quot;The term 5 is added three times: 5 + 5 + 5 = 15.&quot;
  },
  {
    lesson: &quot;Lesson 3 — Powers&quot;,
    question: &quot;What is the value of 3²?&quot;,
    options: [&quot;6&quot;, &quot;9&quot;, &quot;8&quot;],
    answer: 1,
    explanation: &quot;3² means 3 multiplied by itself: 3 × 3 = 9.&quot;
  },
  {
    lesson: &quot;Lesson 3 — Powers&quot;,
    question: &quot;Calculate: Σ from i = 1 to 3 of i².&quot;,
    options: [&quot;6&quot;, &quot;14&quot;, &quot;9&quot;],
    answer: 1,
    explanation: &quot;1² + 2² + 3² = 1 + 4 + 9 = 14.&quot;
  },
  {
    lesson: &quot;Lesson 3 — Powers&quot;,
    question: &quot;Calculate: Σ from i = 1 to 2 of (i² + 2).&quot;,
    options: [&quot;7&quot;, &quot;9&quot;, &quot;11&quot;],
    answer: 1,
    explanation: &quot;(1² + 2) + (2² + 2) = 3 + 6 = 9.&quot;
  },
  {
    lesson: &quot;Lesson 4 — Double summation&quot;,
    question: &quot;If i has 2 possible values and j has 3 possible values, how many pairs are there?&quot;,
    options: [&quot;5&quot;, &quot;6&quot;, &quot;9&quot;],
    answer: 1,
    explanation: &quot;There are 2 × 3 = 6 combinations.&quot;
  },
  {
    lesson: &quot;Lesson 4 — Double summation&quot;,
    question: &quot;Calculate: Σ i=1..2 Σ j=1..2 (i+j).&quot;,
    options: [&quot;10&quot;, &quot;12&quot;, &quot;14&quot;],
    answer: 1,
    explanation: &quot;(1+1) + (1+2) + (2+1) + (2+2) = 2 + 3 + 3 + 4 = 12.&quot;
  },
  {
    lesson: &quot;Lesson 5 — Complex numbers&quot;,
    question: &quot;What is i² for the imaginary unit?&quot;,
    options: [&quot;1&quot;, &quot;-1&quot;, &quot;0&quot;],
    answer: 1,
    explanation: &quot;The imaginary unit is defined by i² = -1.&quot;
  },
  {
    lesson: &quot;Lesson 5 — Complex numbers&quot;,
    question: &quot;Calculate (2 + 3i) + (4 + 5i).&quot;,
    options: [&quot;6 + 8i&quot;, &quot;6 + 15i&quot;, &quot;8 + 8i&quot;],
    answer: 0,
    explanation: &quot;Add real parts: 2 + 4 = 6. Add imaginary parts: 3i + 5i = 8i.&quot;
  },
  {
    lesson: &quot;Lesson 5 — Complex numbers&quot;,
    question: &quot;What is the magnitude squared of z = 3 + 4i?&quot;,
    options: [&quot;5&quot;, &quot;25&quot;, &quot;7&quot;],
    answer: 1,
    explanation: &quot;|z|² = 3² + 4² = 9 + 16 = 25.&quot;
  },
  {
    lesson: &quot;Lesson 6 — Binary strings&quot;,
    question: &quot;What does {0,1}³ represent?&quot;,
    options: [
      &quot;Three values: 0, 1 and 3&quot;,
      &quot;All binary strings of length 3&quot;,
      &quot;Only 000 and 111&quot;
    ],
    answer: 1,
    explanation: &quot;It represents all eight strings of length 3, from 000 to 111.&quot;
  },
  {
    lesson: &quot;Lesson 6 — Binary strings&quot;,
    question: &quot;How many strings are in {0,1}⁴?&quot;,
    options: [&quot;4&quot;, &quot;8&quot;, &quot;16&quot;],
    answer: 2,
    explanation: &quot;There are 2⁴ = 16 binary strings of length 4.&quot;
  },
  {
    lesson: &quot;Lesson 6 — Binary strings&quot;,
    question: &quot;Expand Σ over x ∈ {0,1}² of f(x).&quot;,
    options: [
      &quot;f(00) + f(11)&quot;,
      &quot;f(00) + f(01) + f(10) + f(11)&quot;,
      &quot;f(0) + f(1)&quot;
    ],
    answer: 1,
    explanation: &quot;The four binary strings of length 2 are 00, 01, 10 and 11.&quot;
  },
  {
    lesson: &quot;Lesson 7 — Quantum state formula&quot;,
    question: &quot;How many amplitudes are needed to describe a general pure state of 3 qubits?&quot;,
    options: [&quot;3&quot;, &quot;6&quot;, &quot;8&quot;],
    answer: 2,
    explanation: &quot;There are 2³ = 8 computational basis states, each with an amplitude.&quot;
  },
  {
    lesson: &quot;Lesson 7 — Quantum state formula&quot;,
    question: &quot;In αₓ|x⟩, what does αₓ represent?&quot;,
    options: [
      &quot;The number of qubits&quot;,
      &quot;The amplitude associated with basis state |x⟩&quot;,
      &quot;The measurement result&quot;
    ],
    answer: 1,
    explanation: &quot;αₓ is the complex amplitude associated with the basis state |x⟩.&quot;
  },
  {
    lesson: &quot;Lesson 7 — Quantum state formula&quot;,
    question: &quot;What does Σₓ |αₓ|² = 1 mean?&quot;,
    options: [
      &quot;All amplitudes must be equal&quot;,
      &quot;The total probability of all measurement outcomes is 1&quot;,
      &quot;There must be exactly one qubit&quot;
    ],
    answer: 1,
    explanation: &quot;The squared magnitudes of all amplitudes are probabilities, and their sum must be 1.&quot;
  },
  {
    lesson: &quot;Lesson 7 — Quantum state formula&quot;,
    question: &quot;What does Σ over x ∈ {0,1}ⁿ of αₓ|x⟩ mean?&quot;,
    options: [
      &quot;Add every basis state multiplied by its corresponding amplitude&quot;,
      &quot;Multiply all the binary strings&quot;,
      &quot;Measure all basis states at once&quot;
    ],
    answer: 0,
    explanation: &quot;The quantum state is a sum of all computational basis states, each weighted by its amplitude.&quot;
  },
  {
    lesson: &quot;Lesson 7 — Measurement&quot;,
    question: &quot;Does one computational-basis measurement reveal every amplitude?&quot;,
    options: [
      &quot;Yes, all amplitudes are returned&quot;,
      &quot;No, one measurement returns one outcome&quot;,
      &quot;Yes, if there are two qubits&quot;
    ],
    answer: 1,
    explanation: &quot;A measurement returns one outcome. Repeated experiments and additional methods are needed to learn about the state.&quot;
  }
];
const quiz = document.getElementById(&quot;quiz&quot;);
function renderQuiz() {
  quiz.innerHTML = &quot;&quot;;
  questions.forEach((q, index) =&gt; {
    const card = document.createElement(&quot;section&quot;);
    card.className = &quot;question&quot;;
    card.id = &quot;question-&quot; + index;
    const heading = document.createElement(&quot;p&quot;);
    heading.className = &quot;muted&quot;;
    heading.textContent = q.lesson;
    const title = document.createElement(&quot;h3&quot;);
    title.textContent = (index + 1) + &quot;. &quot; + q.question;
    card.appendChild(heading);
    card.appendChild(title);
    q.options.forEach((option, optionIndex) =&gt; {
      const label = document.createElement(&quot;label&quot;);
      const radio = document.createElement(&quot;input&quot;);
      radio.type = &quot;radio&quot;;
      radio.name = &quot;q&quot; + index;
      radio.value = optionIndex;
      label.appendChild(radio);
      label.appendChild(document.createTextNode(option));
      card.appendChild(label);
    });
    const feedback = document.createElement(&quot;div&quot;);
    feedback.className = &quot;feedback&quot;;
    feedback.id = &quot;feedback-&quot; + index;
    feedback.hidden = true;
    card.appendChild(feedback);
    quiz.appendChild(card);
  });
}
function checkAnswers() {
  let score = 0;
  let unanswered = 0;
  questions.forEach((q, index) =&gt; {
    const selected = document.querySelector(
      &#x27;input[name=&quot;q&#x27; + index + &#x27;&quot;]:checked&#x27;
    );
    const feedback = document.getElementById(&quot;feedback-&quot; + index);
    feedback.hidden = false;
    if (!selected) {
      unanswered++;
      feedback.className = &quot;feedback incorrect&quot;;
      feedback.textContent = &quot;Not answered. &quot; + q.explanation;
      return;
    }
    if (Number(selected.value) === q.answer) {
      score++;
      feedback.className = &quot;feedback correct&quot;;
      feedback.textContent = &quot;Correct! &quot; + q.explanation;
    } else {
      feedback.className = &quot;feedback incorrect&quot;;
      feedback.textContent =
        &quot;Not quite. Correct answer: &quot; + q.options[q.answer] +
        &quot;. &quot; + q.explanation;
    }
  });
  const result = document.getElementById(&quot;result&quot;);
  result.style.display = &quot;block&quot;;
  result.innerHTML =
    &quot;&lt;h2&gt;Your score: &quot; + score + &quot; / &quot; + questions.length + &quot;&lt;/h2&gt;&quot; +
    &quot;&lt;p&gt;Unanswered questions: &quot; + unanswered + &quot;&lt;/p&gt;&quot; +
    &quot;&lt;p&gt;&quot; +
    (score &gt;= 18 ? &quot;Excellent work! You have a strong grasp of these concepts.&quot; :
     score &gt;= 14 ? &quot;Good progress. Review the explanations for any mistakes.&quot; :
     &quot;Keep practising. Revisit the relevant lessons and try again.&quot;) +
    &quot;&lt;/p&gt;&quot;;
  document.getElementById(&quot;checkButton&quot;).disabled = true;
  window.scrollTo({ top: result.offsetTop, behavior: &quot;smooth&quot; });
}
function resetQuiz() {
  document.getElementById(&quot;result&quot;).style.display = &quot;none&quot;;
  document.getElementById(&quot;checkButton&quot;).disabled = false;
  renderQuiz();
  window.scrollTo({ top: 0, behavior: &quot;smooth&quot; });
}
renderQuiz();
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;">
</iframe>
</div>

---

## Suggested way to study these notes

1. Read one lesson at a time.
2. Work through each mathematical example yourself before looking at the solution.
3. Expand summation expressions into ordinary addition whenever possible.
4. Complete the **embedded quiz** at the end of this document (or open `Summation_Basics.html` in a browser).
5. Revisit the quantum-state formula and try explaining every symbol in your own words.

**The most important takeaway:** Summation is just a compact way of adding terms. In quantum computing, the terms happen to be complex amplitudes multiplied by basis states.
