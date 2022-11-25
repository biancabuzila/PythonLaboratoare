import os
import re

# 1. Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.
def extract_words(text):
    return re.findall("[a-zA-Z0-9]+", text)
# print(extract_words("This text has letters and the numbers: 12, 14."))

# 2. Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those long-length x substrings that match the regular expression.
def match_expr(regex, text, x):
    match_list = re.findall(regex, text)
    return [substr for substr in match_list if len(substr) == x]
# print(match_expr("\d+", "Text 153 word 61 number, 321, 345, 6.", 3))

# 3. Write a function that receives two parameters: a list of strings and a list of regular expressions. The function will return a list of the strings that match on at least one regular expression from the list given as parameter.
def match_at_least_one(strings, regex_list):
    result = []
    for string in strings:
        if any([re.match(regex, string) for regex in regex_list]):
            result.append(string)
    return result
# print(match_at_least_one(["this", "26", "word 34"], ["[a-zA-Z]+$", "\d+", "[a-z]+[_]"]))

# 4. Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values. For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags whose attributes are class="url" si name="url-form" si data-id="item".
def xml_elements_all_attrs(xml_doc, attrs):
    try:
        f = open(xml_doc, "r")
        content = f.read()
        f.close()
    except Exception as e:
        return str(e)
    elements = []
    for el in re.findall("<\w+.*?>", content):
        if all([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", el) for item in attrs.items()]):
            elements.append(el)
    return elements
# print(xml_elements_all_attrs("doc.xml", {"class": "url", "name": "url-form", "data-id": "item"}))

# 5. Write another variant of the function from the previous exercise that returns those elements that have at least one attribute that corresponds to a key-value pair in the dictionary.
def xml_elements_at_least_one_attr(xml_doc, attrs):
    try:
        f = open(xml_doc, "r")
        content = f.read()
        f.close()
    except Exception as e:
        return str(e)
    elements = []
    for el in re.findall("<\w+.*?>", content):
        if any([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", el) for item in attrs.items()]):
            elements.append(el)
    return elements
# print(xml_elements_at_least_one_attr("doc.xml", {"class": "url", "name": "url-form", "data-id": "item"}))

# 6. Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship means replacing characters from odd positions with *.
def replace(text):
    word = text.group(0)
    if word[0] in "aeiouAEIOU" and word[-1] in "aeiouAEIOU":
        return "".join([ch if index % 2 == 0 else "*" for index, ch in enumerate(word)])
    return word

def censure(text):
    return re.sub("\w+", replace, text)
# print(censure("alone bored house use awesome username"))

# 7. Verify using a regular expression whether a string is a valid CNP.
def valid_cnp(cnp):
    regex = '^[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2])(00[1-9]|0[1-9]\d|[1-9]\d{2})\d$'
    if re.match(regex, cnp) is not None:
        return "Valid"
    return "Not valid"
# print(valid_cnp("3860325079824"))

# 8. Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>".
def files_match_reg(dir, reg):
    if not os.path.isdir(dir):
        return f"{dir} is not a directory or it doesn't exist."
    result = []
    for (root, directories, files) in os.walk(dir):
        for file in files:
            full_name = os.path.join(root, file)
            match = 0
            if re.match(reg, file):
                match += 1
            try:
                if re.match(reg, open(full_name, "r").read()):
                    match += 1
            except:
                return f"Error on open/read of file {full_name}"
            if match == 1:
                result.append(full_name)
            elif match == 2:
                result.append(">>" + full_name)
    return result
# print(files_match_reg("tests", ".*file.*"))
