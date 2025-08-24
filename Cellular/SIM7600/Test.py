import serial
import time

# Change port if needed
PORT = "/dev/serial1"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

def send_at(command, delay=1):
    ser.write((command + "\r\n").encode())
    time.sleep(delay)
    while ser.in_waiting:
        print(ser.readline().decode(errors="ignore").strip())

# Flush any old data
ser.flushInput()

print("Testing SIM7600 connection...")
send_at("AT")            # Basic check
send_at("AT+CSQ")         # Signal quality
send_at("AT+CREG?")       # Network registration
send_at("AT+COPS?")       # Operator info
send_at("AT+CGATT?")      # Packet service attach status

ser.close()