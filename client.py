import socket

HOST = 'localhost'
PORT = 7778

def send_message(message):
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as client:
        client.sendto(message.encode('UTF-8'), (HOST, PORT)) 

if __name__ == '__main__':
    message = "Mensaje enviado con éxito desde el cliente al servidor."
    send_message(message)