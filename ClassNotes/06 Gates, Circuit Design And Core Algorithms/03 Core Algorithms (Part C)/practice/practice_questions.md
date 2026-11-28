# Practice Workbook — Quantum Fourier Transform, Roots of Unity and Hidden Periods

**Companion:** [Return to main lecture notes](../Lecture_Notes.md). This workbook follows the lecture's sequence but includes additional beginner-level practice. **Every question has a worked explanation in Section B**. Try the questions first without scrolling to the solutions.

## A. Questions (attempt first)

### A1. Fundamental concepts

**Q1.** In simple language, what does a Fourier transform do? Why is it useful for finding a repeating pattern?

**Q2.** What is the difference between $N$ possible basis labels and $k$ qubits? How many basis labels are available with 3, 4, and 5 qubits?

**Q3.** Explain (a) a ket, (b) an amplitude, (c) a measurement probability and (d) a relative phase. Give a one-qubit example.

**Q4.** Explain why a complex conjugate is required when calculating an inner product. What would go wrong if you used the ordinary dot product of $(1,i)^T$ with itself?

**Q5.** What does arithmetic modulo 8 mean? Compute $7+6\pmod8$ and $5\times5\pmod8$.

**Q6.** What property defines a character $\chi$ on integers modulo $N$? Why do we need $a^N=1$ when using $\chi(x)=a^x$?

**Q7.** What makes a set of vectors *orthonormal*? Explain why Fourier basis vectors can be orthogonal even though all of them have nonzero coefficients on $|0\rangle$.

**Q8.** How is a Fourier-basis *coordinate change* different from physically applying the QFT gate to a state?

**Q9.** Why does a single transformed computational-basis state have equal measurement probabilities at all $N$ possible outcomes, even when it has nontrivial phases?

**Q10.** Explain why a circuit using $O(k^2)$ gates on $k$ qubits cannot necessarily output a classical list of all $2^k$ Fourier coefficients.

### A2. Roots of unity and character calculations

**Q11.** For $N=4$, compute $\omega_4$ and list $\omega_4^0$ through $\omega_4^7$.

**Q12.** For $N=8$, calculate $\omega_8$, $\omega_8^2$, $\omega_8^4$, and $\omega_8^6$. Show the angles.

**Q13.** With $N=8$ and $\gamma=2$, list $\chi_\gamma(x)=\omega_8^{2x}$ for $x=0,1,2,3,4$.

**Q14.** Verify that $\chi_3(2+5\bmod8)=\chi_3(2)\chi_3(5)$, where $\chi_3(x)=\omega_8^{3x}$.

**Q15.** Compute $S=1+i+i^2+i^3$. Then compute $1+(-1)+(-1)^2+(-1)^3$. Explain why the sums vanish.

**Q16.** Show geometrically or algebraically why $\sum_{x=0}^{N-1}\omega_N^{mx}=0$ whenever $m\not\equiv0\pmod N$. What is the sum if $m=0$?

### A3. Fourier basis vectors, conjugates and coordinates

**Q17.** Write all four $|f_0\rangle,|f_1\rangle,|f_2\rangle,|f_3\rangle$ vectors for $N=4$ in the computational basis.

**Q18.** Verify $\langle f_1|f_1\rangle=1$ for $N=4$. Show how the bra differs from the ket.

**Q19.** Calculate $\langle f_1|f_3\rangle$ for $N=4$ without skipping terms. Explain the mistake made if the first vector is not conjugated.

**Q20.** Let $|\psi\rangle=|0\rangle$ for $N=4$. Find its Fourier-basis coordinates $\widehat\alpha_0,\widehat\alpha_1,\widehat\alpha_2,\widehat\alpha_3$. Check normalization.

**Q21.** Let $|\psi\rangle=(|0\rangle+|2\rangle)/\sqrt2$ for $N=4$. Find the Fourier-basis coordinates using the **negative-sign** formula. Which coordinates are zero?

**Q22.** Write the matrix $F_4$ and compute its entry at row 3, column 2; row 1, column 3; and row 2, column 2. Use zero-based indexing.

