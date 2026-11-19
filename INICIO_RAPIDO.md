# INÍCIO RÁPIDO - Projeto SOAP Adoção de Pets

**⏱️ 5 minutos para ter tudo rodando**

---

## 1️⃣ Instalar Dependências (1 min)

```bash
pip install zeep lxml flask
```

---

## 2️⃣ Iniciar Servidor (1 min)

```bash
cd servidor-python
python servidor_alternativo.py
```

**Esperado:**
```
Servidor SOAP Parea Pet iniciado!
Endpoint: http://127.0.0.1:8000/soap
WSDL: http://127.0.0.1:8000/
Aguardando requisições...
```

---

## 3️⃣ Verificar WSDL (1 min)

Abrir browser: http://127.0.0.1:8000/

Deve retornar XML com as 3 operações.

---

## 4️⃣ Testar Cliente Python (1 min)

```bash
python cliente-python-teste.py
```

**Esperado:** `[SUCESSO] TODOS OS TESTES EXECUTADOS COM SUCESSO!`

---

## 5️⃣ Testar Cliente Java (1 min)

```bash
javac -d . adocao/ClienteSoapSimples.java
java -cp . adocao.ClienteSoapSimples
```

**Esperado:** `[SUCESSO] TODOS OS TESTES EXECUTADOS COM SUCESSO!`

---

## ✅ Pronto!

Ambos os clientes funcionando = Interoperabilidade confirmada ✅

---

## 📚 Documentação

- **ROTEIRO_APRESENTACAO.md** - Como apresentar (10 min)
- **DOCUMENTO_ENTREGA.md** - Checklist completo
- **docs/contrato-api.md** - Contrato SOAP detalhado
- **EVIDENCIAS.txt** - Logs dos testes

---

## 🎯 Requisitos Atendidos

✅ Servidor SOAP  
✅ Contrato WSDL  
✅ 3 Operações  
✅ Cliente em linguagem diferente  
✅ Testes completos  
✅ Documentação  

**13/13 TESTES PASSANDO ✅**

---

Pronto para apresentação e entrega! 🚀
