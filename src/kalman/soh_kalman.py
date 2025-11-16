import numpy as np

class SOHKalmanFilter:
    def __init__(self, x0=1.0, P0=1e-3, Q=1e-6, R=1e-3):
        """
        x0 : Initial SOH estimate (1.0 = 100%)
        P0 : Initial covariance
        Q  : Process noise (SOH drift)
        R  : Measurement noise
        """
        self.x = x0
        self.P = P0
        self.Q = Q
        self.R = R

    def predict(self):
        self.P = self.P + self.Q

    def update(self, z):
        y = z - self.x        
        S = self.P + self.R    
        K = self.P / S        

        self.x = self.x + K * y     
        self.P = (1 - K) * self.P     

    def step(self, z):
        self.predict()
        self.update(z)
        return self.x