**Q23.** Compute $F_4|1\rangle$. Then explain why $F_4\ne H\otimes H$.

**Q24.** Find $F_4^\dagger$ and check that $F_4^\dagger F_4|1\rangle=|1\rangle$.

**Q25.** Show that $F_N^2|x\rangle=|-x\bmod N\rangle$. What are $F_8^2|3\rangle$ and $F_8^4|3\rangle$?

### A4. Interference, shifts and periodic patterns

**Q26.** Calculate the output amplitudes of $F_8(|0\rangle+|4\rangle)/\sqrt2$ at $y=0,1,2,3$. Then identify all nonzero output outcomes and their probabilities.

**Q27.** Repeat Q26 for $F_8(|0\rangle-|4\rangle)/\sqrt2$. Explain the physical importance of the relative minus sign.

**Q28.** Calculate $F_8(|1\rangle+|5\rangle)/\sqrt2$ and show that its *probability* peaks occur at the same positions as in Q26.

**Q29.** For $N=16,r=4$, write the normalized periodic input $|\psi_r\rangle$ and the exact QFT output. Check both normalizations.

**Q30.** For $N=16,r=2$, how many input spikes and output spikes are there? Give all their labels and each surviving amplitude.

**Q31.** Derive the output amplitude $A_y$ for a uniform periodic input, beginning with $A_y=\langle y|F_N|\psi_r\rangle$. Explain why it is zero unless $y$ is a multiple of $N/r$.

**Q32.** What happens to the output if the periodic input is shifted by $s$? Show where $\omega_N^{sy}$ appears and explain what remains unchanged.

### A5. Phase gates, circuits and applications

**Q33.** Write $R_1,R_2,R_3$ as $2\times2$ diagonal matrices. Which known gate is each one?

**Q34.** Give the action of controlled-$R_2$ on each basis state $|00\rangle,|01\rangle,|10\rangle,|11\rangle$.

**Q35.** For $N=8$, $x=5$, derive the three one-qubit factors in $F_8|5\rangle$. Use the bit order $y_0y_1y_2$ with $y_0$ the most significant output bit.

**Q36.** **Supplementary application:** Find the period of $7^x\bmod15$ for $x=0,1,2,3,4$ and obtain factors of 15 from the period. Explain why this does not by itself constitute a full proof of Shor's algorithm.

### A6. Multiple choice — select one unless stated

**Q37.** The eighth root of unity $\omega_8^4$ equals (A) $1$ (B) $i$ (C) $-1$ (D) $-i$.

**Q38.** Which formula gives the coordinates of the *unchanged* state in the Fourier basis $|f_\gamma\rangle$ defined in the main notes? (A) $\widehat\alpha=F_N\alpha$ (B) $\widehat\alpha=F_N^\dagger\alpha$ (C) $\widehat\alpha=\alpha$ always (D) all of the above.

**Q39.** The quantum transform of a normalized computational basis ket $|x\rangle$ has measurement probabilities: (A) all equal to $1/N$ (B) all zero (C) one outcome 1, others zero (D) depends only on whether $x$ is even.

**Q40.** $F_4^2|1\rangle$ is (A) $|1\rangle$ (B) $|0\rangle$ (C) $|3\rangle$ (D) $|2\rangle$.

**Q41.** When $N=16$ and a normalized input has four equal spikes at 0,4,8,12, the QFT has (A) one spike (B) two spikes (C) four spikes (D) sixteen spikes.

**Q42.** Controlled-$R_3$ changes the phase of (A) $|00\rangle$ only (B) $|01\rangle$ only (C) $|10\rangle$ only (D) $|11\rangle$ only.

**Q43.** Which statement is true? (A) All QFT output states are tensor products (B) $F_4=H\otimes H$ (C) $F_N|x\rangle$ is a tensor product for a computational-basis input $|x\rangle$ (D) a single measurement returns every complex amplitude.

**Q44.** If $N=32$, the number of qubits needed to represent $N$ basis labels is (A) 32 (B) 16 (C) 10 (D) 5.

---

## B. Worked answers and explanations (check after attempting)

