#coding:utf-8
import socket
import sys,time
import threading
import struct
import sys
sys.path.append("../")
import utils.tools as tools
class party():
    max_length = 1024
    Host = ''
    Port = 50025
    Protocol = ""

    def broadcastUdp(self,message,Port=50025, broadcast_address='255.255.255.255'):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.bind(Host,Port)
        print(message)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        for m in message:
            s.sendto(m.encode(), (broadcast_address, Port))
        s.sendto(b'T', (broadcast_address, Port))
        s.close()
        return None
    def revBroadcastUdp(self,Port=50025, broadcast_address=''):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((broadcast_address, Port))
        received_message = []
        while(True):
            data, addr = s.recvfrom(1024)
            received_message.append(data)
            print(data.decode())
            if data.decode()=="T":
                break
        s.close()
        with open('/Users/jaden/PycharmProjects/ISEC_MPC/Networking/transData/'+self.Protocol, 'ab') as f:
            for i in received_message[:-1]:
                f.write(i)
        return received_message[:-1]
