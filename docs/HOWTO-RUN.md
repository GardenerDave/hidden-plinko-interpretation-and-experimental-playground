# HOWTO-RUN: Λ(x,t) Kernels & Protocols

## Install
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt

## Echo asymmetry (AB vs BA)
python -m experiments.echo --kernel exp --M 0.02 --N 0.0 --trials 200 --out exports

Artifacts:
- exports/echo_delta_vs_M.csv
- exports/figures/echo_delta_vs_M.png

## Double-well escape hysteresis
python -m experiments.double_well --kernel exp --M 0.05 --phase-steps 64 --sweep forward --out exports
python -m experiments.double_well --kernel exp --M 0.05 --phase-steps 64 --sweep backward --out exports

Artifacts:
- exports/dw_hysteresis.csv
- exports/figures/dw_hysteresis.png

## History-loaded interferometer (surrogate)
python -m experiments.interferometer --kernel exp --M 0.03 --preload 0.2 --out exports

Artifacts:
- exports/interference_visibility.csv
- exports/figures/interference_visibility.png

## Notes
- Effects should → 0 as `--M 0.0`.
- Each run logs `(M, N, β, Ω)` in CSV headers.
## Echo Asymmetry (AB vs BA Simulation)
Simulates a Loschmidt echo with two protocol orderings (AB vs BA) using the Λ(x,t) kernel module.

Run example:
python -m experiments.echo --kernel exp --M 0.02 --N 0.0 --trials 200 --out exports

Artifacts generated:
- exports/echo_delta_vs_M.csv
- exports/figures/echo_delta_vs_M.png

Notes:
- Change `--M` to test different memory numbers (e.g., 0.0, 0.05, 0.1).
- All runs log (M, N, β, Ω) in the CSV header.
- Effects should → 0 as M→0.
