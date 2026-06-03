def convert_base_x(conv_string, base):
    converted_int = 0
    if len(conv_string) == 1:
        return int(conv_string)
    converted_int + = convert_base_x(str(int(conv_string) % base))


print(convert_base_x("1284231",10))