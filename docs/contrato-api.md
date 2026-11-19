# Contrato SOAP - Serviço de Adoção de Pets

**Versão:** 1.0  
**Data:** 2026-11-19  
**Status:** Validado e Funcional  

---

## 📋 Visão Geral

Contrato formal (WSDL) do Serviço Web SOAP de Adoção de Pets. Define as operações disponíveis, tipos de dados e regras de negócio.

**Namespace:** `urn:pareapet:soap`  
**Versão SOAP:** 1.1  
**Estilo:** Document/Literal  
**Transporte:** HTTP POST  

---

## 🎯 Operações

### 1. cadastrarPet

Registra um novo pet no sistema.

#### Entrada (Request)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:tns="urn:pareapet:soap">
  <soap:Body>
    <tns:cadastrarPet>
      <nome>Rex</nome>
      <especie>Cachorro</especie>
      <porte>Grande</porte>
    </tns:cadastrarPet>
  </soap:Body>
</soap:Envelope>
```

#### Saída (Response - Sucesso)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:tns="urn:pareapet:soap">
  <soap:Body>
    <tns:cadastrarPetResponse>
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

#### Saída (Response - Erro)

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

#### Parâmetros

| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| nome | String | Sim | Nome do pet (máx 100 chars) |
| especie | String | Sim | Espécie (Cachorro, Gato, Passaro, etc) |
| porte | String | Sim | Porte (Pequeno, Medio, Grande) |

#### Validações

- ✅ Todos os campos são obrigatórios
- ✅ Nome não pode estar vazio
- ✅ Espécie não pode estar vazia
- ✅ Porte não pode estar vazio
- ✅ Sem limites de quantidade

#### Retorno

Objeto `Pet` com:
- `id`: Identificador único (incrementado automaticamente)
- `nome`: Nome do pet
- `especie`: Espécie do pet
- `porte`: Porte do pet
- `status`: Status do pet (inicialmente "Disponivel")

#### Erros Possíveis

- **Code: Client, Message: "O nome do pet é obrigatório."** - Nome vazio
- **Code: Client, Message: "A especie do pet é obrigatória."** - Espécie vazia
- **Code: Client, Message: "O porte do pet é obrigatório."** - Porte vazio

---

### 2. cadastrarUsuario

Registra um novo usuário no sistema.

#### Entrada (Request)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:tns="urn:pareapet:soap">
  <soap:Body>
    <tns:cadastrarUsuario>
      <nome>Joao Silva</nome>
      <email>joao@email.com</email>
    </tns:cadastrarUsuario>
  </soap:Body>
</soap:Envelope>
```

#### Saída (Response - Sucesso)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:tns="urn:pareapet:soap">
  <soap:Body>
    <tns:cadastrarUsuarioResponse>
      <result>
        <id>1</id>
        <nome>Joao Silva</nome>
        <email>joao@email.com</email>
      </result>
    </tns:cadastrarUsuarioResponse>
  </soap:Body>
</soap:Envelope>
```

#### Saída (Response - Erro)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>Client</faultcode>
      <faultstring>Informe um email válido.</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

#### Parâmetros

| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| nome | String | Sim | Nome do usuário (máx 100 chars) |
| email | String | Sim | Email válido (máx 100 chars) |

#### Validações

- ✅ Nome obrigatório
- ✅ Email obrigatório
- ✅ Email deve seguir formato válido (conter @)
- ✅ Email não pode ser duplicado

#### Retorno

Objeto `Usuario` com:
- `id`: Identificador único (incrementado automaticamente)
- `nome`: Nome do usuário
- `email`: Email do usuário

#### Erros Possíveis

- **Code: Client, Message: "O nome do usuario é obrigatório."** - Nome vazio
- **Code: Client, Message: "Informe um email válido."** - Email vazio ou inválido
- **Code: Client, Message: "Este email já foi cadastrado."** - Email duplicado

---

### 3. adotarPet

Realiza uma adoção de pet por um usuário.

#### Entrada (Request)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:tns="urn:pareapat:soap">
  <soap:Body>
    <tns:adotarPet>
      <petId>1</petId>
      <usuarioId>1</usuarioId>
    </tns:adotarPet>
  </soap:Body>
</soap:Envelope>
```

#### Saída (Response - Sucesso)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:tns="urn:pareapet:soap">
  <soap:Body>
    <tns:adotarPetResponse>
      <result>Adoção realizada com sucesso! Pet: Rex. Adotante: Joao Silva.</result>
    </tns:adotarPetResponse>
  </soap:Body>
</soap:Envelope>
```

#### Saída (Response - Erro)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>Client</faultcode>
      <faultstring>Este pet não está disponível.</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

#### Parâmetros

| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| petId | Integer | Sim | ID do pet a ser adotado |
| usuarioId | Integer | Sim | ID do usuário que vai adotar |

#### Validações

- ✅ petId deve ser um inteiro válido
- ✅ usuarioId deve ser um inteiro válido
- ✅ Pet deve existir no sistema
- ✅ Usuário deve existir no sistema
- ✅ Pet deve ter status "Disponivel" (não pode estar já adotado)

#### Regras de Negócio

- Quando um pet é adotado, seu status muda para "Adotado"
- Um pet adotado não pode ser adotado novamente
- Cada adoção registra a relação entre usuário e pet

#### Retorno

String com mensagem de sucesso no formato:  
`"Adoção realizada com sucesso! Pet: [NOME]. Adotante: [NOME]."`

#### Erros Possíveis

- **Code: Client, Message: "Pet nao encontrado."** - ID do pet inválido
- **Code: Client, Message: "Usuario nao encontrado."** - ID do usuário inválido
- **Code: Client, Message: "Este pet não está disponível."** - Pet já foi adotado

---

## 📊 Tipos de Dados

### Pet

```
{
  id: Integer (autoincrementado)
  nome: String (máx 100)
  especie: String (máx 50)
  porte: String (Pequeno|Medio|Grande)
  status: String (Disponivel|Adotado)
}
```

### Usuario

```
{
  id: Integer (autoincrementado)
  nome: String (máx 100)
  email: String (máx 100, único)
}
```

---

## 🔄 Fluxo Típico de Uso

```
1. cadastrarUsuario(nome, email)
   ↓ Retorna: Usuario { id: 1, nome, email }

2. cadastrarPet(nome, especie, porte)
   ↓ Retorna: Pet { id: 1, nome, especie, porte, status: "Disponivel" }

3. adotarPet(petId: 1, usuarioId: 1)
   ↓ Retorna: "Adoção realizada com sucesso! Pet: X. Adotante: Y."
   ↓ Pet agora tem status: "Adotado"

4. adotarPet(petId: 1, usuarioId: 2) ← ERRO: Pet não disponível
```

---

## 🌐 Endpoint

**URL:** `http://127.0.0.1:8000/soap`  
**Método:** POST  
**Content-Type:** `application/xml` ou `text/xml`  

---

## 📄 WSDL

**URL:** `http://127.0.0.1:8000/`

WSDL auto-gerado. Contém definição completa de tipos, operações e binding.

---

## ✅ Conformidade

- ✅ SOAP 1.1 compliant
- ✅ Document/Literal style
- ✅ XML Schema validation
- ✅ SOAP Faults para erros
- ✅ Namespaces corretamente utilizados

---

## 📝 Notas

- Dados armazenados em memória durante a sessão do servidor
- IDs são auto-incrementados iniciando em 1
- Sem persistência em banco de dados (simulado)
- Apropriado para fins acadêmicos

---

**Versão:** 1.0  
**Data:** 2026-11-19  
**Status:** ✅ Validado e Funcional
