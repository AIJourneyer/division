def divide_numbers(request):
    request_args = request.args
    num1 = float(request_args.get('num1', 1))
    num2 = float(request_args.get('num2', 1))

    if num2 == 0:
        return {"error": "Division by zero is not allowed."}

    return {
        'num1': num1,
        'num2': num2,
        'result': num1 / num2
    }

#test