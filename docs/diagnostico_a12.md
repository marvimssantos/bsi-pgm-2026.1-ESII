# Diagnóstico de Code Smells — Aula 12

## 1. Primitive Obsession

Antes os eventos eram representados por valores soltos (`email`, `mensagem`), o que dificultava manutenção e evolução. Foi substituído pelo objeto `Evento`.

## 2. Long Method

O método `registrar()` concentrava múltiplas responsabilidades. Foi aplicado Extract Function para mover a criação do empréstimo.

## 3. Temporary Field

O atributo `multa` aparece apenas em situações específicas de atraso, podendo indicar dependência temporária.

## 4. Data Clumps

Conjunto recorrente de dados (`email`, `mensagem`) aparecia em diversos pontos do Observer antes da criação do objeto `Evento`.

## 5. Falso positivo — Hierarquia de subclasses (Strategy)

As classes de estratégia poderiam parecer excesso de subclasses, porém nesse caso representam variações legítimas do algoritmo e seguem o padrão Strategy, portanto não configuram smell.