### B1. Conceptual answers

**A1.** A Fourier transform changes how information is represented: from values indexed by labels or time to weighted combinations of repeating phase patterns. Periodic inputs create constructive interference at some output labels and destructive interference at others. Measuring the pattern can reveal the spacing. It does not automatically solve every computational problem.

**A2.** $N=2^k$. For $k=3$, $N=8$; for $k=4$, $N=16$; for $k=5$, $N=32$. The state can have one amplitude for each of those basis labels, but its physical register uses $k$ qubits.

**A3.** A ket is a symbolic column vector of a quantum state, e.g. $|\psi\rangle=(|0\rangle+i|1\rangle)/\sqrt2$. The amplitudes are $1/\sqrt2$ and $i/\sqrt2$. Both outcomes have probability $1/2$. The second component has a relative phase $90^\circ$ ($i$) compared with the first; that can affect later interference even though the immediate probabilities are the same.

**A4.** The standard quantum inner product uses $\langle v|v\rangle=\sum v_j^*v_j=\sum|v_j|^2\ge0$. Without the complex conjugate, $(1,i)\cdot(1,i)=1+i^2=0$. But $(1,i)$ is nonzero; its correct unnormalized norm-squared is $1+(-i)i=2$. Conjugation fixes the inconsistency.

**A5.** Modulo 8 means reduce an integer to its remainder between 0 and 7. $7+6=13\equiv5\pmod8$, and $5\times5=25\equiv1\pmod8$.

**A6.** $\chi(x+y\bmod N)=\chi(x)\chi(y)$. If $\chi(x)=a^x$, then $N\equiv0\pmod N$ requires $a^N=a^0=1$. This forces $a$ to be an $N$th root of unity. Example: $a=i$ is valid modulo 4 because $i^4=1$.

**A7.** Orthonormal means every vector has length one and the inner product of any two different vectors is zero. Fourier vectors contain every computational ket, but their coefficients have different complex phases; the positive and negative contributions cancel when calculating cross-inner-products.

**A8.** A change of basis is a *different description of one unchanged state*: if $\alpha$ is its computational-coordinate column, its Fourier-basis coordinate column is $F_N^\dagger\alpha$. Applying QFT changes the state physically to $F_N|\psi\rangle$, whose computational amplitudes are $F_N\alpha$. For $N=2$ they coincide numerically because $H=H^\dagger$; not generally for larger $N$.

**A9.** $(F_N|x\rangle)_y=\omega_N^{xy}/\sqrt N$ and every root of unity has magnitude 1. Thus $|\omega_N^{xy}/\sqrt N|^2=1/N$. The phases may be different even while the probabilities are the same.

**A10.** A single measurement samples one label $y$ according to $|\alpha'_y|^2$. It does not disclose all complex amplitudes, and learning a full exponentially large state by tomography generally requires many preparations and measurements. QFT helps when the sampling distribution encodes a small useful feature.

### B2. Roots and characters

**A11.** $\omega_4=e^{2\pi i/4}=e^{i\pi/2}=i$. Its powers for 0 through 7 are $1,i,-1,-i,1,i,-1,-i$. The cycle repeats after 4 because $i^4=1$.

**A12.** $\omega_8=e^{i\pi/4}=(1+i)/\sqrt2$ (45 degrees). $\omega_8^2=e^{i\pi/2}=i$ (90 degrees), $\omega_8^4=e^{i\pi}=-1$ (180 degrees), and $\omega_8^6=e^{3\pi i/2}=-i$ (270 degrees).

**A13.** $\chi_2(x)=\omega_8^{2x}=e^{i\pi x/2}$. For $x=0,1,2,3,4$ the phases are $1,i,-1,-i,1$. This corresponds to one 90-degree rotation per sample.

**A14.** Left: $2+5\bmod8=7$; $\chi_3(7)=\omega_8^{21}=\omega_8^5$. Right: $\chi_3(2)\chi_3(5)=\omega_8^{6}\omega_8^{15}=\omega_8^{21}=\omega_8^5$. Both are identical. Reducing powers modulo 8 is valid because $\omega_8^8=1$.

