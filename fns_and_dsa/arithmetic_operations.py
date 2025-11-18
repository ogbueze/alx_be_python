def perform_operation(first_num, second_num, operation):
    match operation:
        case '+':
            result = first_num + second_num
        case '-':
            result = first_num - second_num
        case '/':
            if first_num == 0:
                return 'cannot divide by zero'
        case '*':
            result = first_num * second_num
        case _:
            result = 'invalid operation'
    return result

