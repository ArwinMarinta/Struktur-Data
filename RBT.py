class Node():
    def __init__(self,val):
        self.val = val                                  
        self.parent = None                               
        self.left = None                                
        self.right = None                                
        self.color = 1                                   

# Mendefinisikan Sebuah Class Red Black Tree
class RBTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # Fungsi Untuk Menambahkan Sebuah Node
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                 

        y = None
        x = self.root

        while x != self.NULL :                          
            y = x
            if node.val < x.val :
                x = x.left
            else :
                x = x.right

        node.parent = y                                  
        if y == None :                                 
            self.root = node
        elif node.val < y.val :                   
            y.left = node
        else :
            y.right = node

        if node.parent == None :                
            node.color = 0
            return

        if node.parent.parent == None :              
            return

        self.fixInsert ( node )                     


    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node


    # Fungsi untuk rotasi bagian Kiri node
    def LR ( self , x ) :
        y = x.right                                     
        x.right = y.left                                
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                      
        if x.parent == None :                     
            self.root = y                            
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


    # Fungsi untuk Rotasi bagian kanan node
    def RR ( self , x ) :
        y = x.left                                     
        x.left = y.right                             
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                           
        if x.parent == None :                          
            self.root = y                            
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y


    # Mengupdate jika ada Node baru yang akan masuk
    def fixInsert(self, k):
        while k.parent.color == 1:                      
            if k.parent == k.parent.parent.right:         
                u = k.parent.parent.left                 
                if u.color == 1:                        
                    u.color = 0                         
                    k.parent.color = 0
                    k.parent.parent.color = 1             
                    k = k.parent.parent                 
                else:
                    if k == k.parent.left:              
                        k = k.parent
                        self.RR(k)                     
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:                                         
                u = k.parent.parent.right                 
                if u.color == 1:                          
                    u.color = 0                          
                    k.parent.color = 0
                    k.parent.parent.color = 1            
                    k = k.parent.parent                   
                else:
                    if k == k.parent.right:            
                        k = k.parent
                        self.LR(k)                       
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)              
            if k == self.root:                          
                break
        self.root.color = 0                           


    # Sebuah Fungsi Untuk mengupdate jika ada masalah saat selesainya proses delete node
    def fixDelete ( self , x ) :
        while x != self.root and x.color == 0 :           
            if x == x.parent.left :                       
                s = x.parent.right                       
                if s.color == 1 :                       
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.LR ( x.parent )                  
                    s = x.parent.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                          
                    x = x.parent
                else :
                    if s.right.color == 0 :               
                        s.left.color = 0                  
                        s.color = 1                      
                        self.RR ( s )                     
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0                    
                    s.right.color = 0
                    self.LR ( x.parent )                 
                    x = self.root
            else :                                        
                s = x.parent.left                         
                if s.color == 1 :                         
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.RR ( x.parent )                  
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.parent
                else :
                    if s.left.color == 0 :                
                        s.right.color = 0                 
                        s.color = 1
                        self.LR ( s )                     
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RR ( x.parent )
                    x = self.root
        x.color = 0


    # sebuah fungsi kode untuk transplantasi sebuah node
    def __rb_transplant ( self , u , v ) :
        if u.parent == None :
            self.root = v
        elif u == u.parent.left :
            u.parent.left = v
        else :
            u.parent.right = v
        v.parent = u.parent


    # fungsi untuk menghadel penghapusan node berikutnya
    def delete_node_helper ( self , node , key ) :
        z = self.NULL
        while node != self.NULL :                          
            if node.val == key :
                z = node

            if node.val <= key :
                node = node.right
            else :
                node = node.left

        if z == self.NULL :                                
            print ( "Value not present in Tree !!" )
            return

        y = z
        y_original_color = y.color                          
        if z.left == self.NULL :                            
            x = z.right                                    
            self.__rb_transplant ( z , z.right )            
        elif (z.right == self.NULL) :                       
            x = z.left                                      
            self.__rb_transplant ( z , z.left )             
        else :                                             
            y = self.minimum ( z.right )                    
            y_original_color = y.color                     
            x = y.right
            if y.parent == z :                             
                x.parent = y                                
            else :
                self.__rb_transplant ( y , y.right )
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant ( z , y )
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0 :                          
            self.fixDelete ( x )


    # FUngsi untuk menghapus nilai node
    def delete_node ( self , val ) :
        self.delete_node_helper ( self.root , val )         

    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # fungsi untuk memangil output yang akan muncul di terminal
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )


if __name__ == "__main__":
    bst = RBTree()

    bst.insertNode(10)
    bst.insertNode(11)
    bst.insertNode(9)
    bst.insertNode(7)
    bst.insertNode(12)
    bst.insertNode(2)

    bst.print_tree()

    # print("\nSetelah menghapus sebuah elemen")
    # bst.delete_node(2)
    # bst.print_tree()