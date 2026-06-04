import pytest

from datetime import date, timedelta

from services.servico_emprestimo import (
    ServicoEmprestimo
)

from models.emprestimo import (
    Emprestimo
)

from tests.fakes.fake_repositorio import (
    FakeRepositorio
)

from tests.fakes.fake_notificador import (
    FakeNotificador
)


def test_servico_recebe_repo_fake():

    repo = FakeRepositorio()

    servico = ServicoEmprestimo(
        repo,
        None
    )

    assert servico.repo == repo


def test_servico_recebe_notificador_fake():

    repo = FakeRepositorio()

    notificador = FakeNotificador()

    servico = ServicoEmprestimo(
        repo,
        notificador
    )

    assert (
        servico.notificador
        ==
        notificador
    )


def test_salvar_emprestimo():

    repo = FakeRepositorio()

    notificador = FakeNotificador()

    servico = ServicoEmprestimo(
        repo,
        notificador
    )

    emprestimo = {
        "id": 1,
        "usuario": "Marcos"
    }

    repo.salvar_emprestimo(
        emprestimo
    )

    assert len(
        repo.emprestimos
    ) == 1


@pytest.mark.parametrize(
    "equipamento_id, resultado_esperado",
    [
        (1, True),
        (999, False)
    ]
)
def test_busca_parametrizada(
    equipamento_id,
    resultado_esperado
):

    repo = FakeRepositorio()

    equipamento = repo.buscar_equipamento(
        equipamento_id
    )

    assert (
        (equipamento is not None)
        ==
        resultado_esperado
    )


def test_equipamento_indisponivel():

    repo = FakeRepositorio()

    equipamento = repo.buscar_equipamento(
        2
    )

    assert (
        equipamento["disponivel"]
        is False
    )


def test_calcular_multa_do_servico_aplica_carencia():

    repo = FakeRepositorio()

    notificador = FakeNotificador()

    servico = ServicoEmprestimo(
        repo,
        notificador
    )

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        nome_usuario="Marcos",
        email="marcos@email.com",
        data_devolucao=date.today() - timedelta(days=5),
        devolvido=False
    )

    multa = servico.calcular_multa(
        emprestimo
    )

    assert multa == 20