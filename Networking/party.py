#coding:utf-8
from socket import *
import sys,time
import threading

class party():
    max_length = 1024
    received_meg = []
    Host = ''
    Port = 50025


    # def send(self,data,party_list):
    #     n = len(party_list)
    #     sockobj_client = socket(AF_INET, SOCK_STREAM)
    #     threads = []
    #
    #     def send_one_party(self,data,party,sockobj_client):
    #         rev_data = []
    #         sockobj_server = socket(AF_INET, SOCK_STREAM)
    #         sockobj_server.bind(party.Host,party.Port)
    #         sockobj_server.listen(n)
    #         while True:
    #             try:
    #                 connection, address = sockobj_server.accept()
    #                 print(f"{party.Host} is connected by {address}")
    #                 while True:
    #                     d = connection.recv(self.max_length)
    #                     rev_data.append(d)
    #                     if not d: break
    #             finally:
    #                 connection.close()
    #     try:
    #         for i in party_list:
    #
    #             sockobj.connect((i.Host, i.Port))
    #             for line in data:
    #                 sockobj.send(line.encode(encoding='utf-8', errors='strict'))
    #             response = sockobj.recv(self.max_length)
    #             print(f"Receive response from {i.Host}:{response.decode(encoding='utf-8')}")
    #     finally:
    #         sockobj.close()

    def listening(self):
        buf = []
        def stoc(client_socket, addr):
            while True:
                try:
                    client_socket.settimeout(500)
                    b = client_socket.recv(self.max_length).decode(encoding='utf-8',errors= 'strict')
                    print("server got msg from", str(addr[1]), b)
                    if b:
                        buf.append(b)
                    else:
                        print("b is null")
                except socket.timeout:
                    print('time out')
                client_socket.close()
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.bind((self.Host, self.Port))
        sockobj.listen(5)
        while True:
            client, address = sockobj.accept()
            print('Server connected by', address)
            thread = threading.Thread(target=stoc, args=(client, address))
            thread.start()
        sockobj.close()
        return buf

    def connecting(self,party):
        serverHost,serverPort = party.Host, party.Port
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((serverHost, serverPort))
        return sockobj

    def send(self,sockobj,data):
        while True:
            sockobj.send(data.encode(encoding='utf-8',errors= 'strict'))
            time.sleep(4)
            data = sockobj.recv(self.max_length)
            if not data: break
            print('Client received:', data)
        sockobj.close()

