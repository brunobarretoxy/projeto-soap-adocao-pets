from spyne import (
    Application,
    ServiceBase,
    rpc,
    Integer,
    Unicode,
    ComplexModel
)

from spyne.model.fault import Fault
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


# MODELOS

class Pet(ComplexModel):
    id = Integer
    nome = Unicode
    especie = Unicode
    porte = Unicode
    status = Unicode


class Usuario(ComplexModel):
    id = Integer
    nome = Unicode
    email = Unicode


# DADOS EM MEMORIA

pets = []
usuarios = []

proximo_pet_id = 1
proximo_usuario_id = 1


# SERVICO SOAP

class AdocaoPetService(ServiceBase):

    # OPERACAO 1 - CADASTRAR PET
    @rpc(
        Unicode,
        Unicode,
        Unicode,
        _returns=Pet
    )
    def cadastrarPet(ctx, nome, especie, porte):

        global proximo_pet_id

        if not nome or not nome.strip():
            raise Fault(
                faultcode="Client",
                faultstring="O nome do pet e obrigatorio."
            )

        if not especie or not especie.strip():
            raise Fault(
                faultcode="Client",
                faultstring="A especie do pet e obrigatoria."
            )

        if not porte or not porte.strip():
            raise Fault(
                faultcode="Client",
                faultstring="O porte do pet e obrigatorio."
            )

        pet = Pet(
            id=proximo_pet_id,
            nome=nome,
            especie=especie,
            porte=porte,
            status="Disponivel"
        )

        pets.append(pet)
        proximo_pet_id += 1

        return pet

    # OPERACAO 2 - CADASTRAR USUARIO
    @rpc(
        Unicode,
        Unicode,
        _returns=Usuario
    )
    def cadastrarUsuario(ctx, nome, email):

        global proximo_usuario_id

        if not nome or not nome.strip():
            raise Fault(
                faultcode="Client",
                faultstring="O nome do usuario e obrigatorio."
            )

        if not email or not email.strip() or "@" not in email:
            raise Fault(
                faultcode="Client",
                faultstring="Informe um email valido."
            )

        for usuario in usuarios:
            if usuario.email.lower() == email.lower():
                raise Fault(
                    faultcode="Client",
                    faultstring="Este email ja esta cadastrado."
                )

        usuario = Usuario(
            id=proximo_usuario_id,
            nome=nome,
            email=email
        )

        usuarios.append(usuario)
        proximo_usuario_id += 1

        return usuario

    # OPERACAO 3 - ADOTAR PET
    @rpc(
        Integer,
        Integer,
        _returns=Unicode
    )
    def adotarPet(ctx, pet_id, usuario_id):

        pet_encontrado = None
        usuario_encontrado = None

        for pet in pets:
            if pet.id == pet_id:
                pet_encontrado = pet
                break

        for usuario in usuarios:
            if usuario.id == usuario_id:
                usuario_encontrado = usuario
                break

        if pet_encontrado is None:
            raise Fault(
                faultcode="Client",
                faultstring="Pet nao encontrado."
            )

        if usuario_encontrado is None:
            raise Fault(
                faultcode="Client",
                faultstring="Usuario nao encontrado."
            )

        if pet_encontrado.status != "Disponivel":
            raise Fault(
                faultcode="Client",
                faultstring="Este pet nao esta disponivel."
            )

        pet_encontrado.status = "Adotado"

        return (
            f"Adocao realizada com sucesso! "
            f"Pet: {pet_encontrado.nome}. "
            f"Adotante: {usuario_encontrado.nome}."
        )


# CONFIGURACAO SOAP

application = Application(
    [AdocaoPetService],
    tns="urn:pareapet:soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)


# PUBLICACAO DO SERVIDOR

wsgi_application = WsgiApplication(application)


if __name__ == "__main__":

    from wsgiref.simple_server import make_server

    host = "127.0.0.1"
    port = 8000

    print("Servidor SOAP Parea Pet iniciado!")
    print(f"Endpoint: http://{host}:{port}")
    print(f"WSDL: http://{host}:{port}/?wsdl")

    server = make_server(host, port, wsgi_application)
    server.serve_forever()
