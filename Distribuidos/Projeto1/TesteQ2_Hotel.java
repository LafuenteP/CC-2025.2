import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Date;


public class TesteQ2_Hotel {

    public static void main(String[] args) {
        
        Cliente cli1 = new Cliente(1, "Ana Silva", "111.111.111-11");
        Cliente cli2 = new Cliente(2, "Bruno Costa", "222.222.222-22");
        
        Quarto q101 = new QuartoSimples(101, 2, 150.0, true);
        Quarto q201 = new Suite(201, 4, 300.0, true);
        
        Reserva[] minhasReservas = new Reserva[2];
        minhasReservas[0] = new Reserva(10, cli1, q101, new Date(), new Date());
        minhasReservas[0].setStatus("Confirmada");
        
        minhasReservas[1] = new Reserva(11, cli2, q201, new Date(), new Date());
        minhasReservas[1].setStatus("Cancelada");

        System.out.println("=========================================");
        System.out.println("Teste (i): Enviando para Saida Padrao (System.out)");
        System.out.println("--- INICIO SAIDA PADRAO (Bytes) ---");
        try {
            ReservaOutputStream outPadrao = new ReservaOutputStream(minhasReservas, 2, System.out);
            outPadrao.writeObjects();
            System.out.flush(); // Garante que os dados sejam escritos
        } catch (IOException e) {
            System.err.println("Erro no teste (i): " + e.getMessage());
        }
        System.out.println("\n--- FIM SAIDA PADRAO ---");
        System.out.println("=========================================\n");


        // Arquivo (FileOutputStream)
        String nomeArquivo = "reservas.dat";
        System.out.println("=========================================");
        System.out.println("Teste (ii): Enviando para Arquivo (" + nomeArquivo + ")");
        try (FileOutputStream fos = new FileOutputStream(nomeArquivo);
             ReservaOutputStream outArquivo = new ReservaOutputStream(minhasReservas, 2, fos)) {
            
            outArquivo.writeObjects();
            System.out.println("Dados escritos em '" + nomeArquivo + "' com sucesso.");

        } catch (IOException e) {
            System.err.println("Erro no teste (ii): " + e.getMessage());
            e.printStackTrace();
        }
        System.out.println("=========================================\n");


        // Servidor Remoto (TCP)
        String host = "localhost";
        int porta = 12345;
        System.out.println("=========================================");
        System.out.println("Teste (iii): Enviando para Servidor TCP (" + host + ":" + porta + ")");
        try (Socket socket = new Socket(host, porta);
             OutputStream outRede = socket.getOutputStream();
             ReservaOutputStream outSocket = new ReservaOutputStream(minhasReservas, 2, outRede)) {
            
            outSocket.writeObjects();
            System.out.println("Dados enviados para o servidor com sucesso.");
            
        } catch (IOException e) {
            System.err.println("Erro no teste (iii): Não foi possível conectar ao servidor.");
            System.err.println("Verifique se o 'ServidorTesteHotel.java' está rodando.");
        }
        System.out.println("=========================================");
    }
}