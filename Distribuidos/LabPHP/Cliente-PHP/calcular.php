<?php
  $num1 = $_GET['num1'] ?? 0;
  $num2 = $_GET['num2'] ?? 0;
  $operacao = $_GET['operacao'] ?? 'somar';
  $url = "http://localhost:8080/$operacao/$num1/$num2";

  // Usa stream context em vez de cURL
  $context = stream_context_create([
    'http' => [
      'method' => 'GET',
      'timeout' => 10
    ]
  ]);

  try {
    $resposta = @file_get_contents($url, false, $context);
    
    if ($resposta === false) {
      die("Erro na requisição: Não foi possível conectar ao servidor em $url");
    }
  } catch (Exception $e) {
    die("Erro na requisição: " . $e->getMessage());
  }

  // Redireciona para a página de resultado
  header("Location: resultado.php?resposta=" . urlencode($resposta));
?>