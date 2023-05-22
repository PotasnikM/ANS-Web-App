from math import ceil, floor
import numpy as np

def uans_encode(msg):
    p = 0.3
    x = 1
    for s in msg:
        if s == 0:
            x = ceil((x+1)/(1-p)) - 1
        else:
            x = floor(x/p)
    return x

def uans_decode(encoded_msg):
    encoded_msg = int(encoded_msg)
    p = 0.3
    msg = []
    while encoded_msg > 1:
        s = ceil((encoded_msg+1)*p) - ceil(encoded_msg*p)
        msg.append(s)
        if s == 0:
            encoded_msg = encoded_msg - ceil(encoded_msg*p)
        else:
            encoded_msg = ceil(encoded_msg*p)
    return ''.join(map(str, reversed(msg)))

if __name__ == '__main__':
    p1 = 0.3
    msg = np.ndarray.tolist(np.random.choice(np.arange(0,2), p=[1-p1, p1], size=30))
    print(msg)
    encoded = uans_encode(msg)
    print(encoded)
    decoded = uans_decode(encoded)
    print(decoded)
