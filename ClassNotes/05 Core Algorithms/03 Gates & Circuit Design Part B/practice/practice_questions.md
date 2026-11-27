# Practice Workbook — Entanglement as a Resource

**Companion to:** [Full beginner-friendly lecture notes](../Lecture_Notes.md)  
**How to study:** First try **Part A–D**, then scroll to **Part E: Detailed Answers**. All **eight problems from the professor's slide 29** appear in **Part A**. All new exercises are labeled *Extra*.

---

## Part A — The Professor's Eight Problems (Slides 29–31)

**P1 — CNOT and no-cloning.** What does `CNOT(|−⟩|0⟩)` produce? Is it equal to `|−⟩|−⟩`? Expand each expression into the four computational basis states.

**P2 — Copying a known basis.** Can a single unitary copy both `|+⟩` and `|−⟩`, given a blank `|0⟩`? Write a circuit, show the intermediate states for both inputs, and explain why no-cloning does not prohibit it.

**P3 — Teleportation Bell-basis expansion.** Prove that

\[
|\psi\rangle_0|\Phi^+\rangle_{12}=\frac12\left[
|\Phi^+\rangle_{01}|\psi\rangle_2
+|\Phi^-\rangle_{01}Z|\psi\rangle_2
+|\Psi^+\rangle_{01}X|\psi\rangle_2
+|\Psi^-\rangle_{01}XZ|\psi\rangle_2\right]
\]

by expanding all four terms and canceling matching terms. Assume `|ψ⟩=α|0⟩+β|1⟩`.

**P4 — A non-Bell input to the decoder.** Apply Alice's CNOT-then-H decoding to `|+⟩|+⟩`. What state do you get before measurement, and what are the possible measurement outcomes and probabilities?

**P5 — Different shared Bell pair.** Suppose teleportation starts with `|Ψ+⟩` on Alice's and Bob's shared qubits instead of `|Φ+⟩`. Alice performs the same CNOT-then-H and measurement. For each outcome `m₁m₂ ∈ {00,01,10,11}`, find Bob's conditional state and the correction he should perform.

**P6 — Superdense message 11.** Which Bell state does Alice create to encode message `11`? Show what happens when Bob applies CNOT-then-H, and explain how he reads the original message.

**P7 — Change CHSH strategy.** Alice uses the lecture's angles `A₀=0`, `A₁=π/4`, but Bob now **copies Alice's angles**: `B₀=0`, `B₁=π/4`. Calculate the average CHSH winning probability under uniform inputs.

**P8 — Prove the correlation formula.** For `|Φ+⟩` and real-plane projective measurements at angles `φA`, `φB`, derive

\[
P(\text{same answer})=\cos^2(\varphi_A-\varphi_B).
\]

Use the states `|v₀(φ)⟩=cosφ|0⟩+sinφ|1⟩` and `|v₁(φ)⟩=−sinφ|0⟩+cosφ|1⟩`.

---

## Part B — Extra Conceptual Questions

**C1.** Explain what a qubit is in everyday language. Why does a single Z-basis measurement not reveal its complete amplitudes?

**C2.** How do the four Bell states differ? Are `|Φ+⟩` and `|Φ−⟩` distinguishable by measuring only the first qubit in the Z basis?

**C3.** Why are CNOT and H sufficient to build **and** decode a Bell pair? In which order are they used for each direction?

**C4.** What is the difference between **copying** a classical basis bit and **copying** an arbitrary unknown quantum state?

**C5.** What is the difference between **global** and **relative** phase? Explain with `|ψ⟩` versus `−|ψ⟩`, and `|+⟩` versus `|−⟩`.

**C6.** In teleportation, what information do Alice's two measured classical bits carry? Do they reveal the unknown amplitudes?

**C7.** Why does the teleportation protocol not violate the no-cloning theorem and not allow faster-than-light messages?

**C8.** What is the difference between **classically controlled X** and **quantum-controlled X (CNOT)**?

**C9.** Why does teleport–then–undo provide a stronger test than measuring the teleported `|+⟩` directly?

**C10.** In superdense coding, why can't Bob recover the two classical bits *before* Alice sends her qubit?

**C11.** What does “the Bell pair is consumed” mean in teleportation or dense coding?

**C12.** Why does a quantum CHSH winning probability greater than 75% not allow Alice to send an instantaneous message to Bob?

