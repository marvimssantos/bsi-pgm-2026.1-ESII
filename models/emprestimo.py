# Emprestimo: representar um empréstimo realizado.
from dataclasses import dataclass
from datetime import date

@dataclass
class Emprestimo:
    id: int
    equipamento_id: int
    nome_usuario: str
    email: str
    data_devolucao: date
    devolvido: bool
