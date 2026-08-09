from datetime import date, timedelta
from types import SimpleNamespace

from app.sistema import SistemaDeEmprestimos
from models.emprestimo import Emprestimo
from models.evento import Evento
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from services.observer import NotificadorEmail
from services.servico_emprestimo import ServicoEmprestimo


class RepoFakeAula13:

    def __init__(self):
        self.emprestimos = []
        self.equipamentos = [
            SimpleNamespace(
                id=1,
                nome="Notebook",
                disponivel=True
            ),
            SimpleNamespace(
                id=2,
                nome="Projetor",
                disponivel=False
            )
        ]

    def buscar_equipamento(self, id):
        for equipamento in self.equipamentos:
            if equipamento.id == id:
                return equipamento

        return None

    def buscar_emprestimos(self):
        return self.emprestimos

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def marcar_indisponivel(self, id):
        equipamento = self.buscar_equipamento(id)

        if equipamento:
            equipamento.disponivel = False

    def marcar_disponivel(self, id):
        equipamento = self.buscar_equipamento(id)

        if equipamento:
            equipamento.disponivel = True


class NotificadorFakeAula13:

    def __init__(self):
        self.emprestimos = []
        self.atrasos = []

    def notificar_emprestimo(self, email, data_devolucao):
        self.emprestimos.append(
            (email, data_devolucao)
        )

    def notificar_atraso(self, email):
        self.atrasos.append(email)


class ObserverFakeAula13:

    def __init__(self):
        self.eventos = []

    def atualizar(self, evento):
        self.eventos.append(evento)


# ---------------------------------------------------------
# RepositorioEmprestimo
# ---------------------------------------------------------

def test_repositorio_cria_equipamentos():

    repo = RepositorioEmprestimo()

    assert len(repo.emprestimos) == 0
    assert repo.buscar_equipamento(1) is not None
    assert repo.buscar_equipamento(2) is not None
    assert repo.buscar_equipamento(3) is not None


def test_repositorio_busca_equipamento_inexistente():

    repo = RepositorioEmprestimo()

    assert repo.buscar_equipamento(999) is None


def test_repositorio_salva_emprestimo():

    repo = RepositorioEmprestimo()

    emprestimo = SimpleNamespace(
        id=1
    )

    repo.salvar_emprestimo(emprestimo)

    assert len(repo.emprestimos) == 1
    assert repo.emprestimos[0] == emprestimo


def test_repositorio_busca_emprestimos():

    repo = RepositorioEmprestimo()

    emprestimo = SimpleNamespace(
        id=1
    )

    repo.salvar_emprestimo(emprestimo)

    assert repo.buscar_emprestimos() == [emprestimo]


def test_repositorio_marca_indisponivel():

    repo = RepositorioEmprestimo()

    equipamento = repo.buscar_equipamento(1)

    assert equipamento.disponivel is True

    repo.marcar_indisponivel(1)

    assert equipamento.disponivel is False


def test_repositorio_marca_disponivel():

    repo = RepositorioEmprestimo()

    equipamento = repo.buscar_equipamento(1)

    repo.marcar_indisponivel(1)
    assert equipamento.disponivel is False

    repo.marcar_disponivel(1)

    assert equipamento.disponivel is True


def test_repositorio_id_inexistente_nao_altera_equipamento():

    repo = RepositorioEmprestimo()

    repo.marcar_indisponivel(999)
    repo.marcar_disponivel(999)

    assert repo.buscar_equipamento(999) is None


# ---------------------------------------------------------
# Notificador
# ---------------------------------------------------------

def test_notificador_emprestimo(capsys):

    notificador = Notificador()

    notificador.notificar_emprestimo(
        "marcos@gmail.com",
        date(2026, 8, 15)
    )

    saida = capsys.readouterr().out

    assert "[EMAIL]" in saida
    assert "Empréstimo registrado" in saida
    assert "2026-08-15" in saida


def test_notificador_atraso(capsys):

    notificador = Notificador()

    notificador.notificar_atraso(
        "marcos@gmail.com"
    )

    saida = capsys.readouterr().out

    assert "[EMAIL]" in saida
    assert "atrasado" in saida


def test_notificador_enviar_email(capsys):

    notificador = Notificador()

    notificador.enviar_email(
        "Mensagem de teste"
    )

    saida = capsys.readouterr().out

    assert "[EMAIL] Mensagem de teste" in saida


# ---------------------------------------------------------
# Observer
# ---------------------------------------------------------

def test_notificador_email_recebe_evento(capsys):

    observer = NotificadorEmail()

    evento = Evento(
        email="marcos@gmail.com",
        mensagem="Empréstimo registrado"
    )

    observer.atualizar(evento)

    saida = capsys.readouterr().out

    assert "[EMAIL]" in saida
    assert "marcos@gmail.com" in saida
    assert "Empréstimo registrado" in saida


def test_evento_possui_dados_corretos():

    evento = Evento(
        email="marcos@gmail.com",
        mensagem="Teste"
    )

    assert evento.email == "marcos@gmail.com"
    assert evento.mensagem == "Teste"


# ---------------------------------------------------------
# ServicoEmprestimo
# ---------------------------------------------------------

