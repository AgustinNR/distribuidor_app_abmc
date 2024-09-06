import socketserver
import os
import datetime

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

class UDPserver_request_handler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request[0].strip().decode("UTF-8") + " - " + str(datetime.datetime.now()) + "\n")
        write_log(data)
        socket = self.request[1]
        reply = "Se recibieron los datos en el servidor."
        socket.sendto(reply.encode("UTF-8"), self.client_address)


def write_log(data):
    server_log_path = os.path.join(BASE_DIR, "server_log.txt")
    server_log_file = open(server_log_path, "a") #argumento "a" = modo de apertura: append
    server_log_file.write(data)
    server_log_file.close()


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 7778
    print("Servidor iniciado con éxito.")
    print("Escuchando en el puerto:", PORT)
    with socketserver.UDPServer((HOST, PORT), UDPserver_request_handler) as server:
        server.serve_forever()