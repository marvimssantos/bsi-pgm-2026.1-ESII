# Production Readiness Checklist

## 1. Pipeline e qualidade

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Lint executado automaticamente a cada push/PR | ✅ OK | feito | alta | GitHub Actions executa `ruff check .` no pipeline de CI. |
| Testes automatizados executados no CI | ✅ OK | feito | alta | O pipeline executa os testes com pytest a cada push e pull request. |
| Gate mínimo de cobertura | ✅ OK | feito | alta | O pipeline exige pelo menos 80% de cobertura; atualmente o projeto apresenta 94,87%. |
| Cobertura e qualidade suficientes para produção | ⚠ PARCIAL | 1–2 dias | média | O pipeline está estruturado, mas ainda é necessário ampliar a avaliação de qualidade para cenários reais e de produção. |

## 2. Containerização

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Receita de build (Dockerfile) | ❌ FALTA | 2–4 horas | média | O repositório não possui uma receita de build em Docker identificada. |
| Build reprodutível | ❌ FALTA | 2–4 horas | média | Sem uma receita de container e dependências totalmente fixadas, o build não é completamente reprodutível. |
| Imagem com tamanho razoável | ⚠ PARCIAL | 2–4 horas | baixa | É possível definir uma imagem enxuta, mas isso ainda não foi implementado nem medido. |
| Execução sem root | ❌ FALTA | 1–2 horas | média | Não existe configuração de container definindo um usuário não privilegiado. |
| Exclusão de arquivos desnecessários do contexto | ❌ FALTA | 30 min–1 hora | baixa | Não há configuração de `.dockerignore` identificada. |

## 3. Persistência

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Empréstimos sobrevivem ao encerramento do programa | ❌ FALTA | 1–2 dias | alta | Os dados utilizados pelo sistema permanecem em memória e não há persistência em banco de dados identificada. |
| Equipamentos e seus estados são persistidos | ❌ FALTA | 1–2 dias | alta | O estado dos equipamentos não é armazenado de forma persistente. |
| Recuperação dos dados após reinicialização | ❌ FALTA | 1–2 dias | alta | Ao encerrar o processo, os dados mantidos em memória deixam de estar disponíveis. |
| Backup dos dados | ❌ FALTA | 1–2 dias | média | Não existe mecanismo de backup porque ainda não há uma camada de persistência implementada. |

## 4. Segurança

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Credenciais fora do código | ⚠ PARCIAL | 2–4 horas | alta | Não foram identificadas credenciais reais no código analisado, mas ainda não existe uma estratégia explícita de gerenciamento de segredos. |
| Validação das entradas | ⚠ PARCIAL | 1 dia | alta | Existem regras de negócio e testes, mas a validação sistemática das entradas do sistema ainda precisa ser fortalecida. |
| Dependências fixadas | ❌ FALTA | 1–2 horas | média | `requirements-dev.txt` usa especificações como `pytest>=8.0`, sem fixar versões exatas. |
| Auditoria de dependências | ❌ FALTA | 2–4 horas | média | Não há etapa específica de auditoria de vulnerabilidades de dependências no CI. |

## 5. Observabilidade

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Logs estruturados com níveis | ❌ FALTA | 1 dia | média | O sistema utiliza saída simples, como `print`, em vez de uma estratégia de logging estruturado. |
| Métricas da aplicação | ❌ FALTA | 1–2 dias | baixa | Não há coleta de métricas de execução, erros ou desempenho identificada. |
| Rastreamento de falhas anteriores | ❌ FALTA | 1 dia | média | Não existe armazenamento centralizado de logs que permita investigar uma falha ocorrida anteriormente. |
| Monitoramento da aplicação | ❌ FALTA | 1–2 dias | baixa | Não há mecanismo de monitoramento ou alertas configurado. |

## 6. Deployment

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Processo automatizado de publicação | ❌ FALTA | 1–2 dias | média | O CI valida o código, mas não existe uma etapa de deployment automatizado identificada. |
| Estratégia para disponibilizar uma nova versão | ⚠ PARCIAL | 1 dia | média | O código é versionado no GitHub e o CI valida alterações, mas o processo de entrega ao usuário ainda não está definido. |
| Plano de rollback | ❌ FALTA | 2–4 horas | alta | Não há procedimento documentado para retornar rapidamente à versão anterior em caso de falha. |
| Versionamento e rastreabilidade das versões implantadas | ⚠ PARCIAL | 2–4 horas | média | O Git fornece histórico dos commits, mas não existe um processo de releases/deployments formalizado. |

## Síntese executiva

A primeira prioridade para tornar o sistema production-ready deve ser implementar a persistência dos dados. Atualmente, os empréstimos e estados dos equipamentos dependem da execução do processo, o que significa que informações importantes podem ser perdidas quando o programa é encerrado. Esse risco é alto porque afeta diretamente a confiabilidade do sistema. Em seguida, eu atacaria a segurança, principalmente o gerenciamento de dependências e a validação das entradas. Uma aplicação que armazena dados de forma persistente precisa garantir que esses dados e as operações realizadas sobre eles estejam protegidos. A terceira prioridade seria melhorar a observabilidade, substituindo saídas simples por logs estruturados e criando mecanismos que permitam investigar falhas.

A principal dependência entre esses itens está entre persistência e observabilidade. Primeiro é necessário definir uma forma confiável de armazenar os dados e estruturar o funcionamento da aplicação; depois, os logs e métricas podem acompanhar as operações realizadas sobre essa estrutura. Fazer a observabilidade antes de resolver a persistência ajudaria a diagnosticar problemas, mas não resolveria o risco principal de perda dos dados.

A containerização pode ser atacada depois dessas prioridades. Ela melhora a reprodutibilidade e facilita a entrega, mas não corrige os riscos funcionais mais graves do sistema. O pipeline atual já fornece uma boa base, pois executa lint, testes e gate de cobertura de 80%, alcançando atualmente 94,87% de cobertura. Portanto, não seria racional substituir imediatamente esse trabalho por uma preocupação de infraestrutura.

Essa ordem considera risco, esforço e dependências: primeiro reduzir a possibilidade de perda de dados, depois proteger e observar o sistema e, por fim, avançar nas melhorias de infraestrutura e entrega. A abordagem está alinhada à ideia de evolução incremental da qualidade e da arquitetura discutida por Valente, Cap. 10.