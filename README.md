# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_CLI_TOKEN
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais
 
#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os 
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- **Nome completo:**
Jamilly Quimmy Vereda de Souza
- **GitHub:**
https://github.com/jamillyquimmy
---

## Visão Geral da Solução
O objetivo do projeto é implementar um **Contador de Produção Não-Intrusivo** voltado para linhas de montagem e esteiras industriais que operam sem CLPs (Controladores Lógicos Programáveis).

O sistema embarcado utiliza um sensor óptico baseado em LDR para monitorar o fluxo de peças e caixas através da variação de luminosidade. Ao identificar a passagem completa de um objeto, o firmware incrementa a contagem de produção, monitora eventuais gargalos e travamentos da esteira (micro-paradas) e permite o zeramento dos contadores do turno de trabalho por meio de um botão físico de reset.

---

## Arquitetura do Sistema Embarcado
A solução foi estruturada em MicroPython utilizando o conceito de **máquina de estados finitos (FSM)** e **temporização não-bloqueante**:

1. **Inicialização:** Configuração do pino analógico (ADC) para o LDR e pino digital em Pull-Up para o botão. Emissão obrigatória da mensagem `Contador de Producao Inicializado`.
2. **Loop Principal (`while True`):**
   - **Detecção de Peça:** Transição de ambiente iluminado para bloqueado (< 1000 lux) sinaliza a entrada da peça. O incremento do contador ocorre na borda de subida (retorno da luz > 2000 lux), emitindo a mensagem `Peca detectada! Total: X`.
   - **Detecção de Micro-parada:** Caso a luz permaneça bloqueada por um período superior a 5000 ms (5 segundos), o cronômetro não-bloqueante dispara o alerta `Alerta: Micro-parada detectada!`.
   - **Rotina de Reset:** Leitura do botão `btn1` com tratamento de *debounce* por tempo (200 ms) para zerar as variáveis globais e exibir `Turno resetado com sucesso. Contadores zerados.`.

---

## Componentes Utilizados na Simulação
Mapeados e configurados no arquivo `diagram.json`:

- **ESP32 DevKit C v4 (`esp`):** Microcontrolador principal responsável pela execução da lógica de controle e temporização.
- **Sensor Fotorresistor LDR (`ldr1`):** Conectado ao pino analógico `GPIO 34` (ADC), responsável pela leitura dos níveis de luminosidade em lux.
- **Botão Pushbutton (`btn1`):** Conectado ao pino digital `GPIO 32` em modo `PULL_UP`, utilizado pelo operador para resetar a contagem do turno.
- **Interface Serial (UART):** Comunicação via pinos `TX/RX` para transmissão de telemetria e validação automática.

---

## Decisões Técnicas Relevantes

- **Programação Não-Bloqueante:** Uso exclusivo de `time.ticks_ms()` e `time.ticks_diff()` em vez de `time.sleep()` prolongado. Isso garante alta frequência de amostragem dos sensores sem perder eventos de tempo na esteira contínua.
- **Tratamento de Debounce:** Implementação de controle de reboco via software no botão de reset para evitar múltiplos disparos falsos causados por ruídos mecânicos.
- **Detecção por Borda de Subida:** A contagem só é efetivada quando o objeto sai totalmente da frente do sensor, garantindo precisão e evitando contagens duplicadas.
- **Padronização Estrita de Strings:** Garantia de correspondência exata de maiúsculas, minúsculas e pontuações exigidas pela esteira de integração contínua (Wokwi CI).
---

## Resultados Obtidos

- **Contagem Precisa:** Identificação e incremento correto do fluxo de peças na esteira simulada.
- **Detecção de Falhas:** Emissão bem-sucedida de alerta de micro-parada ao simular retenção de objeto por mais de 5 segundos.
- **Reset Operacional:** Zeramento correto de todos os acumuladores ao acionar o botão de reset.
- **Aprovação no CI:** Sucesso na validação de todos os cenários automatizados via GitHub Actions.

## Comentários Adicionais (Opcional)

---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
