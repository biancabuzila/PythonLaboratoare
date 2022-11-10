# 1) a) Write a module named utils.py that contains one function called process_item. The function will have one parameter, x, and will return the least prime number greater than x. When run, the module will request an input from the user, convert it to a number and it will display the output of the process_item function.
def process_item(x):
    if x >= -2 and x <= 1:
        return 2
    if x % 2 == 0:
        x += 1
    else:
        x += 2
    while x == 0 or x == 1 or len([y for y in range(2, x//2 + 1) if x % y == 0]) > 0:
        x += 2
    return x

if __name__ == "__main__":
    number = input("Enter a number: ")
    try:
        number = int(number)
        print(process_item(number))
    except ValueError:
        print(f"{number} is not a number!")