# Пользователь вводит текст. 
# Задача: написать функцию, которая будет считать количество символов и 
# возвращать их в виде словаря,
# ключами в котором будут символы, а значениями - количество.

from collections import defaultdict

string = input().strip()

def task2(string):
  symbols = defaultdict()
  print(symbols)

  for symbol in string:
    if symbol not in symbols.keys():
      symbols[symbol] = 1
    else:
      symbols[symbol] += 1

  return dict(symbols)

print(task2(string))
