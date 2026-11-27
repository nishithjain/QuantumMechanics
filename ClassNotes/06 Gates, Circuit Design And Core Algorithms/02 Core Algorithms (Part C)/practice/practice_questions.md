# Core Algorithms (Part C) — Practice Questions and Fully Worked Answers

> Source basis: the professor's lecture transcription. These exercises are **supplementary practice created to teach the lecture**, not a claim that the lecturer assigned this exact worksheet. All dot products of bit strings use **modulo 2**, and all measurements are in the computational basis unless stated otherwise.

## Part A — Conceptual Questions

**Q1.** Explain the difference between a classical bit, a quantum amplitude, and a measurement probability. Why can an amplitude be negative but a probability cannot?

**Q2.** A professor says “\(a=1010\) selects bits of \(x\).” What does that mean? Which bits are selected and how do you compute \(a\cdot x\)?

**Q3.** What special promise distinguishes Deutsch–Jozsa from an arbitrary function-identification problem? How does the final all-zero measurement separate the two cases?

**Q4.** Explain the promise in Simon's problem in ordinary language. Why is the secret assumed nonzero?

**Q5.** Why does Simon need two \(n\)-qubit registers and a reversible oracle \(U_f\), rather than simply replacing \(|x\rangle\) by \(|f(x)\rangle\)?

**Q6.** Why do we measure Simon's output register before the final Hadamards? What changes if instead we directly measure the input register in the paired superposition?

**Q7.** In Simon's algorithm, what exactly is the meaning of “amplitudes interfere”? Why is the secret not printed directly in one measurement?

**Q8.** What does it mean that two equations \(s\cdot z=0\) are *linearly dependent*? Why can dependent results occur even if each quantum run is valid?

**Q9.** Carefully distinguish: “describing the same state in the \(+/-\) basis” versus “applying a Hadamard gate and measuring in the computational basis.”

**Q10.** What is a character, and why does the identity \(\chi(x\oplus y)=\chi(x)\chi(y)\) matter for finding hidden symmetries?

**Q11.** Why is the Hadamard transform suitable for XOR-based symmetry, but a cyclic-number Fourier transform needed for integer-period symmetry?

**Q12.** The professor says the all-plus Fourier coefficient gives the “average” of amplitudes. What normalization qualification should be added?

## Part B — Numerical and Derivation Questions

**Q13.** Compute \(1011\oplus0110\), \(1011\cdot0110\), and \(1101\cdot1011\). Show every bit product and parity.

**Q14.** Expand \(H^{\otimes2}|11\rangle\) from the tensor products. Give every amplitude and measurement probability.

**Q15.** Let \(n=2\) and \(f(00)=0,f(01)=1,f(10)=0,f(11)=1\). Is \(f\) balanced? Compute the final Deutsch–Jozsa all-zero amplitude from the sum of signs.

**Q16.** In Bernstein–Vazirani, take \(s=110\). List \(f(000),f(001),f(010),f(011),f(100),f(101),f(110),f(111)\) and explain the effect of the final Hadamards.

**Q17.** For Simon secret \(s=101\) on three-bit strings, list all four partner pairs and all values of \(z\) satisfying \(s\cdot z=0\).

**Q18.** Let Simon's secret be \(s=110\) and the output measurement leave \((|001\rangle+|111\rangle)/\sqrt2\). Compute the final amplitudes of \(|000\rangle\), \(|001\rangle\), \(|101\rangle\) and \(|111\rangle\) after the input Hadamards; give probabilities.

**Q19.** For nonzero \(s\in\{0,1\}^5\), prove that exactly 16 strings \(z\) obey \(s\cdot z=0\), without listing all 32.

**Q20.** A Simon run with \(n=4\) returns `1000`, `0100`, `1100`, `0010`, `1000`. Which results are redundant? Find every candidate \(s\) and use the Simon nonzero promise.

**Q21.** Let \(|g\rangle=3|0\rangle/5+4|1\rangle/5\). Derive both \(+/-\)-basis amplitudes and their probabilities. Verify they add to 1.

**Q22.** Let \(|g\rangle=|01\rangle\). Compute the complete two-qubit Fourier/Hadamard coordinates \(\widehat g(00),\widehat g(01),\widehat g(10),\widehat g(11)\). Explain the signs.

