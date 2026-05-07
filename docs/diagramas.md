# Diagramas e Decomposição
A decomposição abaixo foi baseada na arquitetura definida no ADR-001 e nos princípios discutidos na resenha da Aula 3, como coesão, separação de responsabilidades e ocultamento de informação.
---

## Decomposição em camadas

### models/Equipamento
Responsável por representar os dados do equipamento de forma tipada.

### models/Emprestimo
Representa as informações de um empréstimo realizado no sistema.

### services/ServicoEmprestimo
Centraliza as regras de negócio relacionadas aos empréstimos.

### services/Notificador
Responsável pelo envio de notificações do sistema.

### repositories/RepositorioEmprestimo
Responsável pelo armazenamento e recuperação de dados.

### main.py
Controla a interação principal do sistema com o usuário.

---

# Diagramas de sequência

## UC01 — Registrar Empréstimo

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo
    participant notif as Notificador

    Atendente->>main: informa equip_id, nome, email, dias
    main->>servico: registrar(equip_id, nome, email, dias)
    servico->>repo: buscar_equipamento(equip_id)
    repo-->>servico: Equipamento

    alt equipamento disponível
        servico->>repo: salvar_emprestimo(emprestimo)
        servico->>repo: marcar_indisponivel(equip_id)
        servico->>notif: notificar_emprestimo(email, data_devolucao)
        servico-->>main: True
    else equipamento indisponível
        servico-->>main: False
    end
```

---

## UC02 — Registrar Devolução

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo

    Atendente->>main: informa id do empréstimo
    main->>servico: registrar_devolucao(id)
    servico->>repo: buscar_emprestimo(id)
    repo-->>servico: Emprestimo

    alt empréstimo encontrado
        servico->>repo: marcar_devolvido(id)
        servico->>repo: marcar_disponivel(equip_id)
        servico-->>main: devolução realizada
    else empréstimo não encontrado
        servico-->>main: erro
    end
```

---

## UC03 — Listar Empréstimos em Atraso

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo

    Atendente->>main: solicita atrasados
    main->>servico: listar_atrasados()
    servico->>repo: buscar_emprestimos()
    repo-->>servico: lista emprestimos

    loop para cada empréstimo
        servico->>servico: verificar_atraso()
    end

    servico-->>main: lista de atrasados
```
