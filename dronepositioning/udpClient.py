import socket
import time
import binascii
import struct
import threading
UDP_HOST = "127.0.0.1"
UDP_PORT = 7000
ADDRESS = (UDP_HOST, UDP_PORT)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

drone_position = (1, 345, bytes('cordX', 'utf-8'), bytes('cordY', 'utf-8'))
drone_position2 = (2, 345, bytes('cordX', 'utf-8'), bytes('cordY', 'utf-8'))
drone_position3 = (3, 345, bytes('cordX', 'utf-8'), bytes('cordY', 'utf-8'))
drone_position4 = (4, 345, bytes('cordX', 'utf-8'), bytes('cordY', 'utf-8'))
drone_position5 = (5, 345, bytes('cordX', 'utf-8'), bytes('cordY', 'utf-8'))
pack_data = struct.Struct('i i 5s 5s')
packed_data = pack_data.pack(*drone_position)
packed_data2 = pack_data.pack(*drone_position2)
packed_data3 = pack_data.pack(*drone_position3)
packed_data4 = pack_data.pack(*drone_position4)
packed_data5 = pack_data.pack(*drone_position5)


def threads(packed_data_thread):
    while True:
        time.sleep(0.3)
        print(binascii.hexlify(packed_data_thread), drone_position)
        clientSocket.sendto(packed_data_thread, ADDRESS)


if __name__ == "__main__":

    process1 = threading.Thread(target=threads, args=(packed_data,))
    process2 = threading.Thread(target=threads, args=(packed_data2,))
    process3 = threading.Thread(target=threads, args=(packed_data3,))
    process4 = threading.Thread(target=threads, args=(packed_data4,))
    process5 = threading.Thread(target=threads, args=(packed_data5,))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()

