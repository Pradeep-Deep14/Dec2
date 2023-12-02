def calculate_sum(numbers):
    return sum(numbers)

def wrapper(func):
    def inner(*args):
        if any(not isinstance(arg,int) for arg in args):
            print("Invalid Input")
        else:
            return func(*args)
    return inner

calculate_sum=wrapper(calculate_sum)
result=calculate_sum([1,2,3,'4'])
print(result)