**A15.** Since $i^2=-1$ and $i^3=-i$, $1+i+i^2+i^3=1+i-1-i=0$. For $-1$: $1-1+1-1=0$. These are full cycles of phase vectors, cancelling in opposite directions.

**A16.** Let $z=\omega_N^m$. Then $z^N=1$. If $m\not\equiv0\pmod N$, $z\ne1$, and $S=1+z+\cdots+z^{N-1}$ satisfies $(1-z)S=1-z^N=0$, hence $S=0$. If $m=0\pmod N$, every term equals 1 and the sum is $N$.

### B3. Fourier basis, matrices and conjugation

**A17.** For $N=4,\omega=i$:

$$\begin{aligned}
|f_0\rangle&=(1,1,1,1)^T/2,\\
|f_1\rangle&=(1,i,-1,-i)^T/2,\\
|f_2\rangle&=(1,-1,1,-1)^T/2,\\
|f_3\rangle&=(1,-i,-1,i)^T/2.
\end{aligned}$$

For example, $f_3$ comes from $i^{3x}$ for $x=0,1,2,3$, giving $1,-i,-1,i$.

**A18.** $|f_1\rangle=(1,i,-1,-i)^T/2$, so $\langle f_1|=(1,-i,-1,i)/2$ after conjugation. Multiply corresponding positions:

$$\langle f_1|f_1\rangle=\tfrac14[1+(-i)i+(-1)(-1)+i(-i)]=\tfrac14(1+1+1+1)=1.$$

**A19.** Use the $f_1$ bra and $f_3$ ket:

$$\langle f_1|f_3\rangle=\tfrac14[1+(-i)(-i)+(-1)(-1)+(i)(i)]$$
$$=\tfrac14[1-1+1-1]=0.$$

If you fail to conjugate $f_1$, the phases do not represent the correct quantum inner product, and a spurious nonzero result can occur. The spoken lecture notes a sign issue at this exact example.

**A20.** For $|\psi\rangle=|0\rangle$, $\alpha_0=1$ and every other $\alpha_x=0$. Then

$$\widehat\alpha_\gamma=\tfrac12\sum_{x=0}^3\alpha_x i^{-\gamma x}=\tfrac12 i^0=\tfrac12$$

for every $\gamma=0,1,2,3$. Norm check: four coefficients, each magnitude-squared $1/4$, so the sum equals 1.

**A21.** $\alpha_0=\alpha_2=1/\sqrt2$, others zero. Therefore

$$\widehat\alpha_\gamma=\frac1{2\sqrt2}(1+i^{-2\gamma})=\frac1{2\sqrt2}[1+(-1)^\gamma].$$

Even $\gamma=0,2$: amplitude $1/\sqrt2$. Odd $\gamma=1,3$: amplitude zero. Normalization: two outcomes each $1/2$, total 1. In this particular example the output of $F_4$ gives the same even support because the phases are real.

**A22.**

