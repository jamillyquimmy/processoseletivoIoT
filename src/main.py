import machine
import time


ldr_pin = machine.ADC(machine.Pin(34))
ldr_pin.atten(machine.ADC.ATTN_11DB)

btn_pin = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

contador = 0
peca_passando = False
tempo_bloqueio = 0
alerta_enviado = False
ultimo_estado_btn = 1
ultimo_tempo_debounce = 0

print("Contador de Producao Inicializado")

while True:
    tempo_atual = time.ticks_ms()

    valor_ldr = ldr_pin.read()
    
    if valor_ldr < 1000 and not peca_passando:
        peca_passando = True
        tempo_bloqueio = tempo_atual
        alerta_enviado = False

    elif valor_ldr > 2000 and peca_passando:
        peca_passando = False
        contador += 1
        print(f"Peca detectada! Total: {contador}")


    if peca_passando and not alerta_enviado:
        if time.ticks_diff(tempo_atual, tempo_bloqueio) > 5000:
            print("Alerta: Micro-parada detectada!")
            alerta_enviado = True


    estado_btn = btn_pin.value()
    
    if estado_btn == 0 and ultimo_estado_btn == 1:
        if time.ticks_diff(tempo_atual, ultimo_tempo_debounce) > 200:
            contador = 0
            peca_passando = False
            alerta_enviado = False
            ultimo_tempo_debounce = tempo_atual
            print("Turno resetado com sucesso. Contadores zerados.")
            
    ultimo_estado_btn = estado_btn

    time.sleep_ms(10)