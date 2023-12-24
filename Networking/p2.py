from party import *

if __name__ == "__main__":
    data = "2"
    p2 = party()
    sockobj = p2.connecting(1,2)
    p2.send(sockobj,data)
    p2.close(sockobj)
    print("sender")
