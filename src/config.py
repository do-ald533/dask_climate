import os
from dotenv import load_dotenv

load_dotenv()

DATA_FILE = os.getenv("DATA_FILE", "data/climate_data.nc")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
THRESHOLD = float(os.getenv("THRESHOLD", 5.0))
DASK_SCHEDULER = os.getenv("DASK_SCHEDULER", "tcp://scheduler:8786")
