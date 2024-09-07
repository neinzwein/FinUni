# Реализовать структуру "Стек". 
# Написать функцию, которая читает и выводит на печать три нижних элемента стека,
# а также меняет местами верхний и нижний элементы.

class Stack: #LIFO

    def __init__(self) -> None:
        self.stack = []

    def __str__(self) -> str:
        return f"{self.stack}"

    def pop(self):
        if len(self.stack) <1:
            return None
        return self.stack.pop()
    
    def push(self,item):
        self.stack.append(item)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)
    
def FLchange(stack:Stack):

    tmp_stack = Stack()
    tmp = 0

    while stack.size()!=1:
        tmp_stack.push(stack.pop())
    
    tmp = stack.pop() # теперь pop - пустой

    while tmp_stack.size()!=0:
        stack.push(tmp_stack.pop())

    stack.push(tmp)

def print3(stack:Stack,leftprint:int=3)->None:

    tmp_stack = Stack()
    tmp = 0

    while stack.size()!=leftprint:
        tmp_stack.push(stack.pop())

    print(stack)

    while tmp_stack.size()!=0:
        stack.push(tmp_stack.pop())

if __name__ == "__main__":

    stack = Stack()

    for i in range(10):
        stack.push(i)

    for i in range(3):
        FLchange(stack)
        print3(stack)
        # print(stack)




# Либо LifoQueue  (но проще адекватными способами)

# from collections import deque

# def read3top_changelast(stack:deque)->deque:
#     i = 0
#     while i!=3:
#         down = stack.popleft()
#         # print(stack)
#         print(down)
#         stack.append(down)
#         i+=1

#     return stack

# stack = deque([1,2,3,4,5,6,7,8,9,0])

# read3top_changelast(stack)