# Practice Questions and Fully Worked Answers

**Lecture:** *Gates & Circuit Design [2/3] — Universality and Cost* (IIT Delhi, Prof. Kolin Paul)

These questions use the lecture lecture and slides, expanded with additional beginner-level checks. Work through **Part A** before opening **Part B**. Answers are placed separately so you can test yourself honestly. A calculator is optional; use `π≈3.14159`, `√2≈1.4142`, and `√3≈1.7321` when needed.

---

# Part A — Questions (Try These First)

## A1. Basic understanding (conceptual)

**Q1.** Explain the term *universal gate set* using a construction-toy analogy. Why is classical NAND considered exactly universal?

**Q2.** The professor uses the words *exact universality* and *approximate universality*. What is the difference? Why does the distinction appear when gate angles can vary continuously?

**Q3.** Is CNOT by itself sufficient to implement an arbitrary one-qubit rotation? If not, what gate collection is exactly universal for multi-qubit computation?

**Q4.** What does it mean for a matrix `U` to be unitary? Write its defining equation, and explain why checking only the determinant is not enough.

**Q5.** What does a global phase do to measurement probabilities? Why is a phase applied only to the control=1 branch of a controlled operation potentially observable?

**Q6.** Why is a circuit that is **algebraically exact** not necessarily **physically error-free**?

**Q7.** What is the difference between a *physical qubit* and a *logical qubit*? Why is naive cloning of unknown qubits not a valid quantum error-correction method?

**Q8.** What special property defines Clifford gates? Can Clifford circuits create entangled states? Why does that not contradict efficient classical simulation under the Gottesman–Knill theorem?

## A2. Step-by-step numerical and matrix problems

**Q9. NAND-only XOR.** Build XOR from the four NAND formulas

\[
p=\neg(a\land b),\ q=\neg(a\land p),\ r=\neg(b\land p),\quad a\oplus b=\neg(q\land r).
\]

Calculate `p`, `q`, `r`, and final XOR when `(a,b)=(0,1)` and `(1,1)`.

**Q10. Matrix multiplication.** Given

\[
H=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix},
\]

calculate `H|0⟩` and `H|1⟩`, showing intermediate column-vector multiplication.

**Q11. Controlled-Y rotation.** Start with target `|0⟩`. For `θ=π/3`, compute `Ry(θ)|0⟩` and the probability of measuring target 1. Compare control=0 and control=1 for a controlled `Ry(θ)`.

**Q12. Exact H decomposition.** Verify on `|0⟩` that

\[
H=e^{i\pi/2}R_y(\pi/2)R_z(\pi).
\]

Show every intermediate state and simplify the complex coefficients.

**Q13. Phase gate decomposition.** Starting with `Rz(π/4)`, prove

\[
T=e^{i\pi/8}R_z(\pi/4)
=\begin{bmatrix}1&0\\0&e^{i\pi/4}\end{bmatrix}.
\]

**Q14. Verify one Clifford identity.** Multiply the matrices to show `SXS†=Y`, where `S=diag(1,i)` and `X=[[0,1],[1,0]]`.

**Q15. ABC trick.** Let `A=Ry(θ/2)`, `B=Ry(−θ/2)`, `C=I`. Prove `ABC=I` and `AXBXC=Ry(θ)` using the identity `X Ry(φ) X=Ry(−φ)`.

**Q16. SWAP decomposition.** Track input `(a,b)=(1,0)` through CNOT from first to second, then second to first, then first to second. Explain why the outputs are swapped.

**Q17. Toffoli truth table.** Find CCX outputs for inputs `110`, `111`, `101` and `010`. Show the value of `ab` each time.

**Q18. Toffoli via CCZ.** Starting with `|110⟩`, apply H to the target, then CCZ, then H again. Show that the result is `|111⟩`. State what happens when the first control is 0.

**Q19. Phase-polynomial identity.** Verify

\[
4abc=a+b+c-(a\oplus b)-(a\oplus c)-(b\oplus c)+(a\oplus b\oplus c)
\]

