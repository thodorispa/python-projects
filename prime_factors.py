def is_prime(number):
    flag = 0
    for x in range(1,100):
        if number%x == 0:
            flag += 1
    return True if flag == 2 else False

def get_prime_factors(x):
    factor = 2
    factors_list = []
    for i in range(int(x)):
        if (x % factor) == 0 and is_prime(factor):
            factors_list.append(factor)
            x = x / factor
            if x <= factor:
             factors_list.append(int(x))
        factor += 1
    return factors_list

print(get_prime_factors(12))
