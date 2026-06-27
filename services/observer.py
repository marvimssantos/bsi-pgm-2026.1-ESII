from abc import ABC, abstractmethod

from models.evento import Evento


class Observer(ABC):

    @abstractmethod
    def atualizar(
        self,
        evento: Evento
    ):
        pass


class NotificadorEmail(Observer):

    def atualizar(
        self,
        evento: Evento
    ):

        print(
            f"[EMAIL] "
            f"{evento.email}: "
            f"{evento.mensagem}"
        )