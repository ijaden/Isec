import psutil
import time
import socket

def get_port_traffic(port=50025):
    connections = psutil.net_connections()
    total_bytes = 0
    for conn in connections:
        if conn.status == 'ESTABLISHED' and conn.laddr.port == port:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.bind((conn.laddr.ip, port))
                sock.listen(1)
                while True:
                    client_sock, address = sock.accept()
                    data = client_sock.recv(1024)
                    total_bytes += len(data)
                    print(f"Received {len(data)} bytes from {address}")
                    client_sock.close()
            except KeyboardInterrupt:
                break
            finally:
                sock.close()

    print(f"Total bytes received on port {port}: {total_bytes}")

if __name__ == "__main__":
    while (True):
        port = 50025  # 指定要获取流量的端口
        get_port_traffic(port)