#!/usr/bin/env python3
"""
Servidor SOAP alternativo para Adoção de Pets - Compatible com Python 3.14
Usa Flask + lxml para definir um serviço SOAP puro
"""

from flask import Flask, request, Response
from lxml import etree
from io import BytesIO
import json

app = Flask(__name__)

# Dados em memória
pets = {}
usuarios = {}
next_pet_id = 1
next_usuario_id = 1

# Namespaces
SOAP_NS = "http://schemas.xmlsoap.org/soap/envelope/"
XSD_NS = "http://www.w3.org/2001/XMLSchema"
TNS = "urn:pareapet:soap"

def make_soap_response(body_content):
    """Cria envelope SOAP de resposta"""
    root = etree.Element(
        "{%s}Envelope" % SOAP_NS,
        nsmap={
            "soap": SOAP_NS,
            "xsd": XSD_NS,
            "tns": TNS
        }
    )
    body = etree.SubElement(root, "{%s}Body" % SOAP_NS)
    body.append(body_content)
    return etree.tostring(root, encoding='UTF-8', xml_declaration=True, pretty_print=True)

def make_soap_fault(faultcode, faultstring):
    """Cria SOAP Fault"""
    root = etree.Element(
        "{%s}Envelope" % SOAP_NS,
        nsmap={"soap": SOAP_NS}
    )
    body = etree.SubElement(root, "{%s}Body" % SOAP_NS)
    fault = etree.SubElement(body, "{%s}Fault" % SOAP_NS)
    
    code = etree.SubElement(fault, "faultcode")
    code.text = faultcode
    
    string = etree.SubElement(fault, "faultstring")
    string.text = faultstring
    
    return etree.tostring(root, encoding='UTF-8', xml_declaration=True, pretty_print=True)

@app.route('/', methods=['GET'])
def wsdl():
    """Retorna o WSDL do serviço"""
    wsdl_content = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://schemas.xmlsoap.org/wsdl/"
             xmlns:tns="urn:pareapet:soap"
             xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"
             xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/"
             xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema"
             name="AdocaoPetService"
             targetNamespace="urn:pareapet:soap">

    <types>
        <xsd:schema targetNamespace="urn:pareapet:soap">
            <xsd:complexType name="Pet">
                <xsd:sequence>
                    <xsd:element name="id" type="xsd:integer"/>
                    <xsd:element name="nome" type="xsd:string"/>
                    <xsd:element name="especie" type="xsd:string"/>
                    <xsd:element name="porte" type="xsd:string"/>
                    <xsd:element name="status" type="xsd:string"/>
                </xsd:sequence>
            </xsd:complexType>
            
            <xsd:complexType name="Usuario">
                <xsd:sequence>
                    <xsd:element name="id" type="xsd:integer"/>
                    <xsd:element name="nome" type="xsd:string"/>
                    <xsd:element name="email" type="xsd:string"/>
                </xsd:sequence>
            </xsd:complexType>
        </xsd:schema>
    </types>

    <message name="cadastrarPetRequest">
        <part name="nome" type="xsd:string"/>
        <part name="especie" type="xsd:string"/>
        <part name="porte" type="xsd:string"/>
    </message>
    <message name="cadastrarPetResponse">
        <part name="result" type="tns:Pet"/>
    </message>

    <message name="cadastrarUsuarioRequest">
        <part name="nome" type="xsd:string"/>
        <part name="email" type="xsd:string"/>
    </message>
    <message name="cadastrarUsuarioResponse">
        <part name="result" type="tns:Usuario"/>
    </message>

    <message name="adotarPetRequest">
        <part name="petId" type="xsd:integer"/>
        <part name="usuarioId" type="xsd:integer"/>
    </message>
    <message name="adotarPetResponse">
        <part name="result" type="xsd:string"/>
    </message>

    <portType name="AdocaoPetServicePort">
        <operation name="cadastrarPet">
            <input message="tns:cadastrarPetRequest"/>
            <output message="tns:cadastrarPetResponse"/>
        </operation>
        <operation name="cadastrarUsuario">
            <input message="tns:cadastrarUsuarioRequest"/>
            <output message="tns:cadastrarUsuarioResponse"/>
        </operation>
        <operation name="adotarPet">
            <input message="tns:adotarPetRequest"/>
            <output message="tns:adotarPetResponse"/>
        </operation>
    </portType>

    <binding name="AdocaoPetServiceBinding" type="tns:AdocaoPetServicePort">
        <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="cadastrarPet">
            <soap:operation soapAction="cadastrarPet"/>
            <input><soap:body use="literal"/></input>
            <output><soap:body use="literal"/></output>
        </operation>
        <operation name="cadastrarUsuario">
            <soap:operation soapAction="cadastrarUsuario"/>
            <input><soap:body use="literal"/></input>
            <output><soap:body use="literal"/></output>
        </operation>
        <operation name="adotarPet">
            <soap:operation soapAction="adotarPet"/>
            <input><soap:body use="literal"/></input>
            <output><soap:body use="literal"/></output>
        </operation>
    </binding>

    <service name="AdocaoPetService">
        <port name="AdocaoPetServicePort" binding="tns:AdocaoPetServiceBinding">
            <soap:address location="http://127.0.0.1:8000/soap"/>
        </port>
    </service>
