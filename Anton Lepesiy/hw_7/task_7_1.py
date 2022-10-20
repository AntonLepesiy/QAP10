# 1. Напишите функцию, которая принимает на вход одномерный массив
# и два числа - размеры выходной матрицы. На выход программа должна
# подавать матрицу нужного размера, сконструированную из элементов массива.
# reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
# [
#     [1, 2, 3],
#     [4, 5, 6]


def resape(array, depht, count):
    i = 0
    j = count
    new_array = []

    while i < len(array):
        if depht * count != len(array):
            print('incorrect incoming data')
            break

        new_array.append(array[i:j])
        i = i + count
        j = j + count
    return new_array


print(resape([1, 2, 3, 4, 5, 6], 2, 3))
print(resape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
print(resape([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3))
print(resape([1, 2, 3, 4, 5, 6, 7], 4, 2))
