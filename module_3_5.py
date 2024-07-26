def get_multiplied_digits(number):      # создали функцию принимающию 1 позиционный параметр
    str_number = (str(number))          # сщздали строку из переданного параметра
    # print(str_number[0:])
    # print(str_number[1:])         # что бы посмотреть
    # print(int(str_number[0:]))
    first = int(str_number[0])         # создали переменную которая берет первую цифру из str_number
    if len((str_number)) > 1:          # Если длина строки  больше одного символа то:...
        return first * get_multiplied_digits(int(str_number[1:]))   # умножаем first на нашу же функцию,
                                                        # но уже с длиной строки меньше на один (первый символ - цифру)
                                                        #  со второго знака и до окончания строки
    else:
        return first                   # Если длина строки  стала меньше  одного символа то возвращаем first
                                                                              # и на этом выходим из функции (рекурсии)


result = get_multiplied_digits(40203)
print(result)