# Equipamento: representar um equipamento do sistema.
from dataclasses import dataclass

@dataclass
class Equipamento:
    id: int
    nome: str
    disponivel: bool
