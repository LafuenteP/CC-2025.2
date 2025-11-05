import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

/**
 * Servidor TCP simples
 */
public class ServidorTesteHotel {
    public static void main(String[] args) {
        final int PORTA = 12345;
        
        try (ServerSocket serverSocket = new ServerSocket(PORTA)) {
            System.out.println("Servidor de Teste (Q2-Hotel) ouvindo na porta " + PORTA + "...");
            System.out.println("Aguardando conexão do cliente...");

            Socket clientSocket = serverSocket.accept(); // Aguarda uma conexão
            System.out.println("Cliente conectado: " + clientSocket.getInetAddress());

            InputStream in = clientSocket.getInputStream();
            byte[] buffer = new byte[1024];
            int bytesLidos;

            System.out.println("--- Dados Recebidos do Cliente ---");
            while ((bytesLidos = in.read(buffer)) != -1) {
                //imprimir os bytes como Hexadecimal para ver os dados brutos
                for (int i = 0; i < bytesLidos; i++) {
                    System.out.printf("%02X ", buffer[i]);
                }
            }
            System.out.println("\n--- Fim dos Dados ---");
            System.out.println("Conexão com cliente fechada.");

        } catch (Exception e) {
            System.err.println("Erro no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}