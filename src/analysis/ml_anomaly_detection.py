import xarray as xr
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer
from config import DATA_FILE
from ..logger import logger
from typing import Optional

def detect_anomalies_ml() -> Optional[xr.DataArray]:
    try:
        logger.info("Loading dataset for ML-based anomaly detection...")
        ds = xr.open_dataset(DATA_FILE)

        if "temperature" not in ds:
            raise ValueError("Dataset does not contain 'temperature' variable.")

        temp: xr.DataArray = ds["temperature"]

        temp_values: np.ndarray = temp.values.reshape(-1, 1)

        imputer = SimpleImputer(strategy="mean")
        temp_values = imputer.fit_transform(temp_values)

        logger.info("Training Isolation Forest model for anomaly detection...")
        model = IsolationForest(contamination=0.05, random_state=42, n_jobs=-1)
        anomalies: np.ndarray = model.fit_predict(temp_values)

        anomaly_map = anomalies.reshape(temp.shape)
        anomalies_xr = xr.DataArray(anomaly_map, coords=temp.coords, dims=temp.dims)

        num_anomalies = np.sum(anomalies == -1)
        logger.info(f"ML-based anomaly detection complete. {num_anomalies} anomalies found.")

        return anomalies_xr

    except Exception as e:
        logger.error(f"Error in ML anomaly detection: {e}", exc_info=True)
        return None
