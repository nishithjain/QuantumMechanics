# Why quantum computing?

[Home](README.md) · [Roadmap](00-learning-roadmap.md) · [Glossary](glossary.md)

**Next:** [Scalars and vectors](01-mathematical-foundations/01-scalars-and-vectors.md)

---

Classical computers have been astonishingly successful. The reason people still talk about quantum computers is not that laptops are “bad.” It is that some jobs grow so hard, so fast, that adding more ordinary chips stops being enough.

## What has been driving classical computing

For decades, engineers made transistors smaller and packed more of them onto a chip. A popular slogan for that trend is **Moore’s law**: the number of transistors on a dense integrated circuit roughly doubled about every two years.

Your notes recorded process size shrinking over time:

| Year | Typical process size |
|---|---|
| 1971 | 10 µm |
| 1974 | 6 µm |
| 1977 | 3 µm |
| 1981 | 1.5 µm |
| 1984 | 1 µm |
| 1987 | 800 nm |
| 1990 | 600 nm |
| 1993 | 350 nm |
| 1996 | 250 nm |
| 1999 | 180 nm |
| 2001 | 130 nm |
| 2003 | 90 nm |
| 2005 | 65 nm |
| 2007 | 45 nm |
| 2009 | 32 nm |
| 2012 | 22 nm |
| 2014 | 14 nm |
| 2016 | 10 nm |
| 2018 | 7 nm |
| 2020 | 5 nm |
| 2022 | 3 nm |

Smaller switches mean more of them, and often more speed. But shrinking cannot go on forever in a simple way:

- **Size.** Transistors are already a handful of atoms across. At that scale, electrons can leak through barriers (a quantum effect called tunneling). The chip stops behaving like a clean “on/off” switch.
- **Speed and heat.** Faster switching dumps more heat. You cannot cool an oven-sized hot plate inside a phone.
- **Cores.** You can add more processor cores, but many problems do not split neatly, and moving data between cores has its own cost.

So classical computing continues, but “just wait two years for a free doubling” is no longer a complete strategy.

## Why people study quantum computing

A quantum computer is not a faster laptop for email. It is a different kind of machine. It stores information in **qubits**, which follow the rules of quantum mechanics, and it is hoped to be useful on a *few* special families of problems.

Your 2022 notes said “quantum supremacy expected this year.” That phrase means: a well-chosen task that a real quantum device finishes faster than the best known classical method. Google publicly claimed a result of that kind in 2019; other groups have argued about how hard the classical comparison really was. Treat “supremacy” as an active scientific debate, not as “quantum computers have replaced ordinary ones.” Microsoft, Google, Intel, IBM and others still invest because the *possibility* of advantage is valuable even while hardware is noisy and small.

### Famous algorithms (the textbook reasons)

- **Shor’s algorithm (1994).** Factors large whole numbers efficiently, in theory. That threatens **RSA** encryption, which relies on factoring being hard for classical computers. Practical, large-scale factoring on today’s machines is not here yet. The idea still drives research in both quantum hardware and post-quantum cryptography.
- **Grover’s algorithm (1996).** Searches an unstructured list of \(n\) items in about \(\sqrt{n}\) steps instead of about \(n\). That is a quadratic speedup, not an exponential one, but it is still a genuine quantum trick.
- **Simulating quantum systems.** Molecules and materials *are* quantum. A quantum computer is a natural tool for approximating them. People hope this will help **drug design** and materials science, where classical simulation gets expensive fast.

### Broader application list from the notes

These are *research directions*, not a promise that a quantum chip in a factory already beats a supercomputer at each of them:

- drug discovery and computational biology
- some database-style search (Grover-like)
- cryptography (breaking some schemes; also designing new ones)
- simulation and modeling
- machine learning research
- scheduling, logistics, manufacturing, mobility, factory automation (often as *possible* optimization targets)

### The intellectual reason

Quantum mechanics is outside everyday intuition. Learning this subject is a way to see a piece of nature that your common sense never trained on. That is a fair reason on its own.

## Bit versus qubit, in one page

**Classical computing** stores a **bit**: strictly \(0\) or \(1\) during a calculation. Physically that might be a voltage (\(+5\,\mathrm{V}\) versus \(0\,\mathrm{V}\)) or a magnetic spot on a disk.

**Quantum computing** stores a **qubit**. Physically it might be an atom, a photon, a superconducting circuit, and so on. Mathematically it is a vector, written with **Dirac (ket) notation**, which the next notes teach from scratch.

The rest of this folder is that math, explained slowly.

---

**Next:** [Scalars and vectors](01-mathematical-foundations/01-scalars-and-vectors.md)
