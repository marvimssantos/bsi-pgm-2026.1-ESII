import pytest

from models.equipamento import Notebook, Projetor


@pytest.mark.parametrize(
    "equipamento,dias,multa_esperada",
    [
        (Notebook(1, "Notebook", True), 1, 10),
        (Notebook(1, "Notebook", True), 3, 30),
        (Projetor(2, "Projetor", True), 1, 5),
        (Projetor(2, "Projetor", True), 4, 20),
    ]
)
def test_calcular_multa_atraso_positivo(
    equipamento,
    dias,
    multa_esperada
):

    # Arrange

    # Act
    multa = equipamento.calcular_multa(
        dias
    )

    # Assert
    assert multa == multa_esperada


@pytest.mark.parametrize(
    "equipamento",
    [
        Notebook(1, "Notebook", True),
        Projetor(2, "Projetor", True)
    ]
)
def test_calcular_multa_atraso_negativo_retorna_zero(
    equipamento
):

    # Arrange

    # Act
    multa = equipamento.calcular_multa(
        -5
    )

    # Assert
    assert multa == 0