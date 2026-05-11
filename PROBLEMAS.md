# Problemas Identificados — Leitura Inicial do Código

---

## Minha leitura inicial

- O código faz muitas coisas ao mesmo tempo no mesmo lugar, o que deixa difícil de entender.

- As listas de equipamentos e empréstimos ficam soltas fora da classe, o que parece desorganizado.

- O sistema mostra mensagem de e-mail usando print, mas não envia e-mail de verdade.

- O cálculo da multa aparece mais de uma vez no código, o que pode dar problema se precisar mudar depois.

- Tem partes do código que misturam lógica do sistema com mensagens na tela, o que deixa tudo confuso.

- Não vi nenhuma validação mais forte dos dados, então o sistema pode aceitar informações erradas.

- Tudo está em um único arquivo, o que dificulta organizar melhor o sistema.

---

## Revisão com vocabulário técnico

- O sistema apresentava baixa coesão, pois diferentes responsabilidades estavam concentradas no mesmo arquivo.

- Existia alto acoplamento entre as partes do sistema, dificultando modificações e reutilização de código.

- O uso de variáveis globais aumentava a dependência entre componentes.

- A ausência de separação em camadas dificultava a manutenção e evolução do sistema.

- O sistema não aplicava ocultamento de informação, expondo detalhes internos diretamente.

- A lógica de negócio estava misturada com a interface do usuário, violando a separação de responsabilidades.

- O código possuía características de dívida técnica, principalmente relacionadas à organização e escalabilidade.

- A falta de classes específicas dificultava a modelagem adequada das entidades do sistema.

- O modelo inicial dificultava testes isolados, contrariando o requisito RNF04.

- A estrutura em arquivo único dificultava futuras modificações, contrariando o requisito RNF03.
  
- O arquivo emprestimos.py violava o princípio SRP (Single Responsibility Principle), pois concentrava múltiplas responsabilidades no mesmo módulo.
