## Questionário 

### Questão 1 - Defina Segurança da Informação
#### Slide:
![[Questao1.png]]

#### Resposta Gemini

**Segurança da Informação** ==é o conjunto de práticas, políticas, procedimentos e tecnologias que visam proteger as informações de uma organização ou indivíduo contra uma vasta gama de ameaças.== O seu principal objetivo é garantir a continuidade dos negócios, minimizar os riscos, maximizar o retorno sobre os investimentos e as oportunidades de negócio.

A definição é fundamentada em três pilares principais, conhecidos como a **Tríade CID**:

1. **Confidencialidade (Confidentiality):** Garante que a informação seja acessível apenas por pessoas autorizadas. Trata-se de proteger os dados contra a divulgação não autorizada.
    
    - **Exemplos de controles:** Criptografia de dados, controle de acesso baseado em papéis (RBAC), senhas e autenticação de dois fatores (2FA).
        
2. **Integridade (Integrity):** Assegura que a informação se mantenha exata, completa e inalterada, exceto por modificações autorizadas. O objetivo é proteger os dados contra alterações, inserções ou exclusões indevidas.
    
    - **Exemplos de controles:** Hashes (como SHA-256), assinaturas digitais, controle de versões e permissões de arquivos.
        
3. **Disponibilidade (Availability):** Garante que a informação e os sistemas relacionados estejam disponíveis e operacionais para os usuários autorizados sempre que necessário. O foco é proteger contra interrupções de serviço.
    
    - **Exemplos de controles:** Backups regulares, sistemas redundantes (como RAID e clusters), planos de recuperação de desastres (PRD) e proteção contra ataques de negação de serviço (DDoS).
        

Outros Princípios Importantes

Além da tríade fundamental, a Segurança da Informação moderna também se baseia em outros princípios essenciais:

- **Autenticidade:** Garante que a identidade de um usuário, sistema ou entidade é quem alega ser. Confirma a origem da informação.
    
- **Não-repúdio (Irretratabilidade):** Assegura que uma parte não possa negar a autoria de uma ação ou transação que realizou. É um princípio crucial para contratos e transações digitais.
    

Em resumo, Segurança da Informação não é apenas sobre tecnologia (como firewalls e antivírus), mas sim uma disciplina de gestão de riscos que envolve **pessoas, processos e tecnologias** para proteger o ativo mais valioso de uma organização: a sua informação.

#### Resposta formulada

Segurança da informação é um conjunto de práticas, politicas e protocolos que visam garantir primordialmente o CID, que são Confidencialidade, Integridade e Disponibilidade, Confidencialidade para manter segura a informação e ser acessada somente por quem tem permissão, integridade para se manter inalterada e exata a não ser por modificações permitidas e Disponibilidade para sempre ser possível acessar em qualquer momento, além disso, na Segurança da informação moderna também existe o principio da Autenticidade e do Não repúdio, que respectivamente são: A capacidade do usuário provar que é ele e se autenticar, e não conseguir refutar uma prova de que foi ele que fez uma transação ou algo do gênero.


### Questão 2 - A informação é o ativo mais valioso de uma empresa ou organização. Explique o que isso significa e por que a informação deve ser protegida. Descreva as fases do ciclo de vida da informação (manuseio, armazenamento, transporte e descarte) e explique como a segurança deve ser aplicada em cada uma delas.
#### Slide:
![[Questao2.png]]


#### Resposta Gemini

 A Informação como o Ativo Mais Valioso

A afirmação de que "a informação é o ativo mais valioso de uma empresa" significa que os dados, em suas diversas formas, possuem um valor estratégico e financeiro que muitas vezes supera o de ativos físicos como prédios e equipamentos. A informação é o motor que impulsiona a tomada de decisões, a inovação, a eficiência operacional e o relacionamento com o cliente.

**O que torna a informação tão valiosa?**

- **Vantagem Competitiva:** Segredos comerciais, fórmulas, designs de produtos, códigos-fonte e estratégias de marketing permitem que uma empresa se destaque de seus concorrentes.
    
- **Tomada de Decisão Estratégica:** Dados financeiros, análises de mercado, relatórios de vendas e métricas de desempenho são fundamentais para que os gestores tomem decisões informadas e direcionem o futuro da organização.
    
- **Relacionamento com o Cliente:** Informações de contato, histórico de compras e preferências dos clientes (dados pessoais) são essenciais para personalizar serviços, criar campanhas de marketing eficazes e construir lealdade.
    
- **Propriedade Intelectual:** Patentes, direitos autorais e marcas registradas são ativos de informação que podem ser licenciados ou vendidos, gerando receita direta.
    
- **Conformidade e Operações:** Registros de funcionários, contratos, transações financeiras e dados operacionais são vitais para o funcionamento diário e para cumprir obrigações legais e regulatórias.
    

**Por que a informação deve ser protegida?**

A proteção da informação é crucial porque a sua perda, vazamento ou corrupção pode levar a consequências devastadoras:

- **Perdas Financeiras:** Seja por meio de multas regulatórias (como as da LGPD - Lei Geral de Proteção de Dados), custos de remediação de incidentes, perda de receita ou espionagem industrial.
    
- **Danos à Reputação:** Um vazamento de dados de clientes abala a confiança do público, podendo levar a uma perda massiva de clientes e a danos duradouros à imagem da marca.
    
- **Consequências Legais:** A negligência na proteção de dados pode resultar em processos judiciais de clientes, parceiros e órgãos reguladores.
    
- **Perda de Vantagem Competitiva:** Se um concorrente obtém acesso aos seus planos estratégicos ou segredos comerciais, a empresa pode perder sua posição no mercado.
    
- **Interrupção dos Negócios:** A indisponibilidade de informações críticas (por exemplo, em um ataque de ransomware) pode paralisar as operações da empresa por dias ou semanas.
    

---

Segurança no Ciclo de Vida da Informação

A segurança não deve ser um evento único, mas um processo contínuo que acompanha a informação desde sua criação até seu descarte final. Este processo é conhecido como o ciclo de vida da informação.

1. Fase de Criação e Manuseio (Uso)

Nesta fase, a informação é gerada, recebida, modificada e utilizada nas operações diárias. É o momento de maior manipulação e, consequentemente, de grande exposição a riscos.

**Como aplicar a segurança:**

- **Classificação da Informação:** Antes de tudo, a informação deve ser classificada de acordo com seu nível de sensibilidade (ex: Pública, Interna, Confidencial, Restrita). A classificação determinará todos os controles de segurança subsequentes.
    
- **Controle de Acesso:** Implementar o ==**Princípio do Menor Privilégio**==, garantindo que os funcionários tenham acesso apenas às informações estritamente necessárias para realizar suas funções.
    
- **Políticas de Uso Aceitável (AUP):** Definir regras claras sobre como os funcionários podem manusear a informação, incluindo o uso de dispositivos pessoais (BYOD), e-mail e internet.
    
- **Conscientização e Treinamento:** Educar os colaboradores sobre ameaças como phishing, engenharia social e a importância de seguir as políticas de segurança.
    
- **Soluções de Prevenção de Perda de Dados (DLP):** Utilizar ferramentas que monitoram e impedem a cópia ou o compartilhamento não autorizado de dados sensíveis.
    

 2. Fase de Armazenamento (Em Repouso)

Esta fase ocorre quando a informação não está em uso ativo, mas está guardada em algum meio, como discos rígidos (HDs, SSDs), bancos de dados, servidores de arquivos ou na nuvem.

**Como aplicar a segurança:**

- **Criptografia em Repouso:** Criptografar os dados armazenados para que, mesmo em caso de acesso físico não autorizado ao dispositivo, a informação permaneça ilegível.
    
- **Segurança Física:** Proteger os locais onde os dados são armazenados (data centers, salas de servidores) com controles de acesso físico, como fechaduras, biometria e vigilância por câmeras.
    
- **Backups Seguros:** Realizar backups regulares, testá-los periodicamente e garantir que as cópias de segurança também sejam criptografadas e armazenadas em locais seguros (idealmente, um deles fora do local principal).
    
- **Gestão de Permissões:** Configurar permissões de acesso rigorosas em pastas, arquivos e bancos de dados para reforçar o controle de acesso lógico.
    

 3. Fase de Transporte (Em Trânsito)

Esta é a fase em que a informação se move de um ponto a outro, seja dentro da rede interna (LAN), pela internet (WAN) ou em mídias físicas como pen drives.

**Como aplicar a segurança:**

