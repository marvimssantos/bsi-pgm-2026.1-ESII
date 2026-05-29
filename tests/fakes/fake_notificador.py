class FakeNotificador:

    def __init__(self):

        self.mensagens = []

    def enviar_email(
        self,
        email,
        mensagem
    ):

        self.mensagens.append(
            (
                email,
                mensagem
            )
        )