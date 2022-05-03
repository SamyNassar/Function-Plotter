def is_number(num):
    try:
        int(num)
        return True
    except:
        return False


def is_min_less_max(min, max):
    if min < max:
        return True
    else:
        return False

def is_equation(equation):
    try:
        eval(equation)
        return True
    except:
        return False