# Author: AKHILESH SANTOSHWAR

# Decimal to binary using Stack

class Stack ():

   def __init__(self):
        self.items=[]

    def push (self,item):
        self.items.append(item)

    def pop (self):
        return self.items.pop()

    def size(self):
        return len(self.items)

s1= Stack()




decNum= int(input("Enter the decimal num : "))

newNum=decNum

while newNum==1:

    newNum= decNum%2
    decNum = decNum//2
    s1.push(newNum)
    while s1.size() is not Null:
        a=s1.pop()
        print(a)