for `(a,b,c)=(1,1,1)` and `(1,1,0)`. Here the outer arithmetic uses integers; only `⊕` denotes XOR.

**Q20. Count the textbook Toffoli.** A circuit contains 6 CNOTs, 4 T, 3 T† and 2 H. Find (i) total gate count, (ii) T-count, (iii) CNOT count, and (iv) number of qubit wires in the ancilla-free construction.

**Q21. Adder compilation.** An adder has five CCX and five CX. Each CCX is decomposed using six CX and seven T/T†. Calculate the compiled CX and T counts. The slide gives 20 T and 15 T†: check the sum.

**Q22. Gate count versus depth.** The following two operations can run simultaneously on different qubits: `H(q0)` and `T(q2)`. Then `CX(q0,q1)` runs; then `T†(q0)` and `X(q2)` run together. Find total gate count, depth, T-count and T-depth.

**Q23. Pure-state fidelity.** Let `|ψ⟩=|0⟩`. Find fidelity against each noisy state (a) `X|0⟩`, (b) `Z|0⟩`, (c) `−|0⟩`. Show the overlaps.

**Q24. One T mistake.** Ideal state is `|+⟩`; noisy state is `T|+⟩`. Calculate

\[
F=|\langle+|T|+\rangle|^2
\]

using `T=diag(1,e^{iπ/4})`. Give an exact expression and approximate decimal value.

**Q25. Fidelity over trials.** Four noise trials have fidelities `1, 1, 0, 0.5`. Find the average. Explain why a random fault experiment needs multiple trials.

## A3. Applications and interpretation

**Q26.** Your desired gate is `Rz(0.1)`. A candidate approximation is distance `0.058` away. A second is `0.0013` away. Which pass error budgets `ε=0.1`, `ε=0.01`, and `ε=0.001`? Explain all comparisons.

**Q27.** A particular native chip provides only neighbor-to-neighbor interactions. Your algorithm requests a CNOT between distant logical wires. What routing operation may a compiler add? Why does that change physical cost?

**Q28.** Compare a circuit with 100 CNOTs and no T to a circuit with 10 T and no CNOT. Which is more expensive on a noisy device? Which could be more expensive on a fault-tolerant device? Explain the assumptions.

**Q29.** Why might a relative-phase Toffoli be acceptable inside one algorithm but unacceptable inside another algorithm where phases later interfere?

**Q30. Mini-Capstone check.** Describe the logic of an ideal-state-versus-noisy-state experiment, including where random X/Z faults enter, how `F` is measured, and what must be preserved when editing the autograded notebook.

## A4. Multiple-choice test

**MCQ1.** Which claim is correct? 
A. CNOT alone is exactly universal. 
B. Any one-qubit unitary can be expressed by ZYZ rotations plus a global phase. 
C. H and S reach every Bloch-sphere position exactly from `|0⟩`. 
D. T is a Clifford gate.

**MCQ2.** `T†` contributes how much to T-count? 
A. Zero B. One C. Two D. It depends on measurement basis.

**MCQ3.** For `Rz(β)Ry(γ)Rz(δ)|ψ⟩`, which operation happens first? 
A. `Rz(β)` B. `Ry(γ)` C. `Rz(δ)` D. All simultaneously.

**MCQ4.** Which is an exact Clifford+T construction according to the lecture? 
A. `Rz(0.1)` B. Generic continuously varying rotation C. Textbook CCX / Toffoli D. Every arbitrary unitary with one gate.

**MCQ5.** Which factor is often especially expensive on an error-corrected machine? 
A. T-count B. Global phase of a single isolated state C. Comment lines in Qiskit D. Circuit labels.

**MCQ6.** A quantum state can have fidelity 1 with another state even when its ket equals the negative of the other ket. Why? 
A. Measurement ignores relative phase always B. Global phase is unobservable C. X equals Z D. A fidelity of 1 means bit flips have no effect.

---

# Part B — Detailed Answer Key and Explanations

## B1. Basic understanding answers

