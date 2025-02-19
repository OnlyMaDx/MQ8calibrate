from machine import ADC, Pin
import time

# Konstanta
ADC_MAX = 4095  # Resolusi 12-bit ESP32
V_REF = 3.3  # Tegangan referensi ESP32
SENSOR_PIN = 34  # Gunakan GPIO34 untuk input analog

# Inisialisasi ADC
sensor = ADC(Pin(SENSOR_PIN))
sensor.atten(ADC.ATTN_11DB)  # Mengatur ADC agar bisa membaca hingga 3.3V

print("Sensor mulai...")

while True:
    # Membaca nilai ADC (0 - 4095)
    sensor_value = sensor.read()
    
    # Konversi ke tegangan (Volt)
    sensor_voltage = (sensor_value / ADC_MAX) * V_REF
    
    # Menampilkan hasil ke serial monitor
    print(f"Sensor Voltage = {sensor_voltage:.2f} V")
    
    time.sleep(1)  # Tunggu 1 detik
