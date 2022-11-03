import os
import sys

# 1. Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director. 
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
def sorted_extensions(dir):
    try:
        extensions = list(set(os.path.splitext(file)[1] for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))) - {''})
        return sorted(extensions)
    except Exception as e:
        return str(e)
# print(sorted_extensions("."))

# 2. Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul directorului de la calea director, ce incepe cu litera A. 
def files_with_a(dir, file):
    f = open(file, "wt")
    try:
        files = [file_name for file_name in os.listdir(dir) if os.path.isfile(os.path.join(dir, file_name)) and (file_name[0] == 'A' or file_name[0] == 'a')]
    except Exception as e:
        return str(e)
    for file_name in files:
        f.write(os.path.abspath(file_name) + "\n")
    f.close()
    return "Ok"
# print(files_with_a(".", "files_with_a.txt"))

# 3. Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. 
def recursive_dir(my_path):
    if not os.path.exists(my_path):
        return "Path does not exist."
    if os.path.isfile(my_path):
        return open(my_path, "r").read()[-20:]
    extensions = dict()
    for (root, directories, files) in os.walk(my_path):
        for file_name in files:
            ext = os.path.splitext(file_name)[1]
            extensions[ext] = extensions.get(ext, 0) + 1
    return sorted(list((ext, extensions[ext]) for ext in extensions.keys()), key = lambda el : el[1], reverse = True)
# print(recursive_dir("files_with_a.txt"))
# print(recursive_dir("."))

# 4. Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală. 
def sorted_extensions_arg():
    dir = sys.argv[1]
    return sorted_extensions(dir)
# print(sorted_extensions_arg())

# 5. Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
def search(target, to_search):
    #try:
    if not os.path.isfile(target) and not os.path.isdir(target):
        raise ValueError("The path given is neither file nor directory.")
    #except ValueError as e:
    #   return e
    if os.path.isfile(target):
        if to_search in open(target, "r").read():
            return [target]
        return []
    file_list = []
    for (root, directories, files) in os.walk(target):
        for file_name in files:
            full_file_name = os.path.join(root, file_name)
            if to_search in open(full_file_name, "r").read():
                file_list.append(file_name)
    return file_list
# print(search(".", "lala"))

# 6. Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.
def callback(exception):
    return exception

def search_and_callback(target, to_search, callback):
    #try:
    if not os.path.isfile(target) and not os.path.isdir(target):
        return callback(ValueError("The path given is neither file nor directory."))
    #except ValueError as e:
    #   return e
    if os.path.isfile(target):
        if to_search in open(target, "r").read():
            return [target]
        return []
    file_list = []
    for (root, directories, files) in os.walk(target):
        for file_name in files:
            full_file_name = os.path.join(root, file_name)
            if to_search in open(full_file_name, "r").read():
                file_list.append(file_name)
    return file_list

# print(search_and_callback(".", "lala", callback))

# 7. Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.
def file_info(file):
    try:
        return {"full_path":os.path.abspath(file), "file_size":os.path.getsize(file), "file_extension":os.path.splitext(file)[-1], "can_read":open(file, "r").readable(), "can_write":open(file, "a").writable()}
    except Exception as e:
        return str(e)
# print(file_info("test.txt"))

# 8. Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
# Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
# Calea "C:\\director" are pe disc următoarea structură:
# C:\\director\\fisier1.txt <- fișier
# C:\\director\\fisier2.txt <- fișier
# C:\\director\\director1 <- director
# C:\\director\\director2 <- director
def abs_path(dir_path):
    try:
        return [os.path.abspath(file) for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))]
    except Exception as e:
        return str(e)
# print(*abs_path("."), sep = "\n")
