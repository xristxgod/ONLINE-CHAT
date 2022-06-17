import asyncio
from typing import Optional

import websockets

from src.services.worker import working_with_client
from src.settings import HOST, PORT
from config import logger


async def main():
    logger.error(f"WEBSERVER STARTED WORK\nPATH: ws://{HOST}:{PORT}")
    await websockets.serve(working_with_client, HOST, PORT)


if __name__ == '__main__':
    """ Run ws server """
    loop: Optional[asyncio.AbstractEventLoop] = None
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.run_forever()
    except Exception as error:
        logger.error(f"ERROR STEP 20: {error}")
    finally:
        if loop is not None and not loop.is_closed() or loop.is_running():
            loop.close()