---

## Part C — Extra Worked Numerical and Application Problems

**N1 — Normalize a qubit.** Is `|ψ⟩=(3|0⟩+4|1⟩)/5` normalized? Compute the two Z-basis probabilities. Now calculate `X|ψ⟩` and `Z|ψ⟩`.

**N2 — Complex amplitude.** Let `|ψ⟩=(|0⟩+i|1⟩)/√2`. Construct `⟨ψ|`, calculate `⟨ψ|ψ⟩`, and compute `Z|ψ⟩`. Why is the change not visible in an immediate Z measurement?

**N3 — Conditional teleportation.** Alice teleports `|ψ⟩=(3|0⟩+4|1⟩)/5` and measures `m₁m₂=11`. Write Bob's state before correction, after X, and after Z.

**N4 — Probability test.** For `|ψ⟩=(√3|0⟩+|1⟩)/2`, list Alice's four teleportation measurement probabilities. Does she learn whether `|β|²=1/4`?

**N5 — Known angle undo.** Prepare `R_y(π/3)|0⟩`. What are `α,β`? What are the initial Z probabilities? What state results after correct teleportation followed by `R_y(−π/3)`?

**N6 — No-cloning overlap.** Evaluate `⟨0|+⟩`. What would a cloner demand of this number? Calculate both sides numerically.

**N7 — Superdense message decoding.** Fill in the Bell state, top/bottom Bell-decoder output, and recovered message for all four messages in `00,01,10,11` order.

**N8 — CHSH probability, all inputs.** Use Alice's angles `0,π/4` and Bob's `π/8,−π/8`. Compute the angle gap and required same/different relation for each of the four inputs. Evaluate the ideal average win probability to four decimal places.

**N9 — CHSH sample size.** If the ideal success rate is `cos²(π/8)`, how many wins do you expect in 100, 1,000, and 4,000 rounds? Why should actual experiment counts fluctuate?

**N10 — A practical distributed-computing scenario.** Two quantum processors share an entangled Bell pair, and processor A holds an unknown qubit state needed on processor B. Explain each action in the teleportation protocol and why ordinary copying is not valid.

**N11 — Circuit debugging.** A student implements teleportation, but Bob uses X when `m₁=1` and Z when `m₂=1`. For which outcomes and input states could that produce an error? Give an explicit counterexample using `|ψ⟩=|0⟩` and Alice outcome `01`.

---

## Part D — Multiple-Choice Questions (Choose one unless stated)

**M1.** Which is the correct formula for the Bell state `|Φ+⟩`?

A. `( |00⟩ + |11⟩ )/√2`  
B. `( |01⟩ + |10⟩ )/√2`  
C. `( |0⟩ + |1⟩ )/2`  
D. `|00⟩`

**M2.** Bell decoding is:

A. H then CNOT.  
B. CNOT then H on the first qubit.  
C. X on both qubits.  
D. Measure, then CNOT.

**M3.** CNOT with input `|+⟩|0⟩` gives:

A. `|+⟩|+⟩`.  
B. `|00⟩`.  
C. `|Φ+⟩`.  
D. `|11⟩`.

**M4.** Which pair can **not** be copied perfectly by the same universal unitary tailored to the two states?

A. `|0⟩` and `|1⟩`.  
B. `|+⟩` and `|−⟩`.  
C. `|0⟩` and `|+⟩`.  
D. Two identical known states.

**M5.** If Alice's teleportation measurement is `m₁m₂=10`, Bob should apply:

A. X.  
B. Z.  
C. H.  
D. Nothing.

**M6.** Which resource equation correctly describes ideal teleportation?

A. One unknown qubit → two clones.  
B. One Bell pair + two classical bits → one qubit state transferred.  
C. One qubit transmitted → two independent qubits.  
D. Only classical communication, no entanglement → arbitrary unknown state transferred.

**M7.** To send message `01` using the dense-code convention in the notes, Alice applies:

A. X.  
B. H.  
C. Z.  
D. CNOT to Bob's qubit.

**M8.** The standard CHSH win condition is:

A. `a+b=x+y`.  
B. `a⊕b=x∧y`.  
C. `a∧b=x⊕y`.  
D. `a=b` for all questions.

**M9.** The best classical CHSH winning probability (uniform inputs, no communication) is:

