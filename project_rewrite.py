
def min(x, y):
    if x > y:
        return y
    else:
        return x


def max(values_list):
    my_max = values_list[0]
    for n in values_list:
        if n > my_max:
            my_max = n
    return my_max


def len(values_list):
    my_len = 0
    for i in values_list:
        my_len += 1
    return my_len


def multiply(x, y):
    result = 0
    for i in range(y):
        result = result + x
    return result


def pow(x, y):
    pow_res = 1
    for p in range(y):
        pow_res = pow_res * x
    return pow_res


def modulo(x, y):
    division_result_str = str(x/y)
    return int(division_result_str.split(".")[1])

