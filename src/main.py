import machine
import time

PIN_LDR = 34
PIN_LED = 2

ldr = machine.ADC(machine.Pin(PIN_LDR))
ldr.atten(machine.ADC.ATTN_11V)   
ldr.width(machine.ADC.WIDTH_12BIT) 

led = machine.Pin(PIN_LED, machine.Pin.OUT)

INTERVALO_LEITURA_MS = 100 # Intervalo de leitura
ultima_leitura = 0
LIMITE_LUZ = 2000 

print("Iniciando monitoramento Light...")

while True:
    tempo_atual = time.ticks_ms()
    
    if time.ticks_diff(tempo_atual, ultima_leitura) >= INTERVALO_LEITURA_MS:
        ultima_leitura = tempo_atual
        
        valor_luz = ldr.read()
        
        if valor_luz > LIMITE_LUZ: 
            led.value(1) # Liga LED
            print(f"Luz detectada: Escuro ({valor_luz})") 
        else:
            led.value(0) # Apaga LED
            print(f"Luz detectada: Claro ({valor_luz})")
            
    time.sleep_ms(10)