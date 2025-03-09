import numpy as np
import xarray as xr
import os

def generate_climate_data(file_path: str = "data/climate_data.nc") -> None:
    time = np.arange(2000, 2020, 1)
    lat = np.linspace(-90, 90, 50)
    lon = np.linspace(-180, 180, 100)

    temperature = (
        15 + 10 * np.sin(2 * np.pi * time[:, None, None] / 10) +
        np.random.normal(0, 2, (len(time), len(lat), len(lon)))
    )

    ds = xr.Dataset(
        {"temperature": (["time", "lat", "lon"], temperature)},
        coords={"time": time, "lat": lat, "lon": lon}
    )

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    ds.to_netcdf(file_path)
    print(f"Climate data generated: {file_path}")

if __name__ == "__main__":
    generate_climate_data()
