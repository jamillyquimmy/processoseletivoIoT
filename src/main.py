import machine
import time

ldr = machine.ADC(machine.Pin(34))
ldr.atten(machine.ADC.ATTN_11V) # Configuração para leitura total de 0-4095
btn = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

print("Contador de Producao Inicializado")

total_pecas = 0
luz_bloqueada = False
tempo_inicio_bloqueio = 0
alerta_emitido = False
ultimo_clique_btn = 0

while True:
    valor_ldr = ldr.read()
    tempo_atual = time.ticks_ms()
    
    if valor_ldr < 1000 and not luz_bloqueada:
        luz_bloqueada = True
        tempo_inicio_bloqueio = tempo_atual 
        alerta_emitido = False              

    elif valor_ldr > 2000 and luz_bloqueada:
        luz_bloqueada = False               
        total_pecas += 1
        print(f"Peca detectada! Total: {total_pecas}")

    if luz_bloqueada and not alerta_emitido:

        if time.ticks_diff(tempo_atual, tempo_inicio_bloqueio) >= 5000:
            print("Alerta: Micro-parada detectada!")
            alerta_emitido = True # Trava para não repetir o erro infinitamente
            
    if btn.value() == 0:
        if time.ticks_diff(tempo_atual, ultimo_clique_btn) > 200: # Debounce de 200ms
            total_pecas = 0
            luz_bloqueada = False
            alerta_emitido = False
            print("Turno resetado com sucesso. Contadores zerados.")
            ultimo_clique_btn = tempo_atual

    time.sleep_ms(50)