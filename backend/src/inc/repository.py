import uuid
from typing import Optional, Tuple, Dict

from websockets import WebSocketClientProtocol


class ClientRepository:

    def __init__(self):
        # {"username": WebSocketClientProtocol}
        self.users: Dict[str, WebSocketClientProtocol] = {}

    def set_client(self, username: str, ws_client_protocol: WebSocketClientProtocol) -> bool:
        if username not in list(self.users.keys()) and ws_client_protocol not in list(self.users.values()):
            self.users.update({username: ws_client_protocol})
        elif username in list(self.users.keys()) and ws_client_protocol not in list(self.users.values()):
            self.users.update({username+f"@{uuid.uuid4().hex[:5]}": ws_client_protocol})
        elif username not in list(self.users.keys()) and ws_client_protocol in list(self.users.values()):
            for _username, _ws_protocol in self.users.items():
                if _ws_protocol == ws_client_protocol:
                    self.users.pop(_username)
                    self.users.update({username: ws_client_protocol})
                    break
        else:
            if self.users.get(username) != ws_client_protocol:
                for _username, _ws_protocol in self.users.items():
                    if _ws_protocol == ws_client_protocol:
                        self.users.pop(_username)
                        self.users.update({username+f"@{uuid.uuid4().hex[:5]}": ws_client_protocol})
                        break
        return True

    def get_client(self, ws_client_protocol: WebSocketClientProtocol) -> Optional[Tuple[str, WebSocketClientProtocol]]:
        for _username, _ws_protocol in self.users.items():
            if _ws_protocol == ws_client_protocol:
                return _username, _ws_protocol
        else:
            return None

class MessageContainer:
    pass


client_repository = ClientRepository()
