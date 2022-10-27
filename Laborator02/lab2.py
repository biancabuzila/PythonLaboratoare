# 1. Write a function to return a list of the first n numbers in the Fibonacci string.
def first_n_fibonacci(n):
    if n == 0:
        return []
    f1 = 0
    f2 = 1
    list_first_n = [f1]
    for i in range(1, n):
        list_first_n.append(f2)
        next = f1 + f2
        f1 = f2
        f2 = next
    return list_first_n
print(first_n_fibonacci(8))

# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def primes(list):
    return [x for x in list if x != 0 and x !=  1 and len([y for y in range(2, x//2+1) if x % y == 0]) == 0]
print(primes([0, 1, 3, 11, 12, 24, 29]))

# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def lists_operations(a, b):
    #return (list(set(a).intersection(b)), list(set(a).union(b)), list(set(a).difference(b)), list(set(b).difference(a)))
    sa = set(a)
    sb = set(b)
    return (list(sa & sb), list(sa | sb), list(sa - sb), list(sb - sa))
print(lists_operations([1, 2, 3], [2, 3, 4]))

# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]
def compose(musical_notes, moves, start):
    n = len(musical_notes)
    moves = [x % n for x in moves]
    song = [musical_notes[start]]
    for x in moves:
        start = (start + x) % n
        song.append(musical_notes[start])
    return song
print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    
# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def under_main_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(i > j):
                matrix[i][j] = 0
    return matrix
print(under_main_diagonal([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]))

# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. 
# Example: For the [1,2,3], [2,3,4], [4,5,6], [4,1,"test"] and x = 2 lists [1,2,3] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.
def appear_x_times(x, *lists):
    unique_items = set()
    all_items = []
    for l in lists:
        unique_items |= set(l)
        all_items += l
    return [item for item in unique_items if all_items.count(item) == x]
print(appear_x_times(2, [1,2,3], [2,3,4], [4,5,6], [4,1,"test"]))

# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def palindrome_tuple(list):
    palindromes = [x for x in list if str(x) == str(x)[::-1]]
    return(len(palindromes), max(palindromes))
print(palindrome_tuple([12, 131, 1221, 747, 56, 33]))

# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
#Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e", "o"], ["a"]). Note: The function must return list of lists.
def ascii_code_divisible_by_x(list, x = 1, flag = True):
    result = []
    for word in list:
        if flag == True:
            result.append([chr for chr in word if ord(chr) % x == 0])
        else:
            result.append([chr for chr in word if ord(chr) % x != 0])
    return result
print(ascii_code_divisible_by_x(["test", "hello", "lab002"], 2, False))

# 9. Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.
#Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 7, 2],
# [5, 5, 2, 5, 6, 4],
# [6, 6, 7, 6, 7, 5]] 
#Will return : [(2, 2), (3, 4), (2, 4)] 
def spectators(matrix):
    n = len(matrix)
    m = len(matrix[0])
    short_spectators = []
    for j in range(m):
        column = [matrix[i][j] for i in range(n)]
        if column != sorted(column):
            max = column[0]
            for i in range(1, n):
                if max >= column[i]:
                    short_spectators.append((i, j))
                else:
                    max = column[i]
    return short_spectators
matrix = [[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]] 
print(spectators(matrix))

# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a "), (2, 6, "b"), (3, 7, "c")]. 
#Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.
'''
puteai sa vezi cum ai putea folosi zip() dupa ce padai listele cu ''
'''

def tuples(*lists):
    length = max([len(x) for x in lists])
    tuples_list = []
    for list in lists:
        list += [""] * (length - len(list))
    for index in range(length):
        tuples_list.append(tuple([list[index] for list in lists]))
    return tuples_list
print(tuples([1, 2], [5, 6, 7], ["a", "b", "c", "d"]))

# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def order_tuples(list):
    return sorted(list, key = lambda x : x[1][2])
print(order_tuples([('abc', 'bcd'), ('abc', 'zza')]))

# 12. Write a function that will receive a list of words as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
#Example:
#group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']] 
def group_by_rhyme(words):
    last_2_letters = list(dict.fromkeys(x[-2:len(x)] for x in words))
    return [list(filter(lambda word : word[-2:len(word)] == x, words)) for x in last_2_letters]
print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
