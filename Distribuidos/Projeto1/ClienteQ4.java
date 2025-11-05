import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

/**
 * Questão 4: Cliente TCP que consome o serviço remoto 'cadastrarCliente'.
 * Ele usa serialização manual (empacotamento/desempacotamento) de bytes.
 */
public class ClienteQ4 {

    private final String HOST = "localhost";
    private final int PORTA = 12347;

    public void cadastrarNovoCliente(String nome, String cpf) {
        System.out.println("Tentando conectar a " + HOST + ":" + PORTA + "...");
        try (Socket socket = new Socket(HOST, PORTA);
             DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
             DataInputStream dis = new DataInputStream(socket.getInputStream())) {

            System.out.println("Conectado! Enviando dados de cadastro...");

            //Empacota a Requisição
            byte[] nomeBytes = nome.getBytes(StandardCharsets.UTF_8);
            byte[] cpfBytes = cpf.getBytes(StandardCharsets.UTF_8);

            //Protocolo
            dos.writeInt(nomeBytes.length);
            dos.write(nomeBytes);
            dos.writeInt(cpfBytes.length);
            dos.write(cpfBytes);
            dos.flush(); // Garante que os dados sejam enviados

            System.out.println("Dados enviados. Aguardando resposta do servidor...");

            //Desempacota a Resposta
            boolean sucesso = dis.readBoolean();

            if (sucesso) {
                // Sucesso
                int novoId = dis.readInt();
                System.out.println("RESPOSTA: Sucesso! Novo cliente cadastrado com ID: " + novoId);
            } else {
                // Falha
                int erroLength = dis.readInt();
                byte[] erroBytes = dis.readNBytes(erroLength);
                String erroMsg = new String(erroBytes, StandardCharsets.UTF_8);
                System.err.println("RESPOSTA: " + erroMsg);
            }

        } catch (IOException e) {
            System.err.println("Erro no cliente: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        ClienteQ4 cliente = new ClienteQ4();
        
        // Cadastro com Sucesso
        System.out.println("Cadastro com Sucesso");
        cliente.cadastrarNovoCliente("Bruno Costa", "222.222.222-22");
        
        System.out.println("\nCPF Duplicado");
        // Tenta cadastrar o mesmo CPF de novo (é pra dar erro)
        cliente.cadastrarNovoCliente("Ana Silva", "222.222.222-22");
    }
}