$$F_4=\tfrac12\begin{bmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{bmatrix}.$$

Entry $(3,2)=\frac12i^{6}=-1/2$. Entry $(1,3)=\frac12i^3=-i/2$. Entry $(2,2)=\frac12i^4=1/2$.

**A23.** A standard basis ket $|1\rangle$ selects column 1 of the matrix:

$$F_4|1\rangle=\tfrac12(|0\rangle+i|1\rangle-|2\rangle-i|3\rangle).$$

$F_4$ contains imaginary entries, but $H\otimes H$ contains only real $\pm1/2$ entries, so they are not equal.

**A24.** Conjugate and transpose $F_4$:

$$F_4^\dagger=\tfrac12\begin{bmatrix}1&1&1&1\\1&-i&-1&i\\1&-1&1&-1\\1&i&-1&-i\end{bmatrix}.$$

Because Fourier columns are orthonormal, $F_4^\dagger F_4=I$. To verify at coordinate 1, multiply row 1 by column 1: $(1+1+1+1)/4=1$. For coordinate 0, row 0 times column 1 gives $(1+i-1-i)/4=0$; the other nonmatching rows are also zero. Hence the resulting ket is $|1\rangle$.

**A25.** Insert the matrix elements twice:

$$\langle z|F_N^2|x\rangle=\frac1N\sum_y\omega_N^{y(z+x)}.$$

The roots-of-unity sum is 1 after dividing by $N$ only when $z+x\equiv0\pmod N$; otherwise zero. So $F_N^2|x\rangle=|-x\bmod N\rangle$. For $N=8$, $-3\equiv5\pmod8$, so $F_8^2|3\rangle=|5\rangle$. Repeating another two transforms returns $|3\rangle$: $F_8^4|3\rangle=|3\rangle$.

### B4. Interference and periods

**A26.** The coefficient at $|y\rangle$ is

$$A_y=\tfrac1{\sqrt2\sqrt8}(1+\omega_8^{4y})=\tfrac14(1+(-1)^y).$$

For $y=0,1,2,3$ this is respectively $1/2,0,1/2,0$. Thus $0,2,4,6$ survive with amplitude $1/2$ and probability $1/4$ each; all odd labels have probability zero.

**A27.** With relative minus,

$$A_y=\tfrac14(1-(-1)^y).$$

It is 0 for even $y$ and $1/2$ for odd $y$, so the surviving output is $(|1\rangle+|3\rangle+|5\rangle+|7\rangle)/2$. The two inputs have the same immediate measurement probabilities; their different relative phase causes a different interference pattern after $F_8$.

**A28.**

$$A_y=\tfrac14(\omega_8^y+\omega_8^{5y})=\tfrac14\omega_8^y(1+(-1)^y).$$

Odd values vanish, as before. At even positions, the amplitudes are $1/2,\ i/2,\ -1/2,\ -i/2$ for $y=0,2,4,6$. All four have probability $1/4$. The shift adds the phase $\omega_8^y$ but not new probability positions.

**A29.** $N=16,r=4$ gives $m=N/r=4$ input spikes:

$$|\psi_4\rangle=\frac{|0\rangle+|4\rangle+|8\rangle+|12\rangle}{2}.$$

The output formula gives the same four labels and the same coefficient $1/\sqrt4=1/2$:

$$F_{16}|\psi_4\rangle=(|0\rangle+|4\rangle+|8\rangle+|12\rangle)/2.$$

Input and output normalization are each $4\cdot(1/2)^2=1$.

**A30.** $N=16,r=2$: input has $m=8$ equally spaced spikes at $0,2,4,6,8,10,12,14$, amplitude $1/\sqrt8$ each. Output has $r=2$ spikes at $0$ and $N/r=8$, amplitude $1/\sqrt2$ each. Thus

$$F_{16}\frac{|0\rangle+|2\rangle+\cdots+|14\rangle}{\sqrt8}=\frac{|0\rangle+|8\rangle}{\sqrt2}.$$

**A31.** Write $m=N/r$ and $|\psi_r\rangle=\frac1{\sqrt m}\sum_{\ell=0}^{m-1}|\ell r\rangle$. Then

$$A_y=\langle y|F_N|\psi_r\rangle
=\frac1{\sqrt{Nm}}\sum_{\ell=0}^{m-1}\omega_N^{y\ell r}=
\frac1{\sqrt{Nm}}\sum_{\ell=0}^{m-1}e^{2\pi i y\ell/m}.$$

If $y$ is a multiple of $m$, each term is 1, so $A_y=m/\sqrt{Nm}=1/\sqrt r$. Otherwise the $m$ roots of unity cancel to 0. There are $r$ surviving $y$ values, namely $0,m,2m,\dots,(r-1)m$.

**A32.** For $|\psi_{r,s}\rangle=\frac1{\sqrt m}\sum_\ell|s+\ell r\rangle$ with labels mod $N$,

$$\langle y|F_N|\psi_{r,s}\rangle=
\frac{\omega_N^{sy}}{\sqrt{Nm}}\sum_\ell\omega_N^{yr\ell}.$$

The factor $\omega_N^{sy}$ has magnitude 1, so it changes only the relative phases of surviving outputs. Support and probabilities are the same as at offset 0.

### B5. Phase gates, tensor products, and applications

**A33.**

$$R_1=\begin{bmatrix}1&0\\0&-1\end{bmatrix}=Z,\quad
R_2=\begin{bmatrix}1&0\\0&i\end{bmatrix}=S,\quad
R_3=\begin{bmatrix}1&0\\0&e^{i\pi/4}\end{bmatrix}=T.$$

All leave $|0\rangle$ unchanged; their actions on $|1\rangle$ add 180°, 90°, and 45° of phase, respectively.

**A34.** $CR_2=\operatorname{diag}(1,1,1,i)$. Hence

$$CR_2|00\rangle=|00\rangle,\quad
CR_2|01\rangle=|01\rangle,\quad
CR_2|10\rangle=|10\rangle,\quad
CR_2|11\rangle=i|11\rangle.$$

Only the final basis state receives phase because the control is 1 **and** target is 1.

**A35.** Use

$$F_{2^k}|x\rangle=\bigotimes_{j=0}^{k-1}
\frac{|0\rangle+e^{2\pi ix/2^{j+1}}|1\rangle}{\sqrt2}.$$

With $k=3,x=5$: $j=0$ gives $e^{5\pi i}=-1$; $j=1$ gives $e^{5\pi i/2}=i$; $j=2$ gives $e^{5\pi i/4}$. Therefore

$$F_8|5\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}\otimes
\frac{|0\rangle+i|1\rangle}{\sqrt2}\otimes
\frac{|0\rangle+e^{5\pi i/4}|1\rangle}{\sqrt2}.$$

