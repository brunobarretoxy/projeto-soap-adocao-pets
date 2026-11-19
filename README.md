# Projeto SOAP de Adoção de Pets

Projeto acadêmico focado em um serviço SOAP para o domínio de adoção de pets. O servidor SOAP é desenvolvido em Python, e o serviço é consumido por um cliente Java e testado em Python. Este projeto demonstra interoperabilidade entre tecnologias distintas via protocolo SOAP.

**STATUS: ✅ 100% FUNCIONAL E VALIDADO**

## 🎯 Objetivos Alcançados

- ✅ Entender como um serviço SOAP publica operações e descreve seu contrato por meio de um WSDL
- ✅ Consumir operações SOAP por meio de cliente Java e Python
- ✅ Testar as operações SOAP e validar o fluxo completo
- ✅ Demonstrar interoperabilidade entre Python (servidor) e Java (cliente)
- ✅ Implementar tratamento de erros com SOAP Fault
- ✅ Documentar contrato de serviço com exemplos reais

## 🏗️ Arquitetura

```
Servidor SOAP (Python - Flask + lxml)
        ↓
    WSDL + Endpoint
        ↓
    ┌───┴───┐
    ↓       ↓
Cliente Python  Cliente Java
   (Zeep)       (Manual)
```

## 📋 Componentes

| Integrante   | Responsabilidades                                                                |
| ------------ | ---------------------------------------------------------------------- |
| **Patrícia** | Lidera implementação do servidor SOAP em Python e das operações      |
| **Erick**    | Lidera cliente SOAP em Java, testes no SoapUI e documentação/WSDL    |
| **Bruno**    | Implementa testes automatizados, valida fluxo completo e apresentação |
| **Todos**    | Revisão final, testes, apresentação e defesa em conjunto             |

## 🚀 Operações Implementadas

### 1. cadastrarPet
- **Entrada:** nome, especie, porte (strings)
- **Saída:** Pet { id, nome, especie, porte, status }
- **Validação:** Campos obrigatórios
- **Erro:** SOAP Fault com mensagem descritiva

### 2. cadastrarUsuario
- **Entrada:** nome, email (strings)
- **Saída:** Usuario { id, nome, email }
- **Validação:** Email válido, não-duplicado
- **Erro:** SOAP Fault com mensagem descritiva

### 3. adotarPet
- **Entrada:** petId, usuarioId (integers)
- **Saída:** Mensagem de sucesso
- **Validação:** Recursos existem, pet disponível
- **Erro:** SOAP Fault com mensagem descritiva

## 🧪 Testes Executados

### Cliente Python (Zeep) - ✅ 8/8 Testes
```
[1] Cadastrar Usuário ..................... OK
[2] Cadastrar Pet ......................... OK
[3] Realizar Adoção ....................... OK
[4] Erro: Pet já adotado .................. OK (esperado)
[5] Erro: Email inválido .................. OK (esperado)
[6] Cadastrar segundo usuário ............. OK
[7] Cadastrar segundo pet ................. OK
[8] Adotar segundo pet .................... OK
```

### Cliente Java - ✅ 5/5 Testes
```
[1] Cadastrar Usuário ..................... OK
[2] Cadastrar Pet ......................... OK
[3] Realizar Adoção ....................... OK
[4] Erro: Pet já adotado .................. OK (esperado)
[5] Erro: Email inválido .................. OK (esperado)
```

## 🛠️ Tecnologias e Conceitos

- **SOAP:** protocolo de mensagens estruturadas em XML para troca de dados entre aplicações
- **WSDL:** documento XML que descreve o serviço SOAP, suas operações, mensagens e endereço
- **XML Namespaces:** urn:pareapet:soap para identificação de tipos e operações
- **HTTP Transport:** requisições POST com envelope SOAP como payload
- **SOAP Fault:** tratamento padrão de erros em SOAP
- **Interoperabilidade:** servidor em uma linguagem, clientes em outra

## 📁 Estrutura do Repositório

```
projeto-soap-adocao-pets/
├── servidor-python/
│   ├── servidor.py                    # Servidor original (Spyne)
│   ├── servidor_alternativo.py        # Servidor funcional (Flask + lxml)
│   └── requirements.txt               # Dependências
├── cliente-python-teste.py            # Cliente de teste com Zeep
├── adocao/
│   ├── ClienteSoapSimples.java        # Cliente Java
│   └── ClienteSoapSimples.class       # Compilado
├── docs/
│   ├── contrato-api.md                # Contrato com valores reais ✅
│   ├── AdocaoPetsSOAP.wsdl            # WSDL auto-gerado
│   ├── execucao-e-apresentacao.md
│   ├── guia-apresentacao-e-defesa.md
│   ├── status-e-divisao-do-projeto.md
├── VALIDACAO_FINAL.md                 # Validação completa ✅
├── EVIDENCIAS.txt                     # Resultados dos testes ✅
├── README.md                          # Este arquivo
└── .git/                              # Histórico de commits

```

## ✅ Fluxo SOAP Validado

```
1. Cliente Java/Python consulta WSDL
   GET http://127.0.0.1:8000/ → Response: WSDL XML

2. Cliente monta mensagem SOAP
   <soap:Envelope>
     <soap:Body>
       <tns:cadastrarPet>...</tns:cadastrarPet>
     </soap:Body>
   </soap:Envelope>

3. Cliente envia POST para endpoint
   POST http://127.0.0.1:8000/soap
   Content-Type: application/xml

4. Servidor processa e devolve resposta SOAP
   <soap:Envelope>
     <soap:Body>
       <tns:cadastrarPetResponse>
         <result>...</result>
       </tns:cadastrarPetResponse>
     </soap:Body>
   </soap:Envelope>

5. Cliente valida resposta e executa lógica
```

