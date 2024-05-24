from dataclasses import dataclass
from core.entities.entity import Entity
from datetime import datetime

@dataclass
class Noticia(Entity):
    title: str = None
    content: str = None
    img: str = None
    created_at: datetime = None
