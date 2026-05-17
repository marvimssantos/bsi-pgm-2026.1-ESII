## Aula 05 — OCP

A solução desenvolvida aplicou o princípio OCP (Open/Closed Principle) utilizando polimorfismo. Em vez de concentrar regras de cálculo de multa em estruturas condicionais com if/elif, cada tipo de equipamento passou a possuir sua própria implementação do método calcular_multa(). Dessa forma, o sistema ficou aberto para extensão e fechado para modificação, pois novos equipamentos podem ser adicionados sem alterar o serviço principal.

A abordagem funciona bem para variações simples baseadas em tipos de equipamento. Entretanto, conforme discutido por Valente no Capítulo 5, o OCP possui limites práticos. Caso surjam requisitos muito diferentes, como multas por hora, políticas variáveis por dia da semana ou regras dependentes de feriados, a hierarquia atual pode começar a crescer excessivamente e perder flexibilidade.

Nesse cenário, apenas herança talvez não seja suficiente. Seria necessário repensar a decomposição utilizando estratégias mais flexíveis, como composição ou padrões específicos para encapsular políticas de cálculo. Segundo Valente, o uso excessivo de abstrações também pode aumentar a complexidade do sistema, portanto o OCP deve ser aplicado com equilíbrio.
