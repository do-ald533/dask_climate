FROM python:3.11-slim

RUN pip install --no-cache-dir dask[complete] xarray pandas numpy netCDF4 scikit-learn python-dotenv

WORKDIR /app

COPY . /app

EXPOSE 8786 8787

CMD ["dask-worker", "tcp://scheduler:8786"]
