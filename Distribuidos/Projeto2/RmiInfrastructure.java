import java.io.*;
import java.net.*;
import com.google.gson.Gson;

public class RmiInfrastructure {
    private String serverIp;
    private int serverPort;
    private Gson gson = new Gson();

    public RmiInfrastructure(String serverIp, int serverPort) {
        this.serverIp = serverIp;
        this.serverPort = serverPort;
    }

    public String doOperation(String objectRef, int methodId, String jsonArgs) {
        try (Socket socket = new Socket(serverIp, serverPort);
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             DataInputStream in = new DataInputStream(socket.getInputStream())) {

            int reqId = (int) (System.currentTimeMillis() % 10000);
            Message req = new Message(0, reqId, objectRef, methodId, jsonArgs);
            String jsonReq = gson.toJson(req);

            out.writeUTF(jsonReq); // Envia

            String jsonReply = in.readUTF(); // Recebe
            Message reply = gson.fromJson(jsonReply, Message.class);

            return reply.getArguments();

        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public Message getRequest(Socket clientSocket) throws IOException {
        DataInputStream in = new DataInputStream(clientSocket.getInputStream());
        String jsonReq = in.readUTF();
        return gson.fromJson(jsonReq, Message.class);
    }

    public void sendReply(Socket clientSocket, Message replyMsg) throws IOException {
        DataOutputStream out = new DataOutputStream(clientSocket.getOutputStream());
        String jsonReply = gson.toJson(replyMsg);
        out.writeUTF(jsonReply);
    }
}