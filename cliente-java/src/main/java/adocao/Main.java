package adocao;

import adocao.ws.AdocaoPetService;
import adocao.ws.Application;
import adocao.ws.Pet;
import adocao.ws.Usuario;
import jakarta.xml.ws.BindingProvider;
import jakarta.xml.ws.soap.SOAPFaultException;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        try {
            AdocaoPetService service = new AdocaoPetService();
            Application port = service.getApplication();

            String endpointUrl = "http://127.0.0.1:8000/";
            BindingProvider bp = (BindingProvider) port;
            bp.getRequestContext().put(BindingProvider.ENDPOINT_ADDRESS_PROPERTY, endpointUrl);

            System.out.println("=== CLIENTE JAVA CONECTADO AO SERVIDOR PYTHON (PAREA PET) ===");

            System.out.println("\n-> 1. Cadastrando usuário...");
            Usuario usuario = port.cadastrarUsuario("Carlos Mendes", "carlos@email.com");
            BigInteger idUsuario = usuario.getId().getValue();
            System.out.println("Sucesso! Usuário ID: " + idUsuario + " | Nome: " + usuario.getNome().getValue());

            System.out.println("\n-> 2. Cadastrando pet...");
            Pet pet = port.cadastrarPet("Thor", "Cachorro", "Medio");
            BigInteger idPet = pet.getId().getValue();
            System.out.println("Sucesso! Pet ID: " + idPet
                    + " | Nome: " + pet.getNome().getValue()
                    + " | Porte: " + pet.getPorte().getValue()
                    + " | Status: " + pet.getStatus().getValue());

            System.out.println("\n-> 3. Realizando adoção...");
            String respostaAdocao = port.adotarPet(idPet, idUsuario);
            System.out.println("Servidor respondeu: " + respostaAdocao);

            System.out.println("\n-> 4. Testando regra de negócio (tentando adotar o mesmo pet de novo)...");
            port.adotarPet(idPet, idUsuario);

        } catch (SOAPFaultException fault) {
            System.out.println("Validação do servidor Python funcionou: " + fault.getFault().getFaultString());
        } catch (Exception e) {
            System.err.println("Erro de conexão com o servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}