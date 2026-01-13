import com.google.gson.Gson;

public class ClienteServiceStub {
    private RmiInfrastructure rmi;
    private Gson gson = new Gson();

    public ClienteServiceStub(RmiInfrastructure rmi) {
        this.rmi = rmi;
    }

    public Cliente cadastrarCliente(String nome, String cpf) {
        String[] args = {nome, cpf};
        String jsonArgs = gson.toJson(args);

        String jsonRetorno = rmi.doOperation("ClienteService", 1, jsonArgs);

        if (jsonRetorno == null || jsonRetorno.equals("null")) return null;
        return gson.fromJson(jsonRetorno, Cliente.class);
    }
}