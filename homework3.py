from math import log10

#1
def x_power_y (x,y):
    z = 2*y
    value = x**z
    return((value**(1/2)))
print(x_power_y(2,3))

#2
temps = [15, 14, 17, 20, 23, 28, 20]
temps_tuple = (min(temps),max(temps))
print(temps_tuple)

#3
def day_of_the_week (day):
    if (day > 5):
        return True
    else:
        return False
print(day_of_the_week(6))

#4
def travel_fuel (x,y):
    distance = x #miles
    fuel = y #gallons
    return(distance/fuel)
print(travel_fuel(70,21.5))

#5
def moving_number (i):
    n = i//10
    m = i%10
    o = (int(log10(n) + 1))
    p = m*(10**o)
    return(p+n)
print(moving_number(12345))

#6.1
def min_number (list):
    list = [98, 2024, 131, 2, 3, 72]
    min_list = sorted(list)
    x = 0
    if x < min_list[0]:
        return min_list[0]
print(min_number(list))

def max_number (list):
    list = [2024, 98, 131, 2, 3, 72]
    max_list = sorted(list, reverse = True)
    x = 0
    if x < max_list[0]:
        return max_list[0]
print(max_number(list))

#6.2
def min_number (list):
    list = [98, 2024, 131, 2, 3, 72]
    min_list = sorted(list)
    while 0 < min_list[0]:
        return min_list[0]
        break
print(min_number(list))

def max_number (list):
    list = [2024, 98, 131, 2, 3, 72]
    max_list = sorted(list, reverse = True)
    while 0 < max_list[0]:
        return max_list[0]
        break
print(max_number(list))

#7
def vowel_and_consonants (string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    for letters in string:
        if letters in vowels:
            count += 1
    total_count = len(string) - len(string.split(" "))
    count2 = total_count - count  
    return (count, count2)
string = ("Hi, my name is Osky and I LOVE BERKELEY")
print(vowel_and_consonants(string))

#8
def sum_of_digits (number):
    sum = 0
    for digit in str(number):
        sum += int(digit) 
    return(sum)
number = [2468]
print(sum_of_digits(sum(number)))