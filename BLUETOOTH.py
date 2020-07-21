import numpy as np
from time import sleep
import bluetooth
from PIL import Image

# bluetooth addres
bd_addr = "98:D3:34:90:A8:F2"

port = 1

# bluetooth connection
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

endstring = '/n'
data = []
frame = []
new = 'a'
old = 'b'
flag = False
counter = 0
counter1 = 0
HEIGHT = 120
WIDTH = 160
rgb = np.zeros([120, 160], dtype=np.uint8)
rgb2 = np.zeros([160, 120, 3], dtype=np.uint8)
msg_size = HEIGHT * WIDTH + 5
sock.send("S")
while (True):

    # while endstring not in received_data:

    while len(data) < (msg_size):
        data += sock.recv(4096)
    frame = data[:msg_size]
    data = data[msg_size:]
    i = 5
    for y in range(HEIGHT):
        for x in range(WIDTH):
            rgb[y][x] = ord(frame[i])
            i += 1
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # gray image
            Y = rgb[y][x]
            R = Y  # + 1.402*(- 128)
            G = Y  # - 0.34414*(- 128) - 0.71414*( - 128)
            B = Y  # + 1.772*(- 128)

            if (R < 0):
                R = 0
            elif (R > 255):
                R = 255
            if (G < 0):
                G = 0
            elif (G > 255):
                G = 255
            if (B < 0):
                B = 0
            elif (B > 255):
                B = 255
            rgb2[x][y][0] = int(round(R))
            rgb2[x][y][1] = int(round(G))
            rgb2[x][y][2] = int(round(B))

    img = Image.fromarray(rgb2)
    img.show()

    sleep(0.1)
    print("-----------------------------------")
    print(frame)

# print(counter)
sock.close()
