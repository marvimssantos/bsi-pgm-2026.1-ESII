# Cenário BDD — Cálculo de Multa com Carência

Funcionalidade: Cálculo de multa

Cenário: Usuário devolve equipamento após o período de carência

Dado que a carência é de 3 dias
E o valor da multa é R$10 por dia
Quando o equipamento é devolvido com 5 dias de atraso
Então a multa deve ser R$20

Cenário: Usuário devolve equipamento sem atraso

Dado que a carência é de 3 dias
E o valor da multa é R$10 por dia
Quando o equipamento é devolvido sem atraso
Então a multa deve ser R$0

Cenário: Usuário informa atraso negativo

Dado que a carência é de 3 dias
E o valor da multa é R$10 por dia
Quando o atraso informado é -2 dias
Então a multa deve ser R$0