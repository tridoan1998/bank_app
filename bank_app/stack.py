from collections import deque

class Stack:
    global MAX_SIZE_STACK
    MAX_SIZE_STACK = 20


    def __init__(self, stack_size):
        self.stack_list = []
        self.stack_size = stack_size

    def push(self, data):
        assert self.stack_size < MAX_SIZE_STACK
        self.stack_list.append(data)
        self.stack_size += 1 
        return None

    
    def pop(self):
        assert self.stack_size >= 1
        number = self.stack_list.pop(0)
        self.stack_size -= 1 
        return number

    
    def list_stack_data(self):
        print(self.stack_list)
        return None


def main():
    stack0 = Stack(10)
    stack0.push(1)
    stack0.push(2)
    stack0.push(3)
    stack0.push(4)
    stack0.list_stack_data()
    stack0.pop()
    stack0.list_stack_data()

    """
    
    top
    1
    2
    3
    4
    bottom
    """
if __name__ == "__main__":
    main()