Each factor has squared length $(1+1)/2=1$, so their combined state is normalized. To check coefficient $|101\rangle$, multiply the chosen component phases: $(-1)\cdot1\cdot e^{5\pi i/4}=e^{\pi i/4}$, with global magnitude $1/\sqrt8$, agreeing with the full matrix formula $\omega_8^{5\times5}/\sqrt8$.

**A36.** The modular powers are $7^0\bmod15=1$; $7^1\bmod15=7$; $7^2\bmod15=49\bmod15=4$; $7^3\bmod15=28\bmod15=13$; $7^4\bmod15=91\bmod15=1$. They repeat after 4 steps. Since $r=4$ is even, compute $7^{r/2}=7^2=49$. Then $\gcd(49-1,15)=3$ and $\gcd(49+1,15)=5$. This illustrates the number-theoretic use of periods, but **not** the full circuit that finds the period, nor all the conditions/retries of Shor's algorithm. It is an extra explanatory example, not a derivation completed in this lecture.

### B6. Multiple-choice key with reasons

**A37 — C.** $\omega_8^4=e^{2\pi i\cdot4/8}=e^{i\pi}=-1$.

**A38 — B.** The Fourier coordinates of the unchanged state are inner products $\langle f_\gamma|\psi\rangle$; this uses the conjugated (negative-phase) matrix $F_N^\dagger$.

**A39 — A.** The output amplitude is $\omega_N^{xy}/\sqrt N$ for every $y$ and has squared modulus $1/N$.

**A40 — C.** $F_N^2$ maps $|x\rangle$ to $|-x\bmod N\rangle$; with $N=4$, $-1\bmod4=3$.

**A41 — C.** The input has $N/r=16/4=4$ equally spaced spikes; the output has $r=4$ spikes, also spaced 4 apart.

**A42 — D.** Controlled-$R_3$ multiplies $|11\rangle$ by $e^{i\pi/4}$ and leaves the other computational basis states unchanged.

**A43 — C.** The QFT image of each individual computational basis ket factors into $k$ one-qubit states. Arbitrary input superpositions may result in entangled outputs.

**A44 — D.** $2^5=32$, so five qubits label 32 computational basis states.

---

**Revision routine:** Rework Q19 (conjugate), Q22 (matrix), Q26–Q28 (interference), Q31–Q32 (periods) and Q35 (factorization) by hand. Those five clusters capture the heart of the supplied lecture.