A. 25%.  
B. 50%.  
C. 75%.  
D. 100%.

**M10.** The quantum CHSH strategy in this lecture achieves approximately:

A. 65.0%.  
B. 75.0%.  
C. 85.36%.  
D. 100%.

---

# Part E — Detailed Answers and Explanations

## Solutions to the professor's original problems

### P1 — CNOT acting on `|−⟩|0⟩`

First, the definition: `|−⟩=(|0⟩−|1⟩)/√2`. Combine with blank `|0⟩`:

\[
|−\rangle|0\rangle=\frac{|00\rangle-|10\rangle}{\sqrt2}.
\]

CNOT leaves `00` alone but changes `10→11`:

\[
\mathrm{CNOT}|−0\rangle=\frac{|00\rangle-|11\rangle}{\sqrt2}=|\Phi^-\rangle.
\]

A true duplicated product would be:

\[
\begin{aligned}
|−\rangle|−\rangle
&=\frac12(|0\rangle-|1\rangle)(|0\rangle-|1\rangle)\\
&=\frac12(|00\rangle-|01\rangle-|10\rangle+|11\rangle).
\end{aligned}
\]

The actual state has **only two terms** and is entangled; the desired state has **four terms** and is a product state. Therefore **not a copy**.

### P2 — Copying plus/minus states using a single unitary

Because `⟨+|−⟩=(1−1)/2=0`, these two states are orthogonal. Use **H on the input; CNOT into blank; H on both outputs**.

For plus:

\[
|+\rangle|0\rangle\xrightarrow{H\otimes I}|00\rangle
\xrightarrow{\mathrm{CNOT}}|00\rangle
\xrightarrow{H\otimes H}|++\rangle.
\]

For minus:

\[
|−\rangle|0\rangle\xrightarrow{H\otimes I}|10\rangle
\xrightarrow{\mathrm{CNOT}}|11\rangle
\xrightarrow{H\otimes H}|--\rangle.
\]

This is not a universal unknown-state cloner. It is a copier built for **one specified orthogonal basis**.

### P3 — Prove the Bell-basis teleportation identity

The four bracketed terms expand as follows (wire order `q₀q₁q₂`):

\[
\begin{aligned}
|\Phi^+\rangle|\psi\rangle
&=\frac1{\sqrt2}(\alpha|000\rangle+\beta|001\rangle+\alpha|110\rangle+\beta|111\rangle),\\
|\Phi^-\rangle Z|\psi\rangle
&=\frac1{\sqrt2}(\alpha|000\rangle-\beta|001\rangle-\alpha|110\rangle+\beta|111\rangle),\\
|\Psi^+\rangle X|\psi\rangle
&=\frac1{\sqrt2}(\beta|010\rangle+\alpha|011\rangle+\beta|100\rangle+\alpha|101\rangle),\\
|\Psi^-\rangle XZ|\psi\rangle
&=\frac1{\sqrt2}(-\beta|010\rangle+\alpha|011\rangle+\beta|100\rangle-\alpha|101\rangle).
\end{aligned}
\]

Add term by term. For example, coefficient of `|001⟩` is `β−β=0`; coefficient of `|110⟩` is `α−α=0`; similarly `|010⟩` and `|101⟩` disappear. Coefficients of `|000⟩`, `|011⟩`, `|100⟩`, `|111⟩` become `2α`, `2α`, `2β`, `2β`, respectively. Multiply the total by `1/2`:

\[
\frac{2\alpha|000\rangle+2\alpha|011\rangle+2\beta|100\rangle+2\beta|111\rangle}{2\sqrt2}
=\frac{\alpha|000\rangle+\alpha|011\rangle+\beta|100\rangle+\beta|111\rangle}{\sqrt2}.
\]

Factor the top/input qubit and the Bell half-pair back out:

\[
=(\alpha|0\rangle+\beta|1\rangle)\frac{|00\rangle+|11\rangle}{\sqrt2}
=|\psi\rangle|\Phi^+\rangle.
\]

Every term cancels or combines correctly, so the identity is proved.

### P4 — Decoder acting on `|+⟩|+⟩`

First expand the two product states:

\[
|++\rangle=\frac12(|00\rangle+|01\rangle+|10\rangle+|11\rangle).
\]

Apply CNOT (swap `10` and `11`; their coefficients are the same). Therefore **the superposition remains unchanged**:

