import java.util.Date;

public class Reserva {
    private int idReserva;
    private Cliente cliente; // Agregação de Cliente
    private Quarto quarto;   // Agregação de Quarto
    private Date dataEntrada;
    private Date dataSaida;
    private String status; // "Pendente", "Confirmada", "Cancelada"

    public Reserva(int idReserva, Cliente cliente, Quarto quarto, Date dataEntrada, Date dataSaida) {
        this.idReserva = idReserva;
        this.cliente = cliente;
        this.quarto = quarto;
        this.dataEntrada = dataEntrada;
        this.dataSaida = dataSaida;
        this.status = "Pendente";
    }

    // Getters
    public int getIdReserva() {
        return idReserva;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public Quarto getQuarto() {
        return quarto;
    }

    public Date getDataEntrada() {
        return dataEntrada;
    }

    public Date getDataSaida() {
        return dataSaida;
    }

    public String getStatus() {
        return status;
    }

    // Setters
    public void setIdReserva(int idReserva) {
        this.idReserva = idReserva;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public void setQuarto(Quarto quarto) {
        this.quarto = quarto;
    }

    public void setDataEntrada(Date dataEntrada) {
        this.dataEntrada = dataEntrada;
    }

    public void setDataSaida(Date dataSaida) {
        this.dataSaida = dataSaida;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Reserva{" +
                "idReserva=" + idReserva +
                ", cliente=" + cliente.getNome() +
                ", quarto=" + quarto.getNumero() +
                ", status='" + status + '\'' +
                '}';
    }
}