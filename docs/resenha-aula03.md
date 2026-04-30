# Resenha Aula 3 — Modelos UML e Design de Componentes 

**Aluno:** Marcos Vinicius Morais dos Santos
**Data:** 29/04/2026  

---

## Questão 1 — Modelos UML como ferramentas de modelagem 

### (a) Estrutura × comportamento 
No Capítulo 4 (Modelos como abstrações), Valente explica que modelos são abstrações, ou seja, mostram alguns aspectos do sistema e escondem outros. O diagrama de classes representa a estrutura, com classes, atributos e relações. Ele ajuda a entender como o sistema está organizado, mas não mostra o comportamento em execução.

Já o diagrama de sequência mostra o comportamento, evidenciando a troca de mensagens e a ordem das interações. Como discutido por Valente no mesmo capítulo, diagramas estruturais e comportamentais se complementam, pois cada um mostra um ponto de vista diferente do sistema.

---

### (b) Consequência prática 
Na prática, o diagrama de classes ajuda na definição da arquitetura do sistema, como separação de responsabilidades e organização das classes.

Já o diagrama de sequência auxilia no entendimento do fluxo das operações e das interações entre objetos, ajudando a definir métodos e chamadas. Isso está alinhado com a ideia apresentada por Valente no Capítulo 4 de usar diferentes modelos para apoiar decisões distintas de projeto.

---

### (c) Aplicação ao UC01 
No UC01 de registrar empréstimo, um diagrama de sequência mostraria claramente a interação entre menu, serviço e dados do sistema.

Ele evidenciaria a ordem das validações e o registro do empréstimo. Isso reforça a ideia de Valente, no Capítulo 4, de que modelos ajudam a compreender o comportamento que não está explícito em descrições textuais.

Além disso, como Valente destaca nesse capítulo, a escolha do tipo de modelo depende do objetivo da análise. No caso do sistema de empréstimos, o uso combinado desses diagramas permitiria identificar tanto problemas estruturais quanto falhas no fluxo de execução, auxiliando inclusive na identificação de pontos de melhoria para a v2.0.

---

## Questão 2 — Arquitetura, design e os princípios de decomposição 

### (a) Definições 
Segundo o Capítulo 7 (Qualidade de Design), coesão é quando um módulo possui responsabilidades bem relacionadas. Acoplamento é o nível de dependência entre módulos, e deve ser baixo. Ocultamento de informação consiste em esconder detalhes internos e expor apenas o necessário.

---

### (b) Relações entre os princípios 
Esses princípios se complementam. Como discutido por Valente no Capítulo 7, o ocultamento de informação ajuda a reduzir acoplamento, pois limita o acesso a detalhes internos.

Além disso, módulos com alta coesão tendem a ser mais fáceis de manter e entender. Esses conceitos trabalham juntos para melhorar a qualidade do sistema e orientar decisões de design mais sustentáveis.

---

### (c) Aplicação ao projeto v2.0 
Na arquitetura em camadas, models pode conter classes como Equipamento e Emprestimo, representando o domínio.

Services concentra regras de negócio, repositories lida com dados e main.py com a interface.

Essa separação aplica os princípios discutidos por Valente no Capítulo 7, reduzindo acoplamento e aumentando coesão, além de facilitar testes e evolução do sistema, atendendo diretamente aos requisitos RNF03 e RNF04.

Essa organização também facilita a evolução do sistema, pois mudanças em uma camada tendem a impactar menos as outras. Como discutido por Valente nesse capítulo, boas decisões de decomposição ajudam a reduzir o custo de manutenção ao longo do tempo, o que é essencial em sistemas reais.

---

## Questão 3 — Crítica fundamentada à documentação do sistema legado 

### (a) Pontos frágeis 
Um ponto frágil é o alto acoplamento, pois o sistema utiliza variáveis globais e mistura lógica de negócio com interface.

Outro problema é a baixa coesão, já que o código concentra várias responsabilidades no mesmo arquivo.

Além disso, há duplicação do cálculo de multa, o que caracteriza dívida técnica e dificulta manutenção.

Também é possível observar pouca validação de dados, o que pode gerar inconsistências no sistema e comprometer a confiabilidade.

---

### (b) Ponto forte 
Um ponto positivo é que a documentação reconhece explicitamente a dívida técnica (DT01–DT07), o que demonstra consciência dos problemas do sistema.

---

### (c) Síntese 
Como discutido por Valente no Capítulo 1 (Dívida técnica), a dívida técnica pode ser deliberada, ou seja, decisões podem ser tomadas mesmo sabendo das limitações.

Nesse caso, o reconhecimento dessas dívidas permite planejar melhorias na versão 2.0, tornando a evolução do sistema mais organizada.

Além disso, esses problemas observados no código mostram na prática os conceitos discutidos por Valente no Capítulo 7 sobre acoplamento e coesão. Também evidenciam dificuldades em atender o RNF04, já que as regras não estão isoladas para testes. O sistema legado serve como um exemplo real de como a ausência desses princípios impacta negativamente a qualidade do software.

---

## Questão 4 — Tipos como contratos: dicionários × classes 

### (a) Prevenção de erros 
Com dicionários, erros como chaves incorretas ou valores ausentes podem ocorrer facilmente.

Com classes, a estrutura é definida, reduzindo esse tipo de erro. Isso está alinhado com a ideia de tipos como contratos discutida por Valente no Capítulo 5 (Tipos e contratos).

---

### (b) Capacidade de evolução 
Classes permitem adicionar novos comportamentos sem afetar o restante do sistema.

Já com dicionários, as regras ficam espalhadas, dificultando manutenção e evolução, o que pode contrariar o RNF03 em cenários de expansão do sistema.

---

### (c) Comunicação do design 
Classes representam melhor os conceitos do domínio, como Equipamento.

Como discutido por Valente no Capítulo 5, tipos também servem para comunicar decisões de projeto, tornando o sistema mais compreensível.

Isso reforça a ideia de que a escolha da representação dos dados influencia diretamente a qualidade do sistema. Como apresentado por Valente nesse capítulo, tipos não são apenas estruturas de dados, mas também uma forma de expressar decisões de design.
