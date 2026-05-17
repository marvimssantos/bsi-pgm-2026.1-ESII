# main: iniciar execução do sistema.

from services.servico_emprestimo import ServicoEmprestimo

servico = ServicoEmprestimo()

servico.registrar(
    1,
    "Marcos",
    "viniciusmv25@gmail.com",
    7
)

print(servico.listar_atrasados())
