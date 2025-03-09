import pytest
import xarray as xr
from src.analysis import detect_anomalies

def test_detect_anomalies():
    anomalies = detect_anomalies()
    assert anomalies is not None, "detect_anomalies() returned None"
    assert isinstance(anomalies, xr.DataArray), "Anomalies result is not an Xarray DataArray"
    assert anomalies.values is not None, "Anomaly values are None"
    assert anomalies.sum() >= 0, "Anomaly count should not be negative"