## 🎯 Requisitos Atendidos

### ✅ Escopo Obrigatório (5/5)
- [x] Servidor SOAP (Python - Flask + lxml)
- [x] Contrato WSDL funcional (http://127.0.0.1:8000/)
- [x] Mínimo 2 operações (3 implementadas)
- [x] Cliente consumidor em linguagem diferente (Java + Python)
- [x] Testes completos e validados

### ✅ Requisitos Técnicos Mínimos (5/5)
- [x] Uso correto de Envelope, Body e namespaces SOAP
- [x] Publicação local do endpoint (localhost:8000)
- [x] Geração automática/manual do WSDL
- [x] Validação de chamadas bem-sucedidas
- [x] Tratamento básico de erro com SOAP Fault

### ✅ Restrições Atendidas
- [x] Não utiliza REST ou JSON como mecanismo principal
- [x] Não abstrai totalmente o SOAP

### ✅ Simplificações Permitidas
- [x] Dados simulados em memória
- [x] Operações síncronas
- [x] Endpoints locais (localhost)
- [x] Estrutura procedural simples

## 🚀 Como Executar

### Prerequisitos
- Python 3.9+
- Java 11+ (compilador javac)
- pip (gerenciador de pacotes Python)

### 1. Instalar Dependências
```bash
# Python
pip install zeep lxml flask

# Ou usar requirements.txt
pip install -r servidor-python/requirements.txt
```

### 2. Iniciar Servidor
```bash
cd servidor-python
python servidor_alternativo.py

# Resposta esperada:
# Servidor SOAP Parea Pet iniciado!
# Endpoint: http://127.0.0.1:8000/soap
# WSDL: http://127.0.0.1:8000/
# Aguardando requisições...
```

### 3. Executar Cliente Python
```bash
# Em outro terminal
python cliente-python-teste.py

# Resultado: 8/8 testes com sucesso ✅
```

### 4. Executar Cliente Java
```bash
# Compilar
javac -d . adocao/ClienteSoapSimples.java

# Executar
java -cp . adocao.ClienteSoapSimples

# Resultado: 5/5 testes com sucesso ✅
```

## 📊 Validação de Funcionalidade

- **Servidor Respondendo:** ✅ HTTP 200 em http://127.0.0.1:8000/
- **WSDL Acessível:** ✅ XML bem-formado com operações
- **3 Operações:** ✅ cadastrarPet, cadastrarUsuario, adotarPet
- **Cliente Python:** ✅ 8/8 testes passando
- **Cliente Java:** ✅ 5/5 testes passando
- **Validações:** ✅ SOAP Faults funcionando
- **Interoperabilidade:** ✅ Python-Java confirmada

## 📚 Documentação Relacionada

- **[docs/contrato-api.md](docs/contrato-api.md)** - Contrato SOAP com exemplos reais
- **[docs/AdocaoPetsSOAP.wsdl](docs/AdocaoPetsSOAP.wsdl)** - WSDL auto-gerado
- **[VALIDACAO_FINAL.md](VALIDACAO_FINAL.md)** - Validação completa do projeto
- **[EVIDENCIAS.txt](EVIDENCIAS.txt)** - Logs detalhados dos testes
- **[docs/execucao-e-apresentacao.md](docs/execucao-e-apresentacao.md)** - Roteiro de apresentação
- **[docs/guia-apresentacao-e-defesa.md](docs/guia-apresentacao-e-defesa.md)** - Guia de defesa

## 🎓 Conceitos Implementados

✅ **SOAP Basics:** Envelopment XML, Body, Faults  
✅ **WSDL Contract:** Tipos complexos, operações, binding  
✅ **XML Namespaces:** urn:pareapet:soap  
✅ **HTTP Transport:** POST com XML payload  
✅ **Error Handling:** SOAP Fault com faultcode e faultstring  
✅ **Interoperabilidade:** Python ↔ Java via SOAP  
✅ **Data Persistence:** Memória em sessão  
✅ **Business Rules:** Validações e regras de negócio  

## 🔍 Dificuldades Técnicas Enfrentadas

### 1. Compatibilidade Spyne com Python 3.14
- **Problema:** Spyne 2.14.0 não suporta Python 3.14 (módulo six.moves)
- **Solução:** Implementar servidor alternativo com Flask + lxml
- **Resultado:** Servidor 100% funcional

### 2. Ausência de Maven
- **Problema:** Maven não disponível no ambiente
- **Solução:** Implementar cliente Java que constrói requisições SOAP manualmente
- **Resultado:** Cliente compilado com sucesso

### 3. Encoding de Caracteres
- **Problema:** Console Windows com cp1252, suporta mal UTF-8
- **Solução:** Usar ASCII puro nos testes
- **Resultado:** Output legível

## 🏆 Conclusão

Projeto **100% funcional** demonstrando:
- ✅ Servidor SOAP robusto e interoperável
- ✅ Contrato WSDL bem-estruturado
- ✅ Clientes em múltiplas linguagens (Python, Java)
- ✅ Validação completa de funcionalidades
- ✅ Documentação profissional
- ✅ Pronto para apresentação e avaliação

---

## Integrantes

- Bruno
- Patrícia
- Erick

**Versão:** 1.0 (Final)  
**Data:** 2026-11-19  
**Status:** ✅ Concluído e Validado
