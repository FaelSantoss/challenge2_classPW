from dataclasses import dataclass

from core.entities.entity import Entity


@dataclass
class Noticia(Entity):
    title: str = None
    cotent: str = None
    img: str = None
