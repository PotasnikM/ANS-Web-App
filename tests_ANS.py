import random
import math
from ANS.ANS_rescaling import ans_decoder_rescaling, ans_encoder_rescaling
from ANS.ANS_no_rescaling import ans_decoder_no_rescaling, ans_encoder_no_rescaling

# initialize data distribution and input length
p = [20, 50, 80, 106]
c = [0, 20, 70, 150]
r = 8
r_s = 32
r_t = 16
sequence_length = 100000

# randomly sample input
random.seed(2)
symbols = random.choices(range(len(p)), weights=p, k=sequence_length)

# encode
s, t_stack = ans_encoder_rescaling(symbols, p, c, r, r_s, r_t)

# decode
decoded_symbols = ans_decoder_rescaling(s, t_stack[:], p, c, r, r_s, r_t)

# statistics
average_bps = (r_s + len(t_stack) * r_t) / sequence_length
entropy = sum(-i / 2 ** r * math.log2(i / 2 ** r) for i in p)

# sanity check
assert all(x == y for x, y in zip(decoded_symbols, symbols))

# display results
print(f"data source entropy    : {entropy:.5f} bits/symbol")
print("ANS with rescaling")
print(f"average bits per symbol: {average_bps:.5f} bits/symbol")

# encode
s = ans_encoder_no_rescaling(symbols, p, c, r)

# decode
decoded_symbols = ans_decoder_no_rescaling(s, p, c, r)

# statistics
average_bps = math.log2(s) / sequence_length

# sanity check
assert all(x == y for x, y in zip(decoded_symbols, symbols))

# display results
print("ANS with no rescaling")
print(f"average bits per symbol: {average_bps:.5f} bits/symbol")