

def minimum(*args):
    """
    Функция возвращает минимальный из введенных аргументов, если функция
     вызывается без аргументов, то она возвращает None
    """
    if not args:
        return None
    min_value = args[0]
    for nums in args:
        if nums < min_value:
            min_value=nums
    return min_value


#print(minimum(5, 4, 7, 8, 5, 43, 22, 4, 56 ,6, 3 , 7 , 5))
print(minimum())



