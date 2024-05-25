from dataclasses import dataclass
from datetime import datetime
from core.entities.entity import Entity


@dataclass
class Noticia(Entity):
    title: str = None
    content: str = None
    img: str = None
    created_at: datetime = None