- **Criptografia em Trânsito:** Utilizar protocolos seguros que criptografam os dados durante a comunicação. Exemplos incluem **TLS/SSL** (o "S" em HTTPS), **VPNs** (Virtual Private Networks) para acesso remoto e **SSH** (Secure Shell) para gerenciamento de sistemas.
    
- **Redes Seguras:** Empregar firewalls, sistemas de detecção/prevenção de intrusão (IDS/IPS) e segmentação de rede para proteger o fluxo de dados.
    
- **Segurança de E-mail:** Usar criptografia para e-mails que contenham informações sensíveis e filtros para bloquear ameaças.
    
- **Política para Mídias Removíveis:** Exigir que dispositivos como pen drives e HDs externos sejam criptografados, especialmente se forem usados para transportar dados confidenciais.
    

 4. Fase de Descarte (Destruição)

É a fase final, quando a informação não é mais necessária para fins operacionais ou legais. O descarte inadequado é uma fonte comum de vazamentos de dados.

**Como aplicar a segurança:**

- **Política de Retenção de Dados:** Estabelecer por quanto tempo cada tipo de informação deve ser mantido antes de ser descartado, de acordo com as necessidades do negócio e as exigências legais.
    
- **Descarte de Dados Digitais:**
    
    - **Exclusão Segura (Sanitização):** Utilizar software especializado que sobrescreve os dados inúmeras vezes, tornando sua recuperação praticamente impossível.
        
    - **Desmagnetização (Degaussing):** Usar um campo magnético forte para destruir os dados em mídias magnéticas (HDs antigos, fitas).
        
    - **Destruição Física:** O método mais seguro para mídias no fim de sua vida útil é a destruição física por meio de trituração, perfuração ou incineração.
        
- **Descarte de Dados Físicos:** Usar trituradoras de papel (com corte cruzado para maior segurança) para documentos impressos e contratar empresas especializadas para a destruição segura de grandes volumes.
    

Ao aplicar controles de segurança robustos em cada uma dessas fases, uma organização garante uma defesa profunda e abrangente, protegendo seu ativo mais valioso de forma eficaz e contínua.

#### Resposta formulada

- 1 - Ela é o ativo mais importante pois ela pode superar o valor de ativos físicos como prédios, instalações, pelo seu valor de estratégia e financeiro. A informação é o motor que impulsiona a tomada de decisões, a inovação e a eficiência operacional, aumentando também o relacionamento com o cliente. 

- 2 - Ela deve ser protegida pelo seu valor, pelo impacto de sua ausência, pelo impacto de uso de terceiros, pela importância de sua existência, pela perda financeira e de vantagem competitiva que isso pode causar, e pela reputação da empresa que pode ser afetada.

- 3 - Fase de criação e manuseio (uso):
   É a fase onde a informação é gerada e utilizada no dia a dia, o que por consequência, é uma fase que expõe muito a informação ao risco de segurança. O que pode ser feito como medida de segurança é: catalogar a informação com níveis de acesso, exemplo: (público, restrito, interno, confidencial), isso vai gerar subcategorias de acesso para posteriormente. além disso, deve ser feito um treinamento com a equipe para os mesmos aprenderem a manusear a informação sem colocar ela em risco, e também sempre é bom ter ferramentas que auxiliam na recuperação da informação caso algum acidente venha a ocorrer.
   
  Fase de armazenamento (repouso):
  É a fase que a informação não está em uso, mas está guardada em algum dispositivo de persistência (HD's, SSD's, ou até mesmo na nuvem).
  Os métodos de segurança a serem aplicados são: Criptografia de dados, segurança nos data centers que os dados são armazenados, como vigilância, travas biométricas, câmeras, etc, e backups dos dados armazenados, além de uma boa gestão de armazenamento dos arquivos.
  
  Fase de Transporte(Em transito):
  É a fase em que a informação está indo de um ponto a outro, seja por rede ou fisicamente por pen-drives. 
  A segurança pode ser empregada da seguinte forma: Usando protocolos seguros na rede que criptografam a informação no transporte como TCP e o HTTPS, ou até mesmo utilizar VPN'S, além disso, usar sempre redes seguras com Firewall e para mídias físicas usar criptografia sempre que for transportar as informações.
  
  Fase de Descarte:
  É a fase final da informação, onde ela não é mais necessária por fins operacionais e o descarte inadequado pode acabar ocasionando em vazamento de informações,
  Os métodos de segurança são: Uma gestão de armazenamento de quanto de fato as informações podem ser excluídas, além de a utilização de ferramentas (softwares) que sobrescrevem varias vezes os dados, tornando quase impossível a recuperação, mas para uma certeza melhor é indicado a destruição física, como usando campos eletromagnéticos fortes, incineração, perfuração, trituração, etc, dos HD's.


### Questão 3 - Defina:

1. Evento
2. Incidente
3. Risco
4. Análise de Riscos
5. Gestão de Riscos
6. Ameaça
7. Vulnerabilidade.
#### Slide:
![[Questao3.1.png]]
![[Questao3.2.png]]
![[Questao3.3.png]]
![[Questao3.4.png]]
#### Resposta GPT

---

 **Evento**

Um **evento de segurança da informação** é qualquer ocorrência identificável que tenha relação com o funcionamento de um sistema, serviço ou rede. Pode representar tanto uma operação normal quanto uma anomalia que, potencialmente, afete a segurança da informação.

---

 **Incidente**

Um **incidente de segurança da informação** é um ou mais eventos indesejáveis que têm probabilidade significativa de comprometer a **confidencialidade, integridade ou disponibilidade** das informações, dos sistemas ou dos serviços.  
Em outras palavras, é a concretização de uma ameaça que causa impacto negativo na segurança da informação.

---

 **Risco**

O **risco** é a possibilidade de que uma **ameaça** explore uma **vulnerabilidade**, resultando em perda ou dano a um ativo de informação. É geralmente avaliado como a combinação da **probabilidade de ocorrência** e do **impacto** que o evento causaria.

---

 **Análise de Riscos**

A **análise de riscos** é o processo de identificar, avaliar e compreender os riscos que podem afetar a segurança da informação. Envolve a determinação das ameaças, vulnerabilidades, ativos e impactos, permitindo estimar a magnitude dos riscos e apoiar decisões de tratamento.

---

 **Gestão de Riscos**

A **gestão de riscos** consiste no conjunto de atividades coordenadas para **dirigir e controlar uma organização em relação aos riscos**. Envolve identificar, analisar, avaliar, tratar, monitorar e comunicar os riscos, de modo a reduzir sua probabilidade e/ou impacto a níveis aceitáveis.

---

 **Ameaça**

Uma **ameaça** é qualquer circunstância, agente ou ação com potencial para explorar uma vulnerabilidade e causar dano a um ativo de informação. As ameaças podem ser **naturais**, **acidentais** ou **deliberadas** (intencionais).

---

 **Vulnerabilidade**

A **vulnerabilidade** é uma fragilidade em um ativo, sistema ou processo que pode ser explorada por uma ameaça, resultando em comprometimento da segurança da informação. Pode estar relacionada a falhas técnicas, humanas, organizacionais ou físicas.

---

#### Resposta formulada

Evento: Uma situação no ambiente de sistemas, redes ou serviço, que representam uma anomalia ou um comportamento desconhecido, ou até uma falha de controles que seja relevante ou afete a segurança de informação.

Incidente: é um ou vários eventos que de fato comprometem o CID (confidencialidade, integridade e disponibilidade) do sistema, rede ou serviço, em outras palavras é a concretização de uma ameaça que pode acabar causando problemas a segurança da informação.

Risco: o risco é a probabilidade de uma ameaça explorar uma vulnerabilidade, geralmente é avaliado com probabilidade de ocorrência e impacto.

Análise de Riscos: É uma metodologia sistemática que visa listar as ameaças e vulnerabilidades calculando os riscos, juntamente com seus impactos, para assim priorizar tratamentos.

Gestão de Riscos: É um conjunto de atividades coordenadas que visam controlar uma organização em relação aos riscos, como identificar, analisar, avaliar, ratar, monitorar, a fim de diminuir a probabilidade do risco e também seus impactos.

Ameaça: É algo, alguém ou agente que pode oferecer risco por explorar de uma vulnerabilidade do sistema, rede ou serviço, podendo ser deliberado, natural ou acidental. Podendo assim causar dano em ativos da empresa.

