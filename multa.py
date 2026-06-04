def calcular_multa_com_carencia(
    dias_atraso,
    carencia,
    valor_por_dia
):

    dias_cobrados = dias_atraso - carencia

    if dias_cobrados <= 0:
        return 0.0

    return dias_cobrados * valor_por_dia