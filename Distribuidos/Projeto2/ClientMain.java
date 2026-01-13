import java.util.Date;

public class ClientMain {
    public static void main(String[] args) {
        RmiInfrastructure rmi = new RmiInfrastructure("localhost", 12347);
        HotelServiceStub hotelStub = new HotelServiceStub(rmi);
        ClienteServiceStub clienteStub = new ClienteServiceStub(rmi);

        System.out.println("--- Teste RMI ---");
        
        // 1. Usa o Stub de Cliente
        Cliente c = clienteStub.cadastrarCliente("Ana Teste", "123.456.789-00");
        if(c != null) System.out.println("Cliente Cadastrado: " + c.getNome());

        // 2. Usa o Stub de Hotel
        // Usando o cliente retornado pelo servidor ou um novo com mesmo ID
        if(c == null) c = new Cliente(1, "Bruno Costa", "222.222.222-22");

        System.out.println("Tentando reservar...");
        Reserva r = hotelStub.fazerReserva(c, 101, new Date(), new Date());
        
        if (r != null) {
            System.out.println("Reserva OK! ID: " + r.getIdReserva());
            boolean cancelou = hotelStub.cancelarReserva(r.getIdReserva());
            System.out.println("Reserva Cancelada? " + cancelou);
        } else {
            System.out.println("Falha na reserva.");
        }
    }
}