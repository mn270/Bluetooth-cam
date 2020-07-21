import serial
"""
sample uart communication
"""
# Serial takes two parameters: serial device and baudrate
ser = serial.Serial('/dev/ttyACM0', 9600)
counter = 0
# data = ser.read(ser.inWaiting())
data_ = "f"
licz = False
while (1):
    data = ser.read(1)
    # data = ser.read(ser.inWaiting())
    # print(data.encode('hex'))
    print(data)
