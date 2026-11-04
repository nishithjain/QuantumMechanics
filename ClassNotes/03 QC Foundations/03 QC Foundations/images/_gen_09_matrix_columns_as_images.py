"""Regenerate 09_matrix_columns_as_images.png — Section 8.2–8.3 linear map example."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).with_name("09_matrix_columns_as_images.png")

# Input
E1 = (1, 0)
E2 = (0, 1)
PX, PY = 3, 7

# Outputs under T
TE1 = (2, 4)
TE2 = (5, 1)
TPX, TPY = 41, 19

assert PX * TE1[0] + PY * TE2[0] == TPX
assert PX * TE1[1] + PY * TE2[1] == TPY


def arrow(ax, x0, y0, x1, y1, color, lw=2.5, dash=False, zorder=3):
    style = "-|>"
    patch = FancyArrowPatch(
        (x0, y0), (x1, y1),
        arrowstyle=style,
        mutation_scale=14,
        linewidth=lw,
        color=color,
        linestyle="--" if dash else "-",
        zorder=zorder,
    )
    ax.add_patch(patch)


def draw_input(ax):
    ax.set_title("Input: $p = 3e_1 + 7e_2$", fontsize=11, fontweight="bold")
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-0.5, 8)
    ax.set_aspect("equal")
    ax.grid(True, color="#e2e8f0", linewidth=0.8)
    ax.axhline(0, color="#64748b", lw=1)
    ax.axvline(0, color="#64748b", lw=1)

    arrow(ax, 0, 0, 1, 0, "#2459c4", lw=3)
    arrow(ax, 0, 0, 0, 1, "#b95012", lw=3)
    ax.text(1.05, -0.35, "$e_1$", color="#2459c4", fontsize=11)
    ax.text(-0.55, 1.05, "$e_2$", color="#b95012", fontsize=11)

    arrow(ax, 0, 0, 3, 0, "#2459c4", lw=2, dash=True)
    arrow(ax, 3, 0, 3, 7, "#b95012", lw=2, dash=True)
    arrow(ax, 0, 0, PX, PY, "#12834b", lw=3.2)
    ax.plot(PX, PY, "o", color="#0f172a", ms=8, zorder=5)
    ax.text(PX + 0.2, PY + 0.25, "$p=(3,7)$", fontsize=11, fontweight="bold")
    ax.text(1.5, -0.55, "$3e_1$", color="#2459c4", fontsize=10, ha="center")
    ax.text(3.35, 3.5, "$7e_2$", color="#b95012", fontsize=10)


def draw_output(ax):
    ax.set_title("Output: $T(p) = 3\\,T(e_1) + 7\\,T(e_2) = (41,19)$", fontsize=10.5, fontweight="bold")
    ax.set_xlim(-1, 46)
    ax.set_ylim(-1, 22)
    ax.set_aspect("equal")
    ax.grid(True, color="#e2e8f0", linewidth=0.8)
    ax.axhline(0, color="#64748b", lw=1)
    ax.axvline(0, color="#64748b", lw=1)

    arrow(ax, 0, 0, TE1[0], TE1[1], "#2459c4", lw=2.8)
    arrow(ax, 0, 0, TE2[0], TE2[1], "#b95012", lw=2.8)
    ax.text(2.2, 4.3, "$T(e_1)=(2,4)$", color="#2459c4", fontsize=10)
    ax.text(5.3, 1.2, "$T(e_2)=(5,1)$", color="#b95012", fontsize=10)

    arrow(ax, 0, 0, 3 * TE1[0], 3 * TE1[1], "#2459c4", lw=2, dash=True)
    arrow(ax, 3 * TE1[0], 3 * TE1[1], TPX, TPY, "#b95012", lw=2, dash=True)
    arrow(ax, 0, 0, TPX, TPY, "#12834b", lw=3.2)
    ax.plot(TPX, TPY, "o", color="#0f172a", ms=8, zorder=5)
    ax.text(TPX + 1, TPY + 0.6, "$T(p)=(41,19)$", fontsize=11, fontweight="bold")

    ax.text(
        2,
        19,
        "M = [[2, 5], [4, 1]]\ncolumns: T(e1), T(e2)",
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#f8fafc", edgecolor="#cbd5e1"),
    )


def main() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.2), dpi=150)
    draw_input(ax1)
    draw_output(ax2)
    fig.suptitle(
        "Same coefficients (3 and 7); new building blocks after $T$",
        fontsize=13,
        fontweight="bold",
        y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUT, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
