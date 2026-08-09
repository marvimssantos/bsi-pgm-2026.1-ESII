from tests.fakes.fake_notificador import FakeNotificador
from tests.fakes.fake_repositorio import FakeRepositorio


def test_integracao_servico_repo_notificador():

    # Arrange
    repo = FakeRepositorio()

    notificador = FakeNotificador()

    emprestimo = {
        "id": 1,
        "usuario": "Marcos"
    }

    # Act
    repo.salvar_emprestimo(
        emprestimo
    )

    notificador.enviar_email(
        "teste@email.com",
        "Empréstimo realizado"
    )

    # Assert
    assert len(
        repo.emprestimos
    ) == 1

    assert len(
        notificador.mensagens
    ) == 1
