from datetime import datetime

import websockets

from src.inc.repository import client_repository
from config import logger


class WebsocketWorker:
    @staticmethod
    async def get_message():
        pass

    @staticmethod
    async def send_message(message: str):
        for username, data in client_repository.users():
            await data[0].send(message)

    @staticmethod
    async def registration_user(username: str, ws_client_protocol: websockets.WebSocketClientProtocol):
        pass


async def working_with_client(client: websockets.WebSocketClientProtocol, path: str):
    logger.error(f"CONNECT NEW CLIENT: {client} | NOT REGISTRATION")
    websocket_worker = WebsocketWorker
    """
    Functions:
    <method> <params>
    RegNewUser username="HisName/HerName"                   # Create new user
    SendMessage message="Text message"                      # Send message on chat
    """
    message = await client.recv()
    message = message.strip().split(" ")
    if len(message) == 2:
        method, params = message
    else:
        method, params = message, "_"
    if method == "RegNewUser":
        username = params.replace("username=", "")[1:-1]
        logger.error(f"NEW USER: {username}")
        # await websocket_worker.registration_user(username=username, ws_client_protocol=client)
        # await websocket_worker.get_message()
    elif method == "SendMessage":
        message = params.replace("message=", "")[1:-1]
        await client_repository.update(ws_client_protocol=client)
        logger.error(f"{datetime.now()} | MESSAGE: {message}")
    else:
        logger.error("THIS METHOD WAS NOT FOUND")

