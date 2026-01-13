import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.*;
import java.net.InetSocketAddress;
import java.util.Date;
import java.nio.charset.StandardCharsets;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class ApiServer {

    // Instâncias da lógica de negócio (as mesmas dos trabalhos anteriores)
    private static ClienteService clienteService = new ClienteService();
    private static HotelService hotelService = new HotelService();
    private static Gson gson = new Gson();

    public static void main(String[] args) throws IOException {
        int porta = 8080;
        
        // Cria um servidor HTTP leve (nativo do Java)
        HttpServer server = HttpServer.create(new InetSocketAddress(porta), 0);
        System.out.println("=== Servidor API Rodando na porta " + porta + " ===");

        // --- Definindo as Rotas (Endpoints) ---
        
        // 1. Rota para Cadastrar Cliente (POST /clientes)
        server.createContext("/clientes", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                if ("POST".equals(exchange.getRequestMethod())) {
                    // Lê o corpo da requisição (JSON)
                    String jsonBody = lerCorpo(exchange.getRequestBody());
                    JsonObject json = JsonParser.parseString(jsonBody).getAsJsonObject();
                    
                    String nome = json.get("nome").getAsString();
                    String cpf = json.get("cpf").getAsString();
                    
                    // Chama o serviço real
                    Cliente c = clienteService.cadastrarCliente(nome, cpf);
                    
                    // Responde com JSON
                    String resposta = gson.toJson(c);
                    enviarResposta(exchange, 200, resposta);
                } else {
                    enviarResposta(exchange, 405, "Metodo nao permitido");
                }
            }
        });

        // 2. Rota para Reservar (POST /reservas)
        server.createContext("/reservas", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                if ("POST".equals(exchange.getRequestMethod())) {
                    String jsonBody = lerCorpo(exchange.getRequestBody());
                    JsonObject json = JsonParser.parseString(jsonBody).getAsJsonObject();
                    
                    // Extrai dados do JSON vindo do Python/JS
                    // Esperamos um JSON assim: { "nome": "Bruno", "cpf": "123", "quarto": 101 }
                    // Simplificação: Vamos buscar o cliente pelo CPF ou criar um temporário para a busca
                    
                    String cpfCliente = json.get("cpf").getAsString();
                    int numQuarto = json.get("quarto").getAsInt();
                    
                    // Busca cliente existente (se não achar, retorna erro)
                    Cliente cli = clienteService.buscarClientePorCPF(cpfCliente);
                    
                    if (cli != null) {
                        // Faz a reserva
                        Reserva r = hotelService.fazerReserva(cli, numQuarto, new Date(), new Date());
                        if (r != null) {
                            String resposta = gson.toJson(r);
                            enviarResposta(exchange, 200, resposta);
                        } else {
                            enviarResposta(exchange, 400, "{\"erro\": \"Quarto ocupado ou inexistente\"}");
                        }
                    } else {
                        enviarResposta(exchange, 404, "{\"erro\": \"Cliente nao encontrado\"}");
                    }
                }
            }
        });

        server.setExecutor(null); // cria um executor padrão
        server.start();
    }

    // --- Métodos Auxiliares ---

    private static String lerCorpo(InputStream is) throws IOException {
        return new String(is.readAllBytes(), StandardCharsets.UTF_8);
    }

    private static void enviarResposta(HttpExchange exchange, int statusCode, String resposta) throws IOException {
        byte[] bytes = resposta.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json");
        exchange.sendResponseHeaders(statusCode, bytes.length);
        OutputStream os = exchange.getResponseBody();
        os.write(bytes);
        os.close();
    }
}