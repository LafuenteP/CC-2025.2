import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonParser;

public class ServerMain {
    private static ClienteService clienteServiceReal = new ClienteService();
    private static HotelService hotelServiceReal = new HotelService();

    public static void main(String[] args) {
        clienteServiceReal.cadastrarCliente("Bruno Costa", "222.222.222-22");
        
        RmiInfrastructure rmiHelper = new RmiInfrastructure("localhost", 12347);
        Gson gson = new Gson();

        try (ServerSocket serverSocket = new ServerSocket(12347)) {
            System.out.println("=== Servidor RMI Iniciado na porta 12347 ===");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                try {
                    Message req = rmiHelper.getRequest(clientSocket);
                    String resultadoJson = "null";
                    System.out.println("Req: " + req.getObjectReference() + " ID: " + req.getMethodId());

                    if ("ClienteService".equals(req.getObjectReference())) {
                        if (req.getMethodId() == 1) { // cadastrarCliente
                            String[] argsStr = gson.fromJson(req.getArguments(), String[].class);
                            Cliente novo = clienteServiceReal.cadastrarCliente(argsStr[0], argsStr[1]);
                            resultadoJson = gson.toJson(novo);
                        }
                    } else if ("HotelService".equals(req.getObjectReference())) {
                        if (req.getMethodId() == 1) { // fazerReserva
                            JsonArray array = JsonParser.parseString(req.getArguments()).getAsJsonArray();
                            Cliente cli = gson.fromJson(array.get(0), Cliente.class);
                            int numQuarto = array.get(1).getAsInt();
                            Date entrada = gson.fromJson(array.get(2), Date.class);
                            Date saida = gson.fromJson(array.get(3), Date.class);
                            Reserva r = hotelServiceReal.fazerReserva(cli, numQuarto, entrada, saida);
                            resultadoJson = gson.toJson(r);
                        } else if (req.getMethodId() == 2) { // cancelarReserva
                            JsonArray array = JsonParser.parseString(req.getArguments()).getAsJsonArray();
                            int idReserva = array.get(0).getAsInt();
                            boolean sucesso = hotelServiceReal.cancelarReserva(idReserva);
                            resultadoJson = gson.toJson(sucesso);
                        }
                    }
                    Message reply = new Message(1, req.getRequestId(), req.getObjectReference(), req.getMethodId(), resultadoJson);
                    rmiHelper.sendReply(clientSocket, reply);
                } catch (Exception e) {
                    e.printStackTrace();
                } finally {
                    clientSocket.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}