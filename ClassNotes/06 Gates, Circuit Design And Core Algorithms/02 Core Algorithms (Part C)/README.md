# Core Algorithms (Part C) — Offline Study Package

**Topic:** Simon's Algorithm, Change of Basis and the Road to the Quantum Fourier Transform  
**Source:** The uploaded lecture transcription `02 Core Algorithms (Part C).txt`. **No PDF slides were supplied for this lecture.** The educational diagrams are original and the extra worked examples are labeled as supplements in the notes.

## Start here

1. Open **`Lecture_Notes.md`** in a Markdown reader that supports LaTeX mathematics (for example, VS Code with a Markdown math extension or a compatible Markdown previewer). Read the sections in order, because the professor builds each concept from the previous one.
2. When a concept includes an interactive link, open the corresponding HTML file in `animations/` with Chrome, Edge, Firefox, or another modern browser. **No network connection or server is required.** You can double-click the HTML file and it will run offline.
3. Use **Play** to advance automatically, **Pause** to stop, **Step** to inspect one stage, and **Reset** to return to stage one. Adjust the input selectors and sliders to try examples; some animations also include specialized controls such as **Sample z**.
4. Complete the exercises in **`practice/practice_questions.md`** before reading the **Answer Key** lower down in that same file.
5. Before an exam, reread the **Important Formulas**, **Glossary** and **Final Revision Notes** sections of the main notes.

## Folder structure

```text
Lecture_Notes/
├── README.md
├── Lecture_Notes.md
├── animations/
│   ├── animation_01.html     # Several-qubit Hadamard and parity signs
│   ├── animation_02.html     # Deutsch–Jozsa / Bernstein–Vazirani
│   ├── animation_03.html     # Simons paired inputs
│   ├── animation_04.html     # Simon amplitude cancellation
│   ├── animation_05.html     # Sample equations and check rank
│   ├── animation_06.html     # Single-qubit basis change
│   ├── animation_07.html     # Two-qubit Walsh Fourier coefficients
│   ├── animation_08.html     # Z_N modular arithmetic clock
│   └── animation_09.html     # Roots of unity and cyclic characters
├── images/
│   ├── diagram_01.svg       # Lecture roadmap
│   ├── diagram_02.svg       # Hadamard sign pattern
│   ├── diagram_03.svg       # Simon pairing by XOR
│   ├── diagram_04.svg       # Simon oracle circuit
│   ├── diagram_05.svg       # Binary equation elimination
│   ├── diagram_06.svg       # Change of basis
│   ├── diagram_07.svg       # Hadamard sign matrix
│   ├── diagram_08.svg       # Modular addition versus XOR
│   └── diagram_09.svg       # Roots of unity
└── practice/
    └── practice_questions.md
```

## Viewing mathematical equations

The main notes use standard Markdown math delimiters `\(...\)` and `\[...\]`. A Markdown editor that supports math will render them as equations. If your editor shows the raw LaTeX source, enable its equation-rendering feature or use a different local Markdown previewer. You do not need any online image service. The **HTML animations themselves use browser-native Unicode mathematical labels**, so no math-rendering library is needed for them.

## Reading the diagrams

Local SVGs appear within the Markdown as relative references such as `images/diagram_04.svg`. Most Markdown viewers display these directly. You may also open SVG files independently in a web browser. Keep all folders together when moving or unzipping the package, otherwise the relative links in the notes will break.

## What this lecture does and does not include

- The transcript **reviews** Deutsch–Jozsa and Bernstein–Vazirani and **completes** the Simon algorithm.
- The professor then explains Hadamard as a Fourier/change-of-basis operation and introduces the character property on XOR strings.
- Finally, the professor introduces modular arithmetic, complex roots of unity and character cancellation as preparation for the **next** lecture.
- A compact **QFT formula and example** are provided as a clearly identified *supplementary preview*, not falsely attributed as a full QFT derivation taught in this session.
- The formal mathematical qualifications in the notes (normalization, query-cost assumptions and basis-change interpretations) are educational corrections or clarifications of informal speech, not changes to the professor's intended narrative.

## Offline and browser notes

Every animation is a **single standalone HTML file** containing HTML, CSS and JavaScript. It makes no network requests, loads no external fonts or libraries, and requires no installation. Responsive layouts adapt to desktop and mobile browser widths. Numerical values are calculated locally from the selected inputs.

**Suggested order if the math feels difficult:** Animation 01 → 03 → 04 → 05 → 06 → 07 → 08 → 09; animation 02 provides a helpful comparison with earlier algorithms.

---

All examples are for education and for idealized noiseless quantum oracles; this ZIP does not require a quantum computer or Qiskit.
