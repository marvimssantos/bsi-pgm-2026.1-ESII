from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def atualizar(self, email, mensagem):
        pass


class NotificadorEmail(Observer):

    def atualizar(
        self,
        email,
        mensagem
    ):

        print(
            f"[EMAIL] {email}: {mensagem}"
        )