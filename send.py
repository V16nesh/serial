import serial
import time

serial_port = '/dev/ttyS0' 
baud_rate = 9600  
ser = serial.Serial(serial_port, baud_rate)

i = 1
while True:
    data_to_send = "hi " + str(i) + "\n"
    ser.write(data_to_send.encode('utf-8'))  # Encoding string to bytes
    print("Sent data: "+data_to_send)
    i += 1
    time.sleep(1)
