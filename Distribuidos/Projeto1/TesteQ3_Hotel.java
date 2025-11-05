import java.io.FileInputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * Classe principal para testar o ReservaInputStream (Questão 3.b, c, d).
 */
public class TesteQ3_Hotel {

    public static void main(String[] args) {
        
        //Lendo de Arquivo (FileInputStream)
        String nomeArquivo = "reservas.dat";
        System.out.println("=========================================");
        System.out.println("Teste (c): Lendo de Arquivo (" + nomeArquivo + ")");
        try (FileInputStream fis = new FileInputStream(nomeArquivo);
             ReservaInputStream inArquivo = new ReservaInputStream(fis)) {
            
            System.out.println("Lendo objetos do arquivo...");
            Reserva r;
            // Lê objetos até o stream acabar (readReserva() retornar null)
            while ((r = inArquivo.readReserva()) != null) {
                System.out.println("  [LIDO DO ARQUIVO] ID: " + r.getIdReserva() + 
                                   ", Quarto: " + r.getQuarto().getNumero() + 
                                   ", Status: '" + r.getStatus() + "'");
            }
            System.out.println("Fim da leitura do arquivo.");
            
        } catch (IOException e) {
            System.err.println("Erro no teste (c): " + e.getMessage());
            System.err.println("Verifique se o arquivo '" + nomeArquivo + "' existe (foi criado na Q2).");
            e.printStackTrace();
        }
        System.out.println("=========================================\n");


        // Lendo de Servidor Remoto (TCP)
        String host = "localhost";
        int porta = 12346;
        System.out.println("=========================================");
        System.out.println("Teste (d): Lendo de Servidor TCP (" + host + ":" + porta + ")");
        try (Socket socket = new Socket(host, porta);
             ReservaInputStream inRede = new ReservaInputStream(socket.getInputStream())) {
            
            System.out.println("Conectado ao servidor. Lendo objetos da rede...");
            Reserva r;
            while ((r = inRede.readReserva()) != null) {
                System.out.println("  [LIDO DA REDE] ID: " + r.getIdReserva() + 
                                   ", Quarto: " + r.getQuarto().getNumero() + 
                                   ", Status: '" + r.getStatus() + "'");
            }
            System.out.println("Fim da leitura da rede (servidor desconectou).");
            
        } catch (IOException e) {
            System.err.println("Erro no teste (d): Não foi possível conectar ao servidor.");
            System.err.println("Verifique se o 'ServidorTesteQ3_Hotel.java' está rodando.");
        }
        System.out.println("=========================================\n");


        // Lendo da Entrada Padrão (System.in)
        System.out.println("=========================================");
        System.out.println("Teste (b): Lendo da Entrada Padrão (System.in)");
        System.out.println("tem que inserir-> java TesteQ3_Hotel < " + nomeArquivo);
        
        try (ReservaInputStream inPadrao = new ReservaInputStream(System.in)) {
            System.out.println("Aguardando input padrão...");
            Reserva r = inPadrao.readReserva(); // Tenta ler pelo menos um
            if (r != null) {
                System.out.println("  [LIDO DO SYSTEM.IN] ID: " + r.getIdReserva() + 
                                   ", Quarto: " + r.getQuarto().getNumero() + 
                                   ", Status: '" + r.getStatus() + "'");
            } else {
                System.out.println("Nenhum dado lido do System.in.");
            }
        } catch (IOException e) {
            System.err.println("Erro no teste (b): " + e.getMessage());
        }
        System.out.println("=========================================\n");
    }
}