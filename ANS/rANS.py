def rans_encoder(symbols):
    """ ANS encoder (no rescaling)

    Parameters
    ----------
    symbols : list of int
        list of input symbols represented by index
        value should not be larger than len(p)
    p : list of int
        quantized pmf of all input alphabet, sum(p) == 2 ** r
    c : list of int
        quantized cdf of all input alphabet, len(c) = len(p)
        c[0] = 0, and c[-1] = sum(p[:-1])
    r : int
        bit-width precision of the quantized pmf
        sum(p) == 2 ** r


    Returns
    -------
    s : integer representation of the encoded message

    """
    p = [20, 50, 80, 106]
    c = [0, 20, 70, 150]
    r = 8
    s = 0
    symbols = list(map(int, symbols))
    print(symbols)
    for x in symbols:
        if s < c[1]:
            s += 1
        s = 2 ** r * (s // p[x]) + s % p[x] + c[x]
    return s


def rans_decoder(s):
    """ ANS encoder (no rescaling)

    Parameters
    ----------
    s : int
        integer representation of the encoded message
    p : list of int
        quantized pmf of all input alphabet, sum(p) == 2 ** r
    c : list of int
        quantized cdf of all input alphabet, len(c) = len(p)
        c[0] = 0, and c[-1] = sum(p[:-1])
    r : int
        bit-width precision of the quantized pmf
        sum(p) == 2 ** r


    Returns
    -------
    decoded_symbols : list of int
        list of decoded symbols

    """
    p = [20, 50, 80, 106]
    c = [0, 20, 70, 150]
    r = 8
    s = int(s)
    def h(s):
        s = int(s) % 2 ** r
        # this loop can be improved by binary search
        for a in reversed(range(len(c))):
            if s >= c[a]:
                return a

    decoded_symbols = []
    while s:
        x = h(s)
        decoded_symbols.append(x)
        s = p[x] * (s // 2 ** r) + \
            s % (2 ** r) - c[x]
        if s < c[1]:
            s -= 1
    decoded_symbols = list(reversed(decoded_symbols))
    decoded_symbols = ''.join(str(num) for num in decoded_symbols)
    return decoded_symbols
