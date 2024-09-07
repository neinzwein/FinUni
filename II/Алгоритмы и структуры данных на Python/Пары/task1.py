#Задача (20 баллов)
#Написать программу, которая по известной денежной сумме вычисляет количество купюр по 500,
# 100 руб. и монет в 10 руб. и 1 руб., при помощи которых можно выдать данную сумму.
# При этом общее количество купюр и монет должно быть минимально возможным.
#Пример: для выдачи суммы 3875 рублей, потребуется 7 купюр по 500 рублей,
#3 купюры по 100 руб., 7 монет по 10 рублей и 5 монет по 1 рублю.

def task1(money:int):

    total=money
    res='для выдачи суммы '+str(total)+' рублей'
    coin10,coin1=0,0
    banknote500,banknote100=0,0

    while money>=500:
        banknote500+=1
        money-=500

    if banknote500>0:
        res+=', потребуется '+str(banknote500)+' купюр по 500 рублей'

    while money>=100:
        banknote100+=1
        money-=100

    if banknote100>0:
        res+=', потребуется '+str(banknote100)+' купюр по 100 рублей'

    while money>=10:
        coin10+=1
        money-=10

    if coin10>0:
        res+=', потребуется '+str(coin10)+' монет по 10 рублей'

    while money>=1:
        coin1+=1
        money-=1

    if coin1>0:
        res+=', потребуется '+str(coin1)+' монет по 1 рублю.'

    return res

money=3875
print(task1(money))
# money=4000
# print(task1(money))
# money=5943
# print(task1(money))