\[
\mathrm{CNOT}|++\rangle=|++\rangle.
\]

Apply H **only to the first** qubit. Since `H|+⟩=|0⟩`:

\[
(H\otimes I)|++\rangle=|0\rangle|+\rangle
=\frac{|00\rangle+|01\rangle}{\sqrt2}.
\]

Measuring both wires gives `00` and `01`, each with probability `1/2`. It does **not** return one deterministic two-bit string because the input was **not one of the four Bell states**.

### P5 — Teleportation with `|Ψ+⟩` instead of `|Φ+⟩`

Observe:

\[
|\Psi^+\rangle_{12}=(I_1\otimes X_2)|\Phi^+\rangle_{12}.
\]

That means Bob's Bell half has an extra X compared with the standard resource. Because Alice's operations act only on qubits 0 and 1, the extra X remains on Bob's qubit. So take each standard Bob state and apply X **on the left**:

| Alice reads | Standard Bob state with `Φ+` | New Bob state with `Ψ+` | Bob correction |
|---|---|---|---|
| `00` | `|ψ⟩` | `X|ψ⟩` | X |
| `01` | `X|ψ⟩` | `X²|ψ⟩=|ψ⟩` | I |
| `10` | `Z|ψ⟩` | `XZ|ψ⟩` | X, then Z (`ZX`) |
| `11` | `XZ|ψ⟩` | `X²Z|ψ⟩=Z|ψ⟩` | Z |

For `10`, check `ZX(XZ|ψ⟩)=Z(X²)Z|ψ⟩=|ψ⟩`. Every correction restores `|ψ⟩`. Any overall minus sign arising from commuting X and Z is a physically irrelevant global phase. All four results remain equally likely.

### P6 — Superdense message 11

Message `11` means apply X to Alice's half, **then** Z to that half:

\[
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}
\xrightarrow{X\otimes I}\frac{|10\rangle+|01\rangle}{\sqrt2}
\xrightarrow{Z\otimes I}\frac{-|10\rangle+|01\rangle}{\sqrt2}=|\Psi^-\rangle.
\]

When Bob has both qubits:

\[
|\Psi^-\rangle\xrightarrow{\mathrm{CNOT}}
\frac{|01\rangle-|11\rangle}{\sqrt2}=|−\rangle|1\rangle
\xrightarrow{H\text{ on first}}|11\rangle.
\]

Measuring top and bottom gives **`11`**, which is message `11` regardless of the decoding-order convention in this particular symmetric case.

### P7 — Bob uses the same two angles as Alice

Now `A₀=0`, `A₁=π/4`, `B₀=0`, `B₁=π/4`:

| Input | Gap | Required | Win probability |
|---|---|---|---|
| `00` | 0 | Same | `cos²(0)=1` |
| `01` | `π/4` | Same | `cos²(π/4)=1/2` |
| `10` | `π/4` | Same | `cos²(π/4)=1/2` |
| `11` | 0 | **Different** | `sin²(0)=0` |

All questions are equiprobable. Average:

\[
P_{\rm win}=(1+1/2+1/2+0)/4=2/4=\boxed{50\%}.
\]

This illustrates that *having entanglement is not enough*: **choosing the right measurement angles matters**.

### P8 — Derive `P(same)=cos²(φA−φB)`

Let `|Φ+⟩=(|00⟩+|11⟩)/√2`. Write

\[
|v_0(\varphi)\rangle=\cos\varphi|0\rangle+\sin\varphi|1\rangle,
\quad |v_1(\varphi)\rangle=-\sin\varphi|0\rangle+\cos\varphi|1\rangle.
\]

The probability amplitude that **both answer 0** is

\[
\begin{aligned}
\langle v_0(\varphi_A)v_0(\varphi_B)|\Phi^+\rangle
&=\frac{\cos\varphi_A\cos\varphi_B+\sin\varphi_A\sin\varphi_B}{\sqrt2}\\
&=\frac{\cos(\varphi_A-\varphi_B)}{\sqrt2}.
\end{aligned}
\]

Square it:

\[
P(00)=\frac12\cos^2(\varphi_A-\varphi_B).
\]

For **both answer 1**, the amplitude is

\[
\frac{(-\sin\varphi_A)(-\sin\varphi_B)+\cos\varphi_A\cos\varphi_B}{\sqrt2}
=\frac{\cos(\varphi_A-\varphi_B)}{\sqrt2}.
\]

