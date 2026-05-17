# Equipamento: representar equipamentos do sistema.

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Equipamento(ABC):
    id: int
    nome: str
    disponivel: bool

    @abstractmethod
    def calcular_multa(self, dias_atraso):
        pass


@dataclass
class Notebook(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 10)


@dataclass
class Projetor(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 5)