Vulnerabilidade: Vulnerabilidade é uma fragilidade ou espaço que pode ser explorado por uma ameaça, isso pode ser em um ativo ou serviço, e ao ser explorado irá gerar comprometimento a segurança da informação. Pode ser falha humana, técnica ou organizacional.

### Questão 4 - Existe Ameaça sem Vulnerabilidade? E vice-versa? Justifique através de exemplos no contexto de segurança da informação.

#### Slide
![[Questao4.png]]

#### Resposta GPT

 ✅ **Ameaça sem vulnerabilidade**

Sim, **pode existir**, mas **não gera risco efetivo**.  
Uma ameaça só se torna perigosa quando há uma vulnerabilidade que possa ser explorada.

**Exemplo:**  
Um ataque de ransomware é uma ameaça comum.  
Entretanto, se um sistema estiver **atualizado, com antivírus ativo e backups regulares**, o ransomware **não encontrará vulnerabilidades** para explorar.  
➡️ **Ameaça existe**, mas **não há vulnerabilidade** — logo, **não há risco real**.

---

 ✅ **Vulnerabilidade sem ameaça**

Também **pode existir**, mas representa **um risco potencial**.  
A vulnerabilidade, por si só, não causa dano, mas **pode ser explorada futuramente** caso uma ameaça surja.

**Exemplo:**  
Um servidor com **porta administrativa exposta** na rede interna, sem proteção por firewall.  
No momento, não há nenhum agente malicioso com acesso à rede.  
➡️ **Vulnerabilidade existe**, **ameaça não** — o risco é **latente**, podendo se concretizar caso a rede seja comprometida.

---

 ⚖️ **Conclusão**

- **Ameaça + Vulnerabilidade = Risco real.**
    
- **Apenas ameaça = risco inexistente.**
    
- **Apenas vulnerabilidade = risco potencial.**

#### Resposta Formulada

Ambos podem existir sozinhos, porém, só se concretiza risco quando os dois existem, por exemplo, se só existe a ameaça o risco é inexistente, por exemplo: um ransomware num sistema devidamente atualizado, com antivírus e backups constantes, a ameaça existe, é o ransomware, porém não existe vulnerabilidades no sistema para a ameaça explorar, logo não existe risco, porém no caso inverso, quando existe somente a vulnerabilidade, significa que existe um risco potencial, porém que ainda não existe uma ameaça para explora-la, por exemplo: uma porta administrativa aberta indevidamente na rede (exposta), sem proteção for firewall, no momento não há agente invasores na rede (ameaças), mas futuramente pode ser que apareça e se aproveite da vulnerabilidade, ou seja, é um risco potencial. Em conclusão, ambos podem existir separados, mas somente juntos concretizam um risco.

### Questão 5 - Enumere e explique os tipos de origem de ameaças. Dê exemplos.

#### Slide
![[Questao5.png]]

#### Resposta GPT

**1. Ameaças Naturais**

São causadas por **fenômenos da natureza**, fora do controle humano.  
Podem interromper serviços, destruir dados ou danificar equipamentos.

📘 **Exemplos:**

- Enchentes ou tempestades que danificam servidores;
    
- Terremotos que destroem centros de dados;
    
- Descargas elétricas que causam perda de informações.
    

---

**2. Ameaças Humanas Intencionais**

São ações **deliberadas e maliciosas** realizadas por pessoas com o objetivo de causar dano, roubar informações ou comprometer sistemas.

📘 **Exemplos:**

- Ataques de hackers (invasões, ransomware, phishing);
    
- Funcionários que vazam dados propositalmente;
    
- Sabotagem de sistemas ou infraestruturas críticas.
    

---

 **3. Ameaças Humanas Não Intencionais**

Ocorrem por **erro humano**, sem a intenção de causar prejuízo, mas que ainda assim geram impacto na segurança da informação.

📘 **Exemplos:**

- Exclusão acidental de arquivos importantes;
    
- Envio de informações sigilosas para o destinatário errado;
    
- Configuração incorreta de servidores ou permissões de acesso.
    

---

 **4. Ameaças Técnicas (ou de Falha Tecnológica)**

Decorrem de **defeitos, falhas ou mau funcionamento de hardware, software ou redes**.  
Essas ameaças podem ser naturais (desgaste) ou humanas (projeto inadequado).

📘 **Exemplos:**

- Falha no disco rígido que causa perda de dados;
    
- Erros de software que abrem brechas de segurança;
    
- Queda de energia que interrompe serviços.
    

---

 **5. Ameaças Ambientais**

São relacionadas às **condições do ambiente físico** em que os sistemas estão instalados.  
Podem afetar a integridade e disponibilidade dos equipamentos.

📘 **Exemplos:**

- Superaquecimento por falha no ar-condicionado do data center;
    
- Incêndios causados por curto-circuito;
    
- Poeira excessiva que danifica componentes eletrônicos.
    

---

 ⚖️ **Resumo**

|Tipo de Ameaça|Origem|Exemplos|
|---|---|---|
|**Natural**|Fenômenos da natureza|Enchente, raio, terremoto|
|**Humana intencional**|Ação maliciosa|Hacker, sabotagem|
|**Humana não intencional**|Erro humano|Envio errado de dados|
|**Técnica**|Falha de sistemas|Bug, pane elétrica|
|**Ambiental**|Condição física do ambiente|Calor, fogo, poeira|

#### Resposta Formulada

Existem alguns tipos de ameaças, geralmente são divididas em 3: Naturais, intencionais e não intencionais, Exemplos naturais: Incêndios, enchentes, terremotos, etc. Intencionais: ataques hackers, vírus, sabotagem, etc. Não intencionais: vazamento de dados, envio errado, descarte errado, etc. 

Porém, existem também algumas subcategorias: A Técnica e a Ambiental, uma ameaça técnica se dá por problemas do próprio equipamento ou sistema, como bugs ou até panes elétricas, já o ambiental se dá por conta do ambiente em que os equipamentos estão instalados, como calor excessivo, umidade excessiva, maresia, etc.

### Questão 6 - A família de normas ISO/IEC 27000 é um conjunto de padrões que tratam da Gestão da Segurança da Informação. Explique a abrangência da segurança de TI, da segurança cibernética e da proteção de privacidade conforme definido por essas normas. Discuta o papel da ISO/IEC 27001 como a principal norma para sistemas de gerenciamento de segurança da informação (SGSI) e por que é a única passível de certificação para empresas.

#### Slide
![[Questao6.1.png]]
![[Questao6.2.png]]
![[Questao6.3.png]]
![[Questao6.4.png]]
#### Resposta GPT

 🛡️ **Abrangência das áreas segundo a família ISO/IEC 27000**

1. **Segurança da Informação (TI)**  
    Trata da **proteção dos ativos de informação**, independentemente do formato (digital, físico ou verbal).  
    O foco é garantir os **três pilares da segurança**:
    
    - **Confidencialidade** (acesso apenas por pessoas autorizadas);
        
    - **Integridade** (informações corretas e íntegras);
        
    - **Disponibilidade** (informações acessíveis quando necessário).
        
    
    📘 _Exemplo:_ políticas de backup, controle de acesso, criptografia e gestão de incidentes.
    

---

2. **Segurança Cibernética**  
    É um **subconjunto da segurança da informação**, voltado à **proteção de sistemas conectados à internet**, redes e dados contra ataques digitais deliberados.  
    Visa preservar **confidencialidade, integridade e disponibilidade** no **ambiente digital**.
    
    📘 _Exemplo:_ defesa contra phishing, ransomware, invasões e fraudes eletrônicas.
    

---

3. **Proteção de Privacidade**  
    Envolve o **tratamento adequado dos dados pessoais**, garantindo que sejam coletados, usados e armazenados conforme as leis e normas aplicáveis (como a LGPD no Brasil e o GDPR na Europa).  
    Relaciona-se à **proteção dos direitos individuais** sobre as informações pessoais.
    
    📘 _Exemplo:_ anonimização de dados, consentimento informado e gestão de incidentes de violação de privacidade.
    

---

 🧭 **Papel da ISO/IEC 27001**

A **ISO/IEC 27001** é a **norma central** da família 27000.  
Ela define os **requisitos para a implementação, manutenção e melhoria contínua** de um **Sistema de Gestão da Segurança da Informação (SGSI)**.

👉 Seu objetivo é ajudar as organizações a **gerenciar riscos** de forma sistemática, aplicando **controles de segurança** adequados e alinhados ao negócio.

---

 🏅 **Por que é a única norma certificável**