So `P(11) = ½cos²(φA−φB)`. “Same answer” means **00 OR 11**, so

\[
P(\text{same})=P(00)+P(11)
=\left(\tfrac12+\tfrac12\right)\cos^2(\varphi_A-\varphi_B)
=\boxed{\cos^2(\varphi_A-\varphi_B)}.
\]

The complementary event is “different answer,” whose probability is `sin²(φA−φB)`.

---

## Solutions to the extra conceptual questions

**C1.** A qubit is a quantum state described by two amplitudes relative to a chosen pair of basis states. One measurement yields just one outcome. With one copy, the amplitudes themselves are not readable as two stored classical numbers; repeated preparations and measurements in several bases are needed for state estimation.

**C2.** `Φ` combines `00/11`, `Ψ` combines `01/10`, while the `+` and `−` signs specify relative phase. Measuring only the first qubit in Z gives a 50–50 random bit for both `Φ+` and `Φ−`, so it does not distinguish them.

**C3.** H makes `(|0⟩+|1⟩)/√2` from `|0⟩`; CNOT entangles it with a target blank to make `Φ+`. To undo, reverse the order: CNOT, then H on the first wire. This works because `H²=I` and `CNOT²=I`.

**C4.** Classical 0/1 basis copying works because the possible input states are orthogonal and a copier can be designed for that basis. For a universal unknown quantum state, copying all possible amplitudes would contradict preservation of inner products.

**C5.** Multiplying an entire state by `−1` is global phase and changes no physical probabilities. Changing only one term's sign is relative phase, as between `|+⟩` and `|−⟩`; subsequent H operations can reveal the difference.

**C6.** Alice's two bits identify which of four corrections Bob needs. Each result occurs with probability `1/4` independently of `α` and `β`; they do not tell Alice the amplitudes.

**C7.** Teleportation consumes Alice's input when she measures; Bob receives the reconstructed state after correction, not a duplicate alongside Alice's original. Without Alice's bits, Bob's local statistics are indistinguishable from a random qubit (`I/2`), so it cannot signal instantaneously.

**C8.** A classically controlled X requires a stored measured bit and runs X on Bob only when that ordinary bit is 1. A quantum-controlled X is a CNOT whose control is **still a qubit**, capable of acting coherently on superpositions and creating entanglement.

**C9.** A correct teleported plus state produces 50–50 Z outcomes, but so might an incorrect state or mixture. If we prepared a known `R_y(θ)|0⟩`, then teleportation followed by the inverse gate must produce the **definite** outcome `0`, making mistakes easier to spot.

**C10.** Bob only has one half of an entangled Bell pair before Alice's transmission. His local state is a 50–50 mixture that does not depend on her X/Z encoding. Only a *joint measurement on both halves* can distinguish the four Bell states.

**C11.** “Consumed” means the original usable shared entanglement is no longer left available in that same pair. In teleportation, Alice's part is measured; in dense coding, both halves end up with Bob and are decoded/measured. To run again as described, a new shared pair is required.

**C12.** The CHSH advantage appears in **correlations** when the referee later compares the two records. Each person's standalone measurement result is locally random, regardless of the other person's question or choice, so no controllable signal has been sent.

---

## Solutions to extra numerical and application problems

**N1.** `|α|²=9/25`, `|β|²=16/25`, sum `25/25=1` so normalized. `P(0)=9/25=0.36`, `P(1)=16/25=0.64`. Applying X swaps the amplitudes: `(4|0⟩+3|1⟩)/5`. Applying Z flips the sign of the `|1⟩` term: `(3|0⟩−4|1⟩)/5`.

**N2.** The ket is `[1/√2,i/√2]ᵀ`; conjugate transpose gives `⟨ψ|=[1/√2,−i/√2]`. Inner product `=1/2+(-i)(i)/2=1/2+1/2=1`. Z gives `( |0⟩−i|1⟩ )/√2`. Z-basis probabilities remain `1/2` and `1/2` because `|−i|²=|i|²=1`.

**N3.** For outcome `11`, Bob has `−β|0⟩+α|1⟩ = (−4|0⟩+3|1⟩)/5`. Apply X: `(3|0⟩−4|1⟩)/5`. Apply Z: `(3|0⟩+4|1⟩)/5`. This is the original state.

