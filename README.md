# Battery Aging Predictor

Hybrid physics + ML pipeline for estimating and forecasting lithium-ion battery State of Health (SOH) using a simple state-space model and Kalman Filters, with a clean path to future neural network models.

This project is a small exploration of how lithium-ion batteries lose capacity over time and how SOH (State of Health) can be estimated using a basic Kalman Filter. The goal was to build a simple, understandable baseline model before getting into more complex battery degradation or machine learning approaches.

I generated a synthetic aging curve (SOH drifting from ~1.0 to ~0.7 over several hundred cycles), added noise to mimic imperfect capacity measurements, and then used a 1-D Kalman Filter to recover a smoother estimate of the true SOH. This type of filtering is actually close to what many battery management systems do to clean up noisy measurements.

The project is intentionally lightweight just enough logic to show the idea clearly and leave room for future extensions.
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