**A1.** A universal gate is like a construction-toy brick that can be joined to make any shape in the permitted family. NAND can construct NOT by tying both inputs together (`NAND(a,a)=¬a`), and known NAND combinations reproduce AND, OR and the other Boolean functions. Because every Boolean truth table can be decomposed using such logical operations, NAND produces exact truth tables, not numerical approximations.

**A2.** Exact universality means the synthesized circuit represents the requested operation exactly (possibly up to unobservable global phase). Approximate universality means the synthesized circuit lies within a chosen error tolerance. A quantum gate may involve any real rotation angle, giving continuously many possible unitaries. The finite words of a fixed finite gate alphabet are only countably many; we can get arbitrarily close but not hit every angle exactly.

**A3.** No. CNOT acts on two qubits and has a fixed action; it cannot by itself create all arbitrary one-qubit phases and rotations. **All one-qubit unitaries together with CNOT** are exactly universal for arbitrary multi-qubit unitaries. A finite example such as `{H,S,T,CNOT}` is approximately universal.

**A4.** A unitary gate obeys `U†U=I`, where `U†` means conjugate-transpose. It preserves the vector norm and therefore total probability. A determinant condition by itself does not guarantee unitary action: for instance, the real matrix `diag(2,1/2)` has determinant 1 but stretches some vectors and compresses others, so `U†U=diag(4,1/4)≠I`.

**A5.** Multiplying every amplitude in a pure ket by `e^{iα}` changes neither its squared magnitudes nor measurement statistics. But in a controlled gate, applying `e^{iα}` only when the control is 1 introduces a phase **between** the control-0 and control-1 components. That relative phase can affect interference if the control is in a superposition, so the `P(α)` operation cannot in general be dropped.

**A6.** Algebraic exactness means the ideal gate matrices multiply to the exact target matrix. Physical hardware can still experience calibration errors, environmental noise, loss of coherence, crosstalk, and imperfect measurement. The mathematical circuit and the noisy physical implementation are different objects.

**A7.** A physical qubit is a real, imperfect quantum system. A logical qubit is quantum information **encoded and protected** across multiple physical systems. An unknown quantum state cannot be duplicated arbitrarily by a universal cloner, so quantum error correction uses entangled encoding and syndrome measurements rather than simply creating three separate perfect copies of the unknown state.

**A8.** A Clifford gate maps Pauli operators into Pauli operators under conjugation. Clifford gates can indeed create Bell and GHZ entanglement. For suitably restricted stabilizer preparations and measurements, Gottesman–Knill allows efficient classical simulation by tracking the stabilizer/Pauli transformations, even though the states may be entangled.

## B2. Numerical and mathematical solutions

**A9. Four NAND calculations.** Recall `NAND(x,y)=1−xy` when x and y are bits.

Case `(0,1)`:

\[
p=1-0\cdot1=1,\quad q=1-0\cdot1=1,
\quad r=1-1\cdot1=0,
\quad \mathrm{XOR}=1-1\cdot0=1.
\]

Case `(1,1)`:

\[
p=1-1\cdot1=0,\quad q=1-1\cdot0=1,
\quad r=1-1\cdot0=1,
\quad \mathrm{XOR}=1-1\cdot1=0.
\]

Thus the output matches XOR: differing bits give 1, identical bits give 0.

**A10. Hadamard multiplication.**

\[
H|0\rangle=\frac1{\sqrt2}
\begin{bmatrix}1&1\\1&-1\end{bmatrix}
\begin{bmatrix}1\\0\end{bmatrix}
=\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}=|+\rangle.
\]

The first component is `1·1+1·0=1`, and the second is `1·1+(−1)·0=1`.

\[
H|1\rangle=\frac1{\sqrt2}
\begin{bmatrix}1&1\\1&-1\end{bmatrix}
\begin{bmatrix}0\\1\end{bmatrix}
=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}=|-\rangle.
\]

The first component is `1·0+1·1=1`, and the second is `1·0+(−1)·1=−1`.

