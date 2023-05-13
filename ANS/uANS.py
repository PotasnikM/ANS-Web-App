from math import ceil, floor
import numpy as np

def encode(msg, p):
    x = 1
    for s in msg:
        if s == 0:
            x = ceil((x+1)/(1-p)) - 1
        else:
            x = floor(x/p)
    return x

def decode(encoded_msg, p):
    msg = []
    while encoded_msg > 1:
        s = ceil((encoded_msg+1)*p) - ceil(encoded_msg*p)
        msg.append(s)
        if s == 0:
            encoded_msg = encoded_msg - ceil(encoded_msg*p)
        else:
            encoded_msg = ceil(encoded_msg*p)
    return list(reversed(msg))

if __name__ == '__main__':
    p1 = 0.3
    msg = np.ndarray.tolist(np.random.choice(np.arange(0,2), p=[1-p1, p1], size=30))
    print(msg)
    encoded = encode(msg, p1)
    print(encoded)
    decoded = decode(encoded, p1)
    print(decoded)
