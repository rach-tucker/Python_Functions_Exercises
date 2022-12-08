def positive_to_negative(list_of_nums):
    negative_nums = []
    for num in list_of_nums:
        num = num - num * 2
        negative_nums.append(num)
    return negative_nums

positive_to_negative([1, 3, 5, 7, 8])


address = "123 Real Street, Apt. 2, Springfield, OR 43498"
whatever = "jfkds 12 nj 234"

def pull_numbers(string):
    d = [d for d in address if d.isdigit()]  
    
    return d
print(pull_numbers(address))



digits = '123'

def add_number(num):
    num = int(num) + 1
    num = str(num)
    return num
add_number(digits)

print(add_number(digits))