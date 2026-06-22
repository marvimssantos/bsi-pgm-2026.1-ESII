from models.equipamento import Notebook, Projetor, Cabo
from models.multa_strategy import MultaPorDia


class FabricaEquipamento:

    _config = {
        "notebook": (Notebook, MultaPorDia(10.0)),
        "projetor": (Projetor, MultaPorDia(5.0)),
        "cabo": (Cabo, MultaPorDia(2.0)),
    }

    @classmethod
    def criar(cls, tipo, id, nome):

        if tipo not in cls._config:
            raise ValueError("Tipo inválido")

        classe, estrategia = cls._config[tipo]

        return classe(
            id,
            nome,
            tipo,
            estrategia,
        )