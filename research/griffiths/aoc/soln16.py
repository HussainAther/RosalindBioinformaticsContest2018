def hex_to_bin(s):
    return bin(int(s, 16))[2:]


# leading 0's until the length is a multiple of 4
def leading_zeros(a):
    return "0" * ((4 - len(a) % 4) % 4) + a


def parse_header(s, to_decimal=False):
    return (int(s[0:3], 2), int(s[3:6], 2)) if to_decimal else (s[0:3], s[3:6])


def parse_literal(packet, to_decimal=False):
    num_bits = 5
    num_bin = packet[6:]
    binary_numbers = [num_bin[i:i+num_bits] for i in range(0, len(num_bin), num_bits)
                      if len(num_bin[i:i+num_bits]) == 5]

    # binary_numbers = [num for num in binary_numbers if num != "00000"]
    
    parsed_literal = ""
    parse_counter = 0
    
    for binary_number in binary_numbers:
        parsed_literal += binary_number[1:]
        parse_counter += 1
        
        # check if binary_number starts with a 0 and marks the last chunk
        if binary_number[0] == "0":
            # if there are more 5 bit chunks, consider them a new packet
            if len(binary_numbers) != parse_counter:
                parse_packet(num_bin[parse_counter * num_bits:])
            break
        
    if to_decimal:
        return int(parsed_literal, 2)
    
    return parsed_literal


def parse_operator(packet):
    length_type_id = packet[6]
    length_of_bits = 0
    
    if length_type_id == "0":
        length_of_bits = 15
    elif length_type_id == "1":
        length_of_bits = 11
    
    L_bin = packet[7:7+length_of_bits]
    L = int(L_bin, 2)

    if length_type_id == "0":
        sub_packets_1 = packet[7+length_of_bits:7+length_of_bits+L]
        sub_packets_2 = packet[7+length_of_bits+L:]
        parse_packet(sub_packets_1)
        parse_packet(sub_packets_2)

    elif length_type_id == "1":
        sub_packets = packet[7+length_of_bits:]
        parse_packet(sub_packets)


def parse_packet(packet):
    if packet.count("0") == len(packet):
        return
    
    packet_version, type_id = parse_header(packet, True)

    global version_counter
    version_counter += packet_version
    
    if type_id == 4:
        parse_literal(packet, True)
    else:
        parse_operator(packet)
    
    
data = open("../../input/day_16_data.txt").read()

data_bin = hex_to_bin(data)
data_bin = leading_zeros(data_bin)
version_counter = 0

parse_packet(data_bin)
print(version_counter)

import math


def hex_to_bin(s):
    return format(int(s.strip(), 16), f"0{len(s.strip()) * 4}b")


def parse_header(s):
    return int(s[:3], 2), int(s[3:6], 2)


def parse_literal(packet):
    bit_index = 6
    parsed_literal = ""
    
    while True:
        parsed_literal += packet[bit_index + 1 : bit_index + 5]
        
        if packet[bit_index] == "0":
            break
        
        bit_index += 5
    
    return int(parsed_literal, 2), bit_index + 5


def parse_operator(packet):
    if packet[6] == "0":
        L = int(packet[7 : 22], 2)
        bit_index = 22
        numbers = []
        
        while bit_index < L + 22:
            result, length = parse_packet(packet[bit_index : ])
            bit_index += length
            numbers.append(result)
    
    else:
        num_sub_packets = int(packet[7 : 18], 2)
        bit_index = 18
        numbers = []
        
        for _ in range(num_sub_packets):
            result, length = parse_packet(packet[bit_index : ])
            bit_index += length
            numbers.append(result)
            
    return numbers, bit_index


def parse_packet(packet):  
    packet_version, type_id = parse_header(packet)

    if type_id == 4:
        return parse_literal(packet)
    
    else:
        numbers, bit_index = parse_operator(packet)

            
    if type_id in OPERATORS:
        result = OPERATORS[type_id](numbers)

    return result, bit_index


OPERATORS = {
        0: sum,
        1: math.prod,
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])        
    }

data = open("../../input/day_16_data.txt").read()

data_bin = hex_to_bin(data)

print("evaluated expression:", parse_packet(data_bin)[0])
