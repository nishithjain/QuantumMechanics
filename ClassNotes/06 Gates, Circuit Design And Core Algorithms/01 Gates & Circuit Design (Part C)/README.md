# Gates & Circuit Design [2/3] — Beginner-Friendly Study Package

**Lecture:** Universality and Cost  
**Course:** IIT Delhi, Quantum Computing — CEP  
**Instructor:** Prof. Kolin Paul  
**Sources:** Uploaded `01 Gates & Circuit Design (Part C).txt` transcript and `01 Gates & Circuit Design (Part C).pdf` slides (November 2026)

This offline package turns the lecture into a self-contained tutorial for readers new to quantum computing. It includes **complete beginner-friendly Markdown notes, nine interactive HTML animations, ten original SVG diagrams, and a separate practice workbook with detailed answers**.

## Folder contents

```text
Lecture_Notes/
├── README.md
├── Lecture_Notes.md
├── animations/
│   ├── animation_01.html  — Three meanings of universality and NAND XOR
│   ├── animation_02.html  — ZYZ turns on the Bloch sphere
│   ├── animation_03.html  — H, S, T rotation/matrix explorer
│   ├── animation_04.html  — Controlled-Ry using the ABC trick
│   ├── animation_05.html  — SWAP using three CNOTs
│   ├── animation_06.html  — Clifford-only versus Clifford+T reachable states
│   ├── animation_07.html  — Exact 15-gate Toffoli decomposition
│   ├── animation_08.html  — Gate counts, circuit depth, and cost models
│   └── animation_09.html  — Inject X/Z errors and measure fidelity
├── images/
│   ├── diagram_01.svg ... diagram_10.svg
└── practice/
    └── practice_questions.md
```

## Recommended learning path

1. Open **`Lecture_Notes.md`** in a Markdown viewer supporting LaTeX mathematics, such as VS Code with a suitable Markdown math preview, Obsidian with math rendering, or another local Markdown editor with built-in math support.
2. Study **Section 2: Prerequisites** first if qubits, complex numbers, bras/kets, and CNOT feel unfamiliar.
3. Follow the professor's sequence in **Section 3**. Work each equation on paper, then open the linked interactive HTML animation.
4. In **`practice/practice_questions.md`**, solve Part A before reviewing the detailed solutions in Part B.
5. Use **Sections 4, 5 and 8** in the main notes as a formula card and exam-revision guide.

## How to open HTML animations

- **Extract the entire ZIP first** without changing folder names.
- Double-click an `animation_XX.html` file, or right-click → **Open with** a recent browser (Chrome, Edge, Firefox or Safari).
- The animations run directly from local files (`file://`) without a web server or internet connection.
- Use **Play**, **Pause**, **Step**, and **Reset**. Many pages provide sliders or drop-downs that recalculate the state immediately.
- Interactive equations are displayed in regular Unicode text, not with an external math-rendering library, so they remain available offline.

## How to view the diagrams

The `.svg` diagrams are original local vector files; they open in a browser, SVG viewer, or Markdown editor. The main notes reference them as `images/diagram_XX.svg`. Do **not** move the diagrams to another directory unless you also update the notes' relative links.

## Mathematical notation

- `|ψ⟩`: quantum **ket**, a state column vector.
- `⟨ψ|`: **bra**, a conjugate-transposed ket.
- `X`, `Z`, `H`, `S`, `T`: familiar single-qubit gates.
- `CX` = `CNOT`: controlled-NOT.
- `CCX` = Toffoli: controlled-controlled-NOT.
- `T†`: inverse T; it still contributes to T-count.
- `Ry(θ)`, `Rz(θ)`: rotations around the Y/Z axes.
- `⊕`: XOR. `⊗`: tensor product.
- `U†U=I`: unitary/reversible matrix property.
- Matrices act **right to left** on ket column vectors, whereas circuit diagrams read from **left to right** in time.

## Source and accuracy notes

The transcript is the main narrative source. The PDF is used to verify mathematical notation, diagrams, formulas, numerical costs, and the lecture's examples. A few spoken slips and overly simplified physical descriptions are clearly flagged in `Lecture_Notes.md` rather than perpetuated.

The uploaded materials **do not contain** the professor's earlier complete `adder_core()` source or the officially released graded Mini-Capstone starter `.ipynb`. Accordingly, the notes discuss the reported compiler counts and capstone goals, but do **not** claim to reproduce an autograded notebook implementation. Always follow the current starter notebook and LMS submission rules rather than example pseudocode.

## Requirements and privacy

- **HTML animations:** Standard modern web browser only. No internet, CDN, external fonts, accounts, or libraries.
- **SVG images:** Standard image/SVG-capable viewer.
- **Markdown:** A viewer with LaTeX support is recommended to render the `\[...\]` and `$...$` equations properly.
- **Qiskit:** Not required to read notes or run offline HTML animations; required only if you separately run the professor's actual Jupyter lab assignments.
- Nothing in the package sends information over the network. Interactive states and random-number seeds stay in your browser.

## Troubleshooting

**Equations show literal backslashes:** Your Markdown viewer has not enabled LaTeX/math support. Switch to a math-capable Markdown preview.  
**Links do not open:** Verify that the ZIP was extracted and that `animations/`, `images/` and `practice/` remain alongside `Lecture_Notes.md`.  
**Browser does not display SVG:** Try Chrome, Edge or Firefox with the SVG file itself.  
**Noisy results change when adjusting controls:** This is intentional: the animation recomputes deterministic trials for the selected random seed and error probability.

Happy studying! Work slowly through the ZYZ example and ABC controlled-rotation derivation: those two ideas unlock most of the lecture's later discussions of universality and compilation.
