import pytest

from services.servico_emprestimo import (
    ServicoEmprestimo
)

from tests.fakes.fake_repositorio import (
    FakeRepositorio
)

from tests.fakes.fake_notificador import (
    FakeNotificador
)


def test_servico_recebe_repo_fake():

    # Arrange
    repo = FakeRepositorio()

    # Act
    servico = ServicoEmprestimo(
        repo,
        None
    )

    # Assert
    assert servico.repo == repo


def test_servico_recebe_notificador_fake():

    # Arrange
    repo = FakeRepositorio()

    notificador = FakeNotificador()

    # Act
    servico = ServicoEmprestimo(
        repo,
        notificador
    )

    # Assert
    assert (
        servico.notificador
        ==
        notificador
    )


def test_salvar_emprestimo():

    # Arrange
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

    # Act
    repo.salvar_emprestimo(
        emprestimo
    )

    # Assert
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

    # Arrange
    repo = FakeRepositorio()

    # Act
    equipamento = repo.buscar_equipamento(
        equipamento_id
    )

    # Assert
    assert (
        (equipamento is not None)
        ==
        resultado_esperado
    )


def test_equipamento_indisponivel():

    # Arrange
    repo = FakeRepositorio()

    # Act
    equipamento = repo.buscar_equipamento(
        2
    )

    # Assert
    assert (
        equipamento["disponivel"]
        is False
    )