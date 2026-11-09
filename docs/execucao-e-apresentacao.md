# Execução e apresentação

Este documento é um roteiro para preparar, executar e explicar o projeto SOAP de adoção de pets. Os comandos concretos dependem dos arquivos e das dependências do projeto; antes da apresentação, substituam as indicações pelos comandos realmente usados e testados.

## 1. Preparação do ambiente

### Conferir o projeto

Antes de executar, a equipe deve localizar:

- o arquivo Python que inicia o servidor SOAP;
- o arquivo `.wsdl` ou a URL em que o serviço publica o WSDL;
- o ponto de entrada do cliente SOAP Java e o gerenciador de build usado (Maven ou Gradle, se houver);
- os arquivos de dependências e configurações do projeto SOAP, como `requirements.txt`, `pom.xml`, `build.gradle` ou equivalentes.

Anotem aqui os comandos confirmados para a versão final do projeto:

| Componente             | Comando de inicialização/teste confirmado                       |
| ---------------------- | --------------------------------------------------------------- |
| Servidor SOAP (Python) | A preencher após conferir o ponto de entrada e as dependências. |
| Cliente SOAP (Java)    | A preencher conforme o build e o ponto de entrada do cliente.   |
| Testes SoapUI          | Abrir/importar o WSDL e executar as requisições salvas.         |

Não inventem nomes de arquivos, portas ou URLs: usem os valores definidos nas configurações e no código.

### Ordem recomendada

1. Instalar as versões de Python e Java exigidas pelo projeto.
2. Instalar as dependências conforme os arquivos de configuração existentes.
3. Iniciar o servidor SOAP e confirmar que está acessível.
4. Abrir o WSDL no navegador ou importá-lo no SoapUI.
5. Executar no SoapUI ao menos uma operação válida e um caso de erro esperado.
6. Executar o cliente Java e verificar se ele obtém a resposta esperada do serviço.

## 2. Como testar e analisar

Para cada teste, registrem quatro informações: **objetivo**, **dados enviados**, **resultado esperado** e **resultado observado**.

### Testes SOAP no SoapUI

1. Criar ou abrir um projeto SoapUI a partir do WSDL do serviço.
2. Escolher uma operação que realmente esteja descrita no WSDL.
3. Conferir os campos obrigatórios e preencher uma requisição válida.
4. Enviar a requisição e comparar o XML da resposta com o resultado esperado.
5. Repetir com dados inválidos ou incompletos, quando fizer sentido, e observar como o serviço comunica a falha.
6. Guardar evidências sem expor dados pessoais ou informações secretas.

O WSDL descreve o contrato; o SoapUI é o cliente de teste que usa esse contrato para montar requisições. O WSDL, sozinho, não executa a operação.

### Testes do cliente Java

- Confirmar que o cliente aponta para o endereço correto do serviço.
- Executar uma operação suportada pelo servidor SOAP.
- Conferir se os dados enviados e recebidos correspondem ao contrato.
- Verificar como o cliente reage quando o servidor está indisponível ou responde com erro.

## 3. Roteiro de apresentação

### Abertura — todos

> “Nosso projeto aborda a adoção de pets por meio de um serviço SOAP. O servidor foi desenvolvido em Python, seu contrato é descrito por um WSDL, e as operações podem ser consumidas por um cliente Java e testadas no SoapUI. Vamos apresentar como a requisição é enviada, processada e respondida.”

Adaptem a fala ao que estiver realmente implementado e à ordem definida para a apresentação.

### Parte SOAP — Patrícia

Patrícia explica o servidor SOAP em Python e suas operações:

- qual problema o serviço resolve;
- quais operações estão implementadas e que dados cada uma recebe;
- como uma requisição chega ao servidor e como é processada;
- qual resposta é devolvida e como são tratadas falhas.

### Cliente e contrato SOAP — Erick

Erick apresenta o WSDL, o cliente Java e os testes:

- onde o WSDL está ou como acessá-lo;
- como o cliente Java utiliza o contrato para chamar o serviço;
- como uma requisição e uma resposta aparecem no SoapUI;
- um teste válido e, se disponível, um teste de erro.

### Contribuição de código e teste — Bruno

Para deixar uma contribuição de código clara no histórico do GitHub sem assumir a implementação principal do SOAP, Bruno pode adicionar **um teste automatizado para uma operação já existente**. Combine com Patrícia ou Erick qual operação é mais simples e siga a estrutura de testes que o projeto já utiliza. Se possível, teste uma chamada com dados válidos e confirme o resultado esperado; não é necessário criar uma operação nova nem alterar a arquitetura do serviço.

Na apresentação, Bruno mostra o teste que escreveu e explica o caminho básico da chamada:

- como o cliente Java ou o SoapUI envia a requisição;
- como o servidor Python processa a operação solicitada;
- como a resposta SOAP retorna ao cliente;
- o que o teste verifica e qual resultado foi obtido.

Patrícia e Erick continuam como responsáveis principais pela implementação do servidor e do cliente SOAP. Bruno participa da revisão e conhece o propósito do WSDL e o fluxo geral, sem ficar responsável por implementar essas partes.

### Demonstração e encerramento — todos

1. Explicar o cenário que será demonstrado.
2. Mostrar cada etapa com evidências da comunicação, como a requisição XML, a resposta XML e os registros de execução.
3. Dizer o que foi testado e o que foi observado.
4. Apontar limitações conhecidas e melhorias possíveis.
5. Encerrar resumindo o que o grupo aprendeu sobre contratos de serviço, clientes, protocolos, testes e integração.

## 4. Perguntas que o professor pode fazer

- **O que é SOAP?** Um protocolo de troca de mensagens estruturadas em XML entre aplicações.
- **Para que serve o WSDL?** Para descrever o contrato do serviço, incluindo operações, mensagens e endereço de acesso.
- **Qual é a diferença entre WSDL e SoapUI?** O WSDL documenta o contrato; o SoapUI é uma ferramenta para criar e enviar chamadas de teste.
- **O cliente Java é o servidor?** Não. Ele consome as operações oferecidas pelo servidor SOAP.
- **Como sabemos que o teste passou?** Comparando o resultado observado com o resultado esperado e verificando evidências da chamada e da resposta.

## 5. Checklist antes de apresentar

- [ ] Os comandos de execução deste documento foram substituídos por comandos testados.
- [ ] O serviço SOAP inicia e o WSDL está acessível.
- [ ] O cliente Java consegue executar uma chamada de demonstração.
- [ ] O SoapUI está preparado com pelo menos uma requisição válida.
- [ ] O teste automatizado de Bruno foi executado e está registrado no repositório.
- [ ] A equipe testou o fluxo SOAP completo, do envio da requisição ao recebimento da resposta.
- [ ] Cada integrante consegue explicar a própria parte e o fluxo geral.
- [ ] A demonstração possui alternativa caso a rede ou um serviço falhe.
- [ ] As evidências não contêm senhas, tokens ou dados pessoais.
