class FakeRepositorio:

    def __init__(self):

        self.emprestimos = []

        self.equipamentos = {
            1: {
                "id": 1,
                "nome": "Notebook",
                "disponivel": True
            },

            2: {
                "id": 2,
                "nome": "Projetor",
                "disponivel": False
            }
        }

    def buscar_equipamento(
        self,
        equip_id
    ):

        return self.equipamentos.get(
            equip_id
        )

    def salvar_emprestimo(
        self,
        emprestimo
    ):

        self.emprestimos.append(
            emprestimo
        )

    def listar_emprestimos(self):

        return self.emprestimos
