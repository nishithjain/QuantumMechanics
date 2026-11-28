# Chapter 03 — Linear Transformations and Matrices

This is an offline-friendly companion to the 3Blue1Brown **Essence of Linear Algebra**, Chapter 03 lecture (approximately 10 min 58 sec). It is based on the supplied lecture materials and lecture.

## Start here

1. Read **[`notes/lecture-notes.md`](notes/lecture-notes.md)** in order, from Section 1 to Section 16. In **VS Code**, open the Markdown file, then press **Ctrl + Shift + V** (Markdown Preview).
2. Each illustration appears directly after the concept it explains and is stored in `images/`.
3. Open the interactive `.html` files from `animations/` in a browser (Chrome, Edge, Firefox). They are **fully self-contained**: no installation or internet connection required.
4. Run animations from inside the extracted ZIP folder, not from within your ZIP viewer.

## Interactive animations

- [`animation-01.html`](animations/animation-01.html) — **Linear vs. non-linear:** deformation, rotation, translation, curvature, diagonal trick.
- [`animation-02.html`](animations/animation-02.html) — **The lecture's actual arithmetic:** how T(−1,2) becomes (5,2).
- [`animation-03.html`](animations/animation-03.html) — **Matrices move space:** rotation, shear, and custom matrix entry controls.
- [`animation-04.html`](animations/animation-04.html) — **Dependent columns collapse the plane onto a line.**

Every animation includes Play, Pause, Step, and Reset buttons, along with a progress slider. The third animation also has a changeable 2×2 matrix.

## Files

```
lecture-notes/
├── README.md
├── notes/
│ └── lecture-notes.md
├── images/
│ ├── concept-01.png... concept-11.png
└── animations/
 ├── animation-01.html
 ├── animation-02.html
 ├── animation-03.html
 └── animation-04.html
```

## Color key

- Teal green: transformed first basis vector (image of i-hat).
- Pink: transformed second basis vector (image of j-hat).
- Blue: other grid lines or vector illustrations.
- Orange: the tracked input/output vector.

## Troubleshooting

- If Markdown images are missing, retain the same folder structure: `notes/` and `images/` should be siblings under `lecture-notes/`.
- If a relative HTML link does not open from Markdown Preview, find the file in `animations/` and double-click it.
- If a ZIP link is hard to download, the Markdown notes and each animation are also supplied separately with the response.

All extra calculations that are not explicitly provided in the lecture are labeled **Beginner extension** in the notes.