**A11. Controlled `Ry(π/3)`.**

\[
R_y(\theta)|0\rangle=
\cos\frac\theta2|0\rangle+\sin\frac\theta2|1\rangle.
\]

For `θ=π/3`, half the angle is `π/6=30°`, so `cos=√3/2` and `sin=1/2`:

\[
R_y(\pi/3)|0\rangle=\frac{\sqrt3}{2}|0\rangle+\frac12|1\rangle.
\]

The probability of measuring 1 is `|1/2|²=1/4=25%`. With control 0, the gate is not applied and the target remains `|0⟩`, so `P(1)=0`. With control 1, `P(1)=25%`.

**A12. Hadamard from rotations.**

\[
R_z(\pi)|0\rangle=e^{-i\pi/2}|0\rangle=-i|0\rangle.
\]

Next,

\[
R_y(\pi/2)(-i|0\rangle)=-i\frac{|0\rangle+|1\rangle}{\sqrt2}.
\]

Finally `e^{iπ/2}=i`, and `i(−i)=−i²=1`, so

\[
e^{i\pi/2}R_y(\pi/2)R_z(\pi)|0\rangle
=\frac{|0\rangle+|1\rangle}{\sqrt2}=H|0\rangle.
\]

The companion calculation on `|1⟩` produces `|−⟩` (shown in the main notes), proving the full matrix equality.

**A13. T and global phase.**

\[
R_z(\pi/4)=\begin{bmatrix}e^{-i\pi/8}&0\\0&e^{i\pi/8}\end{bmatrix}.
\]

Multiplying both entries by `e^{iπ/8}` gives

\[
\begin{bmatrix}e^{i\pi/8-i\pi/8}&0\\0&e^{i\pi/8+i\pi/8}\end{bmatrix}
=\begin{bmatrix}1&0\\0&e^{i\pi/4}\end{bmatrix}=T.
\]

**A14. Clifford `SXS†`.** Since `S†=diag(1,−i)`,

\[
XS^\dagger=\begin{bmatrix}0&1\\1&0\end{bmatrix}
\begin{bmatrix}1&0\\0&-i\end{bmatrix}
=\begin{bmatrix}0&-i\\1&0\end{bmatrix}.
\]

Then

\[
S(XS^\dagger)=\begin{bmatrix}1&0\\0&i\end{bmatrix}
\begin{bmatrix}0&-i\\1&0\end{bmatrix}
=\begin{bmatrix}0&-i\\i&0\end{bmatrix}=Y.
\]

**A15. ABC controlled rotation.**

\[
ABC=R_y(\theta/2)R_y(-\theta/2)I=R_y(0)=I.
\]

And

\[
\begin{aligned}
AXBXC&=R_y(\theta/2)X R_y(-\theta/2)XI\\
&=R_y(\theta/2)[X R_y(-\theta/2)X]\\
&=R_y(\theta/2)R_y(\theta/2)=R_y(\theta).
\end{aligned}
\]

So the control=0 branch sees I, and the control=1 branch sees `Ry(θ)`.

**A16. SWAP from three CNOTs.** Start `(1,0)`.

1. First control 1, so flip the second bit: `(1,0)→(1,1)`.
2. Second control 1, so flip the first bit: `(1,1)→(0,1)`.
3. First control 0, so leave second bit: `(0,1)→(0,1)`.

The result `(0,1)` equals the original values in reversed order. Algebraically the action is `(a,b)→(a,a⊕b)→(b,a⊕b)→(b,a)`.

**A17. Four Toffoli rows.**

- `110`: `ab=1·1=1`; target `0⊕1=1`, so `110→111`.
- `111`: `ab=1·1=1`; target `1⊕1=0`, so `111→110`.
- `101`: `ab=1·0=0`; target `1⊕0=1`, so `101→101`.
- `010`: `ab=0·1=0`; target `0⊕0=0`, so `010→010`.

**A18. H–CCZ–H.** With `|110⟩`, first H on the target gives

\[
\frac{|110\rangle+|111\rangle}{\sqrt2}.
\]

