from typing import Optional, Tuple, Any


class BaseController:

    async def create(self, **kwargs: Any) -> bool:
        raise NotImplementedError

    async def get(self, **kwargs: Any) -> Optional[Tuple]:
        raise NotImplementedError

    async def delete(self, **kwargs: Any) -> bool:
        raise NotImplementedError


class BaseControllerCRUD(BaseController):
    async def update(self, **kwargs) -> bool:
        raise NotImplementedError
