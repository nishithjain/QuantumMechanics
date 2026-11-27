# Chapter 04 — Matrix Multiplication as Composition

This learning package was prepared using the supplied **04 — Matrix Multiplication as Composition** transcript. It preserves the sequence of the lecturer's explanations and adds beginner-friendly derivations, numerical checks, original diagrams, and standalone interactive animations.

## Open the notes

1. Extract the ZIP package to a normal folder (do **not** open the Markdown from within the ZIP).
2. Open [`notes/lecture-notes.md`](notes/lecture-notes.md) in **Visual Studio Code**.
3. Press **Ctrl + Shift + V** to open the formatted Markdown preview.
4. Open the relevant HTML files below in Chrome, Edge, or another modern browser. All files work **offline**.

## Animations

- [01 — Rotation followed by shear](animations/animation-01.html). The basis vectors explain why S R has columns (1,1) and (-1,0).
- [02 — M₂ after M₁](animations/animation-02.html). Watch the lecture's fully worked matrix-product example, with result [[2,0],[1,-2]].
- [03 — Order matters](animations/animation-03.html). Compare rotation-then-shear and shear-then-rotation, side by side.
- [04 — Associativity](animations/animation-04.html). Three successive transformations with alternative groupings.

Each animation includes **Play, Pause, Step, Reset**, plus x and y sliders for trying your own vectors. They use only HTML, CSS, JavaScript, and Canvas, without libraries or network access.

## Folder layout

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
    ├── animation-02.html
    ├── animation-03.html
    └── animation-04.html
```

For the best learning experience, study the material in chapter order. This chapter builds on vector addition, linear combinations, basis vectors, and the meaning of a single transformation matrix.

**Main insight:** multiplying matrices is composing transformations; **the rightmost one acts first**.
