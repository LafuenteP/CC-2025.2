// cliente.js
const http = require('http');

function enviarPost(path, dados) {
    const data = JSON.stringify(dados);

    const options = {
        hostname: 'localhost',
        port: 8080,
        path: path,
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': data.length
        }
    };

    const req = http.request(options, (res) => {
        let body = '';
        res.on('data', (chunk) => body += chunk);
        res.on('end', () => {
            console.log(`\nRESPOSTA (${path}): Status ${res.statusCode}`);
            console.log("Dados:", body);
        });
    });

    req.on('error', (error) => {
        console.error(error);
    });

    req.write(data);
    req.end();
}

console.log("--- Cliente JavaScript (Node) ---");

// 1. Cadastrar um cliente diferente
setTimeout(() => {
    console.log("Enviando cadastro...");
    enviarPost('/clientes', {
        nome: "Cliente Javascript",
        cpf: "999.999.999-99"
    });
}, 1000);

// 2. Tentar reservar (Quarto diferente, o 201)
setTimeout(() => {
    console.log("Enviando reserva...");
    enviarPost('/reservas', {
        cpf: "999.999.999-99",
        quarto: 201
    });
}, 2000);