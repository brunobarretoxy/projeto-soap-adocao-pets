# ROTEIRO DE APRESENTAÇÃO - SOAP ADOÇÃO DE PETS
**Duração: 10 minutos**

---

## 📌 SLIDE 1: INTRODUÇÃO (1 minuto)

**Título:** Projeto SOAP - Serviço de Adoção de Pets

**Pontos-chave:**
- Projeto acadêmico de Serviço Web SOAP
- Demonstra interoperabilidade entre Python e Java
- 3 operações implementadas
- 100% funcional

**Frase de gancho:** "Vamos mostrar como um servidor em Python pode ser consumido por um cliente Java através de SOAP, comprovando verdadeira interoperabilidade!"

---

## 🏗️ SLIDE 2: ARQUITETURA (2 minutos)

**Visual esperado:**
```
Servidor SOAP Python
      ↓
    WSDL + Endpoint (http://127.0.0.1:8000/)
      ↓
    ┌───┴───┐
    ↓       ↓
Cliente    Cliente
Python     Java
(Zeep)    (Manual)
```

**Explicar:**
1. **Servidor:** Python com Flask + lxml
   - Implementa 3 operações SOAP
   - Gera WSDL automaticamente
   - Valida dados de entrada
   - Retorna SOAP Fault para erros

2. **WSDL:** Contrato entre servidor e cliente
   - Define operações, tipos e namespace
   - Acessível em http://127.0.0.1:8000/
   - Permite geração automática de stubs

3. **Clientes:** Consomem via SOAP
   - Python (Zeep): cliente moderno
   - Java: cliente manual para demonstrar SOAP puro

---

## 📋 SLIDE 3: OPERAÇÕES (2 minutos)

**Show slide com 3 operações:**

### 1. cadastrarPet
```
INPUT:  nome, especie, porte
OUTPUT: { id, nome, especie, porte, status="Disponivel" }
ERRO:   SOAP Fault se campos vazios
```

### 2. cadastrarUsuario
```
INPUT:  nome, email
OUTPUT: { id, nome, email }
ERRO:   SOAP Fault se email inválido/duplicado
```

### 3. adotarPet
```
INPUT:  petId, usuarioId
OUTPUT: "Adoção realizada com sucesso! Pet: X. Adotante: Y."
ERRO:   SOAP Fault se recurso não encontrado ou pet já adotado
```

**Destacar:** Cada operação inclui validação de dados e tratamento de erro robusto.

---

## 💻 SLIDE 4: DEMONSTRAÇÃO - SERVIDOR RODANDO (1 minuto)

**Ação ao vivo:**

1. Mostrar terminal com servidor rodando:
   ```
   Servidor SOAP Parea Pet iniciado!
   Endpoint: http://127.0.0.1:8000/soap
   WSDL: http://127.0.0.1:8000/
   Aguardando requisições...
   ```

2. Abrir browser e acessar: `http://127.0.0.1:8000/`
   - Mostrar WSDL com as 3 operações definidas
   - Destacar namespace: `urn:pareapet:soap`

3. Voltar ao terminal e mostrar logs de requisições

---

## 🧪 SLIDE 5: TESTE - CLIENTE PYTHON (2 minutos)

**Ação ao vivo:**

1. Executar: `python cliente-python-teste.py`

2. Mostrar output com sucessos e validações de erro

3. **Explicar:**
   - 8 testes executados com sucesso
   - Validações de erro funcionando corretamente
   - Demonstra interoperabilidade real

---

## ☕ SLIDE 6: TESTE - CLIENTE JAVA (2 minutos)

**Ação ao vivo:**

1. Compilar e executar: `java -cp . adocao.ClienteSoapSimples`

2. Mostrar output com sucessos e validações de erro

3. **Destacar:**
   - 5 testes executados com sucesso
   - **Cliente diferente (Java) consumindo mesmo servidor (Python)**
   - **ISSO DEMONSTRA INTEROPERABILIDADE REAL!**
   - Sem dependências de framework de alta abstração

---

## 📊 SLIDE 7: VALIDAÇÃO DE REQUISITOS (1 minuto)

**Show checklist:**

✅ **Escopo Obrigatório (5/5)**
- Servidor SOAP funcional
- Contrato WSDL funcional
- 3 operações (mínimo 2)
- Cliente em linguagem diferente (Java + Python)
- Testes completos

✅ **Requisitos Técnicos (5/5)**
- Envelope, Body, namespaces corretos
- Publicação local do endpoint
- WSDL auto-gerado
- Validação de chamadas
- Tratamento de erro (SOAP Fault)

---

## 🎓 SLIDE 8: CONCEITOS DEMONSTRADOS (1 minuto)

**Bullet points:**
- SOAP Basics: Envelopment, Body, Faults
- WSDL Contract: Tipos, operações, binding
- XML Namespaces: Identificação de tipos
- HTTP Transport: POST com XML
- SOAP Fault: Tratamento padrão de erros
- **Interoperabilidade Real: Python ↔ Java**

---

## 🏆 SLIDE 9: CONCLUSÃO (1 minuto)

**Pontos principais:**
✅ Projeto 100% funcional
✅ Servidor respondendo corretamente
✅ WSDL acessível e bem-estruturado
✅ 13/13 testes passando (8 Python + 5 Java)
✅ Interoperabilidade comprovada
✅ Documentação completa

---

## Dicas para Apresentação

1. **Tenha 2 terminais abertos:**
   - Um rodando servidor
   - Outro para executar clientes

2. **Tenha browser pronto:**
   - Acesse WSDL para mostrar contrato

3. **Fale pausado:**
   - SOAP é conceito novo para muitos
   - Explique cada componente

4. **Destaque a interoperabilidade:**
   - Esse é o ponto forte do projeto
   - Servidor Python + Cliente Java = real

5. **Respeite o tempo:**
   - 10 minutos passam rápido
   - Evite detalhes muito técnicos
   - Focar no "o quê" e "por quê"

---

**Versão:** 1.0  
**Data:** 2026-11-19  
**Status:** Pronto para apresentação ✅
