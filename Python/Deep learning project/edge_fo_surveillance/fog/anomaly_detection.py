import numpy as np
from collections import deque

WINDOW_SIZE = 10
ANOMALY_THRESHOLD = 1.5

class TemporalAnomalyDetector:
    def __init__(self):
        self.feature_window = deque(maxlen=WINDOW_SIZE)

    def extract_feature(self, detections):
        return len(detections)

    def detect_anomaly(self, detections):
        feature = self.extract_feature(detections)
        self.feature_window.append(feature)

        if len(self.feature_window) < WINDOW_SIZE:
            return False

        mean = np.mean(self.feature_window)
        std = np.std(self.feature_window)

        if std == 0:
            return False

        z_score = abs(feature - mean) / std
        return z_score > ANOMALY_THRESHOLD
