
### Máquina de Turing onde w != a^n b^n


O jeito correto é marcar um A e marcar um B, se a máquina parar enquanto eles estiverem iguais = erro, caso contrário, aceita.

![[Sem título.jpg]]

### MT, Número de a's é o dobro do numero de b's

![[Sem título-1.jpg]]

Lógica que precisa ser implementada:

define um inicial, e percorre a fita, se no inicial tiver vazio, aceita, se não tiver, marca o inicial
dai pra frente, toda vez que achar um b, marca ele como B e marca 2 a's como A's, e vai repetindo, se todos os b's acabarem e sobrar a's não marcados, rejeita, se tiver b e faltar a, rejeita, se tudo acabar ao mesmo tempo, aceita.

### MT para uma linguagem w | ww

### j) L10​={ww} (Cópia exata)

_O problema é achar onde termina o primeiro w e começa o segundo._ **Lógica da Máquina:**

1. **Achar o Meio:**
    
    - Troque o 1º símbolo por X e o último por Y.
        
    - Troque o 2º por X e o penúltimo por Y.
        
    - Vá fechando o cerco. Se eles se encontrarem sem sobrar letra no meio (comprimento par) → Ótimo. Agora você sabe que os X são o 1º w e os Y são o 2º w.
        
2. **Comparar:**
    
    - Volte ao início. O 1º X era originalmente um `a` ou `b`? (Você precisa de marcadores diferentes para Xa​ e Xb​ na fase 1 para saber disso).
        
    - Verifique se o 1º Y corresponde ao mesmo tipo original.
        
    - Repita para todos. Se todos baterem → **ACEITA**.

