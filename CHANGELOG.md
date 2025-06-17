# Hidden Plinko Interpretation - Changelog

All notable changes to this project are documented in this file.
## [v1.1.1] - 2025-06-16
### Added
- Section 4.6.2: Introduced Informational Torsion as a smooth, rotational deformation mode in the informational substrate
- Section 4.10: Developed the Interface Manifold framework with tomographic projection of interference patterns
- README.md: Fully rewritten to reflect theoretical and experimental progress in v1.1, including:
- New project summary and install instructions
- Summary of theory updates and simulation architecture
- Embedded paper link and citation guidance
- RELEASE_NOTES folder added
- RELEASE_NOTES_v1.1.1.md created to document updates

### Changed
- Manuscript finalized with torsion and manifold additions for public release
- README clarified and aligned with experimental and theoretical advances
- CHANGELOG.md: This versioned changelog file updated for transparent development history
- RELEASE_NOTES_v1.1.md moved to RELEASE_NOTES folder


## [v1.1] - 2025-05-07
### Added
- New experimental batch: `zoomed_batch.csv` exploring parameter sweeps with finer resolution
- Entropy overlays and analysis for dynamic field variations
- Identification and visualization of harmonic structures across parameter space
- 3D surface plots showing collapse strength and final position mapping
- Drift force interpretation formalized in the paper
- Phase zone detection in low-entropy dynamic field configurations
- Introduced the `upload_format/` folder:
  - Includes clean upload templates and example experiments
  - Shows valid parameter ranges and all supported `Symmetry_Type` options
  - Users can now build experiments directly from this folder using the documented format
  - ChatGPT can generate valid experiments with your parameters programmatically based on these formats

### Changed
- Updated `Hidden_Plinko_Interpretation.pdf` with new figures and experimental interpretations
- Expanded mathematical formalism: entropy dynamics, Fokker-Planck analogy, and substrate drift models
- Improved figure captions and alignment between paper and simulator results

### Fixed
- Clarified parameter labels in export CSVs
- Corrected mismatch between batch input and export naming for new sweeps

---

## [v1.0] - 2025-05-01
### Added
- Initial draft of `Hidden_Plinko_Interpretation.pdf`
- One-page overview summary
- Full experimental simulator notebook
- Initial batch experiments and export results
- Reproducible figures demonstrating entropy collapse and symmetry-driven behavior

---
### Added (continued)
- Collapse Landscape Sweep: detailed batch exploring symmetry collapse topology
- Galaxy rotation analogs and spiral formation experiments
- Oscillating field effects including FFT-based resonance detection
- Final export bundle with curated and batch datasets

### Changed (continued)
- Updated README to reflect v1.1 features and paper versioning
- Bundled GitHub release with Zenodo support and experimental index
