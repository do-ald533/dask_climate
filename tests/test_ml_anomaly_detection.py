import pytest
import xarray as xr
from analysis.ml_anomaly_detection import detect_anomalies_ml

def test_ml_anomaly_detection():
    anomalies_ml = detect_anomalies_ml()
    assert anomalies_ml is not None, "detect_anomalies_ml() returned None"
    assert isinstance(anomalies_ml, xr.DataArray), "ML Anomalies result is not an Xarray DataArray"
    assert anomalies_ml.values is not None, "ML Anomaly values are None"
    assert anomalies_ml.sum() >= 0, "ML Anomaly count should not be negative"