</definitions>'''
    return Response(wsdl_content, mimetype='application/xml')

@app.route('/soap', methods=['POST'])
def soap_handler():
    """Handler principal do serviço SOAP"""
    global next_pet_id, next_usuario_id
    
    try:
        # Parse da requisição SOAP
        tree = etree.parse(BytesIO(request.data))
        root = tree.getroot()
        
        # Extrai o body
        body = root.find('{%s}Body' % SOAP_NS)
        if body is None:
            return Response(
                make_soap_fault('Client', 'Envelope inválido'),
                mimetype='application/xml',
                status=500
            )
        
        # Identifica a operação
        for child in body:
            tag = child.tag
            operation = tag.split('}')[-1] if '}' in tag else tag
            
            # OPERAÇÃO 1: cadastrarPet
            if operation == 'cadastrarPet':
                nome = child.findtext('{%s}nome' % TNS) or child.findtext('nome')
                especie = child.findtext('{%s}especie' % TNS) or child.findtext('especie')
                porte = child.findtext('{%s}porte' % TNS) or child.findtext('porte')
                
                if not nome or not nome.strip():
                    return Response(
                        make_soap_fault('Client', 'O nome do pet é obrigatório.'),
                        mimetype='application/xml',
                        status=400
                    )
                if not especie or not especie.strip():
                    return Response(
                        make_soap_fault('Client', 'A espécie do pet é obrigatória.'),
                        mimetype='application/xml',
                        status=400
                    )
                if not porte or not porte.strip():
                    return Response(
                        make_soap_fault('Client', 'O porte do pet é obrigatório.'),
                        mimetype='application/xml',
                        status=400
                    )
                
                pet_id = next_pet_id
                next_pet_id += 1
                
                pets[pet_id] = {
                    'id': pet_id,
                    'nome': nome,
                    'especie': especie,
                    'porte': porte,
                    'status': 'Disponivel'
                }
                
                # Monta resposta
                response_elem = etree.Element('{%s}cadastrarPetResponse' % TNS)
                result = etree.SubElement(response_elem, 'result')
                pet = pets[pet_id]
                for key, val in pet.items():
                    el = etree.SubElement(result, key)
                    el.text = str(val)
                
                return Response(
                    make_soap_response(response_elem),
                    mimetype='application/xml'
                )
            
            # OPERAÇÃO 2: cadastrarUsuario
            elif operation == 'cadastrarUsuario':
                nome = child.findtext('{%s}nome' % TNS) or child.findtext('nome')
                email = child.findtext('{%s}email' % TNS) or child.findtext('email')
                
                if not nome or not nome.strip():
                    return Response(
                        make_soap_fault('Client', 'O nome do usuário é obrigatório.'),
                        mimetype='application/xml',
                        status=400
                    )
                if not email or '@' not in email:
                    return Response(
                        make_soap_fault('Client', 'Informe um email válido.'),
                        mimetype='application/xml',
                        status=400
                    )
                
                # Verifica email duplicado
                for u in usuarios.values():
                    if u['email'].lower() == email.lower():
                        return Response(
                            make_soap_fault('Client', 'Este email já está cadastrado.'),
                            mimetype='application/xml',
                            status=400
                        )
                
                usuario_id = next_usuario_id
                next_usuario_id += 1
                
                usuarios[usuario_id] = {
                    'id': usuario_id,
                    'nome': nome,
                    'email': email
                }
                
                # Monta resposta
                response_elem = etree.Element('{%s}cadastrarUsuarioResponse' % TNS)
                result = etree.SubElement(response_elem, 'result')
                usuario = usuarios[usuario_id]
                for key, val in usuario.items():
                    el = etree.SubElement(result, key)
                    el.text = str(val)
                
                return Response(
                    make_soap_response(response_elem),
                    mimetype='application/xml'
                )
            
            # OPERAÇÃO 3: adotarPet
            elif operation == 'adotarPet':
                pet_id_str = child.findtext('{%s}petId' % TNS) or child.findtext('petId')
                usuario_id_str = child.findtext('{%s}usuarioId' % TNS) or child.findtext('usuarioId')
                
                try:
                    pet_id = int(pet_id_str)
                    usuario_id = int(usuario_id_str)
                except (ValueError, TypeError):
                    return Response(
                        make_soap_fault('Client', 'IDs devem ser números inteiros.'),
                        mimetype='application/xml',
                        status=400
                    )
                
                if pet_id not in pets:
                    return Response(
                        make_soap_fault('Client', 'Pet não encontrado.'),
                        mimetype='application/xml',
                        status=404
                    )
                if usuario_id not in usuarios:
                    return Response(
                        make_soap_fault('Client', 'Usuário não encontrado.'),
                        mimetype='application/xml',
                        status=404
                    )
                
                pet = pets[pet_id]
                if pet['status'] != 'Disponivel':
                    return Response(
                        make_soap_fault('Client', 'Este pet não está disponível.'),
                        mimetype='application/xml',
                        status=400
                    )
                
                usuario = usuarios[usuario_id]
                pet['status'] = 'Adotado'
                
                msg = f"Adoção realizada com sucesso! Pet: {pet['nome']}. Adotante: {usuario['nome']}."
                
                # Monta resposta
                response_elem = etree.Element('{%s}adotarPetResponse' % TNS)
                result = etree.SubElement(response_elem, 'result')
                result.text = msg
                
                return Response(
                    make_soap_response(response_elem),
                    mimetype='application/xml'
                )
        
        return Response(
            make_soap_fault('Client', 'Operação não reconhecida.'),
            mimetype='application/xml',
            status=400
        )
    
    except Exception as e:
        return Response(
            make_soap_fault('Server', f'Erro interno: {str(e)}'),
            mimetype='application/xml',
            status=500
        )

if __name__ == '__main__':
    print("Servidor SOAP Parea Pet iniciado!")
    print("Endpoint: http://127.0.0.1:8000/soap")
    print("WSDL: http://127.0.0.1:8000/?wsdl")
    print("Aguardando requisições...")
    app.run(host='127.0.0.1', port=8000, debug=False)
