class Node(object):

    def _init_(self, val):
        self.val = val
        self.next = None
        
    def get_data(self):
        return self.val
      
    def set_data(self, val):
        self.val = val
 
    def get_next(self):
        return self.next
 
    def set_next(self, next):
        self.next = next
    
 
class LinkedList(object):

        # constructor
    def __init__(self, head = None):
        self.head = head
        self.length = 0
        
    def get_length(self):
        return self.length
      
    def is_empty(self):
        return self.head == None    
        
    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.get_next() != None:
                n = n.get_next()
            n.set_next(new_node)
        self.length+=1
        
        # menambah value berdasarkan index
    def insert(self,value,index):
        if index == 0:
            self.add(value)
        else:
            count=1
            n=self.head
            while count<index and n!=None:
                n=n.get_next()
                count+=1
            
            # mengecek apakah index ada
            if n == None:
                print("index yang dimasukkan melebihi panjang LinkedList")
            else:
                new_node=Node(value)
                new_node.set_next(n.get_next())
                n.set_next(new_node)
        self.length+=1

        
        
        # menghapus node berdasarkan index
    def remove(self, index):
        if index == 0:
            self.head = self.head.get_next()
        else:
            count=1
            n=self.head
            while count<index and n!=None:
                n=n.get_next()
                count+=1
            if n.get_next() == None:
                print("index yang dimasukkan melebihi panjang LinkedList")
            else:
                n.set_next(n.get_next().get_next())
        self.length-=1
        
        # menukar value dari dua index
    def swap(self, index1, index2):
        if index1 >= self.length or index2 >= self.length:
            print("indeks yang dimasukkan melebihi panjang linked list")
        elif index1 == index2:
            print("tidak bisa menjalankan perintah, indeks yang dimasukkan sama")
        elif self.head.get_data() == self.getLL(index1):
            temp = self.getLL(index1)
            self.add_begin(self.getLL(index2))
            self.remove(index1+1)
            self.insert(temp, index2)
            self.remove(index2+1)
        elif self.head.get_data() == self.getLL(index2):
            temp = self.getLL(index2)
            self.add_begin(self.getLL(index1))
            self.remove(index2+1)
            self.insert(temp, index1)
            self.remove(index1+1)
        else:
            n=self.head
            while n != None:
                if n.get_data() == self.getLL(index1):
                    temp = self.getLL(index1)
                    self.insert(self.getLL(index2), index1)
                    self.remove(index1+1)
                    self.insert(temp,index2)
                    self.remove(index2+1)
                    break
                elif n.get_data() == self.getLL(index2):
                    temp = self.getLL(index2)
                    self.insert(self.getLL(index1), index2)
                    self.remove(index2+1)
                    self.insert(temp,index1)
                    self.remove(index1+1)
                    break
                n = n.get_next()
                
    # mendapatkan value dari index tertentu                  
    def getLL(self, index):
        if index == 0:
            return self.head.get_data()
        else:
            count=1
        n=self.head
        while count<index and n!=None:
            n=n.get_next()
            count+=1
        if n.get_next() == None:
            print("index yang dimaksud tidak ada")
        else:
            return n.get_next().get_data()
        
        
        # print seluruh linked list
    def printLL(self):
        # set current dengan head, berhenti apabila next node = null
        current = self.head
        while(current):
            print(current.val, "->", end=" ")
            current = current.next
        print("None")

def main():
    first = LinkedList()
    first.add(5)
    first.add(20)
    first.add(9)
    first.add(10)
    first.printLL()
    print("index 2: ", first.getLL(2))
    first.remove(0)
    first.printLL()
    print("remove index 0\nindex 2 baru: ", first.getLL(2))
    first.insert(100, 2)
    first.printLL()
    print("insert 100 ke index 2")
    first.swap(2, 1)
    first.printLL()
    print("swap index 2 dan 1")

if __name__ == "__main__":
    main()