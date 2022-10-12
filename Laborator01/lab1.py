import re

#1. Find The greatest common divisor of multiple numbers read from the console.
def gcd(a, b):
    if a != 0:
        return gcd(b%a, a)
    else:
        return b

numbers = list(map(int, input("Enter numbers: ").split()))
if len(numbers) == 0:
    print("No numbers introduced")
else: 
    result = numbers[0]
    for number in numbers:
        result = gcd(result, number)
    print(result)


#2. Write a script that calculates how many vowels are in a string.
def numberOfVowels(string):
    count = 0
    for char in string:
        if char in "aeiouAEIOU":
            count = count + 1
    return count
print(numberOfVowels("computer science"))

#3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def occurences(str1, str2):
    results = 0
    for i in range(len(str2)):
        if str2[i:i + len(str1)] == str1:
            results += 1
    return results
    '''
    pattern = '(?=' + str1 + ')'
    return len(re.findall(pattern, str2))
    '''
print(occurences("aa", "aaaa"))

#4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def convertString(string):
    newStr = ""
    for i in range(0, len(string)):
        if string[i] >= 'A' and string[i] <= 'Z' and i > 0:
            newStr = newStr + '_' + string[i].lower()
        else:
            newStr = newStr + string[i].lower()
    return newStr
print(convertString("MyNumberOneFunc"))

'''
5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
firs      1  2  3  4    =>   first_python_lab
n_lt      12 13 14 5
oba_      11 16 15 6
htyp      10 9  8  7
'''
def printInSpiral(matrix):
    n = len(matrix)
    rowStart = 0
    rowEnd = n - 1
    colStart = 0
    colEnd = n - 1
    while(rowStart < (n - 1)//2 + 1):
        for i in range(colStart, colEnd + 1):
            print(matrix[rowStart][i], end = " ")
        for i in range(rowStart + 1, rowEnd + 1):
            print(matrix[i][colEnd], end = " ")
        for i in range(colEnd - 1, colStart - 1, -1):
            print(matrix[rowEnd][i], end = " ")
        for i in range(rowEnd - 1, rowStart, -1):
            print(matrix[i][colStart], end = " ")
        rowStart += 1
        rowEnd -= 1
        colStart += 1
        colEnd -= 1
    print()
matrix1 = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
matrix2 = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
printInSpiral(matrix1)
printInSpiral(matrix2)

#6. Write a function that validates if a number is a palindrome.
def isPalindrome(x):
    '''
    reverse = 0
    copy = x
    while copy != 0:
        reverse = reverse * 10 + copy % 10
        copy //= 10
    if reverse == x:
        return True
    else:
        return False
    '''
    x = str(x)
    return x == x[::-1]
print(isPalindrome(12321), isPalindrome(35))

#7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
def extractNumber(text):
    '''
    firstIndex = len(text) - 1
    for i in "0123456789":
        if text.find(i) != -1:
            index = text.index(i)
            if(index < firstIndex):
                firstIndex = index
    number = ""
    while text[firstIndex] in "0123456789":
        number = number + text[firstIndex]
        firstIndex += 1
    return number
    '''
    return re.search('\d+',text).group()
print(extractNumber("An apple is 123 USD"))
print(extractNumber("abc123abc78"))

#8. Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def countBits1(x):
    return (bin(x).replace("0b","")).count("1")
print(countBits1(77))

#9. Write a function that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
def mostCommonLetter(string):
    letter = ""
    count = 0
    for char in range(ord('a'), ord('z') + 1):
        countChar = string.count(chr(char)) + string.count(chr(char - 32))
        if countChar > count:
            count = countChar
            letter = chr(char)
    return letter, count
print(mostCommonLetter("An apple is not a tomato"))

#10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.
def numberOfWords(text):
    return len(text.split(" "))
print(numberOfWords("I have Python exam."))