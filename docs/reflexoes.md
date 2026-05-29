## Aula 04 — SRP

Durante a decomposição do sistema, a decisão mais difícil foi definir a fronteira entre as responsabilidades do ServicoEmprestimo e do Notificador. Inicialmente, parecia mais simples deixar o envio de notificações dentro do próprio serviço de empréstimos, já que as notificações acontecem diretamente após operações como registro de empréstimo e verificação de atrasos.

Entretanto, essa escolha faria o módulo possuir mais de um motivo para mudança. Caso a lógica de envio de mensagens fosse alterada futuramente, o serviço principal também precisaria ser modificado. Isso aumentaria o acoplamento e reduziria a coesão do módulo.

A decisão final foi separar o Notificador em uma classe própria, deixando o ServicoEmprestimo responsável apenas pelas regras de negócio relacionadas aos empréstimos. O principal critério utilizado foi justamente o SRP discutido por Valente no Capítulo 5, especialmente a ideia de que um módulo deve possuir apenas uma responsabilidade principal e um único motivo para mudar.

Outra fronteira que exigiu atenção foi a separação entre models e services. A decisão adotada foi deixar os models apenas como representação dos dados, enquanto os services concentram comportamento e regras do sistema. Essa divisão ajudou a tornar a arquitetura mais organizada e compreensível.

## Aula 05 — OCP

A solução desenvolvida aplicou o princípio OCP (Open/Closed Principle) utilizando polimorfismo. Em vez de concentrar regras de cálculo de multa em estruturas condicionais com if/elif, cada tipo de equipamento passou a possuir sua própria implementação do método calcular_multa(). Dessa forma, o sistema ficou aberto para extensão e fechado para modificação, pois novos equipamentos podem ser adicionados sem alterar o serviço principal.

A abordagem funciona bem para variações simples baseadas em tipos de equipamento. Entretanto, conforme discutido por Valente no Capítulo 5, o OCP possui limites práticos. Caso surjam requisitos muito diferentes, como multas por hora, políticas variáveis por dia da semana ou regras dependentes de feriados, a hierarquia atual pode começar a crescer excessivamente e perder flexibilidade.

Nesse cenário, apenas herança talvez não seja suficiente. Seria necessário repensar a decomposição utilizando estratégias mais flexíveis, como composição ou padrões específicos para encapsular políticas de cálculo. Segundo Valente, o uso excessivo de abstrações também pode aumentar a complexidade do sistema, portanto o OCP deve ser aplicado com equilíbrio.

## Aula 06 — Verificação de LSP

As subclasses Notebook e Projetor foram revisadas para verificar se respeitam o contrato definido pela classe base Equipamento. Nos testes realizados, calcular_multa(0) retornou 0 em ambas as subclasses, atendendo corretamente ao requisito de multa não negativa.

Também foi verificado o comportamento com valores negativos, como calcular_multa(-5). Em todos os casos o retorno permaneceu 0, devido ao uso da função max(0, valor), impedindo multas negativas.

Além disso, nenhuma das subclasses lança exceções inesperadas durante a execução do método calcular_multa(). O retorno sempre permanece numérico e compatível com o contrato estabelecido na classe abstrata.

Dessa forma, as subclasses respeitam o comportamento esperado da superclasse, mantendo compatibilidade com o ServicoEmprestimo. Isso confirma a aplicação correta do princípio LSP, pois qualquer subclasse pode substituir Equipamento sem quebrar o funcionamento do sistema.

A análise foi baseada na discussão sobre substituição comportamental apresentada por Valente no Capítulo 5, seção sobre LSP (Liskov Substitution Principle).

---

## Aula 06 — DIP

A aplicação do DIP modificou significativamente a relação de dependência entre os módulos do sistema. Antes da alteração, o ServicoEmprestimo criava internamente suas dependências, tornando-se diretamente responsável por instanciar o repositório e o notificador. Isso aumentava o acoplamento e dificultava testes isolados.

Após a mudança, o serviço passou a receber essas dependências pelo construtor, funcionando apenas como consumidor delas. Na prática, isso alterou não apenas a implementação técnica, mas também a forma como os módulos se relacionam. O ServicoEmprestimo deixou de controlar a criação das dependências e passou a depender apenas de comportamentos externos já fornecidos.

Segundo Valente no Capítulo 5, seção sobre DIP (Dependency Inversion Principle), a inversão de dependência reduz acoplamento e aumenta flexibilidade arquitetural, permitindo substituições mais simples entre implementações. Isso ficou evidente ao imaginar o uso de repositórios falsos e notificadores falsos para testes, sem necessidade de alterar o serviço principal.

Além da melhoria arquitetural, a aplicação do DIP preparou o projeto para os testes unitários que serão desenvolvidos nas próximas aulas.

## Aula 08 — Testes Automatizados e CI

Durante a Aula 08 foi possível perceber como os testes automatizados ajudam a validar o comportamento do sistema sem depender de verificações manuais. A utilização do pytest tornou os testes mais organizados e facilitou a execução de múltiplos cenários rapidamente.

A aplicação do DIP realizada anteriormente facilitou bastante os testes, pois o ServicoEmprestimo já recebia suas dependências pelo construtor. Isso permitiu utilizar fakes no lugar de componentes reais, reduzindo acoplamento e tornando os testes mais isolados.

Os dublês de teste também mostraram na prática a importância da separação de responsabilidades. O FakeRepositorio e o FakeNotificador permitiram testar regras de negócio sem depender de banco de dados ou envio real de e-mails.

Outro ponto importante foi a utilização do GitHub Actions para integração contínua. Com isso, os testes passaram a ser executados automaticamente a cada push, ajudando a identificar erros rapidamente e aumentando a confiabilidade do projeto.

De acordo com Valente, Cap. 5, seção sobre modularidade e dependências, reduzir acoplamento entre componentes facilita manutenção, evolução e testes do sistema. Isso ficou evidente durante a implementação dos testes automatizados.
