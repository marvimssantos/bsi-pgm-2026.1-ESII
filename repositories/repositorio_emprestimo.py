from models.fabrica_equipamento import (
    FabricaEquipamento
)

from repositories.interfaces import (
    IRepositorioEmprestimo
)


class RepositorioEmprestimo(
    IRepositorioEmprestimo
):

    def __init__(self):

        criar = (
            FabricaEquipamento.criar
        )

        self._equipamentos = [

            criar(
                "notebook",
                1,
                "Notebook Dell"
            ),

            criar(
                "projetor",
                2,
                "Projetor Epson"
            ),

            criar(
                "cabo",
                3,
                "Cabo HDMI"
            )
        ]

        self._emprestimos = []

    @property
    def emprestimos(
        self
    ):

        return (
            self._emprestimos
        )

    def buscar_equipamento(
        self,
        id
    ):

        for e in (
            self._equipamentos
        ):

            if e.id == id:
                return e

        return None

    def buscar_emprestimos(
        self
    ):

        return (
            self._emprestimos
        )

    def salvar_emprestimo(
        self,
        emprestimo
    ):

        self._emprestimos.append(
            emprestimo
        )

    def marcar_indisponivel(
        self,
        id
    ):

        equipamento = (
            self.buscar_equipamento(
                id
            )
        )

        if equipamento:

            equipamento.disponivel = False

    def marcar_disponivel(
        self,
        id
    ):

        equipamento = (
            self.buscar_equipamento(
                id
            )
        )

        if equipamento:

            equipamento.disponivel = True