import java.io.Serializable;

public class Message implements Serializable {
    private int messageType;      // 0 = Request, 1 = Reply
    private int requestId;        // ID da mensagem
    private String objectReference; // Nome do serviço (ex: "HotelService")
    private int methodId;         // ID do método
    private String arguments;     // JSON com os dados

    public Message(int messageType, int requestId, String objectReference, int methodId, String arguments) {
        this.messageType = messageType;
        this.requestId = requestId;
        this.objectReference = objectReference;
        this.methodId = methodId;
        this.arguments = arguments;
    }

    public int getMessageType() { return messageType; }
    public int getRequestId() { return requestId; }
    public String getObjectReference() { return objectReference; }
    public int getMethodId() { return methodId; }
    public String getArguments() { return arguments; }
}