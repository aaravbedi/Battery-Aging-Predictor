import numpy as np
import matplotlib.pyplot as plt
from src.kalman.soh_kalman import SOHKalmanFilter

def generate_synthetic_data(n_cycles=800, start=1.0, end=0.7, noise=0.02):
    true_soh = np.linspace(start, end, n_cycles)
    measurements = true_soh + np.random.normal(0, noise, n_cycles)
    return true_soh, measurements

def run():
    true_soh, measurements = generate_synthetic_data()
    kf = SOHKalmanFilter()
    estimates = [kf.step(z) for z in measurements]
    plt.plot(true_soh, label='True SOH')
    plt.scatter(range(len(measurements)), measurements, s=8, label='Measurements')
    plt.plot(estimates, label='Kalman Estimate', linestyle='--')
    plt.title("Battery SOH Estimation (Kalman Filter)")
    plt.legend()
    plt.grid(True)
    plt.savefig("outputs/soh_kalman_demo.png")

if __name__ == "__main__":
    run()
