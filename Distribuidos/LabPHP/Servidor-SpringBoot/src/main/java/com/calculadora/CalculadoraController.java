package com.calculadora;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CalculadoraController {

    @GetMapping("/somar/{num1}/{num2}")
    public String somar(@PathVariable double num1, @PathVariable double num2) {
        double resultado = num1 + num2;
        return String.valueOf(resultado);
    }

    @GetMapping("/subtrair/{num1}/{num2}")
    public String subtrair(@PathVariable double num1, @PathVariable double num2) {
        double resultado = num1 - num2;
        return String.valueOf(resultado);
    }

    @GetMapping("/multiplicar/{num1}/{num2}")
    public String multiplicar(@PathVariable double num1, @PathVariable double num2) {
        double resultado = num1 * num2;
        return String.valueOf(resultado);
    }

    @GetMapping("/dividir/{num1}/{num2}")
    public String dividir(@PathVariable double num1, @PathVariable double num2) {
        if (num2 == 0) {
            return "Erro: Divisão por zero!";
        }
        double resultado = num1 / num2;
        return String.valueOf(resultado);
    }
}