**Q23.** Evaluate \(\chi_{101}(011)\), \(\chi_{101}(110)\), and \(\chi_{101}(011\oplus110)\). Verify the character identity numerically.

**Q24.** In \(\mathbb Z_8\), compute \((6+5)\bmod8\), \((5+5)\bmod8\), and \((3\times6)\bmod8\). Contrast \(3+1\bmod8\) with `011 XOR 001`.

**Q25.** In \(\mathbb Z_4\), write all four roots of unity, compute \(\chi_1(3)\), \(\chi_2(3)\), and sum \(\sum_{x=0}^{3}\omega_4^x\).

**Q26.** For \(N=6\), explain why \((-1)^x\) is a valid character. For \(N=5\), show explicitly why the same rule fails when you wrap around.

**Q27.** Starting from \(S=1+q+\cdots+q^{N-1}\), derive \(S=0\) when \(q^N=1\) and \(q\ne1\). Explain why the condition \(q\ne1\) is required.

**Q28.** *(Preview extension)* Expand \(\mathrm{QFT}_4|1\rangle\) and compare its phase pattern with \(H^{\otimes2}|01\rangle\). Why are they different despite having four basis labels?

## Part C — Application Problems

**Q29.** You have two algorithms for a promised Simon oracle: (A) query random classical inputs until a collision occurs; (B) apply Hadamards and sample several equations, then use Gaussian elimination. Identify the role of the quantum processor and classical computer in method B. What work does the query-complexity comparison omit?

**Q30.** A friend argues: “If the Hadamard transform simultaneously computes all Fourier coefficients, we can measure them all and solve every problem in one run.” Identify the error in this argument and explain how the promise changes what a measurement can tell you.

**Q31.** A programmer tests \(f(000)=f(101)\) and thinks the secret is \(s=111\) because both strings contain three bits. Explain why this is wrong and compute the right mask.

**Q32.** A system is described as \(\mathbb Z_8\). An engineer implements its shift by XORing each three-bit register with `001`. Give an input for which their implementation differs from adding one modulo 8, and explain the consequences for Fourier characters.

## Part D — Multiple Choice

**Q33.** Given nonzero \(s\) of length \(n\), how many strings \(z\) satisfy \(s\cdot z=0\)? (A) 1 (B) \(2^{n-1}\) (C) \(2^n-1\) (D) \(n\).

**Q34.** Which step makes Simon's unwanted results disappear? (A) The oracle output measurement alone (B) Applying the input Hadamards after the output-register measurement (C) Sending a classical bit (D) Copying the unknown state.

**Q35.** The Fourier coordinate \(\widehat g(0^n)\) is (A) \(\sum_xg_x\) (B) \(2^{-n/2}\sum_xg_x\) (C) \(\prod_xg_x\) (D) always 1.

**Q36.** Which formula correctly defines a cyclic character on \(\mathbb Z_N\)? (A) \(x\mapsto x+N\) (B) \(x\mapsto e^{2\pi i r x/N}\) (C) \(x\mapsto x^2\) (D) \(x\mapsto 1/x\).

**Q37.** If \(\omega_8=e^{2\pi i/8}\), then \(\sum_{x=0}^7\omega_8^{0x}\) equals (A) 0 (B) 1 (C) 8 (D) \(-8\).

**Q38.** Which statement is most precise? (A) QFT and Hadamard are identical for all addition rules (B) Fourier coefficients are directly measurable all at once (C) Hadamards implement the Fourier transform on the XOR group of bit strings (D) Simon's oracle is injective.

---

# Answer Key — With Explanations

## Part A Solutions

**A1.** A bit is one definite classical 0/1 value. A quantum state has complex amplitudes, which may carry phase, including signs. On computational-basis measurement, \(P(x)=|\alpha_x|^2\) is nonnegative, because a squared magnitude cannot be negative. A negative amplitude can cancel a positive amplitude under interference before measurement, but it is never a negative probability.

**A2.** The mask `1010` selects positions 1 and 3 (from the left) and ignores positions 2 and 4. For \(x=x_1x_2x_3x_4\), \(1010\cdot x=(x_1+x_3)\bmod2\). This is the parity of the selected bits, not an integer dot product involving decimal 1010.

