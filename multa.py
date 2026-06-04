def calcular_multa_com_carencia(
    dias_atraso,
    carencia,
    valor_por_dia
):

    if dias_atraso <= carencia:
        return 0.0

    return (
        dias_atraso - carencia
    ) * valor_por_dia