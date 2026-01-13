import java.util.ArrayList;
import java.util.List;

public class ClienteService {

    //banco de dados de clientes
    private List<Cliente> clientes = new ArrayList<>();
    private int proximoId = 1;

    public Cliente cadastrarCliente(String nome, String cpf) {
        // Verifica se o CPF já existe
        if (buscarClientePorCPF(cpf) != null) {
            System.out.println("[ClienteService] CPF " + cpf + " já cadastrado.");
            return null;
        }
        Cliente novoCliente = new Cliente(proximoId++, nome, cpf);
        clientes.add(novoCliente);
        System.out.println("[ClienteService] Cliente cadastrado: " + nome);
        return novoCliente;
    }

    public Cliente buscarClientePorCPF(String cpf) {
        for (Cliente c : clientes) {
            if (c.getCpf().equals(cpf)) {
                return c;
            }
        }
        return null; // Não encontrado
    }
}