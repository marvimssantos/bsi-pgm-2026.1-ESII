# ServicoEmprestimo: controlar regras de empréstimo.

from datetime import date, timedelta

from models.emprestimo import Emprestimo
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador


class ServicoEmprestimo:

    def __init__(self):
        self.repo = RepositorioEmprestimo()
        self.notificador = Notificador()

    def registrar(self, equip_id, nome, email, dias):

        equipamento = self.repo.buscar_equipamento(equip_id)

        if equipamento is None:
            return False

        if not equipamento.disponivel:
            return False

        devolucao = date.today() + timedelta(days=dias)

        emprestimo = Emprestimo(
            id=len(self.repo.emprestimos) + 1,
            equipamento_id=equip_id,
            nome_usuario=nome,
            email=email,
            data_devolucao=devolucao,
            devolvido=False
        )

        self.repo.salvar_emprestimo(emprestimo)
        self.repo.marcar_indisponivel(equip_id)

        self.notificador.notificar_emprestimo(email, devolucao)

        return True

    def registrar_devolucao(self, id):

        for emprestimo in self.repo.buscar_emprestimos():

            if emprestimo.id == id:

                emprestimo.devolvido = True

                self.repo.marcar_disponivel(
                    emprestimo.equipamento_id
                )

                return True

        return False

    def calcular_multa(self, emprestimo):

        equipamento = self.repo.buscar_equipamento(
            emprestimo.equipamento_id
        )

        dias_atraso = (
            date.today() - emprestimo.data_devolucao
        ).days

        return equipamento.calcular_multa(
            dias_atraso
        )

    def listar_atrasados(self):

        atrasados = []

        for emprestimo in self.repo.buscar_emprestimos():

            if (
                emprestimo.data_devolucao < date.today()
                and not emprestimo.devolvido
            ):

                emprestimo.multa = self.calcular_multa(
                    emprestimo
                )

                atrasados.append(emprestimo)

                self.notificador.notificar_atraso(
                    emprestimo.email
                )

        return atrasados
