def calculation_function(num_a, num_b, operation):
    result = None

    if operation == 'multiply':
        result = num_a * num_b
    elif operation == 'divide':
        result = int(num_a / num_b)
    elif operation == 'add':
        result = num_a + num_b
    elif operation == 'subtract':
        result = num_a - num_b
    return result


operation_func = input()
a = int(input())
b = int(input())
print(calculation_function(a, b, operation_func))