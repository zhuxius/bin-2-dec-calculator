def bin_to_dec(bin_string: str) -> int:
    if not _is_input_valid(bin_string):
        raise ValueError("Input contains a value apart from '0' or '1'")
    decimal_value = 0
    for index in range(len(bin_string)):
        decimal_value += 2**index * int(bin_string[-1-index])
    return decimal_value


def _is_input_valid(bin_str: str) -> bool:
    is_input_valid = True
    for digit in bin_str:
        if digit != "0" and digit != "1":
            is_input_valid = False
            break
    return is_input_valid


binary = input("Please input 8 digit binary string: ")
dec = bin_to_dec(binary)
print("Decimal value is", dec)
