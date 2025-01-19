def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        try:
            answer = numerator/denominator
            return answer
        except ZeroDivisionError:
            print("Cannot divide by zero.")
    except ValueError:
            print("Cannot divide non-numeric values")