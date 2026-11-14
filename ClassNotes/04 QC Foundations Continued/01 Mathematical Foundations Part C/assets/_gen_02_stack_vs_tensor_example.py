"""Optional regen for 02_stack_vs_tensor_example.png (hand-tuned asset may differ)."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

OUT = Path(__file__).with_name("02_stack_vs_tensor_example.png")

INK = "#152744"
MUTED = "#465a75"
ACCENT = "#214fc2"
ACCENT_2 = "#0d7a5f"
LINE = "#c9d6e7"
PAGE = "#edf2fa"
SURFACE = "#ffffff"


def card(ax, x, y, w, h, fc, ec=LINE, lw=1.0):
    p = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.06",
        facecolor=fc, edgecolor=ec, linewidth=lw,
    )
    ax.add_patch(p)


def main() -> None:
    fig, ax = plt.subplots(figsize=(10.2, 5.6), dpi=150)
    ax.set_xlim(0, 10.2)
    ax.set_ylim(0, 5.6)
    ax.axis("off")
    fig.patch.set_facecolor(PAGE)
    ax.set_facecolor(PAGE)

    ax.add_patch(Rectangle((0, 4.85), 10.2, 0.75, facecolor="#162b52", zorder=0))
    ax.text(0.4, 5.28, "WORKED EXAMPLE", color="#a8c4f0", fontsize=9, fontweight="bold")
    ax.text(0.4, 4.98, "u = (1,2,3) and v = (4,5,6): stack vs tensor", color="white", fontsize=12.5, fontweight="bold")

    # Left panel: stacking
    card(ax, 0.35, 0.45, 4.5, 4.15, SURFACE)
    ax.text(0.55, 4.2, "Stack u ⊕ v", color=INK, fontsize=11, fontweight="bold")
    ax.text(0.55, 3.95, "Concatenation → 6 = 3 + 3", color=MUTED, fontsize=9)

    ax.text(0.65, 3.55, "u", color=ACCENT, fontsize=10, fontweight="bold")
    for i, val in enumerate([1, 2, 3]):
        card(ax, 0.6, 2.85 - i * 0.55, 0.55, 0.42, "#e8f0fc", ec=ACCENT)
        ax.text(0.875, 3.06 - i * 0.55, str(val), ha="center", va="center", fontsize=11, color=INK)

    ax.text(0.65, 1.55, "v", color=ACCENT_2, fontsize=10, fontweight="bold")
    for i, val in enumerate([4, 5, 6]):
        card(ax, 0.6, 1.05 - i * 0.55, 0.55, 0.42, "#eef6f3", ec=ACCENT_2)
        ax.text(0.875, 1.26 - i * 0.55, str(val), ha="center", va="center", fontsize=11, color=INK)

    ax.annotate("", xy=(1.45, 2.45), xytext=(1.25, 2.45), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.5))
    ax.text(1.55, 2.7, "below", color=MUTED, fontsize=8.5)

    ax.text(2.0, 3.55, "Combined", color=INK, fontsize=10, fontweight="bold")
    for i, val in enumerate([1, 2, 3, 4, 5, 6]):
        fc = "#e8f0fc" if i < 3 else "#eef6f3"
        ec = ACCENT if i < 3 else ACCENT_2
        card(ax, 2.0, 3.05 - i * 0.45, 0.55, 0.38, fc, ec=ec)
        ax.text(2.275, 3.24 - i * 0.45, str(val), ha="center", va="center", fontsize=10, color=INK)
    ax.text(2.95, 0.65, "Still two separate blocks", color=MUTED, fontsize=8.5)

    # Right panel: tensor grid
    card(ax, 5.15, 0.45, 4.7, 4.15, SURFACE)
    ax.text(5.35, 4.2, "Tensor u ⊗ v", color=INK, fontsize=11, fontweight="bold")
    ax.text(5.35, 3.95, "All pairwise products → 9 = 3 × 3", color=MUTED, fontsize=9)

    v_labels = ["4", "5", "6"]
    u_labels = ["1", "2", "3"]
    grid = [[4, 5, 6], [8, 10, 12], [12, 15, 18]]

    ax.text(6.55, 3.55, "v →", color=ACCENT_2, fontsize=9, ha="center", fontweight="bold")
    for j, lab in enumerate(v_labels):
        ax.text(6.95 + j * 0.95, 3.55, lab, color=ACCENT_2, fontsize=10, ha="center", fontweight="bold")

    ax.text(5.55, 2.5, "u\n↓", color=ACCENT, fontsize=9, ha="center", fontweight="bold")

    for i in range(3):
        ax.text(5.75, 2.85 - i * 0.85, u_labels[i], color=ACCENT, fontsize=10, fontweight="bold")
        for j in range(3):
            x = 6.55 + j * 0.95
            y = 2.55 - i * 0.85
            card(ax, x - 0.35, y - 0.28, 0.7, 0.52, SURFACE if (i + j) % 2 else "#f7f9fc")
            ax.text(x, y, str(grid[i][j]), ha="center", va="center", fontsize=10, color=INK, fontweight="600")

    ax.text(5.35, 0.65, "Column list: 4,5,6,8,10,12,12,15,18", color=MUTED, fontsize=8.3, family="monospace")

    fig.savefig(OUT, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
