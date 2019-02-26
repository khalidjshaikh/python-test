'''
:type magic_number: int 
:type numbers: list[int]
:type rtype: bool
'''

def add(sum, numbers):
    print(numbers, sum)
    if(numbers == []):
        return(sum)
    return(add(sum + numbers[0], numbers[1:]))

def arithmetic_boggle(magic_number, numbers):
    sum = add(0, numbers)
    print(sum, magic_number)
    return(sum == magic_number)

# print(arithmetic_boggle(0, []));
# print(arithmetic_boggle(43, []));
# print(arithmetic_boggle(42, [42]));
# print(arithmetic_boggle(0, [99]));
# print(arithmetic_boggle(6, [1,2,3]));
