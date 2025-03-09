from dask.distributed import Scheduler
import asyncio
from logger import logger

async def start_scheduler():
    try:
        scheduler = Scheduler()
        await scheduler
        logger.info("Dask Scheduler started successfully.")
        await scheduler.finished()
    except Exception as e:
        logger.error(f"Scheduler encountered an error: {e}", exc_info=True)

if __name__ == "__main__":
    try:
        logger.info("Starting Dask Scheduler...")
        asyncio.run(start_scheduler())
    except KeyboardInterrupt:
        logger.warning("Dask Scheduler stopped by user.")
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
