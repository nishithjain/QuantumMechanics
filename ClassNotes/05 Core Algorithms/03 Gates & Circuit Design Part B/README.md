# Offline Lecture Learning Pack

## What this package is

**QC Foundations [4/4]: Entanglement as a Resource**, based on the complete lecture transcript and PDF slides for *03 Gates & Circuit Design Part B* (Prof. Kolin Paul, IIT Delhi; slide date 15 November 2026).

The lesson is intentionally written for someone starting quantum mechanics and quantum computing without a strong mathematics background. Every major idea is introduced in everyday language, then explained with its equations, a worked example, common pitfalls, and understanding checks.

## Open the materials

1. Open **`Lecture_Notes.md`** in a Markdown viewer that supports LaTeX mathematics (for example, VS Code Markdown Preview with a math-capable extension, Obsidian, Typora, or another MathJax/KaTeX-capable viewer). Some plain text editors display the LaTeX source rather than rendering it, which is normal.
2. Click any animation link, or navigate to **`animations/`** and double-click an HTML file to open it in Chrome, Firefox, or Edge.
3. On animation pages, use **Play**, **Pause**, **Step**, **Reset**. Select different input states, bits, or angles when controls are shown. The colored diagrams and step explanations update together.
4. To see static diagrams, open **`images/`**. The original SVG files are scalable: they can be opened in a browser or inserted into other notes.
5. For more exercises, open **`practice/practice_questions.md`**. Try the questions first; the full answer section follows all the questions.

## Folder structure

```text
Lecture_Notes/
├── README.md
├── Lecture_Notes.md
├── animations/
│   ├── animation_01.html  ... animation_09.html
├── images/
│   ├── diagram_01_entanglement_resource.svg
│   ├── diagram_02_bell_reverse_circuit.svg
│   ├── diagram_03_cnot_copy_vs_entangle.svg
│   ├── diagram_04_teleportation_circuit.svg
│   ├── diagram_05_superdense_circuit.svg
│   ├── diagram_06_chsh_axes.svg
│   ├── diagram_07_chsh_referee.svg
│   ├── diagram_08_teleport_vs_dense.svg
│   └── diagram_09_deferred_measurement.svg
└── practice/
    └── practice_questions.md
```

## Special instructions

- **Everything works offline.** There are no library imports or web fonts in the HTML files. The diagrams are local SVG files.
- **Markdown file links are relative** to the `Lecture_Notes` folder. Keep the folder structure intact when moving or unzipping it.
- **Notation:** `|ψ⟩` means an arbitrary one-qubit state; `|Φ±⟩` and `|Ψ±⟩` denote two-qubit Bell states. In teleportation, Alice's `m₁` is the **top** measured bit, and `m₂` the **middle** bit. **X if `m₂=1`, then Z if `m₁=1`.**
- **Read the accompanying explanation** with each animation: every visualization is deliberately simplified to the ideal, noise-free theoretical circuit, unless specifically discussing noise or samples.
- **Qiskit snippets** inside the notes are *reference examples*, not dependencies of the animations. Running the Python snippets requires locally installing compatible Qiskit packages.
- **Accessibility:** The HTML animations include explanatory prose and equations even when diagrams are unavailable. Each static SVG includes a title and description.

## Learning route

Start at §2 of `Lecture_Notes.md` for the prerequisite mathematics. Then follow §3 in order: Bell preparation → reverse decoder → no-cloning → teleportation proof → measured/coherent circuits → superdense coding → CHSH. Finish with the formula card (§4), revision notes (§8), and the practice workbook.

## Sources and accuracy

These notes were prepared from the **user-provided** complete lecture transcription and lecture PDF slides; the source material itself is not redistributed in this ZIP. The original PDF contains 19 physical pages with 31 numbered lecture slides. Typographical transcription errors and minor bit-order ambiguities have been corrected or explicitly noted in `Lecture_Notes.md`.

## Verification completed for this package

- Checked the Markdown and practice workbook: all **32 local Markdown/image/animation references** resolve to files in this folder.
- Parsed all **9 SVG** educational diagrams as valid XML and inspected their text bounds.
- Executed all **9 standalone animations** in a headless Chromium browser session, exercised **Play**, **Pause**, **Step**, **Reset**, and input selectors, and found **no JavaScript runtime errors**. Offline HTML was tested as self-contained content; your local browser's file-opening policy may differ.
- Independently checked the four Bell-decoder mappings, teleportation with non-real amplitudes, all four superdense messages, and the optimal/non-optimal CHSH probabilities using numerical matrix calculations.
