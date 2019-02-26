'''
:type magic_number: int 
:type numbers: list[int]
:type rtype: bool
'''

sums = []

def any(sum, numbers):
    # print(numbers, sum)
    if(numbers == []):
        # print(sum)
        sums.append(sum)
        return
    any(sum + numbers[0], numbers[1:])
    any(sum - numbers[0], numbers[1:])

def arithmetic_boggle(magic_number, numbers):
    global sums
    sums = []
    # print(sums)
    any(0, numbers)
    # print(sums)
    try:
        sums.index(magic_number)
        return(True)
    except ValueError:
        return(False)
    # print(sum, magic_number)

# print(arithmetic_boggle(0, []))
# print(arithmetic_boggle(43, []))
# print(arithmetic_boggle(42, [42]))
# print(arithmetic_boggle(0, [99]))
# print(arithmetic_boggle(1, [6,3]))
# print(arithmetic_boggle(19, [1,3,6,9,5,5]))
