import pytest

from tests.fakes.fake_repositorio import FakeRepositorio
from tests.fakes.fake_notificador import FakeNotificador
from services.servico_emprestimo import ServicoEmprestimo


@pytest.fixture
def repositorio_fake():
    return FakeRepositorio()


@pytest.fixture
def notificador_fake():
    return FakeNotificador()


@pytest.fixture
def servico(
    repositorio_fake,
    notificador_fake
):
    return ServicoEmprestimo(
        repositorio_fake,
        notificador_fake
    )