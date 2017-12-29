def is_armstrong(number):
    value = 0
    number_str = str(number)
    for i in number_str:
        value += pow(int(i),len(number_str))

    return(value == number)
