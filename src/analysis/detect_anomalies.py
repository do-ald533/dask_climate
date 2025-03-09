import xarray as xr
import dask.array as da
import numpy as np
from config import DATA_FILE, THRESHOLD
from logger import logger
from typing import Optional

def detect_anomalies() -> Optional[xr.DataArray]:
    try:
        logger.info("Loading dataset for anomaly detection...")
        ds = xr.open_dataset(DATA_FILE)

        if "temperature" not in ds:
            raise ValueError("Dataset does not contain 'temperature' variable.")

        temp: xr.DataArray = ds["temperature"]

        temp_dask = temp.data
        mean_temp = temp.mean(dim="time")
        std_dev = temp.std(dim="time")

        logger.info(f"Detecting anomalies using threshold: {THRESHOLD} standard deviations")

        mean_temp_dask = mean_temp.data
        std_dev_dask = std_dev.data

        anomalies = da.where((temp_dask - mean_temp_dask) > THRESHOLD * std_dev_dask, 1, 0)

        anomalies_xr = xr.DataArray(anomalies, coords=temp.coords, dims=temp.dims).compute()

        num_anomalies: int = int(np.sum(anomalies_xr.values))  
        logger.info(f"Detected {num_anomalies} anomalies.")

        return anomalies_xr

    except Exception as e:
        logger.error(f"Error in anomaly detection: {e}", exc_info=True)
        return None