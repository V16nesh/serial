import serial
serial_port = '/dev/ttyS0'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)
try:
    while True:
        data = ser.readline().decode().strip()
        print(data)
except KeyboardInterrupt:
    ser.close()
