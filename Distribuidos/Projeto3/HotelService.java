import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.List;
public class HotelService {

    //banco de dados de quartos e reservas
    private final List<Quarto> quartos = new ArrayList<>();
    private final List<Reserva> reservas = new ArrayList<>();
    private int proximoIdReserva = 1;

    public HotelService() {
        // Inicializa o hotel com alguns quartos
        quartos.add(new QuartoSimples(101, 2, 150.0, true));
        quartos.add(new QuartoSimples(102, 2, 150.0, false));
        quartos.add(new Suite(201, 4, 300.0, true));
    }

    public Reserva fazerReserva(Cliente cliente, int numeroQuarto, Date dataEntrada, Date dataSaida) {
        Quarto quarto = buscarQuarto(numeroQuarto);
        if (quarto == null) {
            System.out.println("[HotelService] Quarto " + numeroQuarto + " não existe.");
            return null;
        }

        if (quarto.isOcupado()) {
            // Simplificação: só verifica se está ocupado agora, não as datas
            System.out.println("[HotelService] Quarto " + numeroQuarto + " já está ocupado.");
            return null;
        }

        Reserva novaReserva = new Reserva(proximoIdReserva++, cliente, quarto, dataEntrada, dataSaida);
        novaReserva.setStatus("Confirmada");
        quarto.setOcupado(true);
        reservas.add(novaReserva);
        
        System.out.println("[HotelService] Reserva " + novaReserva.getIdReserva() + " confirmada para " + cliente.getNome());
        return novaReserva;
    }

    public boolean cancelarReserva(int idReserva) {
        for (Reserva r : reservas) {
            if (r.getIdReserva() == idReserva) {
                r.setStatus("Cancelada");
                r.getQuarto().setOcupado(false); // Libera o quarto
                System.out.println("[HotelService] Reserva " + idReserva + " cancelada.");
                return true;
            }
        }
        System.out.println("[HotelService] Reserva " + idReserva + " não encontrada.");
        return false;
    }

    private Quarto buscarQuarto(int numero) {
        for (Quarto q : quartos) {
            if (q.getNumero() == numero) {
                return q;
            }
        }
        return null;
    }
    public Collection<Quarto> getQuartosDisponiveis() {
    return quartos; 
}
    public Collection<Reserva> getReservas() {
        return reservas;
    }
}