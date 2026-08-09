import pytest

from models.equipamento import Cabo, Notebook, Projetor
from models.multa_strategy import MultaPorDia


@pytest.mark.parametrize(
    "equipamento,dias,esperado",
    [
        (
            Notebook(1, "Notebook", "notebook", MultaPorDia(10.0)),
            1,
            10,
        ),
        (
            Notebook(1, "Notebook", "notebook", MultaPorDia(10.0)),
            3,
            30,
        ),
        (
            Projetor(2, "Projetor", "projetor", MultaPorDia(5.0)),
            1,
            5,
        ),
        (
            Cabo(3, "Cabo", "cabo", MultaPorDia(2.0)),
            4,
            8,
        ),
    ],
)
def test_calcular_multa_atraso_positivo(
    equipamento,
    dias,
    esperado,
):
    assert equipamento.calcular_multa(dias) == esperado


@pytest.mark.parametrize(
    "equipamento",
    [
        Notebook(
            1,
            "Notebook",
            "notebook",
            MultaPorDia(10.0),
        ),
        Projetor(
            2,
            "Projetor",
            "projetor",
            MultaPorDia(5.0),
        ),
    ],
)
def test_calcular_multa_atraso_negativo_retorna_zero(
    equipamento,
):
    assert equipamento.calcular_multa(-10) == 0
