def tans_encode(data):
    symbol_occurrences = {}
    for symbol in data:
        if symbol in symbol_occurrences:
            symbol_occurrences[symbol] += 1
        else:
            symbol_occurrences[symbol] = 1
    # Create a dictionary to hold the codewords for each symbol
    codewords = {}
    # Create a list of tuples representing each symbol with its occurrence count
    symbol_counts = [(symbol, symbol_occurrences[symbol]) for symbol in symbol_occurrences]
    # Sort the symbols in descending order of their occurrence count
    symbol_counts = sorted(symbol_counts, key=lambda x: x[1], reverse=True)
    # Calculate the maximum number of bits required to represent the codewords
    max_bits = len(bin(len(symbol_counts) - 1)[2:])
    # Generate the prefix-free codewords for each symbol
    for i in range(len(symbol_counts)):
        binary_codeword = bin(i)[2:].zfill(max_bits)
        symbol = symbol_counts[i][0]
        codewords[symbol] = binary_codeword
    # Encode the data using the codewords
    encoded_data = ''
    for symbol in data:
        encoded_data += codewords[symbol]
    return encoded_data, symbol_occurrences


def tans_decode(encoded_data, symbol_occurrences):
    # Create a dictionary to hold the inverse of the codewords
    inverse_codewords = {}
    # Create a list of tuples representing each symbol with its occurrence count
    symbol_counts = [(symbol, symbol_occurrences[symbol]) for symbol in symbol_occurrences]
    # Sort the symbols in descending order of their occurrence count
    symbol_counts = sorted(symbol_counts, key=lambda x: x[1], reverse=True)
    # Calculate the maximum number of bits required to represent the codewords
    max_bits = len(bin(len(symbol_counts) - 1)[2:])
    # Generate the prefix-free codewords for each symbol
    for i in range(len(symbol_counts)):
        binary_codeword = bin(i)[2:].zfill(max_bits)
        symbol = symbol_counts[i][0]
        inverse_codewords[binary_codeword] = symbol
    # Decode the data using the inverse codewords
    decoded_data = ''
    current_codeword = ''
    for bit in encoded_data:
        current_codeword += bit
        if current_codeword in inverse_codewords:
            decoded_data += inverse_codewords[current_codeword]
            current_codeword = ''
    return decoded_data


if __name__ == '__main__':
    # Example usage
    data = '2137211569420'
    encoded_data = tans_encode(data)
    decoded_data = tans_decode(encoded_data)
    print(f"Data: {data}")
    print(f"Encoded data: {encoded_data}")
    print(f"Decoded data: {decoded_data}")
