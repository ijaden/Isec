from party import *

if __name__ == "__main__":


    data = "2"
    p1 = party()
    sockobj = p1.connecting('',50025)
    p1.send(sockobj, data)
    print("sender")
