from analysis.compute_trends import compute_trends
from analysis.detect_anomalies import detect_anomalies
from analysis.ml_anomaly_detection import detect_anomalies_ml
from analysis.visualize_results import visualize_results
from logger import logger
from typing import Optional
import numpy as np
import xarray as xr

def safe_sum(data: Optional[xr.DataArray]) -> int:
    if data is None:
        return 0
    return int(np.nansum(data.values))

if __name__ == "__main__":
    try:
        logger.info("Starting Climate Data Analysis Pipeline...")

        trends = compute_trends()
        if trends:
            mean, max_, min_ = trends
            logger.info(f"Mean Temp: {mean.values:.2f}°C, Max Temp: {max_.values:.2f}°C, Min Temp: {min_.values:.2f}°C")
        else:
            logger.warning("Temperature trends computation failed.")

        anomalies_stat = detect_anomalies()
        num_stat_anomalies = safe_sum(anomalies_stat)
        logger.info(f"Statistical Anomalies Detected: {num_stat_anomalies}")

        anomalies_ml = detect_anomalies_ml()
        num_ml_anomalies = safe_sum(anomalies_ml)
        logger.info(f"ML-Based Anomalies Detected: {num_ml_anomalies}")

        visualize_results()
        logger.info("Climate Data Analysis Pipeline Completed Successfully.")

    except Exception as e:
        logger.error(f"Error in Climate Data Analysis Pipeline: {e}", exc_info=True)
