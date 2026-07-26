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
