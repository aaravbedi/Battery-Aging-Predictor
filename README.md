# Battery Aging Predictor

Hybrid physics + ML pipeline for estimating and forecasting lithium-ion battery State of Health (SOH) using a simple state-space model and Kalman Filters, with a clean path to future neural network models.

This project is meant to be:
- Physics-aware – grounded in realistic battery degradation behavior  
- Statistically sound – using Kalman filtering for noisy measurements  
- ML-ready – structured so you can later plug in LSTMs / sequence models  
- Readable + teachable – something you’d actually walk a hiring manager or VC through

---

## Motivation

Battery aging is messy:

- SOH doesn’t drop in a straight line  
- Different usage profiles (C-rate, depth of discharge, temperature, voltage window) age cells differently  
- Real measurements (capacity, voltage, current) are noisy and incomplete  

Before you throw deep learning at the problem, you need a **good estimator** that can:

- Track SOH as a **latent state**  
- Handle noise gracefully  
- Update online as new data comes in  

This repo does exactly that with a minimal, transparent implementation of a **1D Kalman Filter for SOH**.

---

## What This Repo Currently Does

✅ **1. Synthetic battery aging profile**

- Simulates SOH drifting from ~1.0 → ~0.7 over a chosen number of cycles  
- Adds Gaussian noise to mimic imperfect capacity measurements  

✅ **2. Kalman Filter–based SOH estimation**

- Models SOH as a slowly-varying latent variable:
  - Process model: `x_k = x_{k-1} + w_k`  
  - Measurement model: `z_k = x_k + v_k`  
- Recovers a smooth SOH curve from noisy observations  
- Provides an estimation framework similar to what real BMS systems use

✅ **3. Visualization of results**

- Plots:
  - True (simulated) SOH  
  - Noisy measurements  
  - Kalman-estimated SOH  
- Saves the figure to `outputs/soh_kalman_demo.png`

---

## Project Structure

```text
Battery-Aging-Predictor/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── kalman/
│       ├── __init__.py
│       └── soh_kalman.py
└── scripts/
    └── run_kalman_demo.py
