from dask.distributed import Worker
import asyncio
import os
from config import DASK_SCHEDULER
from logger import logger

async def start_worker():
    try:
        logger.info(f"Starting Dask Worker, connecting to {DASK_SCHEDULER}...")
        worker = await Worker(DASK_SCHEDULER, nthreads=os.cpu_count())
        logger.info(f"Dask Worker connected to {DASK_SCHEDULER}.")
        await worker.finished()
    except Exception as e:
        logger.error(f"Worker encountered an error: {e}", exc_info=True)

if __name__ == "__main__":
    try:
        logger.info("Initializing worker process...")
        asyncio.run(start_worker())
    except KeyboardInterrupt:
        logger.warning("Dask Worker stopped by user.")
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
