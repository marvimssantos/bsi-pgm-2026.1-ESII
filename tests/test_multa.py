from multa import calcular_multa_com_carencia


def test_multa_zero_quando_sem_atraso():

    resultado = calcular_multa_com_carencia(
        dias_atraso=0,
        carencia=3,
        valor_por_dia=10
    )

    assert resultado == 0.0


def test_multa_apos_carencia():

    resultado = calcular_multa_com_carencia(
        dias_atraso=5,
        carencia=3,
        valor_por_dia=10
    )

    assert resultado == 20.0


def test_multa_nunca_negativa():

    resultado = calcular_multa_com_carencia(
        dias_atraso=-2,
        carencia=3,
        valor_por_dia=10
    )

    assert resultado == 0.0