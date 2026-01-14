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
import java.util.Collection;

public class ApiServer {

    private static ClienteService clienteService = new ClienteService();
    private static HotelService hotelService = new HotelService();
    private static Gson gson = new Gson();

    public static void main(String[] args) throws IOException {
        int porta = 8080;
        HttpServer server = HttpServer.create(new InetSocketAddress(porta), 0);
        System.out.println("=== Servidor API (v3.0 Final) Rodando na porta " + porta + " ===");

        // --- ROTA: CLIENTES ---
        server.createContext("/clientes", exchange -> {
            addCorsHeaders(exchange);
            String metodo = exchange.getRequestMethod();

            if ("POST".equals(metodo)) {
                String jsonBody = lerCorpo(exchange.getRequestBody());
                JsonObject json = JsonParser.parseString(jsonBody).getAsJsonObject();
                String nome = json.get("nome").getAsString();
                String cpf = json.get("cpf").getAsString();
                Cliente c = clienteService.cadastrarCliente(nome, cpf);
                enviarResposta(exchange, 200, gson.toJson(c));
            } 
            else if ("GET".equals(metodo)) {
                // NOVA FUNCIONALIDADE: Listar Clientes
                // (Assumindo que ClienteService tem uma lista interna, senão retornamos vazio por enquanto)
                // OBS: Para funcionar perfeito, adicione um getter no ClienteService (veja abaixo do código)
                Collection<Cliente> lista = clienteService.getClientes(); 
                enviarResposta(exchange, 200, gson.toJson(lista));
            }
            else if ("OPTIONS".equals(metodo)) {
                enviarResposta(exchange, 204, "");
            } else {
                enviarResposta(exchange, 405, "Metodo nao permitido");
            }
        });

        // --- ROTA: QUARTOS ---
        server.createContext("/quartos", exchange -> {
            addCorsHeaders(exchange);
            if ("GET".equals(exchange.getRequestMethod())) {
                Collection<Quarto> lista = hotelService.getQuartosDisponiveis(); 
                enviarResposta(exchange, 200, gson.toJson(lista));
            } else {
                enviarResposta(exchange, 204, ""); // OPTIONS ou outros
            }
        });

        // --- ROTA: RESERVAS (ATUALIZADA COM LISTAGEM) ---
        server.createContext("/reservas", exchange -> {
            addCorsHeaders(exchange);
            String metodo = exchange.getRequestMethod();

            if ("POST".equals(metodo)) {
                String jsonBody = lerCorpo(exchange.getRequestBody());
                JsonObject json = JsonParser.parseString(jsonBody).getAsJsonObject();
                String cpf = json.get("cpf").getAsString();
                int numQuarto = json.get("quarto").getAsInt();
                
                Cliente cli = clienteService.buscarClientePorCPF(cpf);
                if (cli != null) {
                    Reserva r = hotelService.fazerReserva(cli, numQuarto, new Date(), new Date());
                    if (r != null) {
                        enviarResposta(exchange, 200, gson.toJson(r));
                    } else {
                        enviarResposta(exchange, 400, "{\"erro\": \"Quarto ocupado ou invalido\"}");
                    }
                } else {
                    enviarResposta(exchange, 404, "{\"erro\": \"Cliente nao encontrado\"}");
                }
            } 
            else if ("DELETE".equals(metodo)) {
                String jsonBody = lerCorpo(exchange.getRequestBody());
                JsonObject json = JsonParser.parseString(jsonBody).getAsJsonObject();
                int idReserva = json.get("idReserva").getAsInt();
                
                boolean sucesso = hotelService.cancelarReserva(idReserva);
                if (sucesso) {
                    enviarResposta(exchange, 200, "{\"status\": \"Reserva cancelada com sucesso\"}");
                } else {
                    enviarResposta(exchange, 404, "{\"erro\": \"Reserva nao encontrada\"}");
                }
            }
            else if ("GET".equals(metodo)) {
                // AGORA SIM: Retorna a lista real de reservas
                Collection<Reserva> lista = hotelService.getReservas();
                enviarResposta(exchange, 200, gson.toJson(lista));
            }
            else if ("OPTIONS".equals(metodo)) {
                enviarResposta(exchange, 204, "");
            }
        });

        server.setExecutor(null);
        server.start();
    }

    private static void addCorsHeaders(HttpExchange exchange) {
        exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().add("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS");
        exchange.getResponseHeaders().add("Access-Control-Allow-Headers", "Content-Type");
    }

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