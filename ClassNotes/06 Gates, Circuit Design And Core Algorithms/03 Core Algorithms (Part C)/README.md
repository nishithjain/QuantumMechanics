# Quantum Computing — Core Algorithms (Part C): Offline Learning Pack

This complete learning pack was created from the supplied **03 Core Algorithms (Part C)** lecture transcription. **No PDF slides were included in this turn**, so the educational illustrations are original reconstructions of the mathematics described verbally. The transcript, not a guessed slide deck, determines the lecture sequence.

## Start here

1. Open `Lecture_Notes.md` in a Markdown previewer with LaTeX/math support (for example, VS Code Markdown Preview Enhanced or a Markdown viewer that supports `$...$` and `$$...$$`). If your viewer displays formulas literally, use a Markdown application that renders LaTeX. The original Markdown files remain plain text and work offline.
2. Read **Sections 1–2** for prerequisites if this is your first exposure to complex numbers, bras/kets or tensor products.
3. Read **Section 3** in order. This follows the professor's actual progression: roots of unity → character functions → Fourier basis → Fourier matrices → periodic interference → phase gates → QFT factorization.
4. Open the indicated `animations/animation_XX.html` files when you arrive at a link. These are standalone web pages that you can open by double-clicking or using **Open With → browser**. Each has on-screen controls and explanatory calculations. **No local server, external library, login or internet connection is required.**
5. After each major topic, answer the short “Check Your Understanding” questions, then complete `practice/practice_questions.md`. Worked solutions are in **Section B** of the workbook; attempt the questions in Section A before scrolling down.

## Folder map

```text
Lecture_Notes/
├── README.md                      ← You are here
├── Lecture_Notes.md               ← Full Markdown study notes
├── animations/
│   ├── animation_01.html          ← Roots of unity
│   ├── animation_02.html          ← Character phase patterns
│   ├── animation_03.html          ← Fourier basis states
│   ├── animation_04.html          ← Fourier coordinates and F vs F†
│   ├── animation_05.html          ← F4 matrix entries
│   ├── animation_06.html          ← Two-spike interference
│   ├── animation_07.html          ← Periodic comb and shift
│   ├── animation_08.html          ← Controlled phase rotations
│   ├── animation_09.html          ← QFT tensor factorization
│   └── animation_10.html          ← QFT gate cost (preview)
├── images/
│   ├── diagram_01_learning_map.svg
│   ├── diagram_02_modular_clock.svg
│   ├── diagram_03_roots_of_unity.svg
│   ├── diagram_04_fourier_basis.svg
│   ├── diagram_05_change_of_basis.svg
│   ├── diagram_06_fourier_matrix.svg
│   ├── diagram_07_single_spike.svg
│   ├── diagram_08_two_spikes.svg
│   ├── diagram_09_periodic_comb.svg
│   ├── diagram_10_controlled_phase.svg
│   └── diagram_11_tensor_factorization.svg
└── practice/
    └── practice_questions.md      ← 44 exercises and worked solutions
```

## Animation controls

- **Play:** proceed through the teaching stages automatically.
- **Pause:** stop advancement at the currently displayed stage.
- **Step:** advance one teaching stage (wraps at the end).
- **Reset:** return to stage 1 and pause.
- **Lesson inputs:** adjust labels, number of roots, gate phase, spike spacing, offset or other options as the lesson permits. Calculations and visualization update locally in your browser.
- On narrow screens, explanatory panels stack vertically. For the best reading experience, maximize the browser window.

## Conventions that must stay consistent

- **$N$** is the number of basis labels (usually a power of 2); **$k=\log_2N$** is the number of qubits.
- **$\omega_N=e^{2\pi i/N}$** is the positive (counterclockwise) primitive root.
- **$F_N$ uses the positive exponent:** $F_N|x\rangle=N^{-1/2}\sum_y\omega_N^{xy}|y\rangle$.
- **Fourier-basis coordinate coefficients use the negative exponent:** $\widehat\alpha=F_N^\dagger\alpha$. This distinction matters when $N\ge4$.
- **Probabilities** are absolute squares of complex amplitudes, not the amplitudes themselves.
- The professor introduces the complete QFT circuit as material for **the next session**. Section 3.21 and animation 10 are clearly labeled **supplementary previews**, not a reconstruction of an explanation that was never completed in this lecture.

## Corrections and source handling

Speech-to-text mistakes and spoken calculation slips are identified where needed. In particular, the $f_1$/$f_3$ inner-product example uses the correct complex conjugate, the periodic N=16 output excludes odd indices, and the matrix/inverse sign conventions are never silently interchanged. Other mathematical expansions beyond the spoken lecture are labeled as beginner's expansions or supplementary examples.

## Verification status

The package is designed for offline operation. The ZIP generation workflow checks file presence, internal Markdown references, SVG parsing, HTML resources and arithmetic examples. The `animations/` pages contain no external network resources. If opening an HTML file inside a Markdown viewer only shows its source, open it directly in a web browser instead.
