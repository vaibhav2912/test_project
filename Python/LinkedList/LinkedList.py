class Node:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.next = None
    
    def setnext(self,newnext):
        self.next = newnext
        
    def getnext(self):
        return self.next
    
    def setname(self,name):
        self.name = name
        
    def getname(self):
        return self.name
    
    def setage(self,age):
        self.age = age
        
    def getage(self):
        return self.age
    

class unordered_list():
    def __init__(self):
        self.head = None
        
    def add(self,name,age):
        newnode = Node(name,age)
        newnode.setnext(self.head)
        self.head = newnode
        
        
    def printlist(self):
        print("***Printing list:***")
        current = self.head
        while(current != None):
            print(" --> (Name: {}, age: {}) ".format(current.getname(),current.getage()), end = '')
            current = current.getnext()
            
        print("\n")    
    def search(self,name):
        print("Searching for entry: {}".format(name))
        current = self.head
        while(current != None):
            if (current.getname() == name):
                print("\nFound:\nName: {} | age: {}\n".format(name,current.getage()))
                return
            else:
                current = current.getnext()
        print("\nEntry for \"{}\" not found in the list\n".format(name))
            
            
    def remove(self,name):
        current = self.head
        while(current != None):
            if(current.getname() == name):
                if(current == self.head):
                    self.head = current.getnext()
                    print("\nRemoved {} from list\n".format(name))
                    return
                elif(next == None):
                    temp.setnext(None)
                    print("\nRemoved {} from list\n".format(name))
                    return
                else:
                    temp.setnext(next)
                    print("\nRemoved \"{}\" from list\n".format(name))
                    return
            else:
                temp = current
                current = current.getnext()
                next = current.getnext()
        print("\nEntry for {} not found\n".format(name))
        
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
        
        
    def insertAfter(self,elem,name,age):
        if(not(self.isEmpty())):
            current = self.head
            while(current != None):
                if(current.getname() == elem):
                    next = current.getnext()
                    temp = Node(name,age)
                    current.setnext(temp)
                    temp.setnext(next)
                    return
                else:
                    current = current.getnext()
            print("Element {} not found in the list".format(elem))
        else:
            print("List is empty")
            
            
def main():            
    mylist = unordered_list()

    mylist.add("Vaibhav", 27)
    mylist.add("Anish", 26)
    mylist.add("Kaushik", 31)
    
    mylist.search("Vaibhav")

    mylist.printlist()
    mylist.remove("Vaibhav")
    mylist.printlist()
    
    mylist.insertAfter("Kaushik", "Kartik", 27)
    mylist.printlist()

       
if __name__ == '__main__': main()
    
        