**A3.** The oracle is guaranteed to be *constant* or *balanced*—exactly half zeros and half ones. After phase kickback and a final Hadamard layer, the all-zero amplitude is the average sign \((1/2^n)\sum_x(-1)^{f(x)}\). Constant gives \(\pm1\) (measurement all zeros with probability 1); balanced gives 0 (measurement all zeros with probability 0). The promise is what makes a single query decisive.

**A4.** Every input has one distinct partner. Partners give the same output and differ by XOR with the same secret mask. If \(s\) were all zeros, the partner would be the input itself: \(x\oplus0=x\), contradicting the promise that the oracle is 2-to-1 on distinct inputs.

**A5.** Simon's output \(f(x)\) has \(n\) bits, so the oracle requires an output register able to store them. Since \(f\) maps distinct \(x\) values to the same output, \(|x\rangle\mapsto|f(x)\rangle\) is not reversible on its own. The two-register unitary retains \(x\) and adds \(f(x)\) into the other register using XOR: \(|x,y\rangle\mapsto|x,y\oplus f(x)\rangle\).

**A6.** Measuring the output chooses a function-value class and leaves the input in a superposition of the two matching inputs. If we measure that input immediately, we obtain just one random member of the pair, which alone does not reveal the partner or \(s\). Applying input Hadamards *before* that measurement reveals interference about \(s\).

**A7.** The amplitudes associated with two matching inputs contribute to each possible Fourier output \(z\). Depending on \(s\cdot z\), the two signs are equal (reinforce) or opposite (cancel). Only the latter relation excludes an outcome; surviving outcomes encode one homogeneous equation, not all bits of \(s\) by themselves.

**A8.** A row \(z\) is dependent if it can be formed by XORing earlier rows. Its equation is then already implied by earlier equations. Each quantum run independently samples from a distribution; nothing guarantees that the resulting rows will be linearly independent.

**A9.** A basis change is a different mathematical coordinate description of an *unchanged* vector. Applying a Hadamard physically changes the vector when we keep describing states in the computational basis. Because \(H\) interchanges computational and \(+/-\) bases, the numerical coefficient arrays can coincide, but the interpretations are different.

**A10.** A character respects addition: \(\chi(x+y)=\chi(x)\chi(y)\), with the appropriate group addition. In the XOR case, \(\chi_\gamma(x)=(-1)^{\gamma\cdot x}\). This converts the unknown XOR shift into a simple multiplicative sign, permitting factorization and exact cancellation in Fourier amplitudes.

**A11.** In the bit-string group, adding 1 twice returns 0 independently in every bit, so parity signs \(\pm1\) work as the natural waves. In \(\mathbb Z_N\), integer addition is cyclic over all \(N\) values, and the full set of character waves requires \(N\)-th roots of unity \(e^{2\pi i r x/N}\). The two groups generally have different addition rules even when they have equally many labels.

**A12.** For a general state \(|g\rangle=\sum_xg_x|x\rangle\), \(\widehat g(0^n)=(1/\sqrt{2^n})\sum_xg_x\), a **normalized sum**, not literally the arithmetic mean \((1/2^n)\sum_xg_x\). If \(g_x=(-1)^{f(x)}/\sqrt{2^n}\), those two normalization factors combine and the coefficient is exactly the *average sign* used in Deutsch–Jozsa.

## Part B Solutions

**A13.** XOR first: `1011 XOR 0110 = 1101` (positions: 1, 1, 0, 1). For \(1011\cdot0110\), multiply positions: \(1\cdot0+0\cdot1+1\cdot1+1\cdot0=0+0+1+0=1\) (mod 2). For \(1101\cdot1011\), products are \(1\cdot1+1\cdot0+0\cdot1+1\cdot1=1+0+0+1=2\equiv0\pmod2\).

**A14.** \(H^{\otimes2}|11\rangle=H|1\rangle\otimes H|1\rangle=\big((|0\rangle-|1\rangle)/\sqrt2\big)\otimes\big((|0\rangle-|1\rangle)/\sqrt2\big)\). Distribute: \((|00\rangle-|01\rangle-|10\rangle+|11\rangle)/2\). Amplitudes in `00,01,10,11` order: \(+1/2,-1/2,-1/2,+1/2\). Each measurement probability is \(1/4\). Total probability \(4\cdot1/4=1\).