A **ISO/IEC 27001** é a **única norma da família 27000 passível de certificação**, pois:

- Define **requisitos formais e auditáveis** (como política de segurança, análise de riscos, controles e auditorias internas);
    
- Permite que **auditores independentes** verifiquem a conformidade do SGSI da empresa;
    
- As demais normas da família (como a **27002**, **27005**, **27701**) são **complementares e orientativas**, servindo de guia, mas **não exigem conformidade obrigatória**.
    

---

 🧩 **Resumo final (ideal para redação ou prova)**

A família de normas ISO/IEC 27000 estabelece diretrizes para a **gestão da segurança da informação**, abrangendo a proteção de dados corporativos, sistemas cibernéticos e informações pessoais.  
Enquanto a **segurança da informação** busca preservar confidencialidade, integridade e disponibilidade de todos os ativos informacionais, a **segurança cibernética** foca na defesa contra ataques digitais e a **proteção de privacidade** garante o tratamento ético e legal de dados pessoais.  
A **ISO/IEC 27001** destaca-se como o principal padrão da família, pois define os requisitos auditáveis de um **Sistema de Gestão da Segurança da Informação (SGSI)**, sendo a **única norma certificável**, usada para comprovar a conformidade e a maturidade da segurança nas organizações.

#### Resposta Formulada

Segurança da Informação:
Abrangência: Garantir a segurança dos ativos sejam, físicos, digitais, ou verbais, buscando preservar o CID (confidencialidade, integridade, disponibilidade) da informação.
Exemplo: Proteção contra falhas e hardware, backups, criptografias, etc.

Segurança Cibernética:
Abrangência: É como uma subconjunto da segurança da informação, porém, focada somente no mundo digital, sistemas conectados a rede conferindo proteção contra hackers, ataques, malwares, ransomwares, etc.
Exemplo: Firewalls, criptografia de dados, monitoramento da rede, etc.

Proteção da Privacidade:
Abrangência: Proteger as informações privadas e pessoais do usuário, garantindo a segurança na hora de coletar e armazenar essas informações, fazendo com que elas só possam ser acessadas por pessoas autorizadas e serem utilizadas de maneira legítima, segundo a LGPD no Brasil.
Exemplo: Consentimento da hora da coleta dos dados, anonimato quando solicitado, privacidade de informações sensíveis, etc.

A ISO 27001 é a base central da ISO 27000, Pois é nela que são definidos formalmente os requisitos para a implementação, manutenção e melhoria continua de um SGSI (Sistema de gestão da Segurança da informação) para as organizações, essa ISO é a única passível de certificação pois ela além de ser a mais globalmente conhecida, também é a que define formalmente os requisitos formais e auditáveis, (politicas de segurança, gestão de riscos, auditorias internas), e além disso, as ISO's restantes são consideradas mais como boas práticas complementares a ISO 27001. 


### Questão 7 - De acordo com a NBR ISO/IEC 27002, segurança da informação é a preservação da confidencialidade, integridade e disponibilidade. Defina cada um desses três pilares. Em seguida, descreva um cenário em que cada um deles é violado por um ataque ou incidente de segurança.

#### Slide

#### Resposta GPT

 🔒 **1. Confidencialidade**

**Definição:**  
É o princípio que garante que a **informação seja acessada apenas por pessoas autorizadas**.  
Seu objetivo é **proteger o sigilo** dos dados e evitar que terceiros obtenham informações indevidas.

**Exemplo de violação:**  
Um **ataque de phishing** leva um funcionário a revelar suas credenciais de acesso, permitindo que um invasor visualize **dados sigilosos de clientes**.  
➡️ A **confidencialidade** foi comprometida, pois informações restritas se tornaram públicas.

---

 🧩 **2. Integridade**

**Definição:**  
Refere-se à **exatidão e completude da informação**, garantindo que os dados **não sejam alterados, corrompidos ou manipulados** de forma indevida, seja intencionalmente ou por erro.

**Exemplo de violação:**  
Um **malware** modifica registros financeiros em um banco de dados, alterando valores de transações.  
➡️ A **integridade** foi violada, pois os dados deixaram de refletir a realidade original.

---

 ⚙️ **3. Disponibilidade**

**Definição:**  
É o princípio que assegura que as **informações e sistemas estejam acessíveis** aos usuários autorizados **sempre que necessários**.  
Depende da continuidade dos serviços e da resiliência da infraestrutura.

**Exemplo de violação:**  
Um **ataque de negação de serviço (DDoS)** sobrecarrega os servidores de um site bancário, tornando-o inacessível aos clientes.  
➡️ A **disponibilidade** foi comprometida, pois o serviço ficou fora do ar.

---

 🧭 **Resumo**

| Pilar                 | Objetivo                                            | Exemplo de Violação                |
| --------------------- | --------------------------------------------------- | ---------------------------------- |
| **Confidencialidade** | Manter o sigilo da informação                       | Vazamento de dados por phishing    |
| **Integridade**       | Garantir a veracidade e consistência dos dados      | Alteração de registros por malware |
| **Disponibilidade**   | Assegurar acesso contínuo e autorizado à informação | Ataque DDoS derruba o sistema      |

---

#### Resposta Formulada
Primeiro: Confidencialidade - É a proteção da informação para que ela só possa ser acessada por pessoas autorizadas, com o objetivo de proteger o sigilo das informações, evitando que terceiros tenham acesso a ela
Ataque: um ataque de phising faz com que um funcionário vaze suas credenciais, que por consequência faz com que os dados de seus clientes também sejam vazados.

Segundo: Integridade - Refere-se a exatidão, completude e não alteração (não permitida) da informação, garantindo que ela não seja corrompida, alterada ou modificada de forma indevida
Ataque: um malware que corrompe os arquivos de uma organização, fazendo o sequestro dos dados.

Terceiro: Disponibilidade - Refere-se a capacidade do usuário sempre conseguir acessar as informações em qualquer momento, ou seja, ela estar disponível e acessível sempre que necessário.
Ataque: Um ataque DDoS que "derruba" ou sobrecarrega um serviço, fazendo com que novas requisições ou visualizações demorem muito a serem concretizadas, como um ataque DDoS a um banco, que faz com que os usuários não consigam acessar.


### Questão 8 - Defina Ataque. Defina e diferencie Ataques Passivos e Ataques Ativos. Dê exemplos.

#### Slide
![[Questao8.1.png]]
![[Questao8.2.png]]
![[Questao8.3.png]]
#### Resposta GPT

 ⚔️ **Ataque (definição geral)**

Um **ataque** é qualquer **ação deliberada realizada por um agente mal-intencionado** (interno ou externo) com o objetivo de **violar a segurança da informação**, explorando vulnerabilidades em sistemas, redes ou processos.  
O ataque busca comprometer a **confidencialidade, integridade ou disponibilidade** das informações.

---

 🕵️‍♂️ **Ataques Passivos**

**Definição:**  
São ataques em que o invasor **apenas observa, intercepta ou coleta informações**, **sem modificar** os dados nem interferir no funcionamento do sistema.  
O objetivo é **obter conhecimento** sem ser detectado.

📘 **Exemplos:**

- **Escuta de rede (sniffing):** captura de pacotes de dados para descobrir senhas ou mensagens.
    
- **Monitoramento de tráfego:** análise do volume e origem de comunicações para identificar padrões de uso.
    

➡️ **Compromete:** principalmente a **confidencialidade**.  
➡️ **Não altera** informações nem causa danos diretos.

---

 💣 **Ataques Ativos**

**Definição:**  
São ataques em que o invasor **interfere diretamente** no sistema, **modificando, bloqueando ou destruindo** dados e serviços.  
Esses ataques são **mais detectáveis** e visam causar **impacto direto** na operação.

📘 **Exemplos:**

- **Alteração de dados:** modificação de registros em um banco de dados.
    
- **Ataque DDoS:** sobrecarga de um servidor até que ele fique indisponível.
    
- **Injeção de código malicioso:** inserção de scripts (como SQL Injection) para manipular sistemas.
    

➡️ **Compromete:** a **integridade** e/ou **disponibilidade** das informações.  
➡️ **Causa danos diretos** e requer ação corretiva imediata.

---

 ⚖️ **Resumo Comparativo**

|Tipo de Ataque|Ação do Invasor|Objetivo|Compromete|Exemplo|
|---|---|---|---|---|
|**Passivo**|Observa e coleta dados|Espionar, obter informação|Confidencialidade|Sniffing de senhas|
|**Ativo**|Modifica ou interrompe dados/sistemas|Causar dano ou alteração|Integridade / Disponibilidade|DDoS, SQL Injection|

