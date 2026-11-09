# Status e divisão do projeto

Este documento registra a divisão de responsabilidades e o andamento do projeto SOAP de adoção de pets. Atualizem o status conforme o trabalho realmente for concluído; não marquem uma etapa como pronta sem testar ou revisar a entrega.

## Objetivo do projeto

Desenvolver e demonstrar um serviço SOAP para o domínio de adoção de pets, incluindo o servidor em Python, o contrato WSDL, um cliente em Java e testes no SoapUI.

## Divisão de responsabilidades

| Integrante | Foco principal | Entregas esperadas |
|---|---|---|
| **Patrícia** | Servidor SOAP em Python e operações do serviço. | Implementar e explicar as operações; informar entradas, respostas e erros previstos; apoiar a execução do servidor. |
| **Erick** | Cliente SOAP em Java, testes no SoapUI e documentação/WSDL. | Implementar e explicar o consumo do serviço; manter o WSDL/documentação coerentes com as operações; preparar testes no SoapUI. |
| **Bruno** | Contribuição pequena de código e participação na revisão. | Adicionar um teste automatizado para uma operação SOAP existente, seguindo a estrutura do projeto e combinando a operação com Patrícia ou Erick; executar o teste e registrar a contribuição no GitHub. |
| **Todos** | Revisão, validação do fluxo e apresentação. | Revisar o serviço, testar o fluxo SOAP completo e preparar a apresentação em conjunto. |

A responsabilidade principal pelo SOAP fica com Patrícia e Erick. A contribuição de Bruno é delimitada: um teste para uma funcionalidade que já existe, sem exigir que implemente o servidor, o cliente ou uma operação nova.

## Quadro de status

Preencham o responsável, a data e as evidências quando houver avanço. Enquanto não for confirmado pelo grupo, mantenham como **A iniciar**.

| Etapa | Responsável(is) | Status | Evidência / observação |
|---|---|---|---|
| Definir operações e dados do serviço | Patrícia | A iniciar | Preencher após alinhamento do grupo. |
| Implementar servidor SOAP em Python | Patrícia | A iniciar | Informar como iniciar e como verificar que está ativo. |
| Definir e conferir contrato WSDL | Erick, com apoio de Patrícia | A iniciar | Registrar onde está o WSDL ou como acessá-lo. |
| Implementar cliente SOAP em Java | Erick | A iniciar | Registrar como executar e quais operações consome. |
| Preparar e executar requisições no SoapUI | Erick | A iniciar | Guardar evidência de chamadas e respostas. |
| Adicionar teste automatizado de operação existente | Bruno, com orientação de Patrícia ou Erick | A iniciar | Informar operação testada e resultado. |
| Revisar código e documentação | Todos | A iniciar | Anotar ajustes acordados. |
| Testar o fluxo completo SOAP | Todos | A iniciar | Validar chamada, processamento e resposta. |
| Preparar e ensaiar apresentação | Todos | A iniciar | Confirmar divisão das falas e demonstração. |

### Legenda dos status

- **A iniciar:** ainda não começou ou não há evidência de andamento.
- **Em andamento:** há trabalho ativo, mas a etapa ainda não foi validada.
- **Em revisão:** implementação concluída e aguardando revisão ou teste.
- **Concluído:** revisado e validado conforme o objetivo da etapa.
- **Bloqueado:** há uma pendência impedindo o avanço; explicar qual é na coluna de observação.

## O que significa concluir cada parte

### Servidor SOAP — Patrícia

- As operações acordadas estão implementadas.
- O servidor inicia conforme as instruções reais do projeto.
- Entradas, respostas e erros relevantes podem ser demonstrados.

### Cliente, WSDL e SoapUI — Erick

- O contrato WSDL representa as operações disponíveis.
- O cliente Java consegue chamar o servidor SOAP.
- Há pelo menos uma requisição de teste preparada no SoapUI, com resposta conferida.

### Teste automatizado — Bruno

1. Escolher com Patrícia ou Erick uma operação simples que já esteja implementada.
2. Verificar como os testes existentes são organizados e usar o mesmo padrão.
3. Criar um teste que confirme um resultado esperado para essa operação.
4. Executar o teste e corrigir problemas diretamente relacionados à contribuição.
5. Fazer commit no GitHub com uma mensagem objetiva e apresentar o que o teste verifica.

O teste deve corresponder ao comportamento real do serviço. Se o projeto ainda não tiver uma estrutura de testes automatizados, alinhar com a equipe antes de escolher uma forma simples de adicioná-lo.

## Rotina de acompanhamento

- Atualizar este quadro quando uma tarefa começar, ficar bloqueada ou for concluída.
- Em cada conclusão, registrar evidência: teste executado, chamada SoapUI, revisão ou demonstração.
- Avisar o grupo quando uma mudança no contrato afetar o servidor, o cliente ou o WSDL.
- Antes da apresentação, todos devem saber explicar o fluxo básico: cliente envia a requisição SOAP, servidor processa a operação e devolve uma resposta.