CCZ applies −1 only to `|111⟩`, resulting in

\[
\frac{|110\rangle-|111\rangle}{\sqrt2}=|11\rangle\otimes|-\rangle.
\]

The final H takes `|−⟩` to `|1⟩`, so output is `|111⟩`. If first control is 0, CCZ does nothing to either H-produced branch; the two H operations cancel, and the target remains unchanged.

**A19. Phase polynomial.** For `(1,1,1)`, LHS `4·1·1·1=4`. RHS `1+1+1−0−0−0+(1⊕1⊕1)=3+1=4`.

For `(1,1,0)`, LHS=0. RHS `1+1+0−(1⊕1)−(1⊕0)−(1⊕0)+(1⊕1⊕0)` = `2−0−1−1+0=0`. Thus the identity holds for the tested cases. Since `e^{iπabc}` is −1 only at 111, the seven phase terms can implement the CCZ sign with phase gates on computed parities.

**A20. Textbook Toffoli counts.**

Total operations `6+4+3+2=15`. T-count `4+3=7` because inverse T is also a non-Clifford T-type resource. CNOT count=6. Ancilla-free Toffoli acts on three wires: two controls and one target.

**A21. Adder cost.**

\[
N_{CX}=5\cdot6+5=35.
\]

\[
N_{T\text{-type}}=5\cdot7=35.
\]

The slide's `20 T+15 T†=35` agrees with the T-count. The compiler also reports six H in that particular compiled adder; that figure depends on how neighboring decomposition gates simplify.

**A22. Depth scheduling.** Layer 1 contains H(q0), T(q2). Layer 2 contains CX(q0,q1). Layer 3 contains T†(q0), X(q2). Total operations=5, depth=3. T-count=2 (one T plus one T†). T-depth=2 because one T-type gate appears in layer 1 and the other in layer 3. **Notice** this is different from the simple main-notes example, where both T-type gates were in a single layer and T-depth was 1.

**A23. Fidelity examples.**

(a) `X|0⟩=|1⟩`; overlap `⟨0|1⟩=0`, so `F=|0|²=0`.

(b) `Z|0⟩=|0⟩`; overlap `⟨0|0⟩=1`, so `F=|1|²=1`.

(c) Noisy state `−|0⟩`; overlap `⟨0|(−|0⟩)=−1`, so `F=|−1|²=1`. Global sign is not a physical difference.

**A24. Fidelity after an unwanted T.**

\[
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad T|+\rangle=\frac{|0\rangle+e^{i\pi/4}|1\rangle}{\sqrt2}.
\]

Multiply the bra and ket:

\[
\begin{aligned}
\langle+|T|+\rangle
&=\frac12(\langle0|+\langle1|)(|0\rangle+e^{i\pi/4}|1\rangle)\\
&=\frac12(1+e^{i\pi/4}),
\end{aligned}
\]

because the cross terms `⟨0|1⟩` and `⟨1|0⟩` are zero. Then

\[
\begin{aligned}
F&=\left|\frac{1+e^{i\pi/4}}2\right|^2
=\frac{(1+e^{i\pi/4})(1+e^{-i\pi/4})}{4}\\
&=\frac{2+2\cos(\pi/4)}4
=\frac{1+\cos(\pi/4)}2
=\frac{2+\sqrt2}{4}\\
&\approx\frac{2+1.4142}{4}\approx0.85355.
\end{aligned}
\]

This is a useful reminder: two states can both produce 50% Z-basis measurement outcomes while still differing by relative phase and having fidelity below 1.

**A25. Mean fidelity.**

\[
\overline F=(1+1+0+0.5)/4=2.5/4=0.625.
\]

A random experiment needs many repetitions because each trial samples a different set of faults. One outcome may be unusually good or bad; an average estimates the behavior of the chosen probabilistic noise model.

## B3. Applied reasoning solutions

