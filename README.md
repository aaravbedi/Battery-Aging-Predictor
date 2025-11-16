# Battery Aging Predictor 🔋

Hybrid physics + ML pipeline for predicting lithium-ion battery aging (state of health, SOH) using Kalman Filters and (later) neural networks.

The goal of this project is to show how you can:
- Use a simple **state-space model** and a **Kalman Filter** to track SOH over time.
- Treat SOH as a **latent state** that slowly drifts as the battery degrades.
- Build a clean, reproducible structure for future ML models (e.g. LSTMs) to predict degradation.

---

## 🔧 Project Structure

```text
battery-aging-predictor/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── kalman/
│       ├── __init__.py
│       └── soh_kalman.py
└── scripts/
    └── run_kalman_demo.py
