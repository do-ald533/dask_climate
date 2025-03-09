import matplotlib.pyplot as plt
import xarray as xr
from config import DATA_FILE
from ..logger import logger
def visualize_results() -> None:
    try:
        logger.info("Loading dataset for visualization...")
        ds = xr.open_dataset(DATA_FILE)
        
        if "temperature" not in ds:
            raise ValueError("Dataset does not contain 'temperature' variable.")
        
        temp = ds["temperature"].mean(dim=["lat", "lon"])

        if "time" not in temp.dims:
            raise ValueError("Temperature data does not have a 'time' dimension.")

        logger.info("Generating temperature trend plot...")
        plt.figure(figsize=(12, 6))
        temp.plot.line(x="time", label="Mean Temperature")
        plt.title("Global Mean Temperature Over Time")
        plt.xlabel("Year")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.grid()
        plt.show()
        logger.info("Visualization complete.")

    except Exception as e:
        logger.error(f"Error in visualization: {e}", exc_info=True)

