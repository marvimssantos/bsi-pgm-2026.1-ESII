from multa import (
    calcular_multa_com_carencia
)


def test_multa_zero_quando_sem_atraso():

    # Arrange
    dias_atraso = 0

    # Act
    multa = calcular_multa_com_carencia(
        dias_atraso,
        carencia=2,
        valor_por_dia=10
    )

    # Assert
    assert multa == 0.0