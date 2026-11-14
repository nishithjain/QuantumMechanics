"""Optional regen for 02_joint_basis_grid.png (hand-tuned asset may differ)."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

OUT = Path(__file__).with_name("02_joint_basis_grid.png")

INK = "#152744"
MUTED = "#465a75"
ACCENT = "#214fc2"
ACCENT_2 = "#0d7a5f"
LINE = "#c9d6e7"
PAGE = "#edf2fa"
SURFACE = "#ffffff"
GRID_A = "#e8f0fc"
GRID_B = "#eef6f3"


def rounded_card(ax, x, y, w, h, fc, ec=LINE, lw=1.2, zorder=2):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.08",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
        zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def main() -> None:
    fig, ax = plt.subplots(figsize=(10.5, 6.4), dpi=150)
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    fig.patch.set_facecolor(PAGE)
    ax.set_facecolor(PAGE)

    # Header
    ax.add_patch(Rectangle((0, 5.55), 10.5, 0.85, facecolor="#162b52", zorder=0))
    ax.text(0.45, 6.05, "02 / JOINT BASIS", color="#a8c4f0", fontsize=9.5, fontweight="bold")
    ax.text(0.45, 5.72, "Two ℝ³ factors: pair every eᵢ with every fⱼ",
            color="white", fontsize=13.5, fontweight="bold")
    ax.text(10.05, 5.72, "9 = 3 × 3", color="#c5d8ff", fontsize=11, ha="right")

    # Left: first-space basis
    ax.text(0.55, 4.95, "First space V₁", color=INK, fontsize=11, fontweight="bold")
    ax.text(0.55, 4.72, "basis e₁, e₂, e₃", color=MUTED, fontsize=9.5)
    for i, label in enumerate(["e₁", "e₂", "e₃"]):
        y = 3.55 - i * 1.05
        rounded_card(ax, 0.45, y, 1.15, 0.78, GRID_A, ec=ACCENT)
        ax.text(1.02, y + 0.39, label, ha="center", va="center", fontsize=12, color=ACCENT, fontweight="bold")

    # Top: second-space basis
    ax.text(3.35, 4.95, "Second space V₂", color=INK, fontsize=11, fontweight="bold")
    ax.text(3.35, 4.72, "basis f₁, f₂, f₃", color=MUTED, fontsize=9.5)
    for j, label in enumerate(["f₁", "f₂", "f₃"]):
        x = 2.55 + j * 1.55
        rounded_card(ax, x, 4.05, 1.25, 0.55, GRID_B, ec=ACCENT_2)
        ax.text(x + 0.625, 4.32, label, ha="center", va="center", fontsize=12, color=ACCENT_2, fontweight="bold")

    # 3×3 tensor basis grid
    ax.text(2.55, 3.55, "Joint basis directions eᵢ ⊗ fⱼ", color=INK, fontsize=10.5, fontweight="bold")
    for i in range(3):
        for j in range(3):
            x = 2.55 + j * 1.55
            y = 2.35 - i * 1.05
            fc = SURFACE if (i + j) % 2 else "#f7f9fc"
            rounded_card(ax, x, y, 1.25, 0.78, fc)
            ax.text(x + 0.625, y + 0.39, f"e{i+1}⊗f{j+1}", ha="center", va="center",
                    fontsize=10.5, color=INK, fontweight="600")

    # Arrows: each e_i fans out to row
    for i in range(3):
        y0 = 3.94 - i * 1.05
        ax.annotate(
            "",
            xy=(2.45, y0 + 0.15),
            xytext=(1.62, y0 + 0.15),
            arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=1.4, shrinkA=2, shrinkB=2),
        )
    for j in range(3):
        x0 = 2.55 + j * 1.55 + 0.625
        ax.annotate(
            "",
            xy=(x0, 3.28),
            xytext=(x0, 4.02),
            arrowprops=dict(arrowstyle="-|>", color=ACCENT_2, lw=1.2, shrinkA=2, shrinkB=2),
        )

    # Compare stack vs tensor
    rounded_card(ax, 7.15, 2.15, 3.05, 2.75, SURFACE)
    ax.text(7.4, 4.55, "Two ways to list coordinates", color=INK, fontsize=10.5, fontweight="bold")

    rounded_card(ax, 7.35, 3.35, 2.65, 0.95, "#fff5f5", ec="#e8a8a8")
    ax.text(7.5, 4.05, "Stack u then v", color=INK, fontsize=10, fontweight="bold")
    ax.text(7.5, 3.72, "(u₁,u₂,u₃,v₁,v₂,v₃)", color=MUTED, fontsize=8.8, family="monospace")
    ax.text(9.85, 3.72, "6 = 3+3", ha="right", fontsize=11, color="#b45309", fontweight="bold")

    rounded_card(ax, 7.35, 2.35, 2.65, 0.95, GRID_A, ec=ACCENT)
    ax.text(7.5, 3.05, "Tensor / joint basis", color=INK, fontsize=10, fontweight="bold")
    ax.text(7.5, 2.72, "one amplitude per eᵢ⊗fⱼ", color=MUTED, fontsize=8.8)
    ax.text(9.85, 2.72, "9 = 3×3", ha="right", fontsize=11, color=ACCENT, fontweight="bold")

    ax.text(5.1, 0.35,
            "Quantum joint states use the multiply rule: dimension of V₁ ⊗ V₂ is (dim V₁)(dim V₂).",
            ha="center", fontsize=9.5, color=MUTED)

    plt.tight_layout(pad=0.3)
    fig.savefig(OUT, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