**A15.** The function output list is \(0,1,0,1\), so exactly half of the four values are 1: it is balanced. The signs are \(+1,-1,+1,-1\). The all-zero Fourier amplitude is \(A(00)=(1-1+1-1)/4=0\). Therefore the final Deutsch–Jozsa measurement cannot return `00`.

**A16.** With \(s=110\), \(f(x)=x_1\oplus x_2\). In order `000,001,010,011,100,101,110,111`, outputs are `0,0,1,1,1,1,0,0`. These signs form the Fourier state \(H^{\otimes3}|110\rangle\). The final Hadamards apply the inverse transform (the same operation here) and yield \(|110\rangle\) with certainty.

**A17.** XOR pairing for \(s=101\): `000 ↔ 101`, `001 ↔ 100`, `010 ↔ 111`, `011 ↔ 110`. Valid \(z\) satisfy \(z_1\oplus z_3=0\), so bits 1 and 3 agree. They are `000,010,101,111`, each with probability \(1/4\) in an ideal Simon run.

**A18.** The post-measurement state is \((|001\rangle+|111\rangle)/\sqrt2\). For \(n=3\), Equation (10) gives amplitude \((1/4)(-1)^{001\cdot z}[1+(-1)^{110\cdot z}]\). At `000`, both parities are 0: amplitude \(+2/4=+1/2\), probability \(1/4\). At `001`, \(001\cdot001=1\) but \(110\cdot001=0\): amplitude \(-2/4=-1/2\), probability \(1/4\). At `101`, \(110\cdot101=1\): bracket is 0, amplitude and probability 0. At `111`, \(001\cdot111=1\) and \(110\cdot111=(1+1)\bmod2=0\): amplitude \(-1/2\), probability \(1/4\). The remaining valid `110` has amplitude \(+1/2\), giving total probability 1.

**A19.** Since \(s\neq0\), pick a position \(j\) where \(s_j=1\). Choose the other four positions of \(z\) freely: \(2^4=16\) choices. The equation \(\bigoplus_i s_iz_i=0\) uniquely fixes \(z_j\) to match the parity of the selected other bits. Thus exactly \(16=2^{5-1}\) strings satisfy the constraint.

**A20.** `1000` implies \(s_1=0\); `0100` implies \(s_2=0\); `1100` is the XOR of those two rows and adds no information; `0010` adds \(s_3=0\); the final `1000` repeats the first row. Thus the general solution is \(s=(0,0,0,s_4)\), with \(s_4\in\{0,1\}\). Simon's nonzero promise selects \(s=0001\). Rank is 3, which equals \(n-1\).

