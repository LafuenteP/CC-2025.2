### Primeira questão:

![[Pasted image 20251117224745.png]]

#### A)

1. Estou em Q1, leio 0, Me locomovo para q2, Escrevo U e vou para direita
2. Estou em q2, leio U, vou para o estado de aceitação, escrevo U e vou para direita.

#### B)

1. Estou em q1, leio 0, me locomovo para q2, Escrevo U e vou para direita
2. Estou em q2, leio 0, me locomovo para q3, escrevo X e vou para a direita
3. Estou em q3, leio U, me locomovo para q5, escrevo U e vou para esquerda
4. Estou em q5, leio X, me locomovo para q5, escrevo X e vou para esquerda
5. Estou em q5, leio U, me locomovo pra q2, escrevo U e vou para direita
6. Estou em q2, leio U, me locomovo para o estado de aceitação, escrevo U e vou para a direita.

#### A partir daqui vou fazer do jeito certo
O jeito formal de se fazer é assim:
![[Pasted image 20251118000830.png]]

ou seja, inicia com a entrada, e o Q1 atrás da entrada, e vai fazendo as alterações.

#### C)
1. q¹000
2. Uq²00 (leu 0, escreveu U e moveu para a direita, indo para q2)
3. UXq³0 (leu 0, escreveu X, moveu para a direita, indo para q3)
4. UX0q4 (leu 0, escreveu 0, moveu para a direita e foi para q4)
5. UX0Uqr (leu U, escreveu U, moveu para a direita e foi para qr, recusado )

#### D) (muito longa)
1. q1​0000
2. - ⊔q2​000
    
- ⊔xq3​00
    
- ⊔x0q4​0 (Pula um 0)
    
- ⊔x0xq3​⊔ (Marca o próximo 0 com x)
    
- ⊔x0q5​x (Fim da fita, começa a voltar)
    
- ⊔xq5​0x
    
- ⊔q5​x0x
    
- q5​⊔x0x (Chegou no início)
    
- ⊔q2​x0x (Reinicia a varredura)
    
- ⊔xq2​0x (Pula o x)
    
- ⊔xxq3​x (Marca o 0 restante com x)
    
- ⊔xxxq3​⊔ (Pula o x)
    
- ⊔xxq5​x (Fim da fita, volta)
    
- ⊔xq5​xx
    
- ⊔q5​xxx
    
- q5​⊔xxx (Chegou no início)
    
- ⊔q2​xxx (Reinicia a varredura)
    
- ⊔xq2​xx
    
- ⊔xxq2​x
    
- ⊔xxxq2​⊔ (Tudo marcado com x)
    
- ⊔xxx⊔qa​⊔ → **ACEITA**


#### Explicação:

Esse tipo de representação é fácil porém trabalhosa, demora muito fazer todos os passos.
**Conclusão:** A máquina aceita cadeias cujo comprimento é uma potência de 2 (20=1, 21=2, 22=4...).



### Criando MTS

#### A)
![[Pasted image 20251118011138.png]]

 A **Questão 2** é extensa (vai da letra **a** até a **j**), então a melhor estratégia é dividi-la em blocos lógicos. Vamos começar com as duas primeiras, que envolvem contagem e comparação de símbolos a,b,c.

Como eu não consigo desenhar o diagrama diretamente aqui, vou descrever o **algoritmo lógico** e as **transições** de forma que você possa desenhar as bolinhas (estados) e setas no seu caderno.

---

2. (a) L1​={aibjck∣0≤i≤j≤k}

**O Desafio:** Precisamos garantir duas coisas:

1. O número de a's é menor ou igual ao número de b's (i≤j).
    
2. O número total de b's é menor ou igual ao número de c's (j≤k).
    

**Lógica da Máquina (Algoritmo):** Vamos fazer isso em duas fases.

- **Fase 1 (Verificar a≤b):** A cabeça lê um `a`, marca-o (ex: troca por `A`), vai para a direita procurar um `b`, marca-o (ex: troca por `B`) e volta.
    
    - Se acabarem os `a`s e sobrarem `b`s (ou acabarem juntos), tudo bem.
        
    - Se acabarem os `b`s e ainda houver `a`, **Rejeita**.
        
