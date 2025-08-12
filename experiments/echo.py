import argparse
import csv
import os
from pathlib import Path
import math
import random

import matplotlib.pyplot as plt

from hpi.kernels import make_kernel, KernelConfig

def simulate_echo(cfg: KernelConfig, trials: int = 100):
    """
    Dummy echo simulation:
    - AB vs BA protocol.
    - Echo difference scales linearly with M (plus small noise).
    - Returns list of (M, delta_L) pairs.
    """
    kernel = make_kernel(cfg)
    results = []
    for _ in range(trials):
        # Simulate directional bias proportional to M
        delta_L = cfg.M * 0.5 + random.gauss(0, 0.02)
        results.append((cfg.M, delta_L))
    return results

def main():
    parser = argparse.ArgumentParser(description="Run Loschmidt echo AB vs BA simulation.")
    parser.add_argument("--kernel", choices=["exp", "powerlaw", "osc"], default="exp")
    parser.add_argument("--M", type=float, required=True, help="tau_mem / tau_sys")
    parser.add_argument("--N", type=float, default=0.0, help="ell_mem / L_sys")
    parser.add_argument("--beta", type=float, help="power-law index (0,1)")
    parser.add_argument("--omega", type=float, help="oscillatory frequency")
    parser.add_argument("--trials", type=int, default=100, help="number of trials")
    parser.add_argument("--out", type=str, default="exports", help="output folder")
    args = parser.parse_args()

    cfg = KernelConfig(kind=args.kernel, M=args.M, N=args.N, beta=args.beta, omega=args.omega)
    results = simulate_echo(cfg, trials=args.trials)

    # Prepare output folders
    out_dir = Path(args.out)
    fig_dir = out_dir / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    fig_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV
    csv_path = out_dir / "echo_delta_vs_M.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["M", "delta_L", "N", "beta", "omega"])
        for M, delta_L in results:
            writer.writerow([M, delta_L, args.N, args.beta, args.omega])

    # Plot
    plt.figure()
    plt.scatter([r[0] for r in results], [r[1] for r in results], alpha=0.7)
    plt.xlabel("M")
    plt.ylabel("ΔL (AB - BA)")
    plt.title(f"Echo Asymmetry vs M [{args.kernel}]")
    plt.grid(True)
    fig_path = fig_dir / "echo_delta_vs_M.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()

    print(f"Results saved to: {csv_path}")
    print(f"Figure saved to: {fig_path}")

if __name__ == "__main__":
    main()
