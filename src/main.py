import machine
import time

ldr = machine.ADC(machine.Pin(34))
ldr.atten(machine.ADC.ATTN_11DB)
btn = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

print("Contador de Producao Inicializado")

total_pecas = 0
luz_bloqueada = False
tempo_inicio_bloqueio = 0
alerta_emitido = False

btn_pressionado = False
ultimo_clique_btn = 0

while True:
    valor_ldr = ldr.read()
    tempo_atual = time.ticks_ms()

    if valor_ldr < 1000:
        if not luz_bloqueada:

            luz_bloqueada = True
            tempo_inicio_bloqueio = tempo_atual
            alerta_emitido = False
        else:
            if not alerta_emitido and time.ticks_diff(tempo_atual, tempo_inicio_bloqueio) >= 5000:
                print("Alerta: Micro-parada detectada!")
                alerta_emitido = True
                
    elif valor_ldr > 2000:
        if luz_bloqueada:
            # A peça saiu totalmente do sensor
            total_pecas += 1
            print(f"Peca detectada! Total: {total_pecas}")
            luz_bloqueada = False
            alerta_emitido = False

    leitura_botao = btn.value()
    if leitura_botao == 0 and not btn_pressionado:
        if time.ticks_diff(tempo_atual, ultimo_clique_btn) > 200:
            total_pecas = 0
            luz_bloqueada = False
            alerta_emitido = False
            print("Turno resetado com sucesso. Contadores zerados.")
            ultimo_clique_btn = tempo_atual
            btn_pressionado = True
    elif leitura_botao == 1:
        btn_pressionado = False

    time.sleep_ms(10)