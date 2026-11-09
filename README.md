# Projeto SOAP de Adoção de Pets

Projeto acadêmico focado em um serviço SOAP para o domínio de adoção de pets. O servidor SOAP é desenvolvido em Python, e o serviço é consumido por um cliente Java e testado no SoapUI.

Este repositório documenta e organiza o projeto SOAP de adoção de pets.

## Objetivos

- Entender como um serviço SOAP publica operações e descreve seu contrato por meio de um WSDL.
- Consumir operações SOAP por meio de um cliente Java e exercitá-las no SoapUI.
- Testar as operações SOAP pelo SoapUI e pelo cliente Java.
- Revisar o projeto, testar o fluxo SOAP completo e preparar a apresentação em conjunto.

## Componentes e responsabilidades

| Integrante | Responsabilidades principais |
|---|---|
| **Patrícia** | Lidera o servidor SOAP em Python e as operações do serviço. |
| **Erick** | Lidera o cliente SOAP em Java, os testes no SoapUI e a documentação/WSDL. |
| **Bruno** | Faz uma contribuição pequena de código: adicionar um teste automatizado para uma operação SOAP existente, com orientação da equipe. Também participa da revisão e da apresentação. |
| **Todos** | Revisar este projeto, testar o fluxo SOAP completo e preparar/apresentar o trabalho em conjunto. |

A divisão organiza o trabalho sem exigir que todos implementem o serviço inteiro. Patrícia e Erick lideram a implementação SOAP; Bruno contribui com um teste delimitado e todos se preparam para explicar o fluxo geral.

## Tecnologias e conceitos

- **SOAP:** protocolo de mensagens estruturadas em XML para troca de dados entre aplicações.
- **WSDL:** documento XML que descreve o serviço SOAP, suas operações, mensagens e endereço de acesso.
- **Cliente SOAP em Java:** aplicação que consulta o contrato e envia requisições ao serviço.
- **SoapUI:** ferramenta para montar e executar requisições de teste, normalmente a partir do WSDL.
## Fluxo SOAP

1. O cliente Java ou o SoapUI consulta o WSDL.
2. O cliente monta uma mensagem SOAP em XML para uma operação disponível.
3. O servidor SOAP em Python recebe e processa a solicitação.
4. O serviço devolve uma resposta SOAP em XML, ou uma falha apropriada.

## Estrutura do repositório

A estrutura de pastas e os comandos de execução devem refletir os arquivos realmente presentes no repositório. Consulte [docs/execucao-e-apresentacao.md](docs/execucao-e-apresentacao.md) para o roteiro de preparação, execução e apresentação.

## Como começar

1. Clone ou baixe o repositório e abra a pasta do projeto no VS Code.
2. Confira as instruções de instalação e execução do projeto SOAP no documento de execução.
3. Instale as dependências indicadas pelos arquivos do projeto (por exemplo, `requirements.txt` para Python ou `pom.xml`/`build.gradle` para Java, se existirem).
4. Inicie o servidor SOAP e execute os testes pelo SoapUI e pelo cliente Java.

## Testes

- **SOAP:** validar operações, dados enviados e respostas no SoapUI e/ou no cliente Java.
- **Fluxo SOAP:** percorrer as operações de serviço previstas e conferir requisições e respostas.
- Registrar o resultado esperado, o resultado observado e eventuais erros; não considerar uma tela aberta como prova de que a comunicação funcionou.

## Documentação relacionada

- [Contrato da API SOAP](docs/contrato-api.md)
- [Guia de apresentação e defesa](docs/guia-apresentacao-e-defesa.md)
- [Roteiro de execução e apresentação](docs/execucao-e-apresentacao.md)
- [Status e divisão do projeto](docs/status-e-divisao-do-projeto.md)
- WSDL: localizar no repositório o arquivo `.wsdl` ou o endereço publicado pelo servidor, quando estiver disponível.

## Integrantes

- Bruno
- Patrícia
- Erick