---

Quer que eu reformule essa resposta em **formato dissertativo (8 a 10 linhas)**, ideal para usar em uma avaliação escrita?
#### Resposta Formulada

Definição: Ataque é uma ação feita um um agente mal-intencionado, interno ou externo que visa violar a segurança da informação, explorando vulnerabilidades de um sistema, rede ou serviço, atacando diretamente o CID da Segurança da informação.

Ataques passivos: O atacante não atua diretamente, o objetivo muitas vezes é observar e capturar a informação, passando despercebido, então o atacante não altera nada, ele pode fazer sniffing na rede que captura pacotes que se não estiverem criptografados podem resultar em vazamento de senhas etc, e observação de tráfego para ver volumes de mensagens e trackear a rede. Compromente principalmente a confidencialidade.

Ataque Ativos: O invasor ataca diretamente a informação, modificando, destruindo ou bloqueando o acesso, esses ataques são mais detectáveis, pois causam impacto direto e geralmente significativo para quem está sendo atacado. Exemplos são: ataques DDoS, ou um invasor adentrar um banco de dados e mudar as informações nele contida, SQL injection, etc.

### Questão 9 - Responda os itens a seguir:

a) Sobre o packet sniffing, escreva seu propósito, como ele é executado e o tipo de informação que um agente malicioso busca obter.

b) Defina Engenharia Social e explique como ela é utilizada em ataques.

c) Descreva o _phishing_. Forneça um exemplo de ataque de _phishing_ e explique por que este método é tão eficaz, explorando a ingenuidade e a confiança dos usuários.

d) Explique a finalidade do **Port Scanning** e do **Vulnerability Scanning** como técnicas de recuperação de informações. Descreva como essas duas técnicas se complementam na fase de reconhecimento de um ataque, utilizando a analogia de mapear serviços e, em seguida, procurar falhas específicas para esses serviços.

e) O _spoofing_ é um ataque ativo em que um agente malicioso falsifica pacotes de rede para se passar por um _host_ confiável. Discuta os três principais tipos de _spoofing_ — **IP Spoofing**, **ARP Spoofing** e **DNS Spoofing**— explicando como cada um funciona e quais vulnerabilidades ou protocolos eles exploram. Adicionalmente, analise como um tipo de _spoofing_, como o ARP Spoofing, pode ser usado como um passo inicial para ataques mais complexos, como um ataque de DNS Spoofing ou um ataque do tipo "man-in-the-middle" (MitM).

#### Slide

![[Questao9.1.png]]
![[Questao9.2.png]]
![[Questao9.3.png]]
![[Questao9.4.png]]
![[Questao9.5.png]]
#### Resposta GPT
---

 a) Packet sniffing

**Propósito:** capturar e inspecionar tráfego de rede para colher informações transmitidas entre hosts (para monitoramento legítimo ou para exploração maliciosa).

**Como é executado:** um sniffer (software ou hardware) coloca a interface de rede em modo _promiscuous_ (ou usa técnicas de espelhamento/switch port mirroring) para receber todos os pacotes que passam pela rede, mesmo os que não são destinados ao host que executa o sniffer. Ferramentas comuns: Wireshark, tcpdump, tshark.

**Tipo de informação buscada por agente malicioso:** credenciais em texto claro (senhas HTTP, SMTP, FTP), cookies de sessão, tokens, endereços IP e portas, conteúdo de comunicações, informações de configuração e metadados que auxiliam em ataques posteriores (p. ex., serviços expostos).

---

 b) Engenharia Social

**Definição:** técnica que explora o comportamento humano, confiança e erros cognitivos para induzir pessoas a divulgar informações sensíveis ou executar ações que comprometem a segurança.

**Como é utilizada em ataques:** o atacante pesquisa a vítima (reconhecimento), constrói um pretexto crível (por exemplo, fingir ser suporte técnico, colega, fornecedor) e utiliza comunicação persuasiva (telefone, e-mail, redes sociais, presencial) para obter credenciais, autorizar transferências, instalar malware ou divulgar dados. A engenharia social costuma preceder ou acompanhar ataques técnicos, porque é eficaz para contornar controles técnicos por meio de falhas humanas.

**Exemplos de técnicas usadas:** pretexting, baiting, quid pro quo, tailgating (acesso físico), phishing (quando por e-mail — ver item c).

---

 c) Phishing

**Descrição:** forma de engenharia social em que o atacante envia mensagens (normalmente e-mail, SMS, ou mensagens instantâneas) que se apresentam como comunicação legítima para induzir a vítima a clicar em links maliciosos, abrir anexos ou informar credenciais/dados pessoais.

**Exemplo de ataque de phishing:** um e-mail aparentemente enviado pelo banco comunica “atividade suspeita” e solicita que o usuário clique num link para “verificar” a conta. O link leva a um site falsificado que imita o portal do banco; a vítima digita usuário e senha, que são então coletados pelo atacante.

**Por que é eficaz:** explora confiança, urgência e falta de atenção: mensagens bem redigidas, com logos e linguagem convincente, criam senso de legitimidade; chamadas à ação imediata (“conta bloqueada”, “acao necessária”) reduzem o tempo de reflexão; muitas pessoas não verificam URLs, remetentes ou certificados. A combinação de engenharia social bem montada e falhas no discernimento humano torna o phishing um dos vetores mais bem-sucedidos.

---

 d) Port Scanning e Vulnerability Scanning — finalidade e complementaridade

**Port Scanning (mapeamento de portas):** técnica para identificar quais portas e serviços estão abertos num host (por exemplo: 22/SSH, 80/HTTP, 443/HTTPS, 3306/MySQL). Ferramentas: Nmap, masscan. Finalidade: descobrir _o que_ está rodando e em quais pontos um alvo oferece serviços.

**Vulnerability Scanning (varredura de vulnerabilidades):** análise automatizada que verifica serviços e aplicações identificados por possíveis vulnerabilidades conhecidas (correlação com CVEs, versões vulneráveis, configurações fracas). Ferramentas: Nessus, OpenVAS, Qualys. Finalidade: identificar _como_ explorar (quais falhas específicas estão presentes).

**Como se complementam (analogia):** imagine que você quer invadir um prédio:

- **Port scanning** = caminhar pela rua e anotar portas e janelas abertas (quais entradas existem, quais salas têm janelas).
    
- **Vulnerability scanning** = examinar cada porta/janela aberta procurando fechaduras quebradas, dobradiças soltas ou códigos fracos que permitem entrar.
    

Na fase de reconhecimento de um ataque, o atacante primeiro mapeia serviços (port scan) e depois testa vulnerabilidades específicas desses serviços (vulnerability scan) para escolher os vetores de intrusão mais promissores.

---

 e) Spoofing — IP, ARP e DNS (como funcionam, protocolos explorados e uso em ataques compostos)

 IP Spoofing

**Como funciona:** falsificação do campo de endereço IP de origem em pacotes IP para fazer parecer que os pacotes vêm de outro host.  
**Protocolos/vulnerabilidades explorados:** protocolo IP (camada de rede) não autentica a origem por si só; explora falta de validação de origem em roteadores/serviços.  
**Consequências típicas:** bypass de filtros de IP, amplificação em ataques DDoS (p. ex., ataques UDP amplification), ou para ocultar a identidade do atacante.

 ARP Spoofing (ou ARP Poisoning)

**Como funciona:** na rede local Ethernet, o atacante envia mensagens ARP falsas associando o MAC do atacante ao endereço IP de outro host (por exemplo, o gateway). Outros dispositivos atualizam suas tabelas ARP e passam a enviar tráfego para o atacante.  
**Protocolos/vulnerabilidades explorados:** protocolo ARP (Address Resolution Protocol) — que é sem autenticação; explora a confiança das entradas ARP dinâmicas.  
**Consequências típicas:** redirecionamento de tráfego, escuta passiva de pacotes, modificação de pacotes em trânsito (MitM), captura de credenciais e injeção de conteúdo malicioso.

 DNS Spoofing (ou DNS Cache Poisoning / DNS Hijacking)