**A26. Tolerance comparisons.** For `ε=0.1`: `0.058<0.1` and `0.0013<0.1`, so both candidates pass. For `ε=0.01`: `0.058>0.01` fails, while `0.0013<0.01` passes. For `ε=0.001`: `0.058` fails and `0.0013>0.001` also fails. Lower ε means stricter precision.

**A27. Routing.** A compiler may insert SWAP operations to move logical states until the hardware-connected qubits are adjacent. The usual three-CNOT SWAP increases the total number of two-qubit operations and can add depth and noise. The final number depends on the chip's connectivity and the compiler's mapping strategy.

**A28. Machine-dependent expense.** For a noisy physical chip, CNOTs are often relatively slow and error-prone; 100 CNOTs may be a worse burden than 10 native one-qubit T rotations. For an error-corrected architecture, Clifford operations can be relatively inexpensive while each T may consume magic-state factory resources, so 10 T operations may be costlier. No answer is universal without the target machine and cost objective.

**A29. Relative-phase Toffoli.** A relative-phase Toffoli agrees with CCX on the *bit values* produced by each basis input, but can attach signs to some components. If all those signs later cancel or are provably irrelevant, the cheaper circuit may be safe. If branches later interfere, the signs can change probabilities and make the algorithm incorrect. Only substitute it when the surrounding circuit's phase requirements permit.

**A30. Noise/fidelity capstone.** (1) Build a known ideal test circuit. (2) Simulate its ideal final statevector. (3) Make a fault-injected variant by randomly placing X or Z operations according to the supplied model and seed/probability. (4) Simulate its noisy final state. (5) Calculate `|⟨ideal|noisy⟩|²`. (6) Repeat trials and sweep the noise probability. (7) Summarize findings in the required short PDF. When editing the autograded notebook, preserve function names, parameters, setup cells and test harness; fill only explicitly permitted code regions, execute all cells, and save output inside the `.ipynb`. Follow the official LMS starter, not the illustrative pseudocode in the notes.

## B4. Multiple-choice solutions

| Question | Correct choice | Explanation |
|---|---|---|
| MCQ1 | **B** | The ZYZ theorem expresses any one-qubit unitary, with a global phase; CNOT alone is not universal. |
| MCQ2 | **B** | T† is an inverse-T gate but still counts as one T-type gate. |
| MCQ3 | **C** | Matrices act on columns right-to-left; `Rz(δ)` is first in time. |
| MCQ4 | **C** | A textbook Toffoli has an exact Clifford+T decomposition using 15 gates. |
| MCQ5 | **A** | T and T† often require magic-state resources in error-corrected quantum computers. |
| MCQ6 | **B** | The negative sign on the entire ket is a global phase of π, which does not affect physical measurement statistics. |

---

## Additional mini-experiments for learning

Open the offline HTML files in `../animations/`, and use these guided tasks:

1. In **Animation 02**, choose input `|0⟩`, `δ=90°`, `γ=60°`, `β=45°`. What is the final value of P(1)? How does changing only the last Z angle affect it?
2. In **Animation 04**, set control=0 and `θ=150°`. Does the target still return to `|0⟩`? Set control=1 and repeat. Explain the difference.
3. In **Animation 06**, switch between H/S and H/T with length 9. Why does one set still show only six directions?
4. In **Animation 07**, try all eight Toffoli basis inputs. Only which two inputs have different final basis strings?
5. In **Animation 09**, choose `p=0%`; all fidelity values should be 1, within floating point precision. Increase to `p=50%`, then change the seed. Why do individual trials vary?

**Answers:** (1) From `|0⟩`, the first Z turn does nothing to the Bloch direction; the Y tilt sets `P(1)=sin²(60°/2)=sin²30°=1/4`, and the last Z turn does not change it. (2) Yes for control=0, because half turns cancel; control=1 performs the full rotation. (3) Single-qubit Clifford words map the six Pauli-axis states among themselves, whereas T adds non-Clifford directions. (4) `110→111` and `111→110`. (5) With no faults, the trial is identical to ideal. With random faults, the number and positions of X/Z gates vary from trial to trial.
