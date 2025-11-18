def perform_operation(num1, num2, operation):
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '/':
            if num1 == 0:
                return 'cannot divide by zero'
        case '*':
            result = num1 * num2
        case _:
            result = 'invalid operation'
    return result

