from party import *

if __name__ == "__main__":
    p2 = party()
    p2.Protocol='MSS'
    data = p2.revBroadcastUdp()[:-1]
    print(data)
    print("receiver")