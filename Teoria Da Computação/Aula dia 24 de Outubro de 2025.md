## Máquinas de Turing

- Definição formal (Definição de Baixo nível)
- Definição de nível de implementação
- Definição de alto nível

Fazendo de cabeça para baixo um exemplo:

1 - Marque o último elemento da entrada

2 - Avance a cabeça de leitura para a direita até encontrar um U, volte uma posição a esquerda e marque o símbolo com *

3 - A construção do próprio autômato.


Exemplo:

M (a primeira linha é uma descrição, a máquina opera sob oque?) 

1. "Sobre uma entrada w ∈ Σ*...

---
---
---

4. Se ... , então aceite, caso contrário, rejeite"


Fazendo essa linguagem em alto nível: $L = {w#w | w ∈ Σ*} onde Σ = {a,b}$
*(O lado esquerdo e direito da hashtag são iguais)*

M = "Sobre uma entrada w:
1. Se a cabeça de leitura inicia sobre #, verifique se existe símbolos não marcados a direita. Se sim, **rejeite**, caso contrário, **aceite.**"
2. Marque o primeiro símbolo não marcado. Verifique se o primeiro símbolo não marcado a direita da # é o mesmo. Se não for, **rejeite**, se não houver símbolos não marcados, também **rejeite.** Caso contrário marque.
3. Volte a cabeça de leitura para a direita do primeiro símbolo marcado no passo 2. Vá para o passo 1.
