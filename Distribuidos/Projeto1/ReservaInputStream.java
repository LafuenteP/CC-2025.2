import java.io.IOException;
import java.io.InputStream;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

/**
 * Questão 3: Subclasse de InputStream para desserializar objetos Reserva.
 * Esta classe lê uma sequência de bytes de um InputStream de origem
 * e os converte de volta em objetos Reserva.
 */
public class ReservaInputStream extends InputStream {

    private final InputStream origem;

    // Tamanhos dos atributos (devem ser idênticos aos do OutputStream)
    private static final int SIZE_ID_RESERVA = 4; // int = 4 bytes
    private static final int SIZE_NUM_QUARTO = 4; // int = 4 bytes
    private static final int SIZE_STATUS = 20;    // 20 bytes para o status

    /**
     * Construtor da subclasse, conforme especificado na Questão 3.a.
     *
     * @param origem (a) um InputStream de origem
     */
    public ReservaInputStream(InputStream origem) {
        this.origem = origem;
    }

    /**
     * Método principal que implementa a lógica de "desserialização".
     * Ele lê os bytes da origem e reconstrói um objeto Reserva.
     *
     * @return Um objeto Reserva, ou null se o stream acabar.
     * @throws IOException
     */
    public Reserva readReserva() throws IOException {
        
        // 1. Ler ID_RESERVA (4 bytes)
        byte[] idBytes = new byte[SIZE_ID_RESERVA];
        int bytesLidos = origem.read(idBytes);
        
        // Se read() retornar -1 ou menos bytes que o esperado, o stream acabou
        if (bytesLidos < SIZE_ID_RESERVA) {
            return null; // Fim do stream
        }
        int idReserva = ByteBuffer.wrap(idBytes).getInt();

        // 2. Ler NUM_QUARTO (4 bytes)
        byte[] quartoBytes = new byte[SIZE_NUM_QUARTO];
        if (origem.read(quartoBytes) < SIZE_NUM_QUARTO) return null; // Stream inesperado
        int numQuarto = ByteBuffer.wrap(quartoBytes).getInt();

        // 3. Ler STATUS (20 bytes)
        byte[] statusBytes = new byte[SIZE_STATUS];
        if (origem.read(statusBytes) < SIZE_STATUS) return null; // Stream inesperado
        String status = new String(statusBytes, StandardCharsets.UTF_8).trim();

        // --- Montando o Objeto de volta ---
        // Como só salvamos os IDs, não temos os dados completos do Cliente
        // ou do Quarto. Criamos "dummies" (objetos parciais) para
        // preencher o construtor da Reserva.
        
        Cliente dummyCliente = new Cliente(0, "N/A", "N/A");
        Quarto dummyQuarto = new QuartoSimples(numQuarto, 0, 0.0, false); // Usamos QuartoSimples como um placeholder

        Reserva reserva = new Reserva(idReserva, dummyCliente, dummyQuarto, null, null);
        reserva.setStatus(status); // Definimos o status que lemos

        return reserva;
    }


    /**
     * Método read() obrigatório da superclasse InputStream.
     * Apenas repassa a chamada para o stream de origem.
     */
    @Override
    public int read() throws IOException {
        return origem.read();
    }
    
    @Override
    public void close() throws IOException {
        System.out.println("[ReservaInputStream] Fechando stream de origem.");
        origem.close();
    }
}