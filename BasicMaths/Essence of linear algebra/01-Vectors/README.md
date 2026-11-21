# 01 — Vectors | Interactive Lecture Notes

Beginner-friendly study material based on the uploaded **01-Vectors** video and transcript from the *Essence of Linear Algebra* series.

## Start here

1. Open **`notes/lecture-notes.md`** in VS Code (Markdown Preview: `Ctrl+Shift+V`), Obsidian, or a Markdown viewer that supports LaTeX mathematics.
2. Read the sections **in order**. They follow the lecture's progression, not a reorganized textbook syllabus.
3. When you encounter a **▶ Open Animation** link, open the linked HTML file in your browser. You can also double-click the HTML files directly in `animations/`.
4. Press **Play**, **Pause**, **Step**, or **Reset**. Try the examples from the video and then change the values yourself.
5. Review the questions and worked answers at the end of the notes.

**No setup needed:** All three animations use self-contained HTML, CSS, JavaScript, and SVG, with no external libraries, network connections, or build steps.

## What is included?

```text
lecture-notes/
├── README.md
├── notes/
│   └── lecture-notes.md
├── images/
│   ├── concept-01.png   Three perspectives on vectors
│   ├── concept-02.png   Free arrows vs arrows rooted at the origin
│   ├── concept-03.png   Reading 2D coordinates
│   ├── concept-04.png   Negative coordinates
│   ├── concept-05.png   3D vector with x, y, z components
│   ├── concept-06.png   Tip-to-tail addition
│   ├── concept-07.png   Adding movements on a number line
│   ├── concept-08.png   Numerical example (1,2) + (3,−1)
│   ├── concept-09.png   Scaling by 2, 1/3, −1.8
│   └── concept-10.png   Translating numbers ↔ geometry
└── animations/
    ├── animation-01.html    Coordinates: horizontal, vertical, arrow
    ├── animation-02.html    Vector addition: tip-to-tail
    └── animation-03.html    Scalar multiplication
```

## Which animation should I open?

| After reading | Animation | What you can do |
|---|---|---|
| Section 3: 2D coordinates | `animations/animation-01.html` | Change x and y, including negative values; see the walk become an arrow. |
| Section 5: vector addition | `animations/animation-02.html` | Watch u and v move tip-to-tail; try lecture and alternative examples. |
| Section 6: scalar multiplication | `animations/animation-03.html` | Choose 2, 1/3, −1.8 or 0; visualize size and direction. |

## Troubleshooting

- **Mathematical formulas appear as raw `$$ ... $$`:** Open the `.md` in VS Code's Markdown Preview or another Markdown reader with mathematical notation support. The `.html` animations work normally in any current Chrome, Edge, or Firefox browser.
- **Images are missing:** Keep the entire extracted `lecture-notes` directory together. Relative paths depend on the `notes/`, `images/`, and `animations/` folders remaining side by side.
- **Animation doesn't respond:** Open the file in a current browser with JavaScript enabled. No internet is needed.

## Source fidelity

The attached video (about 9 minutes 51 seconds) and transcript were used together. The notes preserve the order and main examples of the lecture. Extra analogies, additional coordinate examples, the zero-scalar case, worked exercises, illustrations, and HTML demonstrations are identified as instructional additions where appropriate. The three-dimensional video example is `[2,1,3]`, and the addition example is `[1,2] + [3,−1]`.
