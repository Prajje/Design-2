#Time Complexity :
#Space Complexity :
#Did this code successfully run on Leetcode :
#Any problem you faced while coding this : Nope

'''
Main idea:
stack1 -> [ c
           b
           a ]

stack2 -> [ a
           b
           c ]
'''
class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int:
        return self.stack1.pop()
                

    def peek(self) -> int:
        return self.stack1[-1]
        

    def empty(self) -> bool:
        return not self.stack1
