# 2) Create a function and an anonymous function that receive a variable number of arguments. Both will return the sum of the values of the keyword arguments.
# Example:
# For the call my_function(1, 2, c=3, d=4) the returned value will be 7.

def sum_keyword_args(*list, **dict):
    return sum([dict[key] for key in dict.keys()])

sum_lambda = lambda *list, **dict : sum(dict.values())

# print(sum_keyword_args(1, 2, c = 3, d = 4), sum_lambda(1, 2, c = 3, d = 4), sep = " and ")


# 3) Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list with all the vowels in a given string.
# For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

def vowels_function(text):
    vowels = []
    for chr in text:
        if chr in "aeiouAEIOU":
            vowels += chr
    return vowels

def vowels_list(text):
    return [chr for chr in text if chr in "aeiouAEIOU"]

def vowels_filter(text):
    return list(filter(lambda chr : chr in "aeiouAEIOU", text))

# print(vowels_function("Programming in Python is fun"), vowels_list("Programming in Python is fun"), vowels_filter("Programming in Python is fun"), sep = " and ")


# 4) Write a function that receives a variable number of arguments and keyword arguments. The function returns a list containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with minimum 3 characters.
# Example:
# my_function(
#  {1: 2, 3: 4, 5: 6}, 
#  {'a': 5, 'b': 7, 'c': 'e'}, 
#  {2: 3}, 
#  [1, 2, 3],
#  {'abc': 4, 'def': 5},
#  3764,
#  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#  test={1: 1, 'test': True}
# ) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]

def dictionaries(*arg, **keyarg):
    final_list = []
    arg = list(arg)
    arg += list(keyarg.values())
    for el in arg:
        if type(el) == dict:
            string_keys = [key for key in el.keys() if type(key) == str and len(key) >= 3]
            if len(el) >= 2 and len(string_keys) >= 1:
                final_list.append(el)
    return final_list

# print(dictionaries({1: 2, 3: 4, 5: 6}, 
#     {'a': 5, 'b': 7, 'c': 'e'}, 
#     {2: 3}, 
#     [1, 2, 3],
#     {'abc': 4, 'def': 5},
#     3764,
#     dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#     test={1: 1, 'test': True}))


# 5) Write a function with one parameter which represents a list. The function will return a new list containing all the numbers found in the given list.
# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]

def only_numbers(list):
    return [x for x in list if type(x) in [int, float]]

# print(only_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


# 6) Write a function that receives a list with integers as parameter that contains an equal number of even and odd numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number.
# Example:
# my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]

def pairs(numbers):
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2]
    return list(zip(even, odd))
    
# print(pairs([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))


# 7) Write a function called process that receives a variable number of keyword arguments.
# The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
# If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument and returning True/False) and will retain from the generated numbers only those for which the predicates are True. 
# If the function receives a parameter called limit, it will return only that amount of numbers from the sequence. 
# If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list. 
# The function will return the processed numbers.
# Example:
# def sum_digits(x):
#     return sum(map(int, str(x)))
# process(
#     filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
#     limit=2,
#     offset=2
# ) returns [34, 144]
# Explanation:
# # Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
# # Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040
# # After offset: 34, 144, 610, 2584, 10946, 832040
# # After limit: 34, 144

def sum_digits(x):
    return sum(map(int, str(x)))

def process(**args):
    fibo = [0, 1]
    for i in range(2, 1000):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    if "filters" in args.keys():
        for filt in args["filters"]:
            fibo = list(filter(filt, fibo))
    if "offset" in args.keys():
        fibo = fibo[args["offset"]:]
    if "limit" in args.keys():
        fibo = fibo[:args["limit"]]
    return fibo

#print(process(filters = [lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit = 2, offset = 2))


# 8) 
# a) Write a function called print_arguments with one parameter named function. The function will return one new function which prints the arguments and the keyword arguments received and will return the output of the function received as a parameter.

def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def print_arguments(function):
    def fun(*args, **keyargs):
        print("Arguments are: " , end = "")
        print(args, ", ", keyargs, sep = "")
        return function(*args, **keyargs)
    return fun

# augmented_multiply_by_two = print_arguments(multiply_by_two)
# x = augmented_multiply_by_two(10)
# print(x)

# augmented_add_numbers = print_arguments(add_numbers)
# x = augmented_add_numbers(3, 4)
# print(x)


# b) Write a function called multiply_output with one parameter named function. The function will return one new function which returns the output of the function received multiplied by 2.

def multiply_by_three(x):
    return x * 3

def multiply_output(function):
    def fun(*args, **keyargs):
        return 2 * function(*args, *keyargs)
    return fun

# augmented_multiply_by_three = multiply_output(multiply_by_three)
# x = augmented_multiply_by_three(10)
# print(x)


# c) Write a function called augment_function with two parameters named function and decorators. decorators will be a list of functions which will have the same signature as the previous functions (print_arguments, multiply_output). augment_function will create a new function which is augmented using all the functions in the decorators list.

def augment_function(function, decorators):
    def fun(*args, **keyargs):
        decorated_function = decorators[0](function)
        for decorator in decorators[1:]:
            decorated_function = decorator(decorated_function)
        return decorated_function(*args, **keyargs)
    return fun

# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
# x = decorated_function(3, 4) 
# print(x)


# 9) Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs). The function should return a list of dictionaries for each pair (in the same order as in the input list) that contain the following keys (as strings): sum (the value should be sum of the 2 numbers), prod (the value should be product of the two numbers), pow (the value should be the first number raised to the power of the second number) 
# Example:
# f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] )  will return [{'sum': 7, 'prod': 10, 'pow': 25}, {'sum': 20, 'prod': 19, 'pow': 19}, {'sum': 36, 'prod': 180, 'pow': 729000000}, {'sum': 4, 'prod': 4, 'pow': 4}] 

def operations(pairs):
    result = []
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        result += [{"sum":a + b, "prod":a * b, "pow":pow(a, b)}]
    return result

# print(operations([(5, 2), (19, 1), (30, 6), (2, 2)]))