**Como funciona:** comprometimento das respostas DNS para associar nomes de domínio legítimos a endereços IP controlados pelo atacante, fazendo com que usuários sejam direcionados para servidores maliciosos. Pode ser feito corrompendo cache de servidores DNS, manipulando respostas em trânsito ou comprometendo servidores DNS.  
**Protocolos/vulnerabilidades explorados:** protocolo DNS e implementações com validação fraca; exploração de falta de DNSSEC, vulnerabilidades em resolvers ou em comportamentos previsíveis de transações DNS.  
**Consequências típicas:** direcionamento de usuários a sites falsos (facilitando phishing), interceptação de tráfego, distribuição de malware.

 Como ARP Spoofing pode ser passo inicial para ataques mais complexos (ex.: MitM, DNS Spoofing)

- **ARP Spoofing → MitM:** ao envenenar as tabelas ARP de computadores e do gateway, o atacante coloca-se no caminho entre vítima e internet; assim ele pode **capturar** (sniff), **modificar** ou **bloquear** pacotes.
    
- **MitM → DNS Spoofing local:** estando em posição MitM, o atacante pode interceptar e alterar respostas DNS que passam pelo seu host (ou responder antes do servidor legítimo), forjando respostas que direcionam a vítima a servidores maliciosos.
    
- **Fluxo típico de ataque composto:** o atacante realiza ARP spoofing para controlar o tráfego da LAN → inspeciona/ modifica requisições DNS ou injeta respostas falsificadas → vítima é redirecionada a servidor controlado → credenciais/ conteúdo malicioso são capturados ou entregues.
    
#### Resposta Formulada

Sniffing: Captura pacotes diretamente pelo fluxo da rede, conectando-se a rede com um software (sniffer), que geralmente configura a placa de rede no modo promíscuo, ou seja, recebe todos os pacotes, inspecionando o tráfego e capturando pacotes que podem vazar informações caso não sejam encriptados, o objetivo do atacante é conseguir senhas, tokens, cookies, ou até mesmo informações mais sutis para usar em ataques posteriores, como fragilidades ou alvos.

Engenharia Social: é uma técnica que explora a ingenuidade, confiança ou inocência de uma pessoa para conseguir informações privilegiadas, ela explora erros cognitivos e brechas que uma pessoa possa dar para conseguir informações que antes poderiam ser confidenciais, geralmente em ataques, o atacante faz um reconhecimento(estudo) da vítima, escolhe uma abordagem que faça sentido (colega de trabalho, fornecedor, cliente) e tenta obter credenciais, instalar um malware, fazer transferências ou algo que ataque a segurança da informação.   

Phishing: é uma modalidade de engenharia social, que consiste em o ataque enviar uma mensagem não solicitada se passando por um site conhecido ou aplicativo/empresa, geralmente junto com a mensagem que clama por urgência vem um link ou aplicativo malicioso que é feito como uma réplica de um site maior ou aplicativo, esses sites falsos são feitos pra roubar as credenciais da vitima, ou induzir ela a realizar pagamentos, assinar o nome dela, etc
Phishing é um método que faz com que muita gente seja enganada pois na maioria das vezes as mensagens são muito bem redigidas, sempre clamando um teor de urgência e que uma ação precisa ser feita, a vitima na maioria das vezes nem se dá o tempo de verificar as URL's e o email remetente com afinco, e acabam realizando o vazamento das informações.

Port Scanning e Vulnerability Scanning: 
Port Scanning: É um metodo que utilizar port scanners para verificar quais portas e serviços estão sendo utilizados, quais portas estão abertas, TCP e UDP, fazendo com que o atacante não desperdice tempo em portas que não estão sendo utilizadas
Vulnerability Scan: Ele verifica as vulnerabilidades em uma rede, fazendo diversos tipos de testes a procura de falhas de segurança.

Analogia: Imaginando que o atacante quer invadir um prédio, o port scanning é o momento em que ele passa observando quais salas possuem janelas, e portas, e o vulnerability scanning é o momento em que ele passa nas janelas e portas que ele observou testando as fechaduras, vendo se elas tem tranca, vendo se não dá pra arrombar elas, etc. Os dois se completam.

IP spoofing: Visa camuflar o IP de origem de uma solicitação/Mensagem, fazendo parecer que as mensagens e solicitações vem de outro HOST, ele explora o protocolo IP que não faz a autenticação do IP origem por si só
ARP Spoofing: é uma variante do IP spoofing (adress attack), porém utilizar o MAC ao invés do IP, o atacante utiliza altera o ARP cache da vitima para mudar o mapeamento da rede, fazendo com que a informação passe pelo Host atacante antes de ir para seu destino final, Ele explora o Protocoolo ARP que não possui verificação de envio, gerando redirecionamento de tráfego, escuta na rede, entre outros.
DNS Spoofing: é um ataque mais simples que modifica o host name, a vitima vai pesquisar o nome de domínios legítimos, porém o atacante fez um spoofing e associou esse nome ao IP de um servidor malicioso dele redirecionando o usuário. Isso é feito alterando as tabelas de mapeamento host name - IP
protocolo atacado: DNS de implementações com verificação simples/insegura.

Como Arp spoofing pode ajudar a iniciar um ataque:
O atacante realiza o ARP spoofing para ficar com uma escuta na rede, podendo bloquear também pacotes e eventualmente evoluir pra um  DNS Spoofing local, que vai dar o controle para o atacante interceptar solicitações DNS e substituir por um DNS que vai direcionar a vitima para um site malicioso onde ele vai conseguir roubar as credenciais da vitima.


### Questão 10 - O termo "hacker" abrange uma ampla gama de indivíduos com diferentes motivações e códigos de ética. Escolha **quatro arquétipos de hackers distintos** do texto (por exemplo, White Hat, Black Hat, Grey Hat, Hacktivistas, ou Script Kiddies). Para cada um, defina seu papel e motivação, fornecendo um exemplo de um indivíduo ou grupo conhecido que se encaixe nessa descrição.

#### Slide

#### Resposta GPT

 **1. White Hat (Hackers Éticos)**

**Definição:**  
São profissionais de segurança que utilizam técnicas de invasão de forma **legal e autorizada**, com o objetivo de **proteger sistemas**.  
Trabalham em **testes de penetração (pentests)**, auditorias de segurança e pesquisas para fortalecer defesas.

**Motivação:**  
Melhorar a segurança, corrigir vulnerabilidades e proteger usuários e organizações.

**Exemplo:**

- **Kevin Mitnick** — ex-hacker famoso que, após cumprir pena, tornou-se consultor de segurança e referência mundial em _ethical hacking_.
    
- Empresas como **Synack** e **HackerOne** empregam diversos _white hats_ para realizar programas de _bug bounty_.
    

---

 **2. Black Hat (Hackers Maliciosos)**

**Definição:**  
Hackers que agem **ilegalmente**, explorando falhas de sistemas para **obter ganhos pessoais**, roubo de dados, espionagem ou sabotagem.  
Costumam vender informações no mercado negro (_dark web_).

**Motivação:**  
Lucro financeiro, vingança, poder, ou simples desafio técnico.

**Exemplo:**

- **Grupo LAPSUS$**, responsável por ataques a grandes empresas como Microsoft e Nvidia (2022).
    
- Também se encaixam nesse perfil os criadores de ransomwares como **WannaCry**.
    

---

 **3. Grey Hat (Hackers Cinzentos)**

**Definição:**  
Atuam na **zona intermediária entre o ético e o ilegal**.  
Costumam descobrir falhas e divulgá-las sem autorização — às vezes notificam a empresa, outras vezes tornam público o problema para forçar uma correção.

**Motivação:**  
Ego técnico, reconhecimento público ou pressão por transparência.

**Exemplo:**

- **Khalil Shreateh**, que em 2013 invadiu o perfil de Mark Zuckerberg no Facebook para demonstrar uma falha que a empresa ignorou — violou regras, mas sem intenção maliciosa.
    

---

 **4. Hacktivistas**

**Definição:**  
Grupos ou indivíduos que usam a invasão como **forma de protesto político ou social**, buscando chamar atenção para causas ideológicas.

**Motivação:**  
Ativismo digital — denunciar injustiças, censura, governos autoritários ou corporações.

**Exemplo:**

- **Anonymous**, coletivo descentralizado que já atacou governos, igrejas e empresas em protesto por liberdade de expressão e privacidade.
    
- Outro exemplo é o grupo **LulzSec**, que realizava ataques “pelo riso” e para expor falhas de grandes corporações.
#### Resposta Formulada

Hackers de chapéu branco:
São hackers éticos, que trabalham em empresas ou como free lancers para testar o sistema constantemente procurando por vulnerabilidades, eles também são responsáveis pela defesa do sistema em ataques hackers. 
Pessoa: Kevin Mitnick

