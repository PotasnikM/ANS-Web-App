from math import ceil, floor
import numpy as np

def uans_encode(msg, p1):
    msg_dec = [int(x) for x in msg]
    #p1 = 0.1
    x = 1
    for s in msg_dec:
        if s == 0:
            x = ceil((x+1)/(1-p1)) - 1
        else:
            x = floor(x/p1)
    return x

def uans_decode(encoded_msg, p1):
    encoded_msg = int(encoded_msg)
    msg = []
    #p1=0.1

    while encoded_msg > 1:
        s = ceil((encoded_msg+1)*p1) - ceil(encoded_msg*p1)
        msg.append(s)
        if s == 0:
            encoded_msg = encoded_msg - ceil(encoded_msg*p1)
        else:
            encoded_msg = ceil(encoded_msg*p1)
    return ''.join(map(str, reversed(msg)))

if __name__ == '__main__':
    p1 = 0.6
    msg = np.ndarray.tolist(np.random.choice(np.arange(0,2), p=[1-p1, p1], size=30))
    msg='011001100101011010110110010011'
    print(msg)
    encoded = uans_encode(msg)
    print(encoded)
    decoded = uans_decode(encoded)
    print(decoded)
