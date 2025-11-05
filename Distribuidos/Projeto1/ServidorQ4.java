import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

/**
 * Questão 4: Servidor TCP que implementa o serviço remoto 'cadastrarCliente'.
 * Ele usa serialização manual (empacotamento/desempacotamento) de bytes.
 */
public class ServidorQ4 {

    private final int PORTA = 12347;
    private ClienteService clienteService; // Serviço da Questão 1

    public ServidorQ4() {
        this.clienteService = new ClienteService();
    }

    public void iniciar() {
        try (ServerSocket serverSocket = new ServerSocket(PORTA)) {
            System.out.println("Servidor (Q4) iniciado na porta " + PORTA + ". Aguardando clientes...");

            while (true) {
                // Bloqueia até um cliente se conectar
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado: " + clientSocket.getInetAddress());
                // Lida com a conexão do cliente
                handleClient(clientSocket);
            }

        } catch (IOException e) {
            System.err.println("Erro no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }

    // Lida com a requisição de um único cliente.
    private void handleClient(Socket clientSocket) {
        try (DataInputStream dis = new DataInputStream(clientSocket.getInputStream());
             DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream())) {

            // Servidor Desempacota a Requisição
            System.out.println("Lendo dados do cliente...");
            
            int nomeLength = dis.readInt();
            byte[] nomeBytes = dis.readNBytes(nomeLength);
            String nome = new String(nomeBytes, StandardCharsets.UTF_8);

            int cpfLength = dis.readInt();
            byte[] cpfBytes = dis.readNBytes(cpfLength);
            String cpf = new String(cpfBytes, StandardCharsets.UTF_8);

            System.out.println("Requisição recebida: {Nome: " + nome + ", CPF: " + cpf + "}");

            //2. Servidor Processa a Lógica de Negócio
            Cliente novoCliente = clienteService.cadastrarCliente(nome, cpf);

            //3. Servidor Empacota a Resposta
            if (novoCliente != null) {
                // Sucesso
                System.out.println("Cliente cadastrado com ID: " + novoCliente.getId());
                dos.writeBoolean(true); // 1 byte (sucesso)
                dos.writeInt(novoCliente.getId()); // 4 bytes (ID)
            } else {
                // Falha (CPF duplicado)
                System.out.println("Falha: CPF já cadastrado.");
                String erroMsg = "Falha ao cadastrar: CPF ja existe.";
                byte[] erroBytes = erroMsg.getBytes(StandardCharsets.UTF_8);

                dos.writeBoolean(false); // 1 byte (falha)
                dos.writeInt(erroBytes.length); // 4 bytes (tamanho do erro)
                dos.write(erroBytes); // N bytes (mensagem de erro)
            }
            
            dos.flush();

        } catch (IOException e) {
            System.err.println("Erro ao comunicar com o cliente: " + e.getMessage());
        } finally {
            try {
                clientSocket.close();
                System.out.println("Cliente desconectado.");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        ServidorQ4 servidor = new ServidorQ4();
        servidor.iniciar();
    }
}