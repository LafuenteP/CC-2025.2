# Relatório Técnico: Implementação de API REST para Sistema Distribuído de Hotel

**Dupla:** Évila Maria Vasconcelos de Araújo-554162, Lafuente Paulino da Silva-556275  


---

## 1. Introdução

Este relatório descreve a implementação do Trabalho 3, cujo objetivo foi evoluir um sistema de reservas de hotel (anteriormente baseado em RMI) para uma arquitetura orientada a serviços utilizando **API REST** (Application Programming Interface).

O foco principal deste trabalho foi demonstrar a interoperabilidade entre sistemas distribuídos, onde o servidor e os clientes são implementados em linguagens de programação distintas, comunicando-se através do protocolo HTTP e troca de mensagens em formato JSON.

## 2. Arquitetura da Solução

A solução foi desenvolvida seguindo o modelo Cliente-Servidor stateless, eliminando o uso de sockets puros ou middleware de objetos distribuídos (RMI).

### 2.1. Tecnologias Utilizadas

* **Servidor:** Java (JDK 17+).
* **Biblioteca de Serialização:** Google Gson (2.10.1).
* **Servidor Web:** `com.sun.net.httpserver.HttpServer` (Nativo do Java).
* **Cliente 1:** Python 3 (Biblioteca `urllib`).
* **Cliente 2:** JavaScript / Node.js (Módulo `http`).

### 2.2. O Servidor (Java)

O servidor (`ApiServer.java`) foi implementado para escutar na porta `8080`. Diferente da abordagem anterior com `ServerSocket`, aqui utilizamos um servidor HTTP que abstrai a camada de transporte TCP.

A lógica de negócio foi reutilizada integralmente das classes `HotelService` e `ClienteService` do Trabalho 1/2, demonstrando que a regra de negócio independe da camada de comunicação. O servidor mantém o estado dos objetos (lista de clientes, quartos e reservas) em memória durante a execução.

## 3. Descrição da API (Endpoints)

A comunicação segue o protocolo HTTP, utilizando o verbo **POST** para envio de dados e recebimento de resultados.

### 3.1. Recurso: Clientes

* **Rota:** `/clientes`
* **Método:** `POST`
* **Entrada (JSON):**
    ```json
    {
      "nome": "Nome do Cliente",
      "cpf": "000.000.000-00"
    }
    ```
* **Saída (JSON):** Retorna o objeto `Cliente` criado, contendo o ID gerado pelo servidor.

### 3.2. Recurso: Reservas

* **Rota:** `/reservas`
* **Método:** `POST`
* **Entrada (JSON):**
    ```json
    {
      "cpf": "000.000.000-00",
      "quarto": 101
    }
    ```
* **Saída (JSON):** Retorna o objeto `Reserva` completo, incluindo detalhes do quarto (se é Simples ou Suíte), datas de entrada/saída e status de confirmação.

## 4. Interoperabilidade e Clientes Poliglotas

Um dos requisitos fundamentais foi a implementação de clientes em linguagens diferentes da linguagem do servidor. Isso comprovou a neutralidade da API REST.

### 4.1. Cliente Python
O script em Python utilizou a biblioteca padrão `urllib`. Ele foi capaz de serializar um dicionário Python para JSON, enviar a requisição POST e deserializar a resposta do servidor Java, imprimindo o ID do cliente cadastrado.

### 4.2. Cliente JavaScript (Node.js)
O script em Node.js utilizou chamadas assíncronas nativas. Ele consumiu os mesmos endpoints, comprovando que estruturas de dados complexas (como a classe `Suite` que estende `Quarto`) foram corretamente serializadas pelo servidor Java e interpretadas nativamente pelo JavaScript como objetos JSON.

## 5. Conclusão

A migração para API REST simplificou significativamente a arquitetura do sistema em comparação ao uso de Sockets e RMI. A utilização do padrão JSON permitiu um desacoplamento total entre as tecnologias de cliente e servidor.

Os testes realizados demonstraram que o sistema é capaz de:
1.  Receber requisições concorrentes de diferentes plataformas.
2.  Manter a consistência dos dados em memória (ID incremental compartilhado).
3.  Tratar erros (como quarto inexistente ou cliente não encontrado) retornando códigos de status HTTP apropriados (400, 404) ou mensagens de erro em JSON.
