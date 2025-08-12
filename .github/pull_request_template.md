## Summary
What does this change and why?

## Changes
- [ ] New kernel module (`hpi/kernels.py`)
- [ ] Experiment routines (`experiments/echo.py`, `double_well.py`, `interferometer.py`)
- [ ] Exports (CSVs) under `/exports`, figures under `/exports/figures`
- [ ] Docs updated (`docs/HOWTO-RUN.md`, README link)

## Testing
Reproduce locally:
python -m experiments.echo --kernel exp --M 0.05
python -m experiments.double_well --kernel exp --M 0.05 --sweep forward
python -m experiments.double_well --kernel exp --M 0.05 --sweep backward

Expected artifacts:
- exports/echo_delta_vs_M.csv, exports/figures/echo_delta_vs_M.png
- exports/dw_hysteresis.csv, exports/figures/dw_hysteresis.png

## Verification
- [ ] Effects vanish as M→0 (smoke test)
- [ ] Metadata logs (M, N, β, Ω) per run
- [ ] No API/CLI breakage

Notes:
- Merge strategy: **Create a merge commit** (no squash).
- Link issues: Closes #<id> if applicable.
