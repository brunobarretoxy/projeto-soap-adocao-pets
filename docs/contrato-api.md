# Contrato da API SOAP — Adoção de Pets

Este documento registra o contrato que os clientes devem seguir para consumir o serviço SOAP. As informações foram validadas no servidor e nos clientes (Python e Java).

## 1. Identificação do serviço

| Item                           | Valor confirmado                                                           |
| ------------------------------ | -------------------------------------------------------------------------- |
| Nome do serviço                | Serviço SOAP de Adoção de Pets - Parea Pet                                 |
| Finalidade                     | Disponibilizar operações para cadastro de pets e usuários, e adoções       |
| URL do WSDL                    | `http://127.0.0.1:8000/`                                                   |
| Endereço do serviço (endpoint) | `http://127.0.0.1:8000/soap`                                               |
| Versão SOAP                    | SOAP 1.1                                                                   |
| Namespace XML                  | `urn:pareapet:soap`                                                        |
| Transporte                     | HTTP                                                                       |
| Autenticação                   | Não implementada (serviço acadêmico)                                       |

## 2. Como interpretar o contrato

- **WSDL:** descreve o serviço, suas operações, mensagens, tipos de dados e binding/endereço de acesso.
- **Operação:** ação que o serviço oferece, como cadastrar um pet, cadastrar um usuário ou realizar uma adoção.
- **Mensagem SOAP:** envelope XML enviado ou recebido durante a chamada.
- **Endpoint:** endereço `http://127.0.0.1:8000/soap` para o qual o cliente envia requisições.
- **SoapUI e cliente Java/Python:** consumidores do serviço; devem enviar mensagens compatíveis com o WSDL.

SOAP não é uma API REST: não há endpoints como `/pets` nem métodos HTTP `GET`, `PUT` ou `DELETE`. Em serviços SOAP, as operações são descritas pelo WSDL e são chamadas por mensagens SOAP conforme o binding configurado.

## 3. Operações publicadas

| Operação       | Finalidade                           | Entradas e tipos                                   | Resposta e tipos                                | Pode gerar SOAP Fault? |
| -------------- | ------------------------------------ | -------------------------------------------------- | ----------------------------------------------- | ---------------------- |
| cadastrarPet   | Cadastrar um pet no sistema          | nome (String), especie (String), porte (String)   | Pet (id, nome, especie, porte, status)          | Sim                    |
| cadastrarUsuario | Cadastrar um usuário/adotante        | nome (String), email (String)                      | Usuario (id, nome, email)                       | Sim                    |
| adotarPet      | Realizar a adoção de um pet por um usuário | petId (Integer), usuarioId (Integer)         | String (mensagem de confirmação)                | Sim                    |

### Detalhes por operação:

#### 3.1 cadastrarPet
- **Campos obrigatórios:** nome, especie, porte
- **Formato:** todos são strings não-vazias
- **Resposta:** objeto Pet com status "Disponivel" (padrão)
- **Erros:**
  - Se nome estiver vazio: `"O nome do pet é obrigatório."`
  - Se especie estiver vazia: `"A espécie do pet é obrigatória."`
  - Se porte estiver vazio: `"O porte do pet é obrigatório."`

#### 3.2 cadastrarUsuario
- **Campos obrigatórios:** nome, email
- **Formato:** nome é string não-vazia; email deve conter "@"
- **Resposta:** objeto Usuario com id, nome, email
- **Erros:**
  - Se nome estiver vazio: `"O nome do usuário é obrigatório."`
  - Se email inválido (sem "@"): `"Informe um email válido."`
  - Se email já cadastrado: `"Este email já está cadastrado."`

#### 3.3 adotarPet
- **Campos obrigatórios:** petId (Integer), usuarioId (Integer)
- **Validações:**
  - Pet deve existir (caso contrário: `"Pet não encontrado."`)
  - Usuário deve existir (caso contrário: `"Usuário não encontrado."`)
  - Pet deve estar com status "Disponivel" (caso contrário: `"Este pet não está disponível."`)
- **Resposta:** String com mensagem de sucesso como "Adoção realizada com sucesso! Pet: [nome]. Adotante: [nome]."
- **Efeito colateral:** altera o status do pet para "Adotado"

## 4. Formato da mensagem

As chamadas SOAP usam um envelope XML com estrutura padrão SOAP 1.1:

### Exemplo de requisição - cadastrarPet

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <tns:cadastrarPet xmlns:tns="urn:pareapet:soap">
      <nome>Rex</nome>
      <especie>Cachorro</especie>
      <porte>Grande</porte>
    </tns:cadastrarPet>
  </soap:Body>
</soap:Envelope>
```

### Exemplo de resposta bem-sucedida

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <tns:cadastrarPetResponse xmlns:tns="urn:pareapet:soap">
      <result>
        <id>1</id>
        <nome>Rex</nome>
        <especie>Cachorro</especie>
        <porte>Grande</porte>
        <status>Disponivel</status>
      </result>
    </tns:cadastrarPetResponse>
  </soap:Body>
</soap:Envelope>
```

## 5. Respostas e falhas

| Situação                       | Como identificar                       | Comportamento confirmado pelo serviço |
| ------------------------------ | -------------------------------------- | ------------------------------------- |
| Sucesso                        | HTTP 200, envelope com resposta        | Retorna objeto com dados e status 200 |
| Validação falhou (nome vazio)  | HTTP 400, SOAP Fault com faultstring   | Fault com mensagem específica         |
| Validação falhou (email inválido) | HTTP 400, SOAP Fault com faultstring | Fault com mensagem específica         |
| Recurso não encontrado         | HTTP 404, SOAP Fault com faultstring   | Fault: "Pet não encontrado."          |
| Regra de negócio violada       | HTTP 400, SOAP Fault com faultstring   | Fault: "Este pet não está disponível" |

### Exemplo de SOAP Fault (erro)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>Client</faultcode>
      <faultstring>O nome do pet é obrigatório.</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

## 6. Regras de uso

- **Sem limite de requisição:** aceita múltiplas chamadas sem throttling (serviço acadêmico)
- **Sem paginação:** não aplicável (dados em memória, volume pequeno)
- **Sem versionamento:** versão única (não é mencionada no contrato)
- **Sem autenticação:** acesso aberto (serviço local)
- **Dados simulados:** todos os dados são armazenados em memória durante a execução

## 7. Como validar e manter o contrato

1. ✅ Contrato WSDL está disponível em `http://127.0.0.1:8000/`
2. ✅ Servidor Python implementa as operações com os nomes e tipos corretos
3. ✅ Cliente Python (zeep) executou com sucesso todas as operações
4. ✅ Cliente Java compilado e testado com êxito
5. ✅ Validação de erros confirmada (SOAP Faults gerados corretamente)
6. ✅ Este documento foi atualizado com valores reais

## 8. Validação completa

- [x] WSDL acessível e funcional
- [x] Servidor respondendo em http://127.0.0.1:8000/
- [x] Cliente Python validando todas as 3 operações
- [x] Cliente Java executando operações com sucesso
- [x] Tratamento de erros (Faults) funcionando
- [x] Dados persistindo em memória durante sessão