Hackers de Chapéu Preto:
São hackers maliciosos que possuem a intenção de realizar ataques, sequestrar informações derrubar aplicações, fazer ataques DDoS, costumam conseguir informações para ganho próprio e vender na Deep/Dark WEB
Grupo LAPSUS$

Hackers de Chapéu Cinza:
São hackers que muitas vezes procuram fama, ou ego tecnológico, que invadem uma empresa sem permissão e anunciam a invasão sem causar danos, muitas vezes é para fazer uma pressão por transparência, ou vingança pessoal
Pessoa: **Khalil Shreateh**

Script Kiddies:
Pessoas com habilidade reduzida ou não aprofundada que muitas vezes utilizam programas prontos para realizar seus ataques, muitas vezes nem entendem o que estão fazendo, só utilizando ferramentas automatizadas
pessoa: Mafiaboy

### Questão 11 -

#### Slide

#### Resposta GPT

**a) Tipos de Malware**

De acordo com o material, os principais tipos de **malwares** são:

- **Vírus:** programa que se propaga infectando outros arquivos e programas. Pode causar desde pequenas alterações até destruição de dados.
    
- **Worm:** propaga-se automaticamente pela rede, explorando falhas de segurança.
    
- **Backdoor:** ponto de acesso secreto que permite o retorno de um invasor ao sistema.
    
- **Cavalo de Troia (Trojan):** programa que aparenta ser legítimo, mas executa funções maliciosas ocultas.
    
- **Keylogger:** captura tudo o que é digitado pelo usuário.
    
- **Rootkit:** conjunto de programas usados para esconder a presença de um invasor.
    
- **Spyware:** monitora e coleta informações do usuário, podendo incluir adwares e stalkerwares.
    
- **Ransomware:** bloqueia acesso aos dados ou sistemas e exige pagamento de resgate.
    
- **Bot/Zumbi:** programa que controla um computador remotamente, geralmente usado em ataques coordenados (botnets).
    
- **Scareware:** engana o usuário com mensagens falsas de vírus, induzindo-o a instalar softwares maliciosos.
    

---

 **b) Comparação entre três tipos de malware**

| **Malware**         | **Dependência de Hospedeiro**                                | **Método de Propagação**                                              |
| ------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| **Vírus**           | Dependente (precisa infectar outro arquivo para se propagar) | Execução de programas infectados, anexos de e-mail, mídias removíveis |
| **Worm**            | Independente (não precisa de hospedeiro)                     | Rede, exploração de vulnerabilidades e falhas de segurança            |
| **Cavalo de Troia** | Dependente da execução pelo usuário                          | Downloads de arquivos, anexos de e-mail disfarçados, sites maliciosos |
|                     |                                                              |                                                                       |

 **c) Estudos de caso**

- **Ransomware WannaCry (2017):**  
    Infectou mais de **200 mil computadores** em **150 países**, afetando hospitais, empresas e governos. Explorava uma vulnerabilidade do Windows (EternalBlue). Exigia pagamento em **Bitcoin** para descriptografar arquivos.
    
- **Colonial Pipeline (2021):**  
    Ataque de ransomware que interrompeu o fornecimento de combustível na costa leste dos EUA. A empresa pagou **US$ 4,4 milhões** de resgate ao grupo **DarkSide**, evidenciando o impacto em **infraestruturas críticas**.
    
- **Backdoor SolarWinds (2020):**  
    Hackers comprometeram atualizações do software **Orion**, instalando um backdoor que permitia espionagem em larga escala. Atingiu órgãos governamentais dos EUA e grandes empresas privadas.
    

---

 **d) Diferença entre as gerações de antivírus**

- **Primeira Geração – Scanner por Assinaturas:**  
    Detecta malwares conhecidos comparando o código com uma **assinatura digital** armazenada no antivírus. Funciona apenas para vírus já identificados.
    
- **Segunda Geração – Heurística e Verificação de Integridade:**  
    Utiliza **regras heurísticas** para detectar comportamentos suspeitos e **funções hash** (checksums) para verificar alterações em arquivos, possibilitando detectar **novas variantes** ou vírus polimórficos.
    

---

 **e) Backdoor: inserção e caso real**

Um **backdoor** pode ser inserido:

- Por um **invasor**, após explorar uma vulnerabilidade;
    
- Ou embutido em um **software legítimo**, de forma proposital ou acidental.
    

**Importância para o atacante:**  
Permite **retornar ao sistema comprometido** sem precisar repetir o processo de invasão, mantendo o **acesso remoto e invisível**.

**Exemplo real:**  
O ataque à **C&M Software (2025)**, no Brasil, onde um funcionário instalou um backdoor que permitiu o **desvio de R$ 541 milhões** via sistema de mensageria do **Pix**, afetando o **Sistema de Pagamentos Brasileiro**.

---

 **f) Fases do ciclo de vida de um vírus**

1. **Latente (Inativo):**  
    O vírus está presente no sistema, mas ainda não foi ativado.
    
2. **Propagação:**  
    O vírus começa a se replicar, inserindo cópias de si mesmo em outros arquivos ou programas.
    
3. **Disparo:**  
    Ocorre quando uma **condição específica** é atendida (data, ação do usuário, execução de um programa).
    
4. **Execução:**  
    O vírus **entra em ação**, executando seu código malicioso, como apagar arquivos, roubar dados ou corromper o sistema.
    

---
#### Resposta formulada

**a)** O termo _malware_ (software malicioso) refere-se a qualquer programa criado com o objetivo de causar danos, coletar informações indevidamente ou comprometer o funcionamento de um sistema. Entre os principais tipos de malware estudados estão:

**Vírus:** programa que infecta outros arquivos, propagando-se quando o arquivo contaminado é executado.
    
 **Worm:** propaga-se automaticamente pela rede, explorando falhas de segurança sem depender de um hospedeiro.
    
 **Backdoor:** ponto de acesso oculto que permite ao invasor retornar ao sistema comprometido.
    
 **Cavalo de Troia:** programa aparentemente legítimo que executa funções maliciosas sem o conhecimento do usuário.
    
 **Keylogger:** registra todas as teclas digitadas, capturando informações sensíveis.
    
 **Rootkit:** oculta a presença de outros códigos maliciosos, garantindo persistência no sistema.
    
 **Spyware:** monitora atividades do usuário e envia dados coletados a terceiros.
    
 **Ransomware:** bloqueia o acesso a arquivos ou sistemas e exige o pagamento de resgate.
    
 **Bot/Zumbi:** programa que transforma o computador em parte de uma rede de dispositivos controlados remotamente (_botnet_).
    
 **Scareware:** utiliza engenharia social para enganar o usuário com falsos alertas de segurança.
    

---

**b)** Comparando três tipos de malware quanto à dependência de hospedeiro e métodos de propagação:

- O **vírus** é **dependente de hospedeiro**, pois precisa infectar um arquivo existente para se propagar. Normalmente se espalha por anexos de e-mail, downloads e mídias removíveis.
    
- O **worm** é **independente**, conseguindo se disseminar automaticamente pela rede ao explorar vulnerabilidades de sistemas.
    
- Já o **cavalo de troia** depende da **execução pelo usuário**, disfarçando-se como programa legítimo, jogo ou arquivo atrativo para induzir sua instalação.
    

---

**c)** Entre os casos reais estudados, destacam-se:

- **WannaCry (2017):** ransomware que afetou mais de 200 mil computadores em 150 países, explorando uma falha no Windows (EternalBlue). Criptografava os dados e exigia pagamento em Bitcoin para liberação. O ataque atingiu principalmente hospitais e órgãos públicos.
    
- **Colonial Pipeline (2021):** ataque de ransomware que paralisou o fornecimento de combustível na costa leste dos EUA. O grupo _DarkSide_ exigiu e recebeu um resgate de US$ 4,4 milhões, demonstrando o impacto desse tipo de ameaça em infraestruturas críticas.
    
- **SolarWinds (2020):** caso de _backdoor_ em atualizações do software Orion, utilizado por grandes empresas e órgãos governamentais. O código malicioso permitia espionagem em larga escala por meses sem ser detectado.
    

---

