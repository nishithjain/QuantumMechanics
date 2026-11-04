"""Regenerate 04_change_of_basis_projection.png for Section 4.2 (p = (4,5) in Hadamard basis)."""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).with_name("04_change_of_basis_projection.png")

SQ2 = math.sqrt(2)
PX, PY = 4.0, 5.0
ALPHA_P = (PX + PY) / SQ2  # 9/sqrt(2)
ALPHA_M = (PX - PY) / SQ2  # -1/sqrt(2)
QX, QY = ALPHA_P / SQ2, ALPHA_P / SQ2  # (4.5, 4.5)
RX, RY = ALPHA_M / SQ2, -ALPHA_M / SQ2  # (-0.5, 0.5)

assert abs(QX - 4.5) < 1e-9 and abs(QY - 4.5) < 1e-9
assert abs(RX + 0.5) < 1e-9 and abs(RY - 0.5) < 1e-9
assert abs(QX + RX - PX) < 1e-9 and abs(QY + RY - PY) < 1e-9


def right_angle_marker(ax, foot_x, foot_y, dir_along, size=0.22):
    """Square marker at foot; dir_along is unit vector along the axis (line direction)."""
    dx, dy = dir_along
    px, py = -dy, dx  # perpendicular (for y-up math coords)
    s = size
    xs = [
        foot_x,
        foot_x + dx * s,
        foot_x + dx * s + px * s,
        foot_x + px * s,
        foot_x,
    ]
    ys = [
        foot_y,
        foot_y + dy * s,
        foot_y + dy * s + py * s,
        foot_y + py * s,
        foot_y,
    ]
    ax.plot(xs, ys, color="#475569", linewidth=1.2, solid_capstyle="round", zorder=6)


def arrow(ax, x0, y0, x1, y1, color, lw=2.6, zorder=4):
    arr = FancyArrowPatch(
        (x0, y0),
        (x1, y1),
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=lw,
        color=color,
        zorder=zorder,
    )
    ax.add_patch(arr)


def main() -> None:
    fig, ax = plt.subplots(figsize=(8.2, 7.2), dpi=150)
    ax.set_title("Same point, different coordinates", fontsize=14, fontweight="600", pad=12)
    ax.set_xlim(-2.2, 6.2)
    ax.set_ylim(-2.2, 6.2)
    ax.set_aspect("equal")
    ax.grid(True, color="#e2e8f0", linewidth=0.8)
    ax.axhline(0, color="#94a3b8", linewidth=1)
    ax.axvline(0, color="#94a3b8", linewidth=1)
    ax.set_xlabel("$x$", fontsize=11)
    ax.set_ylabel("$y$", fontsize=11)

    # Basis axes (infinite lines in window)
    lim = 6.0
    ax.plot([-lim, lim], [-lim, lim], "--", color="#0d9488", linewidth=1.4, alpha=0.55, zorder=1)
    ax.plot([-lim, lim], [lim, -lim], "--", color="#7c3aed", linewidth=1.4, alpha=0.55, zorder=1)
    ax.text(5.35, 5.55, "$h_+$ axis ($y=x$)", color="#0d9488", fontsize=10, ha="right")
    ax.text(5.55, -4.85, "$h_-$ axis ($y=-x$)", color="#7c3aed", fontsize=10, ha="right")

    # Component vectors α+ h+ and α- h-
    arrow(ax, 0, 0, QX, QY, "#0d9488", lw=2.8)
    arrow(ax, 0, 0, RX, RY, "#7c3aed", lw=2.8)
    ax.text(QX * 0.52, QY * 0.52 + 0.35, r"$\alpha_+ h_+$", color="#0d9488", fontsize=11)
    ax.text(RX - 0.05, RY + 0.72, r"$\alpha_- h_-$", color="#7c3aed", fontsize=11, ha="left")

    # Point P
    ax.plot(PX, PY, "o", color="#0f172a", markersize=11, zorder=7)
    ax.text(PX + 0.15, PY + 0.25, r"$P=(4,5)$", fontsize=12, fontweight="600")

    # Projection points Q, R
    ax.plot(QX, QY, "o", color="#0d9488", markersize=7, zorder=7)
    ax.plot(RX, RY, "o", color="#7c3aed", markersize=7, zorder=7)
    ax.text(QX + 0.2, QY - 0.45, r"$Q=(4.5,4.5)$", color="#0d9488", fontsize=10)
    ax.text(RX - 1.55, RY + 0.15, r"$R=(-0.5,0.5)$", color="#7c3aed", fontsize=10)

    # Perpendicular drops P → Q and P → R
    ax.plot([PX, QX], [PY, QY], "--", color="#ea580c", linewidth=2, dashes=(6, 4), zorder=5)
    ax.plot([PX, RX], [PY, RY], "--", color="#ea580c", linewidth=2, dashes=(6, 4), zorder=5)
    ax.text(4.35, 4.95, "⊥", color="#ea580c", fontsize=13, ha="center")
    ax.text(1.85, 3.05, "⊥", color="#ea580c", fontsize=13, ha="center")

    hplus_dir = (1 / SQ2, 1 / SQ2)
    hminus_dir = (1 / SQ2, -1 / SQ2)
    right_angle_marker(ax, QX, QY, hplus_dir, size=0.28)
    right_angle_marker(ax, RX, RY, hminus_dir, size=0.28)

    # Coefficient labels (scalars, not points)
    ax.text(
        -1.95,
        6.05,
        r"$\alpha_+=\langle h_+,p\rangle=\dfrac{9}{\sqrt{2}}$" + "\n"
        r"$\alpha_-=\langle h_-,p\rangle=-\dfrac{1}{\sqrt{2}}$",
        fontsize=11,
        va="top",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#f8fafc", edgecolor="#cbd5e1"),
    )

    fig.tight_layout()
    fig.savefig(OUT, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
