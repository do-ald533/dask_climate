import xarray as xr
import numpy as np
from config import DATA_FILE
from ..logger import logger
from typing import Tuple

def compute_trends() -> Tuple[xr.DataArray, xr.DataArray, xr.DataArray]:
    try:
        logger.info("Loading dataset for temperature trend analysis...")
        ds = xr.open_dataset(DATA_FILE)

        if "temperature" not in ds:
            raise ValueError("Dataset does not contain 'temperature' variable.")

        temp: xr.DataArray = ds["temperature"]

        temp = temp.fillna(temp.mean())  

        logger.info("Computing temperature statistics...")
        mean_temp = temp.mean(dim="time").compute()
        max_temp = temp.max(dim="time").compute()
        min_temp = temp.min(dim="time").compute()

        logger.info(
            f"Computed Trends - Mean: {mean_temp.values:.2f}°C, "
            f"Max: {max_temp.values:.2f}°C, Min: {min_temp.values:.2f}°C"
        )

        return mean_temp, max_temp, min_temp

    except Exception as e:
        logger.error(f"Error in computing temperature trends: {e}", exc_info=True)
        raise
