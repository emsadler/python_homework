#2.1
WhateverNameYouWant = []
for i in range(1,21):
    WhateverNameYouWant.append(i)
print(WhateverNameYouWant)

#2.2
WhateverNameYouWant = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
AnotherNameYouWant = []
def squared_int(list):
    for i in WhateverNameYouWant: 
        AnotherNameYouWant.append(i**2)
    '''NewINT = [int]**2 TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'. 
    So I changed it to remove the second variable and instead just appended the function straight into the new list.
    '''
    return AnotherNameYouWant
print(squared_int(WhateverNameYouWant))

#2.3
def fifteen(list):
    first_fifteen_elements = AnotherNameYouWant[0:15]
    return first_fifteen_elements
print(fifteen(AnotherNameYouWant))

#2.4
def fifth(list):
    every_fifth_element = AnotherNameYouWant[4::5]
    return every_fifth_element
print(fifth(AnotherNameYouWant))

#2.5
def fancy_function(list):
    for element in list:
        last_thirty = list[0:30]
        every_third_element = last_thirty[::-3]
        return every_third_element
print(fancy_function(AnotherNameYouWant))

#3.1
def five_by_five(x):
    outer = []
    for row in x:
        inner = []
        for num in range(1,6):
            inner.append(row*5+num)
        outer.append(inner)
    return outer

my_matrix = five_by_five(range(5))
print(five_by_five(range(5)))

#3.2
def multiple_of_3(matrix):
    for row in range(0,len(matrix)):
        for num in range(0,len(matrix[row])):
                if matrix[row][num] % 3 == 0:
                    matrix[row][num] = "?"
    return matrix

my_matrix_updated = multiple_of_3(my_matrix)
print(my_matrix_updated)

#3.3
def total_sum(matrix):
    total_sum = 0    
    for row in matrix:
        for num in row:
            if num != "?":
                total_sum += num
    return total_sum
print(total_sum(my_matrix_updated))