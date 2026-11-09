# Guia de apresentação e defesa

Este guia ajuda o grupo a apresentar e explicar o projeto SOAP de adoção de pets. Os detalhes entre colchetes devem ser preenchidos com informações reais do servidor, do cliente e do WSDL. Não apresentem como implementado algo que ainda não foi concluído ou testado.

## 1. Objetivo da apresentação

Explicar o problema que o serviço pretende resolver, mostrar como uma chamada SOAP percorre o sistema e comprovar o funcionamento com uma demonstração ou evidência de teste.

A ideia principal a transmitir é:

> Um cliente usa o contrato do serviço para montar uma mensagem SOAP; o servidor Python recebe a chamada, executa uma operação e devolve uma resposta. O cliente Java e o SoapUI podem consumir esse serviço.

## 2. Divisão das falas

### Abertura — todos

Uma pessoa pode iniciar com esta fala, ajustando o texto ao estado real do projeto:

> “Nosso projeto implementa um serviço SOAP relacionado à adoção de pets. O serviço é desenvolvido em Python, seu contrato é descrito pelo WSDL e ele pode ser consumido por um cliente Java ou testado pelo SoapUI. Vamos apresentar o objetivo, o fluxo de uma requisição e os testes realizados.”

### Patrícia — servidor e operações

Patrícia explica a parte principal do servidor:

- qual necessidade do domínio de adoção o serviço atende;
- quais operações estão realmente implementadas;
- quais dados cada operação recebe e o que devolve;
- como o servidor trata entradas inválidas ou falhas, conforme o comportamento existente.

Fala de apoio:

> “Eu fiquei responsável pelo servidor SOAP em Python. Ele disponibiliza as operações [nomes reais]. Quando recebe uma mensagem SOAP para uma dessas operações, processa os dados e devolve [resumo da resposta real].”

### Erick — contrato, cliente Java e SoapUI

Erick apresenta como outros programas conhecem e chamam o serviço:

- onde está o WSDL ou como acessá-lo;
- como o WSDL descreve operações, mensagens, tipos e endereço;
- como o cliente Java consome uma operação;
- como o SoapUI foi usado para montar e conferir requisições e respostas.

Fala de apoio:

> “Eu fiquei responsável pelo cliente Java, pelo WSDL e pelos testes no SoapUI. O cliente chama a operação [nome real] enviando [resumo dos dados] e recebe [resumo da resposta].”

### Bruno — contribuição delimitada e fluxo

Bruno apresenta o teste automatizado que adicionou para uma operação existente. Não precisa explicar a implementação interna completa do servidor ou do cliente.

Fala de apoio:

> “Minha contribuição de código foi um teste automatizado para a operação [nome real]. O teste envia ou prepara [dados usados] e verifica [resultado esperado]. Também revisei o fluxo: o cliente envia a requisição SOAP, o servidor processa a operação e a resposta volta ao cliente.”

Se o teste automatizado ainda não estiver pronto, não afirmem que está concluído: mostrem apenas a parte realizada e expliquem honestamente o que falta.

### Encerramento — todos

> “Com o projeto, praticamos a definição de um contrato de serviço, a comunicação por mensagens SOAP, o consumo por um cliente e a validação por testes. Também verificamos a importância de manter o WSDL, o servidor e os clientes compatíveis.”

## 3. Roteiro da demonstração

Antes da apresentação, escolham uma operação real e confirmem o nome e os dados no WSDL e no código.

1. Mostrar o serviço em execução, se o ambiente permitir.
2. Mostrar o WSDL ou explicar onde está o contrato.
3. No SoapUI, abrir uma requisição para uma operação existente.
4. Apontar os principais dados no corpo XML da requisição, sem ler cada tag.
5. Enviar a chamada e mostrar a resposta recebida.
6. Se preparado, executar também o teste automatizado de Bruno ou uma chamada pelo cliente Java.
7. Se houver tempo, mostrar um caso de falha previsto e explicar o resultado observado.
8. Relacionar a demonstração com o fluxo: cliente → requisição SOAP → operação do servidor → resposta SOAP.

Não exibam credenciais, tokens ou dados pessoais. Tenham capturas ou registros de uma execução anterior como plano alternativo para problemas de rede ou ambiente.

## 4. Conceitos para a defesa

### API, operação e endpoint

