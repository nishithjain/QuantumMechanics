# Core Algorithms — Part B | Beginner-Friendly Learning Pack

A self-contained set of study notes, diagrams, and browser-based interactive demonstrations created from **`02 Core Algorithms Part B.txt`**.

## Start here

1. Open **[`notes/lecture-notes.md`](notes/lecture-notes.md)** in VS Code or Cursor and use its Markdown preview (`Ctrl+Shift+V` in VS Code).
2. Read in order. The headings follow the **professor's sequence** in the Part B recording, beginning with Deutsch–Jozsa and ending with audience questions on earlier linear algebra exercises.
3. When you see an image, it is already linked using a relative path: `../images/concept-XX.png`.
4. Click or open a relative animation link such as `../animations/animation-02.html`. If your Markdown preview doesn't open local links, navigate to the `animations/` folder and **double-click the HTML file** to open it in your browser. No server, installation, network connection, or third-party libraries are needed.
5. Each animation has **Play, Pause, Step, and Reset**. It is best to start with **Step** and read the accompanying explanation before moving on.

## Contents, in lecture order

| Lecture segment | Main topic | Interactive animation |
|---|---|---|
| 1–2 | Deutsch recap and the classical randomized-vs-exact distinction | `animation-01.html` |
| 3–4 | Deutsch–Jozsa quantum circuit and complete amplitude cancellation | `animation-02.html` |
| 5–6 | Bernstein–Vazirani hidden parity string and Hadamard recovery | `animation-03.html` |
| 7–12 | Simon's hidden XOR pairs, two-register oracle, and interference | `animation-04.html` |
| 13 | Collecting Simon's parity equations and determining `s` | `animation-05.html` |
| 14 | Audience's projection, rotation, basis-change, and Pauli-gate questions | `animation-06.html` |

The Markdown has **10 original educational images** in `images/`, matched to the point where each concept is taught. All six HTML demonstrations are standalone and made with HTML, CSS and vanilla JavaScript.

## Why the notes are more detailed than a summary

The lecture repeatedly returns to the same ideas (phase kickback, Hadamard identities, XOR parity, and cancellation). Those repetitions are preserved at the appropriate points, with the missing intermediate mathematics filled in. Supplementary examples are labeled, and possible speech-to-text or mathematical errors are highlighted rather than silently modified.

### Important accuracy cautions

- **Simon's classical randomized query complexity:** `Θ(2^(n/2))`, rather than `2^n`.
- **Projection of (1,0) onto y=x:** `(1/2,1/2)`, rather than `(1/√2,1/√2)`.
- **The two measurements in Simon's algorithm:** the output register is measured first; the later input-register measurement yields `z` with `s·z=0`.
- **Ideal circuit vs real hardware:** “probability 1” refers to an ideal noiseless quantum circuit and an oracle satisfying the problem's promise.
- **Scope:** This is **one lecture** (Part B). The deeper Fourier analysis promised for the next class is not invented in these notes.

## Folder structure

```text
lecture-notes/
├── README.md
├── notes/
│   └── lecture-notes.md
├── images/
│   ├── concept-01.png
│   ├── ...
│   └── concept-10.png
└── animations/
    ├── animation-01.html
    ├── ...
    └── animation-06.html
```

**Offline:** Images are included as PNGs; HTML animations do not depend on external scripts, fonts, services, or libraries.
