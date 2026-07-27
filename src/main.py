import machine
import time

PIN_LDR = 34
PIN_BTN = 32
PIN_LED = 2

ldr = machine.ADC(machine.Pin(PIN_LDR))
ldr.atten(machine.ADC.ATTN_11DB)  

btn = machine.Pin(PIN_BTN, machine.Pin.IN, machine.Pin.PULL_UP)

led = machine.Pin(PIN_LED, machine.Pin.OUT)

total_pecas = 0
estado_bloqueado = False

tempo_inicio_bloqueio = 0
microparada_disparada = False
ultimo_tempo_btn = 0

LIMIAR_LUZ_BLOQUEIO = 1000  
TEMPO_MICROPARADA_MS = 5000  
DEBOUNCE_BTN_MS = 200

print("Contador de Producao Inicializado")

while True:
    tempo_atual = time.ticks_ms()
    valor_lux = ldr.read()

    if valor_lux < LIMIAR_LUZ_BLOQUEIO:
        if not estado_bloqueado:
            estado_bloqueado = True
            tempo_inicio_bloqueio = tempo_atual
            microparada_disparada = False
            led.value(1)  # Acende o LED avisando que há obstrução
        else:
            if not microparada_disparada and time.ticks_diff(tempo_atual, tempo_inicio_bloqueio) >= TEMPO_MICROPARADA_MS:
                print("Alerta: Micro-parada detectada!")
                microparada_disparada = True

    else:

        if estado_bloqueado:
            estado_bloqueado = False
            led.value(0)
            1
            total_pecas += 1
            print(f"Peca detectada! Total: {total_pecas}")


    if btn.value() == 0:  # Botão pressionado (Pull-Up = 0)
        if time.ticks_diff(tempo_atual, ultimo_tempo_btn) >= DEBOUNCE_BTN_MS:
            ultimo_tempo_btn = tempo_atual
            total_pecas = 0
            estado_bloqueado = False
            microparada_disparada = False
            led.value(0)
            print("Turno resetado com sucesso. Contadores zerados.")

    time.sleep_ms(20)