# ADR-001 — Decisão de Arquitetura

## Contexto

O sistema atual apresenta problemas de organização, dificultando manutenção e testes. 
De acordo com os requisitos:

- RNF03 exige que o sistema seja fácil de modificar sem alterar várias partes
- RNF04 exige que as regras possam ser testadas de forma isolada

A versão atual (arquivo único) não atende esses requisitos.

---

## Opções consideradas

### 1. Arquivo único
- Simples, mas desorganizado
- Difícil manutenção
- Não atende RNF03 nem RNF04

### 2. Arquitetura em camadas
- Separa responsabilidades
- Facilita manutenção
- Permite testes isolados
- Atende RNF03 e RNF04

### 3. MVC
- Bem organizado
- Mais complexo
- Desnecessário para sistema simples CLI

---

## Decisão

Foi escolhida a arquitetura em camadas.

As camadas serão:

- **domain** → regras de negócio (empréstimos, multas)
- **data** → armazenamento dos dados
- **service** → lógica principal do sistema
- **ui** → interação com o usuário (menu)

Cada camada terá sua própria pasta no projeto.

---

## Consequências

- O código ficará mais organizado
- Será mais fácil adicionar novos tipos de equipamento
- As regras poderão ser testadas separadamente
- A manutenção do sistema será facilitada
