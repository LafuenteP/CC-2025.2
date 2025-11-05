import java.io.FileInputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Servidor TCP para o teste da Questão 3.d.
 * Ele lê o arquivo 'reservas.dat' e envia seu conteúdo para o cliente.
 */
public class ServidorTesteQ3_Hotel {
    public static void main(String[] args) {
        final int PORTA = 12346; // Porta diferente da Q2
        final String ARQUIVO_ENVIAR = "reservas.dat"; // Arquivo criado na Q2

        try (ServerSocket serverSocket = new ServerSocket(PORTA)) {
            System.out.println("Servidor de Teste (Q3) ouvindo na porta " + PORTA + "...");
            System.out.println("Aguardando cliente para enviar '" + ARQUIVO_ENVIAR + "'...");

            Socket clientSocket = serverSocket.accept();
            System.out.println("Cliente conectado: " + clientSocket.getInetAddress());

            try (FileInputStream fis = new FileInputStream(ARQUIVO_ENVIAR);
                 OutputStream out = clientSocket.getOutputStream()) {

                System.out.println("Enviando dados do arquivo...");
                byte[] buffer = new byte[1024];
                int bytesLidos;
                while ((bytesLidos = fis.read(buffer)) != -1) {
                    out.write(buffer, 0, bytesLidos);
                }
                out.flush();
                System.out.println("Arquivo enviado com sucesso.");

            } catch (Exception e) {
                System.err.println("Erro ao enviar arquivo: " + e.getMessage());
            }
            clientSocket.close();
            System.out.println("Conexão com cliente fechada.");

        } catch (Exception e) {
            System.err.println("Erro no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}