- **API:** contrato/intermediário que permite a um programa solicitar capacidades ou dados de outro sistema.
- **Operação SOAP:** ação nomeada e descrita no contrato, que o serviço executa ao receber uma chamada.
- **Endpoint:** endereço de rede onde o cliente alcança o serviço. O endpoint não é, sozinho, a lista de operações.

### SOAP e WSDL

- **SOAP:** protocolo de mensagens; neste projeto, as mensagens são estruturadas em XML.
- **WSDL:** descrição do contrato do serviço. Ajuda os clientes e ferramentas a conhecer operações e formatos esperados.
- **SoapUI:** ferramenta para consumir e testar o serviço; não é o servidor e não substitui o WSDL.

### Cliente e servidor

- O **servidor Python** oferece as operações e processa as chamadas.
- O **cliente Java** solicita operações e interpreta as respostas.
- O **SoapUI** também atua como cliente para facilitar testes manuais.

### Envelope, Header e Body

- **Envelope:** elemento externo que identifica a mensagem SOAP.
- **Header:** cabeçalhos opcionais, quando definidos ou necessários.
- **Body:** contém a operação solicitada e seus dados; a resposta traz o resultado da operação.

Explique apenas os elementos que aparecem no contrato real do projeto.

### SOAP Fault e status HTTP

- **SOAP Fault** é uma estrutura SOAP usada para comunicar determinados erros do serviço.
- **Status HTTP** pertence à resposta de transporte HTTP; não é sinônimo de operação SOAP nem substitui automaticamente o conteúdo SOAP.
- Na defesa, descreva o que foi observado nos testes. Não invente códigos ou formatos de erro.

## 5. Perguntas prováveis e respostas curtas

**Por que usar SOAP neste projeto?**  
“Porque o trabalho explora serviços baseados em mensagens XML e um contrato formal descrito pelo WSDL. A escolha também permite praticar consumo e testes interoperáveis.”

**O que o WSDL resolve?**  
“Documenta como consumir o serviço: operações disponíveis, mensagens e tipos de dados, além das informações de binding e endereço publicadas.”

**O WSDL executa a operação?**  
“Não. Ele descreve o contrato. Quem executa a operação é o servidor.”

**O SoapUI é a API?**  
“Não. É uma ferramenta cliente que ajuda a enviar chamadas e inspecionar respostas.”

**Quem inicia a comunicação?**  
“Normalmente o cliente envia uma requisição ao endpoint do serviço. O servidor processa e responde.”

**Como vocês sabem que uma operação funciona?**  
“Executamos uma chamada com dados conhecidos e comparamos a resposta observada ao resultado esperado. Também verificamos o teste [citar teste real].”

**O que acontece se a requisição estiver errada?**  
“Depende das validações implementadas. No nosso teste, observamos [descrever o resultado real; por exemplo, SOAP Fault ou mensagem de erro].”

**Como o cliente Java sabe o formato esperado?**  
“Ele pode usar as informações do WSDL e precisa enviar uma mensagem compatível com o contrato.”

**O WSDL e o servidor podem divergir?**  
“Sim. Por isso comparamos o contrato com a implementação e validamos as chamadas no cliente e no SoapUI.”

**O serviço possui autenticação, paginação ou versionamento?**  
“Respondemos conforme o que está implementado e documentado. Se não estiver implementado, dizemos que não faz parte da versão atual.”

## 6. Como responder quando não souber

- Não inventar uma resposta nem afirmar que algo foi implementado sem evidência.
- Explicar o que foi verificado no código, no WSDL ou nos testes.
- Se for uma melhoria futura, identificar claramente como proposta, não como funcionalidade pronta.
- Se uma pergunta for sobre detalhes de outra parte, passar a palavra ao integrante responsável e completar com o fluxo geral.

## 7. Checklist de ensaio

- [ ] Preencher os nomes reais das operações e os exemplos conforme o WSDL.
- [ ] Conferir que servidor, cliente, WSDL e testes estão coerentes.
- [ ] Ensaiar a demonstração pelo menos uma vez na ordem planejada.
- [ ] Confirmar que cada pessoa consegue explicar sua contribuição e o fluxo SOAP.
- [ ] Bruno consegue explicar o teste que escreveu e o resultado esperado.
- [ ] Patrícia consegue explicar o processamento das operações no servidor.
- [ ] Erick consegue explicar o WSDL, o cliente Java e os testes SoapUI.
- [ ] Preparar evidência alternativa caso a demonstração ao vivo falhe.
- [ ] Remover ou ocultar dados sensíveis das telas e capturas.
