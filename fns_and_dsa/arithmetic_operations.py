def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'divide':
            if num1 == 0:
                return 'cannot divide by zero'
        case 'multiply':
            result = num1 * num2
        case _:
            result = 'invalid operation'
    return result

