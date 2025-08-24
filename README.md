# AI-Enabled & Quantum-Resilient Cybersecurity (6G + DT) — Artifacts

Reproducible artifacts for the IEEE Communications Magazine article:
**“AI-Enabled and Quantum-Resilient Cybersecurity with Digital Twin Validation for 6G-Assisted Smart Grids.”**

## What's here
- `/scripts/`: plotting scripts to regenerate Figs. 3–4.
- `/figures/`: final PNG (and optional PDF) figures.
- `/dt-templates/`: co-simulation (DT) templates + instructions.
- `/data-synth/`: synthetic/anonymized traces (no operational data).
- `/latex/`: LaTeX source of the paper.
- `LICENSE` (MIT for code), `assets/LICENSE-CC-BY-4.0.txt` (CC BY 4.0 for figures/templates).

## Reproduce Figs. 3–4
```bash
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/plot_roc.py
python scripts/plot_deadline.py
```

## Citation
Please cite the archived release via Zenodo DOI (badge below) or see `CITATION.cff`.
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.TBD.svg)](https://doi.org/10.5281/zenodo.TBD)

---
This repository: https://github.com/YassirALKarawi/6G-DT-PQC-SmartGrid