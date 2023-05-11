def ans_encoder_no_rescaling(symbols, p, c, r):
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
    s = 0
    for x in symbols:
        if s < c[1]:
            s += 1
        s = 2 ** r * (s // p[x]) + s % p[x] + c[x]
    return s


def ans_decoder_no_rescaling(s, p, c, r):
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

    def h(s):
        s = s % 2 ** r
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
    return list(reversed(decoded_symbols))
