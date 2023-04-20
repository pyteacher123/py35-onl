from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import DBGatewayProtocol


class BaseDAO:
    def __init__(self, db_gateway: DBGatewayProtocol) -> None:
        self._db_gateway = db_gateway
