from models.equipamento import (
    Equipamento,
    Notebook,
    Projetor,
    Cabo
)


class FabricaEquipamento:

    _registro = {
        "notebook": Notebook,
        "projetor": Projetor,
        "cabo": Cabo
    }

    @classmethod
    def criar(
        cls,
        tipo,
        id,
        nome
    ) -> Equipamento:

        classe = (
            cls._registro.get(
                tipo
            )
        )

        if classe is None:

            raise ValueError(
                f"Tipo desconhecido: {tipo}"
            )

        return classe(
            id=id,
            nome=nome
        )