**N4.** `α=√3/2`, `β=1/2`, so `|α|²=3/4`, `|β|²=1/4`. Alice's **two-bit** probabilities are each `1/4`, independent of input amplitudes. Her result does **not** reveal the `1/4` probability for the input's `|1⟩` component.

**N5.** `α=cos(π/6)=√3/2`, `β=sin(π/6)=1/2`. Initial Z probabilities are `3/4`, `1/4`. Correct teleportation leaves Bob with the same state. Applying `R_y(−π/3)` cancels `R_y(π/3)` and yields `|0⟩` with certainty.

**N6.** `⟨0|+⟩=(⟨0|0⟩+⟨0|1⟩)/√2=(1+0)/√2=0.707106...`. A cloner would require `z=z²`, but the square is `0.5`; they are unequal. So a single perfect copier cannot handle both `|0⟩` and `|+⟩`.

**N7.**

| Message `m₁m₀` | Encode with | Bell state | Decoder outputs (top,bottom) | Recover message as (bottom,top) |
|---|---|---|---|---|
| `00` | I | `Φ+` | `00` | `00` |
| `01` | Z | `Φ−` | `10` | `01` |
| `10` | X | `Ψ+` | `01` | `10` |
| `11` | X then Z | `Ψ−` | `11` | `11` |

The two-bit **wire** ordering and the two-bit **message** ordering are not the same in this circuit; the decoding implementation should map them consistently.

**N8.** For `00`, gap `π/8` and same answers needed: `cos²π/8`. For `01`, gap `π/8` and same: same probability. For `10`, gap `π/8` and same: same probability. For `11`, gap `3π/8` and different: `sin²(3π/8)=cos²π/8`. Average `cos²π/8≈0.8536`, i.e. **85.36%**.

**N9.** Multiply `0.853553...` by the number of rounds. For 100: approximately **85** wins; for 1,000: approximately **854** wins; for 4,000: approximately **3,414** wins. Individual measurement results are random, so counts fluctuate around these *expected values*; they are not fixed guarantees.

**N10.** Processor A and B first share one `Φ+` pair, one half on each processor. A applies CNOT between its unknown input and its Bell half, then H to the input, measures both, and sends the two classical results over an ordinary network. B uses those bits to apply X and/or Z to its Bell half. The state of that B qubit now equals the unknown original state, which A no longer holds. Universal copy-and-send would violate no-cloning.

**N11.** For Alice's outcome `01`, Bob's state before correction is `X|ψ⟩`. If `|ψ⟩=|0⟩`, Bob has `|1⟩`. The **correct** action is X (based on `m₂=1`), yielding `|0⟩`. The **incorrect** rule instead applies Z (because it treats `m₂` as the Z trigger), producing `Z|1⟩=−|1⟩`, still physically `|1⟩`. It failed. A swapped-bit implementation can happen to work for special input states/outcomes, but not for arbitrary unknown states.

---

## Multiple-choice answer key (with reasons)

| Question | Answer | Explanation |
|---|---|---|
| M1 | **A** | `Φ+` superposes `00` and `11` with plus sign and proper `1/√2` normalization |
| M2 | **B** | Undo H then CNOT in reverse order: CNOT, then H on first |
| M3 | **C** | CNOT transforms `(00+10)/√2` to `(00+11)/√2=Φ+` |
| M4 | **C** | `|0⟩` and `|+⟩` are distinct nonorthogonal states; overlap `1/√2` |
| M5 | **B** | For `m₁m₂=10`, the phase flip Z must be undone by Z |
| M6 | **B** | Teleportation spends one Bell pair and two classical bits to move one state |
| M7 | **C** | The **second/right** message bit `m₀=1` triggers Z |
| M8 | **B** | Alice/Bob need same answers except when both inputs are 1 |
| M9 | **C** | At least one of four equations fails for any classical deterministic plan |
| M10 | **C** | `cos²(π/8)=0.853553... ≈85.36%` |

---

**Practice method:** After finishing each section, go back to the relevant [offline animation](../Lecture_Notes.md#9-interactive-learning--offline-animations) and choose an input you have **not** tried. Predict the result on paper first; then use Play/Step to check it. When you can reproduce the calculation **without** the diagram, you know the idea rather than just recognizing it.
