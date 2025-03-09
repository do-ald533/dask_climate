import pytest
import xarray as xr
from src.analysis import compute_trends

def test_compute_trends():
    trends = compute_trends()
    assert trends is not None, "compute_trends() returned None"
    
    mean, max_, min_ = trends
    assert isinstance(mean, xr.DataArray), "Mean temperature is not an Xarray DataArray"
    assert isinstance(max_, xr.DataArray), "Max temperature is not an Xarray DataArray"
    assert isinstance(min_, xr.DataArray), "Min temperature is not an Xarray DataArray"
    
    assert mean.values is not None, "Mean temperature values are None"
    assert max_.values is not None, "Max temperature values are None"
    assert min_.values is not None, "Min temperature values are None"
