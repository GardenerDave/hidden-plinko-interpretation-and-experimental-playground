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
