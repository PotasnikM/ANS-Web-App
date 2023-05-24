import random
import math
from ANS.ANS_no_rescaling import ans_decoder_no_rescaling, ans_encoder_no_rescaling

# initialize data distribution and input length
p = [20, 50, 80, 106]
c = [0, 20, 70, 150]
r = 8
r_s = 32
r_t = 16
sequence_length = 10000

# randomly sample input
random.seed(2)
symbols = random.choices(range(len(p)), weights=p, k=sequence_length)

# statistics
entropy = sum(-i / 2 ** r * math.log2(i / 2 ** r) for i in p)

# encode
s = ans_encoder_no_rescaling(symbols)

# decode
decoded_symbols = ans_decoder_no_rescaling(s)

# statistics
average_bps = math.log2(s) / sequence_length

# sanity check
assert all(x == y for x, y in zip(decoded_symbols, symbols))

# display results
print("ANS with no rescaling")
print(f"average bits per symbol: {average_bps:.5f} bits/symbol")