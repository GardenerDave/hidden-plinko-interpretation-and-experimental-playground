

Inspired by the classical Galton board and the [Plinko game on Wikipedia](https://en.wikipedia.org/wiki/Plinko_(pricing_game)), popularized by [The Price Is Right](https://priceisright.fandom.com/wiki/Plinko/Gallery).

📄 [Read the formal paper](Hidden_Plinko_Interpretation_v1.1.pdf)
# Hidden Plinko Interpretation and Experimental Playground

**Created by: Gardener Dave**  
**License: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**

---

## Project Summary

Hidden Plinko is a dynamic simulation and conceptual model designed to explore the possibility that the probabilistic nature of quantum mechanics may be an emergent phenomenon — not fundamental randomness.

By simulating particle-like objects ("pucks") falling through complex, dynamic hidden structures, users can experiment with:

- Hidden biases
- External fields
- Dynamic environmental evolution
- Subtle deterministic effects producing probabilistic-looking distributions

This playground allows independent exploration of how *deterministic rules + complex hidden variables* can yield statistical behaviors.

---

## Key Features

- Adjustable hidden symmetry structures (rotational, elliptical, spoked, randomized, mirrored)
- External field influence simulation
- Dynamic evolution of hidden variables during the puck's journey
- Batch experiment logging and export capabilities
- Comparison tools for analyzing different experimental runs
- Completely open-source, modifiable, and extensible

---

## Installation & Running

This project runs entirely in a Jupyter Notebook. To install the necessary Python libraries, run:

```bash
pip install -r requirements.txt
```

---
Installation & Launch Instructions
1. Install Python
    Make sure you have Python 3.8 or later installed. You can download it from https://python.org.

    We recommend using a virtual environment:
       python -m venv plinko-env
        source plinko-env/bin/activate  # or plinko-env\Scripts\activate on Windows
2. Install Required Packages
    From the root of the repository, run:
        pip install -r requirements.txt

    This installs all dependencies for running the Hidden Plinko Playground notebook.

3. Launch the Notebook
    Start Jupyter Notebook or Jupyter Lab:
       jupyter notebook

    Then open:
        Hidden Plinko Interpretation and Experimental Playground V1.1.ipynb

4. Running Simulations
    You can:

        Upload your own experiment config CSV

        Run batch simulations

        Visualize particle behavior and distribution

        Export results for formal analysis

        Everything runs fully offline, and no data leaves your computer.
---

## Dependencies

This project requires:
- Python 3.8+
- Jupyter Notebook or JupyterLab
- NumPy
- matplotlib
- pandas
- ipywidgets

---

## Citation

If you use this work, please cite:

> Dave, Gardener. *Hidden Plinko Interpretation: A Deterministic Substrate Model for Emergent Quantum Statistics*. 2025. [arXiv link if available].

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.  
You are free to share and adapt the material for non-commercial purposes, as long as appropriate credit is given.



---

## Version 1.1 Update Highlights

- Added entropy analysis and tipping point experiments
- Explored harmonic structures and collapse bifurcations
- Integrated 1000+ experimental outputs and summaries
- Updated manuscript and reorganized exports
- Prepared GitHub-ready structure with Zenodo metadata
