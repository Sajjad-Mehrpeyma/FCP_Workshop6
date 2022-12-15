str_length = int(input())
operation_count = int(input())

string = input()

def shift_char(char):
    ascii_number = ord(char)
    ascii_number += 1
    if ascii_number == 123:
        ascii_number = 97
    
    return chr(ascii_number)

for i in range(operation_count):
    string = string[-1] + string
    string = string.replace(string[-1], '')
    