**d)** As gerações de antivírus evoluíram conforme as ameaças se tornaram mais complexas.  
A **primeira geração** baseava-se em **assinaturas digitais**, identificando vírus por meio de padrões específicos de código. Esse método só detectava malwares já conhecidos.  
A **segunda geração**, por sua vez, utiliza **regras heurísticas** e **verificação de integridade**, buscando comportamentos suspeitos e comparando _hashes_ de arquivos para identificar modificações. Assim, consegue detectar novas variantes e vírus polimórficos, mesmo sem uma assinatura previamente registrada.

---

**e)** Um **backdoor** pode ser inserido após uma invasão bem-sucedida ou embutido em softwares aparentemente legítimos, criando um ponto de acesso secreto para o invasor. Essa técnica é valiosa porque permite o **retorno silencioso** ao sistema, sem necessidade de repetir o processo de invasão.  
Um caso real foi o **ataque à C&M Software (2025)**, no qual um funcionário instalou um backdoor que permitiu o desvio de **R$ 541 milhões** do sistema de mensageria do Pix, afetando instituições financeiras e o Sistema de Pagamentos Brasileiro.

---

**f)** O ciclo de vida de um vírus é composto por quatro fases:

1. **Latente:** o vírus está presente no sistema, mas permanece inativo, aguardando condições específicas para agir.
    
2. **Propagação:** começa a se replicar, inserindo cópias de si mesmo em outros programas ou arquivos.
    
3. **Disparo:** é ativado por um evento determinado, como a execução de um programa ou uma data específica.
    
4. **Execução:** realiza a ação maliciosa planejada, que pode incluir exclusão de arquivos, roubo de informações ou danos ao sistema operacional.


### Questão 12 -

#### Slide

#### Resposta GPT

 **a) Diferença entre DoS e DDoS**

- **DoS (Denial of Service)**: ataque que visa tornar um serviço, servidor ou rede indisponível para os usuários legítimos, consumindo recursos (banda, CPU, memória, conexões) do alvo. Normalmente é executado **a partir de uma única fonte** ou de poucas fontes controladas pelo atacante.
    
- **DDoS (Distributed Denial of Service)**: versão distribuída do ataque DoS em que **múltiplos sistemas** (normalmente máquinas comprometidas chamadas _bots_ ou _zumbis_) são coordenados para inundar o alvo com tráfego simultâneo. A distribuição das fontes dificulta a mitigação e o rastreamento do autor do ataque. O uso de redes de dispositivos comprometidos (botnets) é a forma mais comum de montar um DDoS. (O conceito de _bot/zumbi_ e _botnet_ está descrito no material do curso: “Bot ou Zumbi” / “Botnets”.)

 **b) Descrição dos principais tipos de ataques DDoS**

> Observação: muitos ataques são variantes ou combinações — abaixo descrevo o princípio de cada técnica.

1. **Ataque de Amplificação DNS (DNS amplification)**
    
    - O atacante envia requisições DNS forjadas (com IP de origem igual ao do alvo) para servidores DNS recursivos abertos, solicitando respostas grandes (por exemplo, registros DNS longos). O servidor DNS responde ao IP falsificado (o alvo), amplificando o tráfego de resposta em relação ao pedido — assim um pequeno pedido gera uma grande resposta, sobrecarregando o alvo.
        
2. **Ataque de Amplificação NTP (NTP amplification)**
    
    - Semelhante ao DNS amplification, mas utiliza servidores NTP com comandos que produzem respostas grandes (ex.: `monlist`). Pedidos pequenos resultam em respostas muito maiores enviadas ao IP forjado (alvo), gerando aumento (amplificação) do volume de tráfego.
        
3. **Ataque Reflected ICMP (reflected/ping reflection)**
    
    - O atacante envia pacotes ICMP (ping) com o IP de origem falsificado (o do alvo) para muitos hosts; as respostas ICMP retornam ao alvo, inundando-o. Quando estas respostas são numerosas e provenientes de múltiplas máquinas, o efeito é DDoS.
        
4. **SYN Flood**
    
    - Explora o mecanismo de handshake TCP. O atacante envia muitas solicitações SYN (com IPs falsificados ou sem completar o handshake) ao servidor; o servidor aloca recursos e envia SYN-ACK esperando ACK final. Como as conexões não são concluídas, o servidor fica com muitas conexões em estado semi-aberto, esgotando sua capacidade de aceitar novas conexões legítimas.
        
5. **UDP Flood**
    
    - Envio massivo de pacotes UDP para portas aleatórias do alvo; o sistema destina recursos para processar esses pacotes e pode responder com ICMP “port unreachable” — consumindo banda e processamento do alvo.
        
6. **HTTP Flood**
    
    - Ataque ao nível da aplicação: requisições HTTP legítimas (GET/POST) em alta taxa para consumir recursos do servidor web (CPU, memória, conexões). Difícil de bloquear porque o tráfego pode parecer tráfego humano “real”. Pode visar páginas pesadas ou endpoints que geram processamento intenso.
        
7. **ICMP Flood**
    
    - Envio maciço de pacotes ICMP (ping) diretamente ao alvo para consumir banda e processamento. Variante simples de flood de rede.
        
8. **Slowloris**
    
    - Ataque de camada HTTP que mantém conexões HTTP abertas por longos períodos, enviando cabeçalhos HTTP incompletos (lentamente) para evitar que o servidor finalize a requisição. O objetivo é esgotar o número máximo de conexões disponíveis no servidor web, impedindo novos clientes de se conectar. Eficaz contra servidores que não limitam tempo/conexões por IP.
        
9. **HTTP/2 Rapid Reset**
    
    - Abuso do protocolo HTTP/2 enviando streams e resetando-os repetidamente (RST_STREAM) ou forjando seqüências de frames para causar trabalho extra no servidor, forçando reprocessamentos e consumo de recursos — técnica que explora comportamentos e estados do protocolo HTTP/2.
        
10. **Ping of Death**
    
    - Envio de pacotes ICMP (ou IP) parcelados cuja reassemblagem excede o tamanho máximo permitido pelo protocolo (ultrapassa 65.535 bytes). Sistemas antigos que não tratam corretamente a reassemblagem podem travar ou reiniciar quando tentam reconstruir o pacote. Hoje em dia é menos comum devido a correções em stacks de rede.
        
11. **Smurf Attack**
    
    - Variante de reflexão: solicitações ICMP (ping) são enviadas para um broadcast de uma rede com o endereço de origem forjado (IP do alvo); todos os hosts na rede respondem ao IP forjado, multiplicando as respostas em direção ao alvo — amplificando tráfego. Mitigado ao desabilitar respostas a broadcast e filtrar tráfego forjado.
        
        
 **Como um ataque DDoS é construído (uso de redes de "zumbis") e exemplo real**

 **Construção de um DDoS com botnet (visão geral)**

1. **Comprometimento de dispositivos (criação de bots)**
    
    - O atacante encontra vulnerabilidades (senhas padrão, falhas, serviços expostos) e instala malware que transforma dispositivos (PCs, servidores, IoT — câmeras, DVRs, roteadores) em _zumbis_ (bots). Esses bots geralmente se conectam a um _command-and-control_ (C2) ou aguardam instruções via canais públicos (ex.: IRC, HTTP, protocolos customizados).
        
2. **Formação da botnet**
    
    - Conjunto de bots controlados pelo atacante forma a botnet. Botnets podem ter milhares a milhões de dispositivos. As máquinas comprometidas disfarçam origem (rotatividade de IPs, uso de proxies) e aumentam a escala do ataque.
        
3. **Coordenação e comando**
    
    - O atacante envia comandos ao C2 para iniciar o ataque: parâmetros (tipo de flood, alvo, duração, taxa). O C2 replica instruções para os bots.
        
4. **Execução do ataque (inundação)**
    
    - Os bots geram tráfego coordenado (pacotes sintéticos, requisições legítimas, pedidos forjados) apontando ao alvo. O tráfego pode ser volumétrico (banda), de protocolo (SYN floods), ou de aplicação (HTTP floods). A escala distribuída torna bloqueio por simples bloqueio de IPs ineficaz.
        
5. **Manutenção / evasão**
    
    - Bots alternam padrões, usam IPs rotativos, ou empregam técnicas de reflexão/amplificação para maximizar impacto e dificultar mitigação. O atacante pode também alternar vetores para drenar recursos de mitigação do alvo.
        

> O material do curso registra que _bots/zumbis_ e _botnets_ são usados para ataques de negação de serviço (DDoS), coleta de informação, envio de spam e mineração de criptomoeda — ou seja, DDoS é uma das finalidades típicas de uma botnet.

---
#### Resposta Formulada