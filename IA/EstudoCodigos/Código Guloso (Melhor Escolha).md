### Início do Código

![[BuscaGulosaComeço.png]]

- Na busca gulosa de melhor estado vamos usar a heurística h, que é uma tabela de regras já dispostas pelo enunciado, o h é um dicionário que tem um uma chave que é o nome do estado e um valor, então acessamos o valor pelo nome do estado.
- Nas primeiras linhas, definimos o custo inicial do F(n) que é igual ao h(n) nesse caso. Depois de fazer isso, verificamos se ele é o final, caso não seja, construímos nossa borda como uma fila de prioridade.

![[Código Guloso 2.png]]

- Aqui ele vai pegar o menor h(n) de sua vizinhança, ou seja, ele consulta o heap, pega o menor h(n) e começa a tratar ele, se for o Estado final ele começa a printar o resultado e reconstruir o caminho do nó
- se não for, ele verifica se já foi explorado, se foi, ele pula (continue), caso contrário expande e bota em explorados.

![[Código Guloso 3.png]]
- Aqui é mostrada a expansão, onde o estado que está sendo expandido tem sua vizinhança explorada, funciona da seguinte forma: Para cada transição que haver na vizinhança, cria-se um nó filho, esse nó filho vai ter seu custo_filho calculado, que é o custo dele na heurística, depois disso, ele vai ser construído como nó efetivamente, após construir ele, colocamos ele na borda (caso ele não estiver em explorados ainda)

- Errata: A professora pediu para que o Nó não tivesse método comparativo, logo, nossa borda agora vai mudar, ela vai na verdade guardar uma tupla no formato (Custo_f_do_nó, id_do_nó, nó), isso vai fazer com que, quando ele for fazer comparações pra saber quem é o menor, ele sempre olha os dois primeiros valores da tupla, e se forem iguais, ele olha o ID, isso é só pra corrigir por que se não tivesse ID, ele ia tentar comparar nós, e como não tem a sobrecarga mais, ele ia dar erro de tipos.

![[Errata 1.png]]![[Errata 2.png]]
Agora, como é uma tupla, precisamos ignorar os dois primeiros valores para poder nomear de fato o "no" com o objeto Nó.

![[Errata 3.png]] 
Na parte de dar o push na borda, novamente não podemos mandar mais só o nó, agora mandamos a tupla no formato antes dito. 

fazendo isso, ele vai começar a fazer um Loop