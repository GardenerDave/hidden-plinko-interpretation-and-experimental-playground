# =============================================================================
# NOTE: Placeholder / toy model for development
# This script is for verifying the Λ(x,t) experiment pipeline (CLI, exports, plotting).
# Replace `sweep_rates` internals with actual Λ(x,t) simulation logic for publication.
# =============================================================================
import argparse
import csv
from pathlib import Path
import math
import random

import matplotlib.pyplot as plt

from hpi.kernels import make_kernel, KernelConfig

def sweep_rates(cfg: KernelConfig, phase_steps: int, direction: str, noise=0.02):
    """
    Simulate Kramers-like escape rates under a periodic drive phase.
    Λ-effect: hysteresis term ~ M * dS/dt; here we model dS/dt ~ sin(phi).
    Forward/backward sweeps should differ by a lobe whose amplitude ~ M.
    """
    kernel = make_kernel(cfg)  # not used explicitly in this toy model, but keeps API aligned
    phases = [2.0 * math.pi * k / phase_steps for k in range(phase_steps)]
    if direction == "backward":
        phases = list(reversed(phases))

    rates = []
    for phi in phases:
        # baseline activation rate (positive) with small harmonic structure
        baseline = 0.2 + 0.05 * (1 + math.cos(phi))
        # Λ-asymmetry: sign flips with sweep direction; magnitude ~ M * dS/dt
        sdot = math.sin(phi)  # proxy for dS/dt
        asym = cfg.M * 0.15 * sdot * (1 if direction == "forward" else -1)
        # add small noise; keep positive
        k = max(1e-6, baseline + asym + random.gauss(0, noise))
        rates.append((phi, k))
    return rates

def main():
    ap = argparse.ArgumentParser(description="Double-well escape hysteresis sweep")
    ap.add_argument("--kernel", choices=["exp", "powerlaw", "osc"], default="exp")
    ap.add_argument("--M", type=float, required=True)
    ap.add_argument("--N", type=float, default=0.0)
    ap.add_argument("--beta", type=float)
    ap.add_argument("--omega", type=float)
    ap.add_argument("--phase-steps", type=int, default=64)
    ap.add_argument("--out", type=str, default="exports")
    ap.add_argument("--noise", type=float, default=0.02)
    args = ap.parse_args()

    cfg = KernelConfig(kind=args.kernel, M=args.M, N=args.N, beta=args.beta, omega=args.omega)

    fwd = sweep_rates(cfg, args.phase_steps, "forward", noise=args.noise)
    bwd = sweep_rates(cfg, args.phase_steps, "backward", noise=args.noise)

    out_dir = Path(args.out); fig_dir = out_dir / "figures"
    out_dir.mkdir(parents=True, exist_ok=True); fig_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV (merged forward/backward with same phase indexing)
    csv_path = out_dir / f"dw_hysteresis_M{args.M:.3f}.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["phase_rad", "k_forward", "k_backward", "M", "N", "beta", "omega"])
        for (phi_f, kf), (phi_b, kb) in zip(fwd, bwd):
            # use forward phase as reference; bwd has reversed order by construction
            w.writerow([phi_f, kf, kb, args.M, args.N, args.beta, args.omega])

    # Plot lobe: Δk = k_forward - k_backward vs phase
    phases = [p for p, _ in fwd]
    delta = [kf - kb for (_, kf), (_, kb) in zip(fwd, bwd)]

    plt.figure()
    plt.plot(phases, delta, marker="o", linestyle="none", alpha=0.7)
    plt.xlabel("Phase (rad)")
    plt.ylabel("Δk = k_forward - k_backward")
    plt.title(f"Double-well hysteresis lobe vs phase [M={args.M}]")
    plt.grid(True)
    fig_path = fig_dir / f"dw_hysteresis_M{args.M:.3f}.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()

    print(f"Saved CSV:   {csv_path}")
    print(f"Saved figure:{fig_path}")

if __name__ == "__main__":
    main()
