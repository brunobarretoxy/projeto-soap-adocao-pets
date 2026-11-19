#!/usr/bin/env python3
"""
Cliente Python para testar o servidor SOAP
"""
# -*- coding: utf-8 -*-
import sys
import os
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

from zeep import Client

# Conectar ao WSDL
wsdl = 'http://127.0.0.1:8000/'
client = Client(wsdl=wsdl)

print("=" * 70)
print("CLIENTE PYTHON - TESTANDO SERVICO SOAP DE ADOCAO DE PETS")
print("=" * 70)

try:
    # Operacao 1: Cadastrar Usuario
    print("\n[1] CADASTRANDO USUARIO...")
    usuario_response = client.service.cadastrarUsuario(
        nome='Joao Silva',
        email='joao@email.com'
    )
    print(f"[OK] Usuario cadastrado:")
    print(f"   ID: {usuario_response['id']}")
    print(f"   Nome: {usuario_response['nome']}")
    print(f"   Email: {usuario_response['email']}")
    usuario_id = usuario_response['id']
    
    # Operacao 2: Cadastrar Pet
    print("\n[2] CADASTRANDO PET...")
    pet_response = client.service.cadastrarPet(
        nome='Rex',
        especie='Cachorro',
        porte='Grande'
    )
    print(f"[OK] Pet cadastrado:")
    print(f"   ID: {pet_response['id']}")
    print(f"   Nome: {pet_response['nome']}")
    print(f"   Especie: {pet_response['especie']}")
    print(f"   Porte: {pet_response['porte']}")
    print(f"   Status: {pet_response['status']}")
    pet_id = pet_response['id']
    
    # Operacao 3: Adotar Pet
    print("\n[3] REALIZANDO ADOCAO...")
    adocao_response = client.service.adotarPet(
        petId=pet_id,
        usuarioId=usuario_id
    )
    print(f"[OK] {adocao_response}")
    
    # Teste de erro: Tentar adotar o mesmo pet novamente
    print("\n[4] TESTANDO ERRO (tentando adotar pet ja adotado)...")
    try:
        client.service.adotarPet(
            petId=pet_id,
            usuarioId=usuario_id
        )
    except Exception as e:
        print(f"[ERRO ESPERADO] {str(e)}")
    
    # Teste de erro: Email invalido
    print("\n[5] TESTANDO ERRO (email invalido)...")
    try:
        client.service.cadastrarUsuario(
            nome='Maria',
            email='email_invalido_sem_arroba'
        )
    except Exception as e:
        print(f"[ERRO ESPERADO] {str(e)}")
    
    # Cadastrar outro usuario e pet para teste adicional
    print("\n[6] CADASTRANDO SEGUNDO USUARIO...")
    usuario2 = client.service.cadastrarUsuario(
        nome='Mariana Costa',
        email='mariana@email.com'
    )
    print(f"[OK] Segundo usuario cadastrado: {usuario2['nome']} (ID: {usuario2['id']})")
    
    print("\n[7] CADASTRANDO SEGUNDO PET...")
    pet2 = client.service.cadastrarPet(
        nome='Floquinho',
        especie='Gato',
        porte='Pequeno'
    )
    print(f"[OK] Segundo pet cadastrado: {pet2['nome']} (ID: {pet2['id']})")
    
    print("\n[8] ADOTANDO SEGUNDO PET...")
    adocao2 = client.service.adotarPet(
        petId=pet2['id'],
        usuarioId=usuario2['id']
    )
    print(f"[OK] {adocao2}")
    
    print("\n" + "=" * 70)
    print("[SUCESSO] TODOS OS TESTES EXECUTADOS COM SUCESSO!")
    print("=" * 70)

except Exception as e:
    print(f"\n[ERRO]: {str(e)}")
    import traceback
    traceback.print_exc()