**A21.** The coefficients in the \(+/-\) basis are \(\alpha'=(3/5+4/5)/\sqrt2=7/(5\sqrt2)\), \(\beta'=(3/5-4/5)/\sqrt2=-1/(5\sqrt2)\). Probabilities: \(49/50\) and \(1/50\), totaling 1. A negative \(\beta'\) is a phase sign, not negative probability.

**A22.** The state has \(g_{01}=1\) and all other \(g_x=0\). Each Fourier coefficient is \(\widehat g(\gamma)=\frac12(-1)^{\gamma\cdot01}=\frac12(-1)^{\gamma_2}\). Thus in \(\gamma=00,01,10,11\) order the coefficients are \(+1/2,-1/2,+1/2,-1/2\). Their squared magnitudes sum to \(4\cdot1/4=1\).

**A23.** With \(\gamma=101\), \(\chi_\gamma(011)=(-1)^{0\oplus1}=-1\). For `110`, the selected first and third bits are 1 and 0, giving \(-1\). Their XOR is `101`, whose selected bits are 1 and 1, giving \((-1)^0=+1\). Product of the first two character values is \((-1)(-1)=+1\), matching the value on the XOR.

**A24.** \(6+5=11\equiv3\pmod8\), \(5+5=10\equiv2\pmod8\), \(3\cdot6=18\equiv2\pmod8\). For 3 plus 1 in \(\mathbb Z_8\), the answer is 4; in XOR arithmetic `011 XOR 001 = 010` (binary 2). The two addition operations are different.

**A25.** \(\omega_4=e^{i\pi/2}=i\). The roots are \(1,i,-1,-i\). \(\chi_1(3)=\omega_4^3=-i\). \(\chi_2(3)=\omega_4^6=i^6=-1\). The sum \(1+i-1-i=0\) because the four equal-length vectors cancel around the unit circle.

**A26.** For \(N=6\), \(\chi(x)=(-1)^x\) respects addition modulo 6 because wraparound subtracts an **even** multiple of 6, leaving parity unchanged: \((-1)^{x+y-6}=(-1)^{x+y}\). For \(N=5\), let \(x=4,y=1\): \((4+1)\bmod5=0\), so \(\chi(0)=+1\); but \(\chi(4)\chi(1)=(+1)(-1)=-1\). It fails.

**A27.** Write \(S=1+q+q^2+\cdots+q^{N-1}\) and \(qS=q+q^2+\cdots+q^N\). Subtract: \((1-q)S=1-q^N\). Given \(q^N=1\), the right side is 0. Since \(q\neq1\), divide by \(1-q\) to get \(S=0\). If \(q=1\), dividing by \(1-q=0\) would be invalid; the original sum is then \(N\).

**A28.** With \(N=4\), \(\omega_4=i\): \(\mathrm{QFT}_4|1\rangle=\frac12(|0\rangle+i|1\rangle+i^2|2\rangle+i^3|3\rangle)=\frac12(|0\rangle+i|1\rangle-|2\rangle-i|3\rangle)\). By contrast \(H^{\otimes2}|01\rangle=\frac12(|00\rangle-|01\rangle+|10\rangle-|11\rangle)\). Both are superpositions of four equal-probability labels, but their phases differ because QFT uses addition modulo 4 while the Hadamard transform uses position-wise XOR.

## Part C Solutions

**A29.** Method A makes classical oracle queries until it observes a matching output pair; that can take order \(2^{n/2}\) queries. Method B uses a quantum device to query the reversible oracle on superposition and to produce independent (or sometimes redundant) linear constraints \(s\cdot z=0\). An ordinary computer then performs Gaussian elimination over \(\mathrm{GF}(2)\) and selects the nonzero null-space solution. A query-complexity statement does not include the full cost of constructing the oracle, error correction, circuit depth, hardware connectivity, startup, or classical processing.

**A30.** A Fourier transform produces a state whose amplitudes are the Fourier coefficients, but an ordinary measurement produces only *one basis outcome*. It does not expose the full amplitude vector. The quantum algorithms work because the oracle promises a highly structured pattern: an all-zero outcome is certain/impossible, one BV label is certain, or Simon measurements sample a constrained subspace. Outside such structure, the mere availability of a transform is not enough to read an exponential number of coefficients.

**A31.** The length of a string says how many bit positions it has, not which positions differ. Compute the XOR position by position: `000 XOR 101 = 101`. Therefore the inferred Simon mask is `101`. Only bit positions 1 and 3 differ.

**A32.** For example, start with decimal 1 (binary `001`). Adding one modulo 8 gives decimal 2 (binary `010`), whereas XORing with `001` gives `000` (decimal 0). The engineer implemented a flip of the least-significant bit, not a cyclic increment. Consequently the resulting shift symmetry and the correct Fourier character patterns are those of a different group; a cyclic QFT-based inference could be wrong.

## Part D Solutions

**A33. B.** A nonzero \(s\) fixes one chosen bit of \(z\), leaving \(n-1\) free bits, hence \(2^{n-1}\) solutions.

**A34. B.** The input Hadamards combine phases from paired inputs. For \(s\cdot z=1\) they cancel to zero. The earlier output-register measurement selects a pair; it does not itself impose the final Fourier support condition.

**A35. B.** The normalized formula is \(\widehat g(0^n)=2^{-n/2}\sum_xg_x\); the weight sign is positive for every term.

**A36. B.** The character \(\chi_r(x)=e^{2\pi i r x/N}\) respects addition modulo \(N\) by the exponent law and \(e^{2\pi i r}=1\).

**A37. C.** Since \(\omega_8^{0x}=1\) for all eight values \(x\), the sum contains eight ones and equals 8.

**A38. C.** The tensor-product Hadamard transform is the Fourier transform for the bit-string XOR group. The general cyclic QFT differs, amplitudes are not all measurable at once, and Simon's oracle is deliberately 2-to-1.

---

**How to use this workbook:** Attempt the questions without looking at the solutions, then check **where each sign and normalization factor came from**, not only the final number. For visual follow-up, open the offline animations linked in the main `Lecture_Notes.md`.
