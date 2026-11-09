# Contrato da API SOAP — Adoção de Pets

Este documento registra o contrato que os clientes devem seguir para consumir o serviço SOAP. As informações específicas (endereço, namespace, operações, campos e exemplos) precisam ser confirmadas no WSDL e no servidor implementado. Não invente valores: atualize os campos marcados como **A definir** quando o contrato real estiver disponível.

> **Estado atual deste repositório:** não há arquivo WSDL nem código do serviço disponível aqui para confirmar operações ou formatos. Portanto, este documento é um modelo de contrato a preencher e validar com Patrícia e Erick.

## 1. Identificação do serviço

| Item | Valor confirmado |
|---|---|
| Nome do serviço | A definir |
| Finalidade | Disponibilizar operações relacionadas à adoção de pets. Detalhar conforme o escopo implementado. |
| URL do WSDL | A definir |
| Endereço do serviço (endpoint) | A definir |
| Versão SOAP | A definir conforme o WSDL (SOAP 1.1 ou SOAP 1.2) |
| Namespace XML | A definir conforme o WSDL |
| Transporte | A definir conforme o binding do WSDL; em geral, HTTP ou HTTPS |
| Autenticação | A definir. Não presumir que há autenticação se ela não estiver implementada. |

## 2. Como interpretar o contrato

- **WSDL:** descreve o serviço, suas operações, mensagens, tipos de dados e binding/endereço de acesso.
- **Operação:** ação que o serviço oferece, por exemplo, consultar ou cadastrar um recurso; a lista real depende da implementação.
- **Mensagem SOAP:** envelope XML enviado ou recebido durante a chamada.
- **Endpoint:** endereço de rede para o qual o cliente envia a requisição. Não é, por si só, a lista de operações.
- **SoapUI e cliente Java:** consumidores do serviço; devem enviar mensagens compatíveis com o WSDL.

SOAP não é uma API REST: não se deve deduzir que há endpoints REST como `/pets` nem métodos HTTP `GET`, `PUT` ou `DELETE`. Em serviços SOAP, as operações são descritas pelo WSDL e são chamadas por mensagens SOAP conforme o binding configurado.

## 3. Operações publicadas

Preencher uma linha para cada operação existente no WSDL e implementada no servidor. Os nomes abaixo são campos da tabela, não operações sugeridas.

| Operação (nome exato no WSDL) | Finalidade | Entradas e tipos | Resposta e tipos | Pode gerar SOAP Fault? |
|---|---|---|---|---|
| A definir | A definir | A definir | A definir | A definir |

Para cada operação, documentar também:

- quais campos são obrigatórios ou opcionais;
- formatos, limites e validações aplicados;
- o significado dos valores devolvidos;
- as condições de erro conhecidas;
- se a operação altera dados ou apenas consulta informações.

## 4. Formato da mensagem

As chamadas SOAP usam um envelope XML. A estrutura exata, incluindo namespace, cabeçalho, nome da operação e elementos, deve ser copiada do WSDL ou de uma requisição válida gerada pelo SoapUI.

### Modelo ilustrativo — não é uma requisição executável

O exemplo abaixo mostra apenas a forma geral de um envelope SOAP. Substitua os nomes e namespaces pelos definidos no WSDL:

```xml
<soap:Envelope xmlns:soap="NAMESPACE_SOAP" xmlns:svc="NAMESPACE_DO_SERVICO">
  <soap:Header>
    <!-- Cabeçalhos somente se o contrato/serviço exigir -->
  </soap:Header>
  <soap:Body>
    <svc:OPERACAO_DO_WSDL>
      <!-- Elementos e valores definidos pelo WSDL -->
    </svc:OPERACAO_DO_WSDL>
  </soap:Body>
</soap:Envelope>
```

Não envie os textos `NAMESPACE_SOAP`, `NAMESPACE_DO_SERVICO` ou `OPERACAO_DO_WSDL` literalmente. Eles são marcadores para preenchimento a partir do contrato real.

## 5. Respostas e falhas

A resposta bem-sucedida também é uma mensagem SOAP XML. Para cada operação, registrar um exemplo real ou anonimizado depois de testar no SoapUI ou no cliente Java.

| Situação | Como identificar | Comportamento confirmado pelo serviço |
|---|---|---|
| Sucesso | Resposta SOAP correspondente à operação | A definir por operação |
| Dados inválidos ou incompletos | SOAP Fault ou resposta definida pelo serviço | A definir após teste |
| Recurso não encontrado (se aplicável) | SOAP Fault ou resposta definida pelo serviço | A definir após teste |
| Serviço indisponível | Falha de conexão/HTTP observada pelo cliente | A definir após teste |

Em SOAP, erros de aplicação podem ser representados por **SOAP Fault**; o formato e os códigos dependem do serviço. Não presumir códigos HTTP específicos sem verificá-los na implementação e nos testes.

## 6. Regras de uso

Registrar aqui somente regras que o serviço realmente implemente ou que estejam definidas para o trabalho:

- Limites de requisição: A definir / confirmar se aplicável.
- Paginação: A definir / confirmar se aplicável.
- Versionamento do contrato: A definir / confirmar se aplicável.
- Autenticação e autorização: A definir / confirmar se aplicável.
- Dados de exemplo permitidos: usar dados fictícios ou de teste.

## 7. Como validar e manter o contrato

1. Erick identifica no WSDL o serviço, o binding, o endereço e os nomes/tipos das operações.
2. Patrícia confere se o servidor Python implementa esses mesmos nomes, entradas, respostas e falhas.
3. Importar o WSDL no SoapUI e executar ao menos uma chamada válida por operação prioritária.
4. Comparar a mensagem enviada e a resposta observada com o que está documentado aqui.
5. Atualizar este documento quando o WSDL ou o comportamento do servidor mudar.
6. Revisar em conjunto alterações que afetem o cliente Java, o servidor ou os testes.

## 8. Pendências para completar

- [ ] Registrar o caminho do WSDL ou sua URL.
- [ ] Confirmar versão SOAP, namespace, binding e endpoint.
- [ ] Listar todas as operações com os nomes exatos do WSDL.
- [ ] Documentar entradas, tipos, obrigatoriedade e respostas de cada operação.
- [ ] Registrar os SOAP Faults e demais falhas observadas.
- [ ] Validar os exemplos no SoapUI e no cliente Java.