def criar_servico():

    repo = RepoFakeAula13()
    notificador = NotificadorFakeAula13()

    servico = ServicoEmprestimo(
        repo,
        notificador
    )

    return servico, repo, notificador


def test_adicionar_observer():

    servico, _, _ = criar_servico()

    observer = ObserverFakeAula13()

    servico.adicionar_observer(observer)

    assert observer in servico.observers


def test_emitir_evento():

    servico, _, _ = criar_servico()

    observer = ObserverFakeAula13()

    servico.adicionar_observer(observer)

    servico.emitir_evento(
        "marcos@gmail.com",
        "Teste"
    )

    assert len(observer.eventos) == 1

    evento = observer.eventos[0]

    assert isinstance(evento, Evento)
    assert evento.email == "marcos@gmail.com"
    assert evento.mensagem == "Teste"


def test_criar_emprestimo():

    servico, repo, _ = criar_servico()

    emprestimo = servico.criar_emprestimo(
        1,
        "Marcos",
        "marcos@gmail.com",
        date.today() + timedelta(days=5)
    )

    assert emprestimo.id == 1
    assert emprestimo.equipamento_id == 1
    assert emprestimo.nome_usuario == "Marcos"
    assert emprestimo.email == "marcos@gmail.com"
    assert emprestimo.devolvido is False


def test_registrar_emprestimo():

    servico, repo, notificador = criar_servico()

    observer = ObserverFakeAula13()
    servico.adicionar_observer(observer)

    resultado = servico.registrar(
        1,
        "Marcos",
        "marcos@gmail.com",
        5
    )

    assert resultado is True
    assert len(repo.emprestimos) == 1
    assert repo.buscar_equipamento(1).disponivel is False
    assert len(notificador.emprestimos) == 1
    assert len(observer.eventos) == 1


def test_registrar_equipamento_inexistente():

    servico, repo, _ = criar_servico()

    resultado = servico.registrar(
        999,
        "Marcos",
        "marcos@gmail.com",
        5
    )

    assert resultado is False
    assert len(repo.emprestimos) == 0


def test_registrar_equipamento_indisponivel():

    servico, repo, _ = criar_servico()

    resultado = servico.registrar(
        2,
        "Marcos",
        "marcos@gmail.com",
        5
    )

    assert resultado is False
    assert len(repo.emprestimos) == 0


def test_registrar_devolucao_encontrada():

    servico, repo, _ = criar_servico()

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        nome_usuario="Marcos",
        email="marcos@gmail.com",
        data_devolucao=date.today(),
        devolvido=False
    )

    repo.salvar_emprestimo(emprestimo)
    repo.marcar_indisponivel(1)

    resultado = servico.registrar_devolucao(1)

    assert resultado is True
    assert emprestimo.devolvido is True
    assert repo.buscar_equipamento(1).disponivel is True


def test_registrar_devolucao_nao_encontrada():

    servico, _, _ = criar_servico()

    resultado = servico.registrar_devolucao(999)

    assert resultado is False


def test_listar_atrasados():

    servico, repo, notificador = criar_servico()

    observer = ObserverFakeAula13()
    servico.adicionar_observer(observer)

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        nome_usuario="Marcos",
        email="marcos@gmail.com",
        data_devolucao=date.today() - timedelta(days=5),
        devolvido=False
    )

    repo.salvar_emprestimo(emprestimo)

    atrasados = servico.listar_atrasados()

    assert len(atrasados) == 1
    assert atrasados[0] == emprestimo
    assert emprestimo.multa == 20
    assert "marcos@gmail.com" in notificador.atrasos
    assert len(observer.eventos) == 1


def test_listar_atrasados_ignora_emprestimo_em_dia():

    servico, repo, _ = criar_servico()

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        nome_usuario="Marcos",
        email="marcos@gmail.com",
        data_devolucao=date.today() + timedelta(days=5),
        devolvido=False
    )

    repo.salvar_emprestimo(emprestimo)

    atrasados = servico.listar_atrasados()

    assert atrasados == []


def test_listar_atrasados_ignora_devolvido():

    servico, repo, _ = criar_servico()

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        nome_usuario="Marcos",
        email="marcos@gmail.com",
        data_devolucao=date.today() - timedelta(days=5),
        devolvido=True
    )

    repo.salvar_emprestimo(emprestimo)

    atrasados = servico.listar_atrasados()

    assert atrasados == []


# ---------------------------------------------------------
# Fachada SistemaDeEmprestimos
# ---------------------------------------------------------

def test_sistema_registrar_delega_para_servico():

    sistema = SistemaDeEmprestimos()

    sistema._servico.registrar = lambda *args: True

    resultado = sistema.registrar(
        1,
        "Marcos",
        "marcos@gmail.com",
        5
    )

    assert resultado is True


def test_sistema_devolver_delega_para_servico():

    sistema = SistemaDeEmprestimos()

    sistema._servico.registrar_devolucao = (
        lambda *args: True
    )

    resultado = sistema.devolver(1)

    assert resultado is True


def test_sistema_listar_atrasados_delega_para_servico():

    sistema = SistemaDeEmprestimos()

    sistema._servico.listar_atrasados = (
        lambda: ["atrasado"]
    )

    resultado = sistema.listar_atrasados()

    assert resultado == ["atrasado"]
