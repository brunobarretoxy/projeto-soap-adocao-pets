package adocao;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

/**
 * Cliente SOAP simples que consome o serviço sem dependências de frameworks
 */
public class ClienteSoapSimples {

    private static final String ENDPOINT = "http://127.0.0.1:8000/soap";

    public static void main(String[] args) {
        try {
            System.out.println("===================================================================");
            System.out.println("CLIENTE JAVA - TESTANDO SERVICO SOAP DE ADOCAO DE PETS");
            System.out.println("===================================================================");

            // Test 1: Cadastrar Usuario
            System.out.println("\n[1] CADASTRANDO USUARIO...");
            String usuarioXml = sendSoapRequest(
                "<tns:cadastrarUsuario xmlns:tns=\"urn:pareapet:soap\">" +
                "  <nome>Carlos Mendes</nome>" +
                "  <email>carlos@email.com</email>" +
                "</tns:cadastrarUsuario>"
            );
            System.out.println("[OK] Usuario cadastrado");
            int usuarioId = extractIntFromXml(usuarioXml, "id");
            System.out.println("    ID: " + usuarioId);
            System.out.println("    Email: carlos@email.com");

            // Test 2: Cadastrar Pet
            System.out.println("\n[2] CADASTRANDO PET...");
            String petXml = sendSoapRequest(
                "<tns:cadastrarPet xmlns:tns=\"urn:pareapet:soap\">" +
                "  <nome>Thor</nome>" +
                "  <especie>Cachorro</especie>" +
                "  <porte>Medio</porte>" +
                "</tns:cadastrarPet>"
            );
            System.out.println("[OK] Pet cadastrado");
            int petId = extractIntFromXml(petXml, "id");
            System.out.println("    ID: " + petId);
            System.out.println("    Nome: Thor");
            System.out.println("    Status: Disponivel");

            // Test 3: Realizar Adocao
            System.out.println("\n[3] REALIZANDO ADOCAO...");
            String adocaoXml = sendSoapRequest(
                "<tns:adotarPet xmlns:tns=\"urn:pareapet:soap\">" +
                "  <petId>" + petId + "</petId>" +
                "  <usuarioId>" + usuarioId + "</usuarioId>" +
                "</tns:adotarPet>"
            );
            System.out.println("[OK] " + extractTextFromXml(adocaoXml, "result"));

            // Test 4: Testar erro - tentar adotar pet ja adotado
            System.out.println("\n[4] TESTANDO ERRO (tentando adotar pet ja adotado)...");
            try {
                sendSoapRequest(
                    "<tns:adotarPet xmlns:tns=\"urn:pareapet:soap\">" +
                    "  <petId>" + petId + "</petId>" +
                    "  <usuarioId>" + usuarioId + "</usuarioId>" +
                    "</tns:adotarPet>"
                );
            } catch (Exception e) {
                System.out.println("[ERRO ESPERADO] " + e.getMessage());
            }

            // Test 5: Testar erro - email invalido
            System.out.println("\n[5] TESTANDO ERRO (email invalido)...");
            try {
                sendSoapRequest(
                    "<tns:cadastrarUsuario xmlns:tns=\"urn:pareapet:soap\">" +
                    "  <nome>Maria</nome>" +
                    "  <email>email_invalido</email>" +
                    "</tns:cadastrarUsuario>"
                );
            } catch (Exception e) {
                System.out.println("[ERRO ESPERADO] " + e.getMessage());
            }

            System.out.println("\n===================================================================");
            System.out.println("[SUCESSO] TODOS OS TESTES EXECUTADOS COM SUCESSO!");
            System.out.println("===================================================================");

        } catch (Exception e) {
            System.err.println("\n[ERRO]: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static String sendSoapRequest(String soapBody) throws Exception {
        String soapEnvelope = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" +
            "<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">" +
            "  <soap:Body>" +
            soapBody +
            "  </soap:Body>" +
            "</soap:Envelope>";

        URL url = new URL(ENDPOINT);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/xml; charset=UTF-8");
        conn.setDoOutput(true);

        byte[] payload = soapEnvelope.getBytes(StandardCharsets.UTF_8);
        conn.getOutputStream().write(payload);
        conn.getOutputStream().flush();

        int responseCode = conn.getResponseCode();
        InputStream is = (responseCode >= 200 && responseCode < 300) ? 
            conn.getInputStream() : conn.getErrorStream();

        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        int nRead;
        byte[] data = new byte[16384];
        while ((nRead = is.read(data, 0, data.length)) != -1) {
            buffer.write(data, 0, nRead);
        }

        String response = buffer.toString(StandardCharsets.UTF_8);

        if (responseCode >= 400) {
            String faultString = extractTextFromXml(response, "faultstring");
            if (!faultString.isEmpty()) {
                throw new Exception(faultString);
            }
            throw new Exception("HTTP " + responseCode);
        }

        return response;
    }

    private static int extractIntFromXml(String xml, String tagName) {
        String pattern = "<" + tagName + ">";
        int start = xml.indexOf(pattern);
        if (start == -1) return -1;
        start += pattern.length();
        int end = xml.indexOf("</" + tagName + ">", start);
        if (end == -1) return -1;
        try {
            return Integer.parseInt(xml.substring(start, end));
        } catch (Exception e) {
            return -1;
        }
    }

    private static String extractTextFromXml(String xml, String tagName) {
        String pattern = "<" + tagName + ">";
        int start = xml.indexOf(pattern);
        if (start == -1) return "";
        start += pattern.length();
        int end = xml.indexOf("</" + tagName + ">", start);
        if (end == -1) return "";
        return xml.substring(start, end);
    }
}