- **Fase 2 (Verificar b≤c):** Agora precisamos comparar **todos** os b's (tanto os que viraram `B` quanto os originais `b`) com os c's.
    
    - Voltamos para o início. Procuramos o primeiro `B` ou `b`, trocamos por algo "visto" (ex: `X`), vamos até o final buscar um `c` e trocamos por `C`.
        
    - Se acabarem os `B/b`s, **Aceita** (pois j≤k, não importa se sobrarem c's).
        
    - Se acabarem os `c`s e ainda houver `B` ou `b`, **Rejeita**.
        

**Roteiro para o Diagrama:**

1. **q0​ (Início):**
    
    - Lê `a` → grava `A`, move D, vai para q1​.
        
    - Lê `B` ou `b` → significa que acabaram os `a`s. Move E para alinhar no início e vai para a Fase 2 (qfase2​).
        
    - Lê `Branco` → Aceita (caso cadeia vazia).
        
2. **q1​ (Procura b):**
    
    - Lê `a` ou `B` → ignora (move D).
        
    - Lê `b` → grava `B`, move E, vai para q2​ (retorno).
        
    - Lê `c` ou `Branco` → Rejeita (significa que tem mais `a` que `b`).
        
3. **q2​ (Retorna):**
    
    - Lê `a`, `B`, `b` → ignora (move E).
        
    - Lê `A` → move D, volta para q0​.
        
4. **qfase2​ (Início da comparação b vs c):**
    
    - Daqui em diante, procuramos `B` ou `b` e trocamos por `X`. Buscamos `c` e trocamos por `C`.
        
    - Se acabar os `B/b`s antes dos `c`s (ou juntos), vai para qaceita​.
        

---

2. (b) L2​={aibjck∣i+j=k para i,j,k>0}

**O Desafio:** A soma da quantidade de a's e b's deve ser exatamente igual à quantidade de c's. Além disso, i,j,k>0 exige que tenhamos pelo menos um de cada.

**Lógica da Máquina (Algoritmo):** Essa é mais direta. Vamos "gastar" um `c` para cada `a` e depois um `c` para cada `b`.

1. **Validar Existência:** O estado inicial deve garantir que lê pelo menos um `a`. Se começar com `b`, `c` ou branco, rejeita.
    
2. **Mapear A com C:** Lê `a`, marca (virar `A`), corre até o `c`, marca (vira `C`), volta. Repete até acabarem os `a`s.
    
3. **Mapear B com C:** Quando acabarem os `a`s, começa a ler `b`, marca (vira `B`), corre até o `c`, marca, volta.
    
4. **Verificação Final:**
    
    - Se ao buscar um `c` para um `a` ou `b` não encontrar (achar branco ou fim da fita) → **Rejeita** (soma a+b>c).
        
    - Se terminar de marcar todos os `b`s e ainda sobrarem `c`s → **Rejeita** (a+b<c).
        
    - Se terminar os `b`s e não houver mais `c`s → **Aceita**.
        

**Roteiro para o Diagrama:**

1. **q0​:** Lê `a`, grava `A`, move D, vai para q1​. (Se ler outra coisa, rejeita, garantindo i>0).
    
2. **q1​ (Vai buscar C):** Pula tudo (`a`, `b`, `B`, `C`) até achar `c`. Achou `c`? Grava `C`, move E, vai voltar (q2​). Não achou `c`? Rejeita.
    
3. **q2​ (Volta):** Volta até achar `A` ou `B`. Move D para pegar o próximo símbolo.
    
    - Se for `a` → repete processo (q1​).
        
    - Se for `b` → muda de fase (q3​).
        
4. **q3​ (Processa B):** Lê `b`, grava `B`, move D, vai buscar `c` (q4​).
    
5. **q4​ (Busca C para B):** Igual ao q1​. Achou `c` → grava `C`, volta. Não achou → Rejeita.
    
6. **Finalização:** Quando estiver voltando em q0​ ou no loop do `b` e encontrar apenas `C`s e Branco no final (sem sobrar `c` não marcado), **Aceita**.
    

---

**Próximo Passo:** Você quer tentar desenhar esses dois primeiro, ou quer que eu descreva a lógica para os próximos itens (**c** e **d**)? O item (c) (i=j=k) é um pouco mais "chato" pois exige desigualdade.