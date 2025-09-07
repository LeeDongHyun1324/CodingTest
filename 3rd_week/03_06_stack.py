class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head  head다음 head 다다음
# [5] -> [3] -> [4]

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)  # [3]이라는 노드를 만듦.
        new_head.next = self.head   # [3] -> [4]
        self.head = new_head    # [3] 이라는 노드를 head로 만들어줘

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print("stack is Empty")
        delete_head = self.head     # pop함수는 pop한 값을 반환을 해야하기 때문
        self.head = self.head.next  # [5]노드가 head일 때 다음 노드인 [3]을 head로 지명 
        return delete_head

    def peek(self): # head값 조회하는 함수
        if self.is_empty():
            return "stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):       
        return self.head is None
    
stack = Stack()
stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())