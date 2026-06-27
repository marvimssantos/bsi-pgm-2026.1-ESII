# ServicoEmprestimo: controlar regras de empréstimo.

from datetime import (
    date,
    timedelta
)

from models.emprestimo import (
    Emprestimo
)

from models.evento import (
    Evento
)

from repositories.interfaces import (
    IRepositorioEmprestimo
)

from services.interfaces import (
    INotificador
)

from multa import (
    calcular_multa_com_carencia
)


class ServicoEmprestimo:

    def __init__(
        self,
        repositorio: IRepositorioEmprestimo,
        notificador: INotificador
    ):

        self.repo = repositorio
        self.notificador = notificador
        self.observers = []

    def adicionar_observer(
        self,
        observer
    ):

        self.observers.append(
            observer
        )

    def emitir_evento(
        self,
        email,
        mensagem
    ):

        evento = Evento(
            email=email,
            mensagem=mensagem
        )

        for observer in self.observers:

            observer.atualizar(
                evento
            )

    def criar_emprestimo(
        self,
        equip_id,
        nome,
        email,
        devolucao
    ):

        return Emprestimo(
            id=(
                len(
                    self.repo.emprestimos
                ) + 1
            ),
            equipamento_id=equip_id,
            nome_usuario=nome,
            email=email,
            data_devolucao=devolucao,
            devolvido=False
        )

    def registrar(
        self,
        equip_id,
        nome,
        email,
        dias
    ):

        equipamento = (
            self.repo.buscar_equipamento(
                equip_id
            )
        )

        if (
            equipamento is None
            or not equipamento.disponivel
        ):
            return False

        devolucao = (
            date.today()
            + timedelta(days=dias)
        )

        emprestimo = (
            self.criar_emprestimo(
                equip_id,
                nome,
                email,
                devolucao
            )
        )

        self.repo.salvar_emprestimo(
            emprestimo
        )

        self.repo.marcar_indisponivel(
            equip_id
        )

        self.notificador.notificar_emprestimo(
            email,
            devolucao
        )

        self.emitir_evento(
            email,
            "Empréstimo registrado"
        )

        return True

    def registrar_devolucao(
        self,
        id
    ):

        for emprestimo in (
            self.repo.buscar_emprestimos()
        ):

            if (
                emprestimo.id
                == id
            ):

                emprestimo.devolvido = True

                self.repo.marcar_disponivel(
                    emprestimo.equipamento_id
                )

                return True

        return False

    def calcular_multa(
        self,
        emprestimo
    ):

        dias_atraso = (
            date.today()
            - emprestimo.data_devolucao
        ).days

        return (
            calcular_multa_com_carencia(
                dias_atraso=dias_atraso,
                carencia=3,
                valor_por_dia=10
            )
        )

    def listar_atrasados(self):

        emprestimos_atrasados = []

        for emprestimo in (
            self.repo.buscar_emprestimos()
        ):

            if (
                emprestimo.data_devolucao
                < date.today()
                and not emprestimo.devolvido
            ):

                emprestimo.multa = (
                    self.calcular_multa(
                        emprestimo
                    )
                )

                emprestimos_atrasados.append(
                    emprestimo
                )

                self.notificador.notificar_atraso(
                    emprestimo.email
                )

                self.emitir_evento(
                    emprestimo.email,
                    "Empréstimo atrasado"
                )

        return emprestimos_atrasados