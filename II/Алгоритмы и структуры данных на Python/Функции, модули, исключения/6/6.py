# Напишите функцию, которая принимает имя файла.
# Если файла нет, то возвращает текст "404. File (filename) not found", иначе возвращает содержимое файла.

def Function(fname):
    try:
        with open(fname,"r+",encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ("404. FIle "+fname+" not found")

# Запускайте из папки в терминале
print(Function("example.txt"))