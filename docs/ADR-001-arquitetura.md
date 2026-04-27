# ADR-001 — Decisão de Arquitetura

## Contexto

O sistema atual apresenta problemas de organização, dificultando manutenção e testes. 
De acordo com os requisitos:

- RNF03 exige que o sistema seja fácil de modificar sem alterar várias partes
- RNF04 exige que as regras possam ser testadas de forma isolada

A versão atual (arquivo único) não atende esses requisitos.

A decisão foi baseada na análise comparativa dos estilos arquiteturais realizada na Parte 1.

---

## Opções consideradas

A análise foi feita comparando três estilos arquiteturais com base nos requisitos RNF03 e RNF04.

| Critério | Arquivo único | Em camadas | MVC |
|----------|-------------|------------|-----|
| Atende RNF03 | Não | Sim | Sim |
| Atende RNF04 | Não | Sim | Sim |
| Adequado para CLI | Sim | Sim | Médio |
| Familiar para iniciantes | Sim | Sim | Não |

### Análise

- **Arquivo único**: simples, porém desorganizado e difícil de manter, não atendendo os requisitos.
- **Arquitetura em camadas**: separa responsabilidades, facilita manutenção e testes, atendendo os requisitos.
- **MVC**: bem estruturado, porém mais complexo do que o necessário para este projeto.

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
