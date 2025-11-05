import java.io.IOException;
import java.io.OutputStream;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

/**
 * Questão 2: Subclasse de OutputStream para serializar objetos Reserva.
 */
public class ReservaOutputStream extends OutputStream {

    private final Reserva[] reservas;
    private final int numObjetos;
    private final OutputStream destino;

    // (iii) Definindo os tamanhos dos atributos 
    private static final int SIZE_ID_RESERVA = 4; // int = 4 bytes
    private static final int SIZE_NUM_QUARTO = 4; // int = 4 bytes
    private static final int SIZE_STATUS = 20;    // 20 bytes para o status

    /**
     * Construtor da subclasse. [cite: 9, 10, 11]
     *
     * @param reservas    (i) um array de objetos [cite: 9]
     * @param numObjetos  (ii) o número de Objetos que terão dados enviados [cite: 10]
     * @param destino     (iv) um OutputStream de destino 
     */
    public ReservaOutputStream(Reserva[] reservas, int numObjetos, OutputStream destino) {
        this.reservas = reservas;
        this.numObjetos = numObjetos;
        this.destino = destino;
    }

    /**
     * Método principal que converte Objetos em bytes.
     */
    public void writeObjects() throws IOException {
        for (int i = 0; i < this.numObjetos; i++) {
            Reserva r = this.reservas[i];
            
            // 1. Escrever ID_RESERVA (int - 4 bytes)
            byte[] idBytes = ByteBuffer.allocate(SIZE_ID_RESERVA).putInt(r.getIdReserva()).array();
            destino.write(idBytes);

            // 2. Escrever NUM_QUARTO (int - 4 bytes)
            // (Note: pegamos o número de dentro do objeto Quarto agregado)
            byte[] quartoBytes = ByteBuffer.allocate(SIZE_NUM_QUARTO).putInt(r.getQuarto().getNumero()).array();
            destino.write(quartoBytes);

            // 3. Escrever STATUS (String - 20 bytes)
            byte[] statusBytes = new byte[SIZE_STATUS];
            byte[] statusOriginal = r.getStatus().getBytes(StandardCharsets.UTF_8);
            System.arraycopy(statusOriginal, 0, statusBytes, 0, Math.min(statusOriginal.length, SIZE_STATUS));
            destino.write(statusBytes);
        }
    }

    /**
     * Método write(int b) obrigatório da superclasse OutputStream.
     */
    @Override
    public void write(int b) throws IOException {
        destino.write(b);
    }

    @Override
    public void close() throws IOException {
        System.out.println("[ReservaOutputStream] Fechando stream de destino.");
        destino.close();
    }
}