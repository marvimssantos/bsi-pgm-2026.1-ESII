## Aula 04 — SRP

Durante a decomposição do sistema, a decisão mais difícil foi definir a fronteira entre as responsabilidades do ServicoEmprestimo e do Notificador. Inicialmente, parecia mais simples deixar o envio de notificações dentro do próprio serviço de empréstimos, já que as notificações acontecem diretamente após operações como registro de empréstimo e verificação de atrasos.

Entretanto, essa escolha faria o módulo possuir mais de um motivo para mudança. Caso a lógica de envio de mensagens fosse alterada futuramente, o serviço principal também precisaria ser modificado. Isso aumentaria o acoplamento e reduziria a coesão do módulo.

A decisão final foi separar o Notificador em uma classe própria, deixando o ServicoEmprestimo responsável apenas pelas regras de negócio relacionadas aos empréstimos. O principal critério utilizado foi justamente o SRP discutido por Valente no Capítulo 5, especialmente a ideia de que um módulo deve possuir apenas uma responsabilidade principal e um único motivo para mudar.

Outra fronteira que exigiu atenção foi a separação entre models e services. A decisão adotada foi deixar os models apenas como representação dos dados, enquanto os services concentram comportamento e regras do sistema. Essa divisão ajudou a tornar a arquitetura mais organizada e compreensível.

## Aula 05 — OCP

A solução desenvolvida aplicou o princípio OCP (Open/Closed Principle) utilizando polimorfismo. Em vez de concentrar regras de cálculo de multa em estruturas condicionais com if/elif, cada tipo de equipamento passou a possuir sua própria implementação do método calcular_multa(). Dessa forma, o sistema ficou aberto para extensão e fechado para modificação, pois novos equipamentos podem ser adicionados sem alterar o serviço principal.

A abordagem funciona bem para variações simples baseadas em tipos de equipamento. Entretanto, conforme discutido por Valente no Capítulo 5, o OCP possui limites práticos. Caso surjam requisitos muito diferentes, como multas por hora, políticas variáveis por dia da semana ou regras dependentes de feriados, a hierarquia atual pode começar a crescer excessivamente e perder flexibilidade.

Nesse cenário, apenas herança talvez não seja suficiente. Seria necessário repensar a decomposição utilizando estratégias mais flexíveis, como composição ou padrões específicos para encapsular políticas de cálculo. Segundo Valente, o uso excessivo de abstrações também pode aumentar a complexidade do sistema, portanto o OCP deve ser aplicado com equilíbrio.
