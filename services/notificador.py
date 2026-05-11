# Notificador: enviar notificações do sistema.

class Notificador:

    def notificar_emprestimo(self, email, data_devolucao):
        mensagem = f"Empréstimo registrado. Devolução: {data_devolucao}"
        self.enviar_email(mensagem)

    def notificar_atraso(self, email):
        mensagem = "Seu empréstimo está atrasado."
        self.enviar_email(mensagem)

    def enviar_email(self, mensagem):
        print(f"[EMAIL] {mensagem}")
