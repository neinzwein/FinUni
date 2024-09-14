# 19,11

# 19 Частота букв в тексте
import nltk
from nltk.tokenize import RegexpTokenizer,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.probability import FreqDist

# nltk.download('punkt_tab')
# nltk.download('stopwords')
import re

# У меня предъява к 19 пункту. Смысл поиска частоты букв в тексте, если нужно стеммизировать их и убирать стоп-слова?
with open(file="Lev_Tolstoj.txt", mode = "r", encoding="cp1251") as f:
    text = f.read()   
#сплитим единицы, знаки препинания
text = re.findall(r'[а-яА-ЯёЁa-zA-Z]+',text)
# print(text)

#Разбиваем текст файла на токены (Каждое слово, каждый знак)
# tokenizer = RegexpTokenizer(r'[а-яА-ЯёЁa-zA-Z]')
# tokens = tokenizer.tokenize(text) # toktok требовал бы utf-8
tokens = word_tokenize(' '.join(text))
tokens = [w.lower() for w in tokens] # isalpha() лучше не использовать, забирает символы
# print(tokens)

#теперь добавляем по модели стопслова
stop_words = set(stopwords.words('russian'))
tokens = [w for w in tokens if w not in stop_words]
# print(tokens)

#для русских лучше использовать snowballstemmer или porterstemmer
stemmer = (SnowballStemmer('russian'))
tokens_stem = [stemmer.stem(w) for w in tokens]
# print(tokens_stem)

result_text = ''.join(tokens_stem)
frequen = FreqDist(result_text)

for l,f in sorted(frequen.items()):
    print(f"Буква : {l}, Частота :{f}")


#11 Найти самое длинное слово, в котором все буквы разные

print(max(tokens, key=len))