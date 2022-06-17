import uuid
from datetime import datetime
from typing import Optional, Tuple, Dict

from websockets import WebSocketClientProtocol

from src.inc.base_classes import BaseController, BaseControllerCRUD


class ClientRepository(BaseControllerCRUD):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClientRepository, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # {"username": (WebSocketClientProtocol, lastActive)}
        self.users: Dict = {}

    async def create(self, username: str, ws_client_protocol: WebSocketClientProtocol) -> bool:
        if username not in list(self.users.keys()) and ws_client_protocol not in list(self.users.values()):
            self.users.update({username: (
                ws_client_protocol, int(datetime.timestamp(datetime.now()))
            )})
        elif username in list(self.users.keys()) and ws_client_protocol not in list(self.users.values()):
            self.users.update({username+f"@{uuid.uuid4().hex[:5]}": (
                ws_client_protocol, int(datetime.timestamp(datetime.now()))
            )})
        elif username not in list(self.users.keys()) and ws_client_protocol in list(self.users.values()):
            for _username, data in self.users.items():
                if data[0] == ws_client_protocol:
                    self.users.pop(_username)
                    self.users.update({username: (
                        ws_client_protocol, int(datetime.timestamp(datetime.now()))
                    )})
                    break
        else:
            if self.users.get(username) != ws_client_protocol:
                for _username, data in self.users.items():
                    if data[0] == ws_client_protocol:
                        self.users.pop(_username)
                        self.users.update({username+f"@{uuid.uuid4().hex[:5]}": (
                            ws_client_protocol, int(datetime.timestamp(datetime.now()))
                        )})
                        break
        return True

    async def get(self, ws_client_protocol: WebSocketClientProtocol) -> Optional[Tuple[str, WebSocketClientProtocol]]:
        for _username, data in self.users.items():
            if data[0] == ws_client_protocol:
                return _username, data[0]
        else:
            return None

    async def update(self, ws_client_protocol: WebSocketClientProtocol) -> bool:
        for _username, data in self.users.items():
            if data[0] == ws_client_protocol:
                self.users.get(_username)[1] = int(datetime.timestamp(datetime.now()))
                return True
        else:
            return False

    async def delete(self, ws_client_protocol: WebSocketClientProtocol) -> bool:
        for _username, data in self.users.items():
            if data[0] == ws_client_protocol:
                self.users.pop(_username)
                break
        return True


class MessageContainer(BaseController):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MessageContainer, cls).__new__(cls)
        return cls.instance


client_repository = ClientRepository()
