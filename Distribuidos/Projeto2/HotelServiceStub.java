import com.google.gson.Gson;
import java.util.Date;

public class HotelServiceStub {
    private RmiInfrastructure rmi;
    private Gson gson = new Gson();

    public HotelServiceStub(RmiInfrastructure rmi) {
        this.rmi = rmi;
    }

    public Reserva fazerReserva(Cliente cliente, int numeroQuarto, Date dataEntrada, Date dataSaida) {
        Object[] args = {cliente, numeroQuarto, dataEntrada, dataSaida};
        String jsonArgs = gson.toJson(args);

        String jsonRetorno = rmi.doOperation("HotelService", 1, jsonArgs);

        if (jsonRetorno == null || jsonRetorno.equals("null")) return null;
        return gson.fromJson(jsonRetorno, Reserva.class);
    }

    public boolean cancelarReserva(int idReserva) {
        Object[] args = {idReserva};
        String jsonArgs = gson.toJson(args);

        String jsonRetorno = rmi.doOperation("HotelService", 2, jsonArgs);

        return gson.fromJson(jsonRetorno, boolean.class);
    }
}