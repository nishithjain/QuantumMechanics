# Chapter 02 — Linear Combinations, Span, and Basis Vectors

A self-contained study package based on the user-supplied lecture materials and lecture from **Essence of Linear Algebra, Chapter 2**. The explanations follow the instructor's order. Additional worked examples are explicitly labeled in the notes.

## Start here

1. Open `notes/lecture-notes.md` in **VS Code** and use **Ctrl + Shift + V** to open the Markdown preview. Alternatively use any Markdown previewer that supports images and LaTeX math.
2. Read the numbered sections **in order**. Each picture is directly below the concept it illustrates.
3. When the notes mention an animation, click its link from a Markdown preview or navigate to the matching file under `animations/` and double-click it to open in Chrome, Edge, or Firefox.
4. Use **Play**, **Pause**, **Step**, and **Reset** to follow the geometric idea slowly. Each animation is self-contained and works **offline**.
5. At the end, attempt the **Check your understanding** questions before expanding the answers.

## Package contents

```
lecture-notes/
├── README.md
├── notes/
│ └── lecture-notes.md
├── images/
│ ├── concept-01.png standard i-hat, j-hat decomposition
│ ├── concept-02.png standard and alternative bases
│ ├── concept-03.png a linear combination
│ ├── concept-04.png one fixed scalar gives a line
│ ├── concept-05.png plane, line, or origin span
│ ├── concept-06.png arrows versus tip-points
│ ├── concept-07.png 3D plane spanned by two vectors
│ ├── concept-08.png third vector inside/outside the plane
│ ├── concept-09.png dependent versus independent vectors
│ └── concept-10.png basis definition illustrated
└── animations/
 ├── animation-01.html basis coordinates and vector construction
 ├── animation-02.html the three 2D span cases
 └── animation-03.html how a third vector changes 3D span
```

## Conventions

- Blue: first vector / first scaled component.
- Green: second vector / second scaled component.
- Purple: additional vector or reachable line/sheet as noted.
- Pink-red: resultant vector or highlighted endpoint.
- Symbols such as `i-hat`, `j-hat`, `u`, `w`, `a`, `b`, `c` are explained before use.
- Plotted coordinates are mathematically calculated, not illustrative guesses.

## Source and teaching note

The source lecture is **not copied into this ZIP**, keeping it small and easy to download. The lecture determines the order and the content of the lecture. For concepts shown visually but not assigned exact numerical values by the narrator (such as the alternative slanted basis), the notes give clearly marked **additional beginner examples** with exact numbers. The lecture does not introduce matrices yet; the notes preserve that order.

No external JavaScript, CSS, fonts, web requests, or internet connection